#!/usr/bin/python3
"""
import modules
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import pep8


class Testrectangle(unittest.TestCase):
    """
    test class
    """
    def test_pep8_base(self):
        """
        checks pep8
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/rectangle.py'])
        self.assertEqual(
                check.total_errors, 0,
                "Found code style errors (and warnings)"
                )

    def test_rectangle_subclass(self):
        """
        Test if Rectangle class inherit from
        Base class
        """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_parameters(self):
        """
        Test parameters for Rectangle class
        """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.id, 4)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.id, 5)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

        with self.assertRaises(TypeError):
            r4 = Rectangle()

        def test_type_parameter(self):
        """
        Test different types of parameters
        for a Rectangle class
        """
        with self.assertRaises(TypeError):
            Rectangle(1.23, 3)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(-1234, 56)
            raise ValueError()

        with self.assertRaises(TypeError):
            Rectangle('', 2)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(True, 3)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(1, 2.34)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, "Hello")
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(6, False)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(5, -123456)
            raise ValueError

        with self.assertRaises(TypeError):
            Rectangle(1, 2, 1.50)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, 6, "test")
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, 7, False)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(5, 7, -4798576)
            raise ValueError()

        with self.assertRaises(TypeError):
            Rectangle(5, 1, 1, 1.23)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, 6, 5, "test")
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, 7, 7, False)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(5, 9, 5, -576398576)
            raise ValueError()

    def test_string(self):
        """
        Test string parameters for a
        Rectangle class
        """
        with self.assertRaises(TypeError):
            Rectangle('Monty', 'Python')

