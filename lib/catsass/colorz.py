def kitty_colorz():
    try:
        import crayons
        from pygments import highlight
        from pygments.lexers import get_lexer_by_name, guess_lexer
        from pygments.formatters import get_formatter_by_name
    except ImportError:
        return {}
    else:
        color_map = dict(
            blk=crayons.black,
            bl=crayons.blue,
            rd=crayons.red,
            ye=crayons.yellow,
            cy=crayons.cyan,
            mg=crayons.magenta,
            wh=crayons.white,
            gr=crayons.green
        )

        return locals()   # watz here? hmm.. but duroktarz no nose dis! magic i saez

if __name__ == '__main__':
    test = kitty_colorz()
    import pprint
    pprint.pprint(test)
