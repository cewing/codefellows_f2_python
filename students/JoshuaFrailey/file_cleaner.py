import sys
import codecs


def _overwrite(file_name):
    f = codecs.open(file_name)
    lines = f.readlines()
    clean_lines = map(_clean, lines)
    f = codecs.open(file_name, "w")
    f.writelines(clean_lines)
    f.close()


def _overwrite_list_comp(file_name):
    f = codecs.open(file_name)
    lines = f.readlines()
    clean_lines = [u"{}\n".format(u" ".join(line.split())) for line in lines]
    f = codecs.open(file_name, "w")
    f.writelines(clean_lines)
    f.close()


def _rewrite(file_name):
    f = codecs.open(file_name)
    lines = f.readlines()
    clean_lines = [u"{}\n".format(u" ".join(line.split())) for line in lines]
    f.close()
    f = codecs.open(u"clean_{}".format(file_name), "w")
    f.writelines(clean_lines)
    f.close()


def _rewrite_list_comp(file_name):
    f = codecs.open(file_name)
    lines = f.readlines()
    clean_lines = map(_clean, lines)
    f.close()
    f = codecs.open(u"clean_{}".format(file_name), "w")
    f.writelines(clean_lines)
    f.close()


def _clean(line):
    l = " ".join(line.split())
    return u"{}\n".format(l)

if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = unicode(raw_input(u"Enter file name\n--> "))
    menu = [u"Remove whitespace by\n1: Overwriting the file\n"]
    menu.append(u"2: Writing a new file\n3: Overwriting the file with ")
    menu.append(u"list comprehension\n4: Writing a new file with list ")
    menu.append(u"comprehension\n5: Exit")
    print "".join(menu)
    d = dict(zip([u"1", u"overwrite", u"o"], [_overwrite]*3))
    d.update(zip([u"2", u"write", u"w", u"n", u"new"], [_rewrite]*5))
    d.update(zip([u"5", u"e", u"exit"], [None]*3))
    d[u"3"] = _overwrite_list_comp
    d[u"4"] = _rewrite_list_comp
    while True:
        try:
            d[unicode(raw_input(u"--> ")).lower()](file_name)
        except TypeError:
            break
        except KeyError:
            print u"Please choose from 1, 2, 3"
        else:
            break