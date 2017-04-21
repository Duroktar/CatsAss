from catsass import (the_cats_ass, poke_the_cat, comb,
                     avoid, schrodingers_cat, Cat)


def CatsAss():
    its = [
        "The       ",
        " cats     ",
        "   ass..  ",
        "Seriously."
    ]
    print(the_cats_ass())


def test_all():
    print(schrodingers_cat())
    print(schrodingers_cat(peek=True))
    print(poke_the_cat(Cat.ASS, catnip=True))
    print(comb(the_cats_ass(), 'its'))
    print(avoid(the_cats_ass(), 'its'))


if __name__ == '__main__':
    # This is really just for visual testing..

    CatsAss()
