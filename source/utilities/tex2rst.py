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
                   r'\vfill',
                   r'\end{frame}',
                   r'{\Large',
                   r'{\large',
                   r'{\LARGE',
                   r'{\HUGE',
                   r'\begin{itemize}',
                   r'\end{itemize}',
                   r'\begin{enumerate}',
                   r'\end{enumerate}',
                   r'\url{',
                   r'\\',
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
    full_file = [line.split('%')[0] for line in full_file]

    # title
    title = ''
    for i, line  in enumerate(full_file):
        print line
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

    # new slide header:
    for i, line  in enumerate(full_file):
        if line.startswith(r'\begin{frame}'):
            line = line[line.rindex('{'):][1:-1]
            full_file[i] = line
            full_file.insert(i+1, "="*len(line))

    # extra spacing: \\[0.1in]
    full_file = [line.split(r'\\[')[0]for line in full_file] 

    # horizontal spacing:\hspace{0.5in}
    for i, line  in enumerate(full_file):
        while r'\hspace{' in line:
            j = line.index(r'\hspace{') + 8
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




    open(outfile,'w').write("\n".join(full_file) )


