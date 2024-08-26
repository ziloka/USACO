"""
ID: connorwu3 
LANG: PYTHON3
TASK: milk2
"""
import unittest
from typing import Optional
from functools import reduce

milking = [*map(lambda s: [*map(int, s.rstrip().split(" "))], open("milk2.in", "r").readlines())][1:]
print(milking)

def diff(l: list[int]) -> int:
    return reduce(lambda a, b: b-a, l) if l != None else 0

def milk2(milking: list[list[int]]) -> str:
    duration_min_1_cow_milked = [milking[0][0], milking[0][1]]
    duration_time_no_cows_milked: Optional[list[int]] = None
    for i in range(1, len(milking)):
        (start, end) = milking[i]
        last_end = milking[i-1][1] 

        is_farmers_milking_overlap = last_end > start
        longest_continuous_milking_duration = diff(duration_min_1_cow_milked)
        candidate_continuous_milking_duration = end - duration_min_1_cow_milked[0]
        if is_farmers_milking_overlap and longest_continuous_milking_duration < candidate_continuous_milking_duration:
            duration_min_1_cow_milked[1] = end

        if duration_time_no_cows_milked == None:
            if not is_farmers_milking_overlap and last_end < start:
                duration_time_no_cows_milked = [last_end, start]
        else:
            longest_time_no_cows_milked = diff(duration_time_no_cows_milked)
            candidate_time_no_cows_milked = start - duration_time_no_cows_milked[0]
            if not is_farmers_milking_overlap and last_end < start and longest_time_no_cows_milked < candidate_time_no_cows_milked:
                duration_time_no_cows_milked[0] = last_end
                duration_time_no_cows_milked[1] = start
    return f"{diff(duration_min_1_cow_milked)} {diff(duration_time_no_cows_milked)}"
# print(duration_time_no_cows_milked)

output = milk2(milking)
print(output)
open("milk2.out", "w").write(output + "\n")

class TestMilk2(unittest.TestCase): 
 
    def test_run1(self): 
        input = [[100, 200]]
        expected = "100 0"
        actual = milk2(input)
        # error message in case if test case got failed 
        message = f"expected {expected} but got {actual}, input: {input}\n"
        # assertEqual() to check equality of first & second value 
        self.assertEqual(expected, actual, message) 

    def test_run2(self): 
        input = [[300, 1000], [700, 1200], [1500, 2100]]
        expected = "900 300"
        actual = milk2(input)
        # error message in case if test case got failed 
        message = f"expected {expected} but got {actual}, input: {input}\n"
        # assertEqual() to check equality of first & second value 
        self.assertEqual(expected, actual, message) 

    def test_run3(self): 
        input = [[2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19], [1, 20]]
        expected = "19 0"
        actual = milk2(input)
        # error message in case if test case got failed 
        message = f"expected {expected} but got {actual}, input: {input}\n"
        # assertEqual() to check equality of first & second value 
        self.assertEqual(expected, actual, message) 

unittest.main()