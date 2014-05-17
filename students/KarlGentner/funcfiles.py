#!/usr/bin/python
import sys
import codecs


filename = sys.argv[1]


def cleanLines(filename, isNewFile):
    # Create list of cleaned lines using map
    f = codecs.open(filename)
    lineList = map(lambda line: line.strip() + "\n", f)
    f.close()
    # Create list of cleaned lines using list comprehension
    # lineList = [line.strip() + "\n" for line in f]

    # Write to a new file (or) overwrite existing
    if isNewFile is True:
        filename = raw_input(u"Enter new filename-->") + ".txt"
    f = codecs.open(filename, 'w')
    f.writelines(lineList)
    f.close()


if __name__ == '__main__':
    mainMenu = ""
    while mainMenu != 'o' and mainMenu != 'n' and mainMenu != 'q':
        print ("\n\n-----------------Clean Whitespaces-------------------\n")
        mainMenu = raw_input(u"'o' to overwrite the existing file\n" +
                             "'n' to create a new file\n" +
                             "'q' to quit\n-->")
        # Quit main menu
        if mainMenu.lower() == u'q':
            break
        # Clean & Overwrite existing file
        if mainMenu.lower() == u'o':
            cleanLines(filename, False)
            break
        # Clean & write a new file
        if mainMenu.lower() == u'n':
            cleanLines(filename, True)
            break