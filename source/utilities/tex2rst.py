#!/usr/bin/env python

"""
Simple script to (partially) convert slides written in LaTeX 
using the Beemer style to ReStructuredText suitable for the
Heiroglyph Sphinx package.

Note: some of this would be a lot easier with regexs
   -- but that's not my thing....

"""

import sys

stuff_to_remove = [r'\documentclass{beamer}',
                   r'\usepackage[latin1]{inputenc}',
                   r'\usetheme{Warsaw}',
                   r'\usepackage{listings}',
                   r'\usepackage{hyperref}',
                   r'\begin{document}',
                   r'\author{Christopher Barker}',
                   r'\institute{UW Continuing Education}',
                   r'\vfill',
                   r'\end{frame}',
                   r'{\Large ',
                   r'{\large ',
                   r'{\LARGE ',
                   r'{\HUGE ',
                   r'{\small ',
                   r'{\Large',
                   r'{\large',
                   r'{\LARGE',
                   r'{\HUGE',
                   r'{\small',
                   r'\pause',
                   r'\begin{itemize}',
                   r'\end{itemize}',
                   r'\begin{enumerate}',
                   r'\end{enumerate}',
                   r'\url{',
                   r'\\',
                   r'\bf ',
                   r'}',
                   ]

replacments = [ (r'\item','*'), #punting on enumerated lists...
                ("``",'"'),
                ("''",'"'),
              ]

if __name__ == "__main__":
    infile = sys.argv[1]
    outfile = infile[:-4] + '.rst'

    full_file = open(infile, 'rU').readlines()


    # clean up trailing whitespace:
    full_file = [line.rstrip() for line in full_file]

    # strip comments
    # caused problems with % in verbatim ....
    full_file = [line for line in full_file if (line and line.strip()[0] != '%')]

    # title
    title = ''
    for i, line  in enumerate(full_file):
        if line.lstrip().startswith(r"\title["):
            title = line.split('[',1)[1]
            title = title.replace(']{', ' ')
            title = title.replace(r'\\', ' ')
            full_file[i] = ''
        elif title:
            title = title+ ' ' + line.strip() 

        if title and title[-1] == '}':
            full_file[i] = '='*len(title) +'\n' + title[:-1] +'\n' + '='*len(title)
            break

    #remove date
    for i, line  in enumerate(full_file):
        if line.lstrip().startswith(r'\date'):
            full_file[i] = ''  

    # remove titlepage
    for i, line  in enumerate(full_file):
        if line.lstrip().startswith(r'\begin{frame}'):
            if full_file[i+1].strip() == r'\titlepage':
                full_file[i] = ''
                full_file[i+1] = ''
                full_file[i+2] = ''
                break

    # new slide header:
    for i, line  in enumerate(full_file):
        if line.lstrip().startswith(r'\begin{frame}'):
            line = line[line.rindex('{'):][1:-1]
            full_file[i] = line
            full_file.insert(i+1, "="*len(line))

    # section:
    for i, line  in enumerate(full_file):
        if line.lstrip().startswith(r'\section{'):
            line = line.strip()[9:-1]
            full_file[i] = "="*len(line)
            full_file.insert(i+1, line)
            full_file.insert(i+2, "="*len(line)+'\n')


    # extra spacing: \\[0.1in]
    full_file = [line.split(r'\\[')[0]for line in full_file] 

    # horizontal and vertical spacing:\hspace{0.5in}
    for space_cmd in [r'\hspace{', r'\vspace{']:
        for i, line  in enumerate(full_file):
            while space_cmd in line:
                j = line.index(space_cmd) + 8
                k = line.index('}',j+1)
                line = line[:j-8]+line[k+1:]
            full_file[i] = line     


    for r in replacments:
        full_file = [line.replace(*r) for line in full_file]

    #inline code:
    for i, line  in enumerate(full_file):
        while r'\verb' in line:
            j = line.index(r'\verb') + 5
            k = line.index(line[j],j+1)
            line = line[:j-5]+'``'+line[j+1:k]+'`` '+line[k+1:]
        full_file[i] = line     
    
    # block code:
    in_block = False
    after_block = False
    for i, line in enumerate(full_file):
        if line.lstrip() == r'\begin{verbatim}':
            in_block = True
            full_file[i] = '::'
            full_file.insert(i+1, '\n')
        elif line.lstrip() == r'\end{verbatim}':  
            in_block = False
            after_block = True
            full_file[i] = '\n'
        elif in_block:
            full_file[i] = '    ' + line
        elif after_block:
            # make sure the indendation is gone with next line
            line = line.strip()
            full_file[i] = line
            if line:
                after_block = False 


    # remove useless cruft:
    for i, line  in enumerate(full_file):
        for item in stuff_to_remove:
            line = line.replace(item, '')
        full_file[i] = line


    # clean out empty lines:
    num_empty = 0
    new_file = [] 
    for i, line  in enumerate(full_file):
        num_empty += (1 if not line.strip() else -num_empty)
        if num_empty <= 2:
            new_file.append(line)
    full_file = new_file


    open(outfile,'w').write("\n".join(full_file) )


