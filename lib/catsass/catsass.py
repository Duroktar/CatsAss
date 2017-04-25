#!/usr/bin/env python
"""Seriously the cats ass. Seriously.

CatsAss is the cats ass for replacing multiple prints in
simple debugging situations.

----

![CatsAss_demo](https://github.com/Duroktar/CatsAss/blob/master/screens/CatsAss_dark.png?raw=true)

----

*Requires Python 3.6*

"""
import os.path
from collections import namedtuple
from itertools import groupby
from pprint import pformat

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
    return __cat_whisperer(colors=True)


__LIBDIR__ = os.path.abspath(os.path.dirname(__file__))

# === PrettyKitty() ===


class PrettyKitty:
    """I can has repr?"""

    def __init__(self, ctx, values, template=None, colors=True, term_bg="dark",
                 cat='octocat',     logo='default',          title='default',
                 coat='calico-cat', logo_colors='default',   title_colors='default',
                 marker='|/',       logo_offset=-6,          title_start=(6, 65),
                 p_printer=pformat, output_formatter='terminal', data_lexer='py3'):

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
        self.pretty_printer = p_printer

        # Allows the logo to be offset to either side;
        # negative numbers move it left and positive
        # numbers move it right.
        self.logo_offset = logo_offset

        self.term_bg = term_bg

        self.colors = colors

        self.data_lexer = data_lexer
        self.output_formatter = output_formatter

        # TODO Gotta be public
        Template = namedtuple("Template", "view offset")
        # TODO: Should be customizable.. also needs to be thought out more.. I'm not loving it, but..
        if template is None:
            # template = Template({
            #     "Name": self.ctx,
            #     "Vars": self.values}, 0)
            template = Template({'lyrics': self.values}, -5)
            # template = Template(self.values, 0)

        self.template = template

        from utils import brush_up

        post = brush_up()
        self.scratching_post = post

        self.coat = coat
        self.title_colors = title_colors
        self.logo_colors = logo_colors

        self.logo = post['logoz'][logo]['logo'].splitlines()
        self.cat = post['catz'][cat]['meow'].splitlines()
        self.title = post['titlez'][title]['title']

        self.title_location = title_start

    # ######################################
    # ######################################
    # ######################################
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

        term_width, term_height = get_terminal_size((80, 30))

        cat = list(yield_pads(self.cat, term_width))
        cat_width = max(map(len, self.cat))
        logo_width = max(map(len, self.logo))
        # cat_height = len(cat)

        logo = list(yield_pads(self.logo, logo_width - 1))
        logo_offset = self.logo_offset
        logo_height = len(logo)

        marker = self.marker

        data_start_line = [i - 1 for i, v in enumerate(cat) if v.strip().endswith(marker)]
        if not data_start_line:
            data_start_line = [logo_height + 1]
        data_start_line = data_start_line[0]

        if logo_height > data_start_line:
            data_start_line = logo_height + 1

        # def trim(l):
        #     if len(l) > term_width - cat_width:
        #         return l[:term_width - cat_width - 5] + "[...]"
        #     return l

        def rfill_lines(bg, filler, start=0, offset=0, column=None):
            height = len(filler)
            for i in range(height):
                index = start + i
                try:
                    line = bg[index]
                except IndexError:
                    bg.append(f"{' ' * cat_width}{filler[i]}")
                else:
                    if column is not None:
                        new_l = f"{line[:-(term_width-column)]}{filler.pop()}"
                    else:
                        new_l = f"{line[:-(term_width - cat_width - offset)]}{filler[i]}"

                    # new_l = f"{line[:-(term_width - cat_width - offset)]}{filler[i]}"
                    bg[index] = new_l

        title = self.title
        title_start_line, title_start_column = self.title_location

        data = self.pretty_printer(self.template.view, width=(80 - cat_width))

        if self.colors:
            cat, logo, data, title = self.haz_colorz(cat, logo, data, title)

        rfill_lines(cat, logo, start=0, offset=logo_offset)
        rfill_lines(cat, title, start=title_start_line, column=title_start_column)
        rfill_lines(cat, data, start=data_start_line, offset=self.template.offset)

        return "\n".join((l.rstrip() for l in cat))

    def __repr__(self):
        return self.haz_format() + "\n\n"

    def haz_colorz(self, cat, logo, data, title):
        from colorz import kitty_colorz
        try:
            color_stuffs = kitty_colorz()
        except ImportError:
            return cat, logo, data.splitlines(), title

        def color_lines(lines, colors, words=False):
            if any([len(k) > 1 for k in colors.keys()]):
                words = True
                search_lines = [groupby(lines.split())]
            else:
                search_lines = [groupby(line) for line in lines]
            rv = []
            for groups in search_lines:
                line = []
                for item, group in groups:
                    # print("Item =", item)
                    colour = colors.get(item)
                    # print("Colour", colour)
                    color = color_map.get(colour)
                    # print("Getting colored", color)
                    # print("Group =", group)
                    if color is None:
                        result = "".join(group)
                        # print("group =", result)
                        # print("First")
                        line.append(result)
                    else:
                        result = color("".join(group)).color_str
                        # print("group =", result)
                        # print("Second")
                        line.append(result)
                if words:
                    value = " ".join(line)
                    # print("Appending (words=True) =", value)
                    rv.append(value)
                else:
                    value = "".join(line)
                    # print("Appending (words=False) =", value)
                    rv.append(value)
            return rv

        scratching_post = self.scratching_post

        # Catz
        chosen_logo_color = self.coat
        coats = scratching_post['coatz']
        cat_colorz = coats[chosen_logo_color]['colorz']

        # Logoz
        chosen_logo_color = self.logo_colors
        logos = scratching_post['logoz']
        logo_colorz = logos['default']['colorz']

        # Titlez
        chosen_title = self.title_colors
        titles = scratching_post['titlez']
        title_colors = titles[chosen_title]['colorz']

        color_map = color_stuffs['color_map']
        highlight = color_stuffs['highlight']
        lexer_loader = color_stuffs['get_lexer_by_name']
        formatter_loader = color_stuffs['get_formatter_by_name']

        lexer = lexer_loader(self.data_lexer, stripnl=False)
        formatter = formatter_loader(self.output_formatter, bg=self.term_bg)

        cat = color_lines(cat, cat_colorz)
        logo = color_lines(logo, logo_colorz)
        title = color_lines(title, title_colors)

        data = highlight(data, lexer, formatter)

        return cat, logo, data.splitlines(), title


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


def CatsAss():
    its = [
        "The       ",
        " cats     ",
        "   ass..  ",
        "Seriously."
    ]

    print(the_cats_ass())


if __name__ == '__main__':
    CatsAss()
