#!/usr/bin/env python
"""Seriously the cats ass. Seriously.

CatsAss is the cats ass for replacing multiple prints in
simple debugging situations.

----

![CatsAss_demo](../images/CatsAss_dark.png)

----

*Requires Python 3.6*

"""
import os.path
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


__LIBDIR__ = os.path.abspath(os.path.dirname(__file__))


# === PrettyKitty() ===

class PrettyKitty:
    """I can has repr?"""

    def __init__(self, ctx, values, cat=None, logo=None,
                 marker='|/', logo_offset=-6,
                 formatter=pformat):

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
        # negative numbers move it left and positive
        # numbers move it right.
        self.logo_offset = logo_offset

        if cat is None:
            cat = open(os.path.join(__LIBDIR__, 'octocat'), 'r').readlines()
        self.cat = cat

        if logo is None:
            logo = open(os.path.join(__LIBDIR__, 'logo'), 'r').readlines()
        self.logo = logo

    def haz_format(self):
        from shutil import get_terminal_size

        cat = self.cat
        logo = self.logo
        marker = self.marker
        logo_offset = self.logo_offset

        pivot = max(len(i) for i in cat)
        term_width, term_height = get_terminal_size((80, 30))
        data = self.formatter({self.ctx: self.values}, width=(80-pivot)).splitlines()

        logo_height = len(logo)
        speak_line = [i - 1 for i, v in enumerate(cat) if v.strip().endswith(marker)]
        if not speak_line:
            speak_line = [logo_height + 1]
        speak_line = speak_line[0]

        if logo_height > speak_line:
            logo = ["CatsAss".center(20)]

        def rfill_lines(filler, start=0, offset=0):
            height = len(filler)
            for i in range(height):
                index = start + i
                try:
                    line = cat[index]
                except IndexError:
                    cat.append(f"{' ' * pivot}"
                               f"{filler[i]}")
                else:
                    l_break = '\n'
                    new_l = (f"{line.rstrip(l_break)}"
                             f"{' ' * ((pivot - len(line)) + offset)}"
                             f"{filler[i]}")
                    cat[index] = new_l

        def trim(l):
            if len(l) > term_width - pivot:
                return l[:term_width - pivot - 5] + "[...]"
            return l
        trimmed_data = [trim(line) for line in data]

        rfill_lines(logo, offset=logo_offset)
        rfill_lines(trimmed_data, start=speak_line)
        return "\n".join([l.rstrip('\n')
                          for l in [line[:term_width]
                          for line in cat]])

    def __repr__(self):
        return self.haz_format()


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

def __cat_whisperer():
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
                                      if not any([k.startswith('_'), callable(v)])}))
    return frames

