#!/usr/bin/env python3
"""
A Python module demonstrating polymorphism and method overriding
using Shape, Rectangle, and Circle classes.
"""

import math


class Shape:
    """Base class representing a generic shape."""

    def area(self):
        """
        Method to calculate area.
        Must be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement the area() method.")


class Rectangle(Shape):
    """Derived class representing a rectangle."""

    def __init__(self, length: float, width: float):
        """
        Initializes a Rectangle instance.
        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self) -> float:
        """
        Calculates and returns the area of the rectangle.
        Returns:
            float: The area of the rectangle (length × width).
        """
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle."""

    def __init__(self, radius: float):
        """
        Initializes a Circle instance.
        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self) -> float:
        """
        Calculates and returns the area of the circle.
        Returns:
            float: The area of the circle (π × radius²).
        """
        return math.pi * (self.radius ** 2)
