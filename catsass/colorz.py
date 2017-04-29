def kitty_colorz():
    try:
        import crayons
        from pygments import highlight
        from pygments.lexers import get_lexer_by_name
        from pygments.lexers.python import Python3Lexer
        from pygments.formatters import get_formatter_by_name
        from pygments.formatters.terminal import TerminalFormatter
    except ImportError:
        return None
    else:
        color_map = dict(
            blk=crayons.black,
            bl=crayons.blue,
            rd=crayons.red,
            ye=crayons.yellow,
            cy=crayons.cyan,
            mg=crayons.magenta,
            wh=crayons.white,
            gr=crayons.green,
        )

        calico_colorz = {
            'M': color_map['rd'],
            '_': color_map['rd'],
            '*': color_map['rd'],
            '-': color_map['cy'],
            '.': color_map['wh'],
            '~': color_map['bl'],
            '!': color_map['ye'],
            ':': color_map['gr'],
            ';': color_map['ye'],
            '=': color_map['cy'],
            '+': color_map['wh'],
            'i': color_map['blk'],
        }

        tuxedo_colorz = {
            'M': color_map['blk'],
            'i': color_map['blk'],
            '_': color_map['rd'],
            '*': color_map['rd'],
            ':': color_map['ye'],
            ';': color_map['ye'],
            '=': color_map['cy'],
            '-': color_map['wh'],
            '~': color_map['bl'],
            ',': color_map['bl'],
            '|': color_map['wh'],
            '.': color_map['wh'],
            '+': color_map['wh'],
            "'": color_map['rd'],
            '^': color_map['bl'],
            '"': color_map['blk'],
        }

        logo_colorz = {
            '\\': color_map['bl'],
            '(': color_map['bl'],
            '/': color_map['gr'],
            '_': color_map['rd'],
            '|': color_map['gr'],
            '>': color_map['gr'],
        }

        dark_logo_colorz = {
            '\\': color_map['ye'],
            '(': color_map['ye'],
            '/': color_map['bl'],
            '_': color_map['bl'],
            '|': color_map['ye'],
            '>': color_map['ye'],
        }

        title_colorz = {
            'Meowed': color_map['bl'],
            'with': color_map['bl'],
            'love': color_map['rd'],
            'by': color_map['bl'],
            'Duroktar,': color_map['gr'],
            '2017': color_map['ye']
        }

        return locals()   # watz here? hmm.. but duroktarz no nose dis! magic i saez
