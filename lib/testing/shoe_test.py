#!/usr/bin/env python3

from shoe import Shoe
import io
import sys

class TestShoe:
    '''Shoe in shoe.py'''

    def test_has_brand_and_size(self):
        '''has the brand and size passed to __init__, and values can be set to new instance.'''
        stan_smith = Shoe("Adidas", "model", 9, "color")  # Corrected the arguments
        assert stan_smith.brand == "Adidas"
        assert stan_smith.size == 9

    def test_requires_int_size(self):
     '''prints "size must be an integer" if size is not an integer.'''
    stan_smith = Shoe("Adidas", "model", 9, "color")  # Corrected the arguments
    captured_out = io.StringIO()
    try:
        stan_smith.size = "not an integer"
    except TypeError as e:
        assert str(e) == "Size must be an integer."
    assert captured_out.getvalue() == ""


    def test_can_cobble(self):
        '''says that the shoe has been repaired.'''
        stan_smith = Shoe("Adidas", "model", 9, "color")  # Corrected the arguments
        captured_out = io.StringIO()
        sys.stdout = captured_out
        stan_smith.cobble()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Your shoe is as good as new!\n"
    
    def test_cobble_makes_new(self):
        '''creates an attribute on the instance called 'condition' and set equal to 'New' after repair.'''
        stan_smith = Shoe("Adidas", "model", 9, "color")  # Corrected the arguments
        stan_smith.cobble()
        assert stan_smith.condition == "New"
