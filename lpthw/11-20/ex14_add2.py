#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

script, user_name, user_age = argv
prompt = '> '

print("Hi %s, I'm the %s script." % (user_name, script))
print("Oh, you're %r years old." % user_age)
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = input(prompt)

print("Where do you live %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer))
