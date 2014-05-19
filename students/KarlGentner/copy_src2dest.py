#!/usr/bin/python


src = "/home/karl/projects/cff2py/sea-c15-python/students/KarlGentner/sherlock_small.txt"
dest = "/home/karl/projects/sher_small.txt"


def copy_src2dest(src, dest):

    src = open(src)
    dest = open(dest, 'w')

    content = src.read()
    dest.write(content)

    src.close()
    dest.close()


if __name__ == '__main__':
    copy_src2dest(src, dest)