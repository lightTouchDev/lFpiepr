#!/usr/bin/python3

# Write a program that reverses every other letter of a given string
# Ex. Hello -> eHllo | World -> oWlrd

from itertools import zip_longest

## With import
def flipper(word):
    w = word[::2]
    x = word[1::2]

    r = ''
    for i,a in zip_longest(x,w, fillvalue=''):
        r += i
        r += a

    print(r)

flipper('Hello')

## w/out import
def flip(word):

    r = ''
    for i in range(1,len(word), 2):
        r += word[i]
        r += word[i - 1]

    if len(word) % 2 != 0:
        r += word[ -1 ]
    
    print(r)

flip('Hello')

#---------------------------------
## Failed attempts

# only works for words with 5+ letters
# def flip(word):
#     l = [word[i] for i in range(1,len(word),2)]
#     f = [word[i] for i in range(0,len(word),2)]

#     for i in l:
#         f.insert(l.index(i) + -3,i)

#     print(f)

# flip('World')

# Works with strings of even number, else leaves off final element
# def flipper(word):
#     w = word[::2]
#     x = word[1::2]

#     r = ''
#     for i in range(len(x)) or range(len(w)):
#         if len(word) % 2 == 0:
#             r += x[i] + w[i]
#         else:
#             r += x[i] + w[i]
#             r += word[-1]
    
#     print(r)

# flipper('world')
