import random   # as rand   # when the name of a module is too long we can use short form of it  |||   == from random import *
#from random import randint, choice     # when you want some definitions from a library
#from random import randint as rit, choice as chys      --> some def and short form

print( random.randint(1, 100) )

Gifts = [' ', 'Bicycle', 'Gold', 'BMW 520i', '$ 40 M']
print( random.choice(Gifts) )

#import calculator
#print( calculator.main (23, 12, '+') )

import termcolor
print( termcolor.colored("I have color now", 'black') )
print( termcolor.colored("I have color now", 'blue') )
print( termcolor.colored("I have color now", 'light_grey') )
print( termcolor.colored("I have color now", 'white') )
print( termcolor.colored("I have color now", 'yellow') )

import sys

text = termcolor.colored("Hello, World!", "red", attrs=["reverse", "blink"])
print(text)
termcolor.cprint("Hello, World!", "green", "on_red")

print_red_on_cyan = lambda x: termcolor.cprint(x, "red", "on_cyan")
print_red_on_cyan("Hello, World!")
print_red_on_cyan("Hello, Universe!")

import calendar
print( termcolor.colored( calendar.calendar(2024, 2, 1, 6, 3), "light_cyan" ) )

#help(termcolor)

import pyfiglet

print( termcolor.colored(pyfiglet.figlet_format("Haj Rezvan"), "dark_grey" ) )
print( termcolor.colored( pyfiglet.figlet_format("1403-04-27"), "light_yellow" ) )

print("\n---------------------------------------")

from functions import Say_Hello

def say_name () :
    print( f"__name__ in function is {__name__}" )

say_name()
Say_Hello()