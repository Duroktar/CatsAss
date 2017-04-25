import re
import os.path
import yaml


example = \
    '\x1b[34m\x1b[22mMeowed\x1b[39m\x1b[22m ' \
    '\x1b[34m\x1b[22mwith\x1b[39m\x1b[22m ' \
    '\x1b[31m\x1b[22mlove\x1b[39m\x1b[22m ' \
    '\x1b[34m\x1b[22mby\x1b[39m\x1b[22m ' \
    '\x1b[34m\x1b[22mDuroktar,\x1b[39m\x1b[22m ' \
    '\x1b[32m\x1b[22m2017\x1b[39m\x1b[22m'


# https://regex101.com/r/z5ARGi/5
ansi_escape = re.compile(r'(\\x1b\[\d.+?22m)(.+?)(?=\\x1b)(\\x1b\[\d.+?22m)')


HOME = os.path.expanduser("~")
CATSASSDIR = os.path.join(HOME, '.catsass')
SHAREDIR = os.path.join(CATSASSDIR, 'share')
CATSDIR = os.path.join(SHAREDIR, 'cats')
COATSDIR = os.path.join(SHAREDIR, 'coats')
LOGOSDIR = os.path.join(SHAREDIR, 'logos')
TITLESDIR = os.path.join(SHAREDIR, 'titles')


def file_loader(directory, ftype):
    files = {}
    for dirname, _, filelist, *_ in iter(os.fwalk(directory)):
        for current in filelist:
            profile, element, *collection = current.split(".")
            if ftype != element:
                pass
            group = {}
            with open(os.path.join(dirname, current), 'r') as fs:
                if collection:
                    data = yaml.safe_load(fs.read())
                    group[collection.pop()] = data
                else:
                    data = fs.read()
                    group[element] = data
            if profile in files.keys():
                files[profile].update(group)
            else:
                files[profile] = group
    return files


def brush_up():
    logoz = logo_loader()
    titlez = title_loader()
    catz = catz_loader()
    coatz = coatz_loader()
    return locals()


def logo_loader():
    logos = file_loader(LOGOSDIR, "logo")
    return logos


def title_loader():
    titles = file_loader(TITLESDIR, "title")
    return titles


def catz_loader():
    catz = file_loader(CATSDIR, "meow")
    return catz


def coatz_loader():
    coatz = file_loader(COATSDIR, "coat")
    return coatz
