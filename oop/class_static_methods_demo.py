#!/usr/bin/env python3
"""
A Python module demonstrating the difference between
class methods and static methods using a Calculator class.
"""

class Calculator:
    """A simple Calculator class showcasing static and class methods."""

    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method that returns the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method that returns the product of two numbers."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
