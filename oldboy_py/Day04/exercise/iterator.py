#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Iterable
from collections import Iterable
print(isinstance([], Iterable))
print(isinstance((), Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

# Iterator
