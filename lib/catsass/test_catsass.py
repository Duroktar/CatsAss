from catsass import (the_cats_ass, PrettyKitty)


def CatsAss():
    # its = [
    #     "The       ",
    #     " cats     ",
    #     "   ass..  ",
    #     "Seriously."
    # ]
    #
    # print(the_cats_ass())
    # print(calico_kitty())

    lyrics = """There's a lady who's sure all that glitters is gold
And she's buying a stairway to heaven.
When she gets there she knows, if the stores are all closed
With a word she can get what she came for.
Ooh, ooh, and she's buying a stairway to heaven.

There's a sign on the wall but she wants to be sure
'Cause you know sometimes words have two meanings.
In a tree by the brook, there's a songbird who sings,
Sometimes all of our thoughts are misgiven."""

    """
    Ooh, it makes me wonder,
    Ooh, it makes me wonder.
    
    There's a feeling I get when I look to the west,
    And my spirit is crying for leaving.
    In my thoughts I have seen rings of smoke through the trees,
    And the voices of those who stand looking.
    
    Ooh, it makes me wonder,
    Ooh, it really makes me wonder.
    
    And it's whispered that soon, if we all call the tune,
    Then the piper will lead us to reason.
    And a new day will dawn for those who stand long,
    And the forests will echo with laughter.
    
    If there's a bustle in your hedgerow, don't be alarmed now,
    It's just a spring clean for the May queen.
    Yes, there are two paths you can go by, but in the long run
    There's still time to change the road you're on.
    And it makes me wonder.
    
    Your head is humming and it won't go, in case you don't know,
    The piper's calling you to join him,
    Dear lady, can you hear the wind blow, and did you know
    Your stairway lies on the whispering wind?
    
    And as we wind on down the road
    Our shadows taller than our soul.
    There walks a lady we all know
    Who shines white light and wants to show
    How everything still turns to gold.
    And if you listen very hard
    The tune will come to you at last.
    When all are one and one is all
    To be a rock and not to roll.
    
    And she's buying a stairway to heaven."""

    print(PrettyKitty("Stairway to Heaven", lyrics.splitlines(),
                      cat='zepcat', logo='led-zep', title='stairway',
                      logo_offset=0, title_start=(10, 45), title_colors='stairway'))

# def test_all():
#     print(calico_kitty())
    # print(schrodingers_cat())
    # print(schrodingers_cat(peek=True))
    # print(poke_the_cat(Cat.ASS, catnip=True))
    # print(comb(the_cats_ass(), 'its'))
    # print(avoid(the_cats_ass(), 'its'))


if __name__ == '__main__':
    # This is really just for visual testing..

    CatsAss()
