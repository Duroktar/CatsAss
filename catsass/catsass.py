#!/usr/bin/env python
"""Seriously the cats ass. Seriously.

CatsAss is the cats ass for replacing multiple prints in
simple debugging situations.

----

![CatsAss_demo](https://github.com/Duroktar/CatsAss/blob/master/images/CatsAss_dark.png?raw=true)

----

*Requires Python 3.6*

"""
import os.path
from collections import namedtuple
from itertools import groupby
from pprint import pformat, pprint

__author__ = "Duroktar"
__license__ = "MIT"

# == API ==


# === the_cats_ass() ===

def the_cats_ass():
    """This function is the_cats_ass. That's an over-statement.
    This is an under-statement. See what I did there? 
    What _you_ can do here is save the sys.ENVIRONMENT 
    by reducing print-ed waste. Mew.

    returns: probably what you want
    """
    return __cat_whisperer()[Cat.ASS]


# === comb() ===

def comb(cat, *brush):
    """
    Filter the results of poking the cat. Takes variable
    names as strings for the args.

    cat: 
        the_cats_ass() or similar

    brush: 
        the variables you wish to see (as strings)


    returns: hairballs
    """
    return PrettyKitty(cat.ctx, {k: v for k, v in cat.values.items()
                                 if k in brush})


# === avoid() ===

def avoid(cat, *undesirables):
    """
    Omit any undesirable variables from the result.

    cat: 
        the_cats_ass() or similar

    undesirables: 
        variables you wish to have omitted (as strings)


    returns: from whence it came
    """
    return PrettyKitty(cat.ctx, {k: v for k, v in cat.values.items()
                                 if k not in undesirables})


# === poke_the_cat() ===

def poke_the_cat(where, catnip=False):
    """
    You really shouldn't be poking cats. But if you insist,
    it is recommended to bring catnip as it's not unusual for
    cats to attack dicks who poke them.

    where: 
        I leave this as an exercise for the reader. But
        a word of wisdom from my 1st grade teacher: never do
        anything that you wouldn't want to be caught dead doing.
        Sadly he went to jail not long after whispering those 
        words in my ear.

    catnip: 
        catnip can grow in the wild in many places around
        the world. If no catnip can readily be found in yours
        or any of your neighbors yards then just pass True as the 
        argument.


    returns: possibly what you want.
    """
    if not catnip:
        from random import randint

        class BadCat(InterruptedError):
            pass

        if randint(1, 10) == 7:
            mew = "You attempt to poke the cat but it attacks. " \
                  "Maybe if you gave it some catnip?"
            raise BadCat(mew)

    return __cat_whisperer()[where]


# === schrodingers_cat() ===

def schrodingers_cat(peek=False):
    """
    Peek in the box for a 50/50 shot of retrieving your
    desired output, while the other half of the time the
    cat is dead and the function returns nothing at all.
    If you decide not to peek, the cat -being neither
    dead nor alive- responds with random nonsense.

    peek: 
        whether to peek in the box


    returns: depends
    """
    from random import choice, randint
    if peek:
        if randint(1, 10) % 2 == 0:
            # RIP
            return "Nothing at all"
        else:
            return poke_the_cat(Cat.LEGS, catnip=True)
    else:
        garbled_cries = "mew meow wokka beocat ekkie".split()
        return choice(garbled_cries)


def calico_kitty():
    """I can haz colorz?"""
    return __cat_whisperer(colors=True, coat='calico_colorz', logo_colorz='logo_colorz')[Cat.ASS]


def tuxedo_cat():
    """Finer than a pheasant"""
    return __cat_whisperer(colors=True, coat='tuxedo_colorz', logo_colorz='dark_logo_colorz')[Cat.ASS]


__LIBDIR__ = os.path.abspath(os.path.dirname(__file__))

# === PrettyKitty() ===


