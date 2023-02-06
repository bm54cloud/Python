# Define the 'char_range' generator here
def char_range(start, stop, step=1):
    stop_modifier = 1
    start_code = ord(start)
    stop_code = ord(stop)
    
    if start_code > stop_code:
        step *= -1
        stop_modifier *= -1
        
    for value in range(start_code, stop_code + stop_modifier, step):
        yield chr(value)

#Test to verify the implemenation of char_range
# *Do not modify
###############################################

#Ensure that 'char_range' is a generator function
from inspect import isgeneratorfunction

assert isgeneratorfunction(
    char_range
), f"Expected char_range to be a generator function but was not."

# Ensure that the result *does* includes the stop character
assert list(char_range("a", "e")) == [
    "a",
    "b",
    "c",
    "d",
    "e",
], f"Expected ['a', 'b', 'c', 'd', 'e'] but got {repr(list(char_range('a', 'e')))}"
