"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

import time 
def frequencies(items):
    new_frequencies = {}
    for item in items:
        if str(item) in new_frequencies:
            new_frequencies[str(item)] += 1
        else:
            new_frequencies[str(item)] = 1      
    return new_frequencies