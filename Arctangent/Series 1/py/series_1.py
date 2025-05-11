from decimal import Decimal
from time import perf_counter
from math import atan

iterationCounter: int = 1
approximation: Decimal = 0
previous: Decimal = 0
finalAccuracy: int = 0
totalComputationTime: float = 0
iterationStartTime: float = 0
iterationEndTime: float = 0
a_values: list[float] = [pow(2, 1/2)]
x_copy: int = 0

def a_k(num: int) -> float:
    result: float = 0

    result = pow(a_values[-1] + 2, 1/2)

    a_values.append(result)
    if num != 2: a_values.pop(0)

    return result

try: x: int = int(input("Enter a value for 'x': "))
except ValueError: x = "" # Setting 'x' to a non-integer ensures that the below check fails and the execution flow is transferred to the else statement at the bottom.

flag: bool = isinstance(x, int) and x >= 2
if flag:

    x_copy = x
    if x != 2:
        for i in range(2, x): a_k(i)

    while True:

        iterationStartTime = perf_counter()

        a_k(x)
        approximation += pow(2, x_copy) * Decimal(atan(pow(2 - a_values[0], 1/2) / a_values[-1]))

        iterationEndTime = perf_counter()

        print(f"\nIteration {iterationCounter}")
        print(f"Approximation = {approximation}")

        for i, char in enumerate("3.141592653589793238462643383279502884197169399375"): # using str(pi) instead of writing the whole string like I have done here somehow displays a different number??? idk
            if char != str(approximation)[i]:
                if i < 2: print("No accurate decimal places")
                else:
                    print(f"{i - 2} correct decimal place(s)")
                    finalAccuracy = i - 2
                break

        print(f"Iteration duration: {iterationEndTime - iterationStartTime}  seconds")
        totalComputationTime += iterationEndTime - iterationStartTime

        deviation: Decimal = Decimal(approximation - previous)
        if deviation == 0 and iterationCounter == 1:
            print("\nThe entered value is too large.\n")
            break
        if deviation == 0: 
            print("Negligible deviation (terminating the program)\n")
            break
        elif deviation != approximation: print(f"Deviation from previous iteration: {deviation}") # this if-statement prevents a deviation from being shown during the first iteration.

        previous = approximation
        iterationCounter += 1
        x += 1

else:
    print("\nx must be a natural number >= 2.\n")

if flag and iterationCounter != 1: print(f"\n\nComputed {finalAccuracy} correct decimal places in {totalComputationTime} seconds and {iterationCounter} iterations.\n")