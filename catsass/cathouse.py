import os
from collections import namedtuple
from itertools import groupby
from pprint import pformat

__LIBDIR__ = os.path.abspath(os.path.dirname(__file__))

# === PrettyKitty() ===


class PrettyKitty:
    """I can has repr?"""

    def __init__(self, ctx, values, template=None, colors=True,  term_bg="dark",
                 cat='octocat',     logo='default',              title='default',
                 coat='calico-cat', logo_colors='default',       title_colors='default',
                 marker='|/',       logo_offset=-12,              title_start=(6, 45),
                 p_printer=pformat, output_formatter='terminal', data_lexer='py3',
                 data_offset=0):

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
            # template = Template({'lyrics': self.values}, data_offset)
            # template = Template(self.values, 0)
            template = Template({
                self.ctx: self.values}, 0)

        self.template = template

        self.coat = coat
        self.title_colors = title_colors
        self.logo_colors = logo_colors

        from catsass.utils import brush_up

        self.scratching_post = post = brush_up()
        self.logo = post['logoz'].get(logo, {}).get('logo', "\n").splitlines()
        self.cat = post['catz'].get(cat, {}).get('meow', "\n").splitlines()
        self.title = post['titlez'].get(title, {}).get('title', {}) or title

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
        f_offset = -1

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
                        new_l = f"{line[:-(term_width - column + offset)]}{filler.pop()}"
                    else:
                        new_l = f"{line[:-(term_width - cat_width + offset)]}{filler[i]}"

                    bg[index] = new_l

        title = self.title
        title_start_line, title_start_column = self.title_location

        data_width = term_width - cat_width + f_offset
        data = self.pretty_printer(self.values, width=data_width)

        if self.colors:
            cat, logo, data, title = self.haz_colorz(cat, logo, data, title)

        rfill_lines(cat, logo, start=0, offset=logo_offset)
        rfill_lines(cat, title, start=title_start_line, column=title_start_column)
        rfill_lines(cat, data, start=data_start_line, offset=self.template.offset)

        return "\n".join((l.rstrip() for l in cat))

    def __repr__(self):
        return self.haz_format() + "\n\n"

    def haz_colorz(self, cat, logo, data, title):
        from catsass.colorz import kitty_colorz
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
                    colour = colors.get(item)
                    color = color_map.get(colour)
                    if color is None:
                        result = "".join(group)
                        line.append(result)
                    else:
                        result = color("".join(group)).color_str
                        line.append(result)
                if words:
                    value = " ".join(line)
                    rv.append(value)
                else:
                    value = "".join(line)
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
        logo_colorz = logos[chosen_logo_color]['colorz']

        # Titlez
        chosen_title = self.title_colors
        titles = scratching_post['titlez']
        title_colors = titles.get(chosen_title, {}).get('colorz', {})

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
