#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Add digit 10 in the setense.
x = "There are %d types of people." % 10
# Define variables "binary" and "do_not".
binary = "binary"
do_not = "don't"
# Add "binary" and "do_not" in the variable "y".
y = "Those who know %s and those who %s." % (binary, do_not)

# Print x and y.
print(x)
print(y)

# Print these two sentenses with x and y.
print("I said: %r." % x)
print("I also said: '%s'." % y)

# Define hilarious is False.
hilarious = False
# Define joke_... has this sentense.
joke_evaluation = "Isn't that joke so funny?! %r"

# Print it.
print(joke_evaluation % hilarious)

# Define two variables.
w = "This is the left side of..."
e = "a string with a right side."

# Print them together.
print(w + e)
