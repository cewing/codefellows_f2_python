import codecs


def copy_file(source, destination, filename):
    u"""Copy filename from source to destination."""
    f = codecs.open(u"{}/{}".format(source, filename))
    lines = f.readlines()
    g = codecs.open(u"{}/{}".format(destination, filename), "w")
    g.writelines(lines)
    f.close()
    g.close()