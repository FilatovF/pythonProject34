"""Task1"""
favmovie = 'Nu pogodi'


def my_fav_movie(fav_movie):
    print(f'My favorit movie is {fav_movie}')


my_fav_movie(favmovie)

"""Task2"""

"""Task3"""


def calculator(i, i0, *args):
    rezult = i0
    for v in args:
        if i == "+":
            rezult += v
        if i == '-':
            rezult -= v
        if i == '*':
            rezult *= v
    return rezult

calculator('+', 3, 4, 5)
