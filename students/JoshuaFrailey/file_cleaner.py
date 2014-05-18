import sys
import codecs


def _overwrite(file_name):
    f = codecs.open(file_name, "r+w")
    l = f.readlines()
    print l
    w = map(_clean, l)
    f.seek(0)
    print w
    f.writelines(w)
    f.flush()


def _rewrite(file_name):
    pass


def _clean(line):
    l = " ".join(line.split())
    return u"{}".format(l)

if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = unicode(raw_input(u"Enter file name\n--> "))
    menu = [u"Remove whitespace by\n1: Overwriting the file\n"]
    menu.append(u"2: Writing a new file\n3: Exit")
    print "".join(menu)
    d = dict(zip([u"1", u"overwrite", u"o"], [_overwrite]*3))
    d.update(zip([u"2", u"write", u"w", u"n", u"new"], [_rewrite]*5))
    d.update(zip([u"3", u"e", u"exit"], [None]*3))
    while True:
        try:
            d[unicode(raw_input(u"--> ")).lower()]()
        except TypeError:
            break
        except KeyError:
            print u"Please choose from 1, 2, 3"