class PrettyKitty:
    """I can has repr?"""

    def __init__(self, ctx, values, cat=None, logo=None,
                 marker='|/', logo_offset=6, template=None,
                 formatter=pformat, colors=False, coat=None,
                 logo_colorz=None, term_bg="dark", title=None,
                 title_start=(6, 45)):

        # The callers name usually.
        self.ctx = ctx

        # The local variables data.
        self.values = values

        # The line where the talk bubble should
        # start must end with the marker, or the
        # data will be printed just below the logo,
        # which may not be what you want.
        self.marker = marker

        # Other formatters can be swapped in, JSON
        # -for example- should work, or yaml.
        self.formatter = formatter

        # Allows the logo to be offset to either side;
        # positive numbers move it left and negative
        # numbers move it right.
        self.logo_offset = logo_offset

        self.term_bg = term_bg

        if title is None:
            title = "Meowed with love by Duroktar, 2017"
        self.title = title
        self.title_location = title_start

        # Colors ~*%~
        self.colors = colors
        self.coat = coat
        self.logo_colorz = logo_colorz

        # TODO Should be public
        Template = namedtuple("Template", "view offset")
        if template is None:

            # Option 1
            template = Template({
                "Name": self.ctx,
                "Vars": self.values}, 1)

            # Option 2
            template = Template({self.ctx: self.values}, 1)
        self.template = template

        if cat is None:
            cat = open(os.path.join(__LIBDIR__, 'octocat'), 'r').readlines()
        self.cat = cat

        if logo is None:
            logo = open(os.path.join(__LIBDIR__, 'logo'), 'r').readlines()
        self.logo = logo

    def __repr__(self):
        return self.haz_format() + "\n\n"

    def haz_format(self):
        from shutil import get_terminal_size

        def yield_pads(lines, l):
            for line in lines:
                line = line.rstrip("\n").rstrip()
                length = len(line)

                if length < l:
                    yield line + " " * (l - length - 1)
                else:
                    yield line

        def rfill_lines(filler, start=0, offset=0, column=None):
            height = len(filler)
            for i in range(height):
                index = start + i
                try:
                    line = cat[index]
                except IndexError:
                    cat.append(f"{' ' * pivot}{filler[i]}")
                else:
                    if column is not None:
                        new_l = f"{line[:-(term_width - column) - offset]}{filler[i]}"
                    else:
                        new_l = f"{line[:-(term_width - pivot) - offset]}{filler[i]}"

                    cat[index] = new_l

        term_width, term_height = get_terminal_size((80, 30))
        cat = list(yield_pads(self.cat, term_width))
        pivot = max((len(l.encode('unicode-escape')) for l in self.cat))

        logo_offset = self.logo_offset
        logo_width = max((len(str(l)) for l in self.logo))
        logo = list(yield_pads(self.logo, logo_width - 1))
        logo_height = len(logo)

        marker = self.marker
        data_start_line = [i - 1 for i, v in enumerate(cat) if v.strip().endswith(marker)]
        if not data_start_line:
            data_start_line = [logo_height + 1]
        data_start_line = data_start_line[0]

        if logo_height > data_start_line:
            data_start_line = logo_height + 1

        title = [self.title]
        title_start_line, title_start_column = self.title_location
        data = self.formatter(self.template.view, width=(term_width - pivot))

        if self.colors:
            cat, logo, title, data = self.haz_colorz(cat, logo, title, data)

        rfill_lines(logo, offset=logo_offset)
        rfill_lines(title, start=title_start_line, column=title_start_column)
        rfill_lines(data.splitlines(), start=data_start_line, offset=self.template.offset)
        return "\n".join((l.rstrip() for l in cat))

    def haz_colorz(self, cat, logo, title, data):
        from catsass.colorz import kitty_colorz

        color_stuffs = kitty_colorz()

        if color_stuffs is None:
            return cat, logo, title, data

        def color_lines(lines, color_mapping, words=False):
            if any([len(k) > 1 for k in color_mapping.keys()]):
                words = True
                search_lines = [groupby(line.split()) for line in lines]
            else:
                search_lines = [groupby(line) for line in lines]

            rv = []
            for groups in search_lines:
                line = []
                for item, group in groups:
                    color = color_mapping.get(item)
                    if color is None:
                        line.append("".join(group))
                    else:
                        line.append(color("".join(group)).color_str)
                if words:
                    rv.append(" ".join(line))
                else:
                    rv.append("".join(line))
            return rv

        highlight = color_stuffs.get('highlight')

        # Customz
        cat_colorz = color_stuffs.get(self.coat) or {}
        logo_colorz = color_stuffs.get(self.logo_colorz) or {}

        # All this will be customizable in the next release.
        title_colors = color_stuffs.get('title_colorz')
        python3_lexer = color_stuffs.get('Python3Lexer')
        terminal_formatter = color_stuffs.get('TerminalFormatter')

        # Slap-chop! Why? I dunno..
        cat = color_lines(cat, cat_colorz)
        logo = color_lines(logo, logo_colorz)
        title = color_lines(title, title_colors)
        if highlight is not None:
            data = highlight(data, python3_lexer(stripnl=False), terminal_formatter(bg=self.term_bg))
        return cat, logo, title, data


# === Cat ===

class Cat:
    """
    Different places to poke the cat. If the wrong scope is
    being printed then you probably just need to poke the cat 
    somewhere else.
    """
    TAIL = 0
    ASS = 1
    LEGS = 2


# === __cat_whisperer() ===

def __cat_whisperer(**kwargs):
    """
    The cat whisperer is usually very solitary and private.
    Thus any attempts at invoking the cat whisperer directly
    will be met with no resistance, because this is Python, 
    and honestly he could use the friends.


    returns: whisperings of cats
    """
    from inspect import currentframe
    frames = []
    frame = currentframe()
    while frame is not None:
        frame = frame.f_back
        try:
            c_frame = frame.f_locals.copy()
            co_name = frame.f_code.co_name
        except AttributeError:
            break
        else:
            frames.append(
                PrettyKitty(co_name, {k: v for k, v in c_frame.items()
                                      if not any([k.startswith('_'), callable(v)])}, **kwargs))
    return frames
