"""
ID: connorwu3 
LANG: PYTHON3
TASK: milk2
"""
# import unittest

milking = [*map(lambda s: [*map(int, s.rstrip().split(" "))], open("milk2.in", "r").readlines()[1:])]

"""
milking is a list of intervals where farmers are milking cows

if a farmer shift overlaps with another farmer's shift, that is just one combined shift
"""
def milk2(milking: list[list[int]]) -> str:

    # timestamps where at least 1 cow is being milked
    schedule: list[list[int]] = [milking[0]]
    for i in range(1, len(milking)):

        j = 0
        while j < len(schedule):
            overlapped = False

            # beginning of shift overlaps with other shift and makes new shift longer
            if milking[i][0] < schedule[j][1] and milking[i][1] > schedule[j][1]:
                # print(f"begin of farmers shift overlaps")
                # print(f"before: {schedule[j]}")
                schedule[j][1] = milking[i][1]
                # print(f"after: {schedule[j]}\n")
                overlapped = True
            
            # end of shift overlaps with some other shift and makes new shift longer
            if milking[i][1] > schedule[j][0] and milking[i][0] < schedule[j][0]:
                # print(f"end of farmers shift overlaps")
                # print(f"before: {schedule[j]}")
                schedule[j][0] = milking[i][0]
                # print(f"after: {schedule[j]}\n")
                overlapped = True

            # if a new shift is overlapping with any shifts, combine (remove) them
            k = 0
            foundFirstOccurence = False
            while k < len(schedule):
                if milking[i][0] == schedule[k][0] and schedule[k][1] == milking[i][1]:
                    if not foundFirstOccurence:
                        foundFirstOccurence = True
                    else:
                        del schedule[k]
                        k -= 1
                        j -= 1
                k += 1
            in_schedule = False

            for shift in schedule:
                if milking[i][0] == shift[0] and milking[i][1] == shift[1]:
                    in_schedule = True
                    break
            if not overlapped and not in_schedule:
                schedule.append(milking[i])
                break

            j += 1

    print(schedule)
    longest_shift = max([l[1] - l[0] for l in schedule])
    longest_break = max([schedule[i][0] - schedule[i-1][1] for i in range(1, len(schedule))]) if len(schedule) > 1 else 0
    return f"{longest_shift} {longest_break}"

output = milk2(milking)
print(output)
open("milk2.out", "w").write(output + "\n")

def reconstruct_input(matrix: list[list[int]]) -> str:
    return "\n".join([f"{matrix[i][0]} {matrix[i][1]}" for i in range(len(matrix))])

# print(reconstruct_input([[300, 1000], [700, 1200], [1500, 2100]]))

# class TestMilk2(unittest.TestCase): 
 
#     def test_run1(self): 
#         input = [[100, 200]]
#         expected = "100 0"
#         actual = milk2(input)
#         # error message in case if test case got failed 
#         message = f"expected {expected} but got {actual}, input: {reconstruct_input(input)}\n"
#         # assertEqual() to check equality of first & second value 
#         self.assertEqual(expected, actual, message) 

#     def test_run2(self): 
#         input = [[300, 1000], [700, 1200], [1500, 2100]]
#         expected = "900 300"
#         actual = milk2(input)
#         # error message in case if test case got failed 
#         message = f"expected {expected} but got {actual}, input: {reconstruct_input(input)}\n"
#         # assertEqual() to check equality of first & second value 
#         self.assertEqual(expected, actual, message) 

#     def test_run3(self): 
#         input = [[2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19], [1, 20]]
#         expected = "19 0"
#         actual = milk2(input)
#         # error message in case if test case got failed 
#         message = f"expected {expected} but got {actual}, input: {reconstruct_input(input)}\n"
#         # assertEqual() to check equality of first & second value 
#         self.assertEqual(expected, actual, message) 

#     def test_run6(self):
#         input = [[100, 200], [200, 400], [400, 800], [800, 1600], [50, 100], [1700, 3200]]
#         expected = "1550 100"
#         actual = milk2(input)
#         # error message in case if test case got failed 
#         message = f"expected {expected} but got {actual}, input: {reconstruct_input(input)}\n"
#         # assertEqual() to check equality of first & second value 
#         self.assertEqual(expected, actual, message) 


# unittest.main()
