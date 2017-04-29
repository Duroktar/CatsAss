import os

from catsass import (the_cats_ass, PrettyKitty)


def CatsAss():
    its = [
        "The       ",
        " cats     ",
        "   ass..  ",
        "Seriously."
    ]

    print(the_cats_ass())

import ast
import requests


def ZepCat():

    cachefile = 'temp.data'

    if os.path.exists(cachefile):
        with open(cachefile, 'r') as fp:
            data = ast.literal_eval(fp.read())
    else:

        artist = "Led Zeppelin"
        track = "Stairway to heaven"

        url = f"http://lyric-api.herokuapp.com/api/find/{artist}/{track}"
        response = requests.get(url)
        if response.status_code != 200:
            return 1

        with open(cachefile, 'w') as fs:
            fs.write(response.text)
            data = ast.literal_eval(response.text)

    lyrics = data.get('lyric')
    print(PrettyKitty("Stairway to Heaven", locals(),
                      cat='zepcat', logo='led-zep', title='stairway',
                      logo_offset=-4, title_start=(10, 45), title_colors='stairway',
                      data_offset=-7))


def Gecko():
    quote = \
        "PjMasks,            " \
        "\n" \
        "  all shout hooray! " \
        "\n" \
        "Cause in the night, " \
        "\n" \
        "  we save the day!  "

    print(PrettyKitty("PjMasks", "",
                      cat='gecko', logo='pjmasks', title='gecko',
                      logo_offset=12, title_start=(10, 55), title_colors='gecko',
                      coat='gecko', logo_colors='pjmasks', data_offset=-7))


def CatBoy():
    quote = \
        "PjMasks,            " \
        "\n" \
        "  all shout hooray! " \
        "\n" \
        "Cause in the night, " \
        "\n" \
        "  we save the day!  "

    print(PrettyKitty("PjMasks", "",
                      cat='catboy', logo='pjmasks', title='catboy',
                      logo_offset=4, title_start=(10, 55), title_colors='catboy',
                      coat='catboy', logo_colors='pjmasks', data_offset=-7))

def Owlette():
    quote = \
        "PjMasks,            " \
        "\n" \
        "  all shout hooray! " \
        "\n" \
        "Cause in the night, " \
        "\n" \
        "  we save the day!  "

    print(PrettyKitty("PjMasks", "",
                      cat='owlette', logo='pjmasks', title='owlette',
                      logo_offset=6, title_start=(10, 55), title_colors='owlette',
                      coat='owlette', logo_colors='pjmasks', data_offset=-7))


# def test_all():
#     print(calico_kitty())
    # print(schrodingers_cat())
    # print(schrodingers_cat(peek=True))
    # print(poke_the_cat(Cat.ASS, catnip=True))
    # print(comb(the_cats_ass(), 'its'))
    # print(avoid(the_cats_ass(), 'its'))


if __name__ == '__main__':
    # This is really just for visual testing..
    import time
    ZepCat()
    while True:
        try:
            Gecko()
            time.sleep(2)
            CatBoy()
            time.sleep(2)
            Owlette()
            time.sleep(2)
        except KeyboardInterrupt:
            break
