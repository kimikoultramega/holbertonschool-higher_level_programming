#!/usr/bin/env python3

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def permieter(self):
        pass

import math

class Circle(Shape):

    def __init__(self, radius):

        if radius < 0:
            radius = abs(radius)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def permieter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def permieter(self):
        return (self.width * 2) + (self.height * 2)

    def shape_info(shape):
        area = shape.area()
        perimeter = shape.perimeter()

        print(f"Area: {shape.area()}")
        print(f"Perimeter: {shape.permieter()}")
