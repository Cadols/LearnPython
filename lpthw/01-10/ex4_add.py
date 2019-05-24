#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 100 cars.
cars = 100
# How many people in each car.
space_in_a_car = 4
# How many drivers.
drivers = 30
# How many passengers
passengers = 90
# How many cars did not been driven.
cars_not_driven = cars - drivers
# How many cars had been driven
cars_driven = drivers
# How many people that can be transport today.
carpool_capacity = cars_driven * space_in_a_car
# How many people in each car.
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")