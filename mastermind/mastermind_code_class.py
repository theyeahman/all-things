"""
This script creates a class to store mastermind codes.
Firstly it defines a class colour_choice which specifice each code entry.
It then uses this as part of mastermind_code to form the total code
"""


import random

colour_choices = ["red","blue","yellow","green","black","white"]

def colours_included(num_col):
    colour_choice_now = colour_choices[0:num_col]
    return colour_choice_now

def choose_colour(colours_included):
    return "".join(random.sample(colours_included, 1))

class colour_choice:
    def __init__(self, num_colours , value = ""):
        if not isinstance(num_colours,int):
            raise ValueError("num_colours must be a number")
        elif not ( (num_colours > 1) & (num_colours <= 6) ):
            raise ValueError("num_colours must be between 2 and 6")
        elif not isinstance(value,str):
            raise ValueError("value must be a string")
        colours = colours_included(num_colours)
        if value:
            if value not in colours:
                raise ValueError("""
The value you entered wasn't part of the game:
You entered {}.
The allowed colours are {}""".format(value,colours))
            else:
                self.value = value
        else:
            self.value = choose_colour(colours)


class mastermind_code(list):
    def __init__(self, code_size = 4, numcols = 6,
                col_selection_class = None, code = None, *args, **kwargs):
        if not col_selection_class:
            raise ValueError("You must provide a class to select colours")
        elif not isinstance(code_size,int):
            raise ValueError("code_size must be a number")
        elif not ( (code_size > 1) & (code_size <= 6) ):
            raise ValueError("code_size must be between 2 and 6")
        super().__init__()
        if code:
            if not code_size == len(code):
                raise ValueError("Make sure your entry is the same length as the code you are trying to break!")
            else:
                for i in range(code_size):
                    self.append(col_selection_class(num_colours = numcols,
                    value = code[i]).value)
        else:
            for _ in range(code_size):
                self.append(col_selection_class(num_colours = numcols).value)

"""
code_test1 = mastermind_code(col_selection_class = colour_choice,
                            code = None, numcols = 2)
print(code_test1)

code_test2 = mastermind_code(col_selection_class = colour_choice,
                            code = ["red","blue","purple","green","purple"],
                            code_size = 5)
print(code_test2)
"""
