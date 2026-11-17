"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.


ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

#1. In:
# My function receives a list of marketing budgets.
# These budgets come from my exercise 4.0.

# 2. Process:
# The function adds all the budgets together.
# Then it divides the total by the number of budgets.
# This gives the average marketing budget.

# 3. Out:
# The function returns the average marketing budget.
# If the list is empty, it returns None.

# 4. My function name, and why return rather than print:
# My function is called calculate_average_budget.
# This name clearly explains what the function does.
# It calculates the average marketing budget.
# I use return because I can use the result again.
# Print only shows the result on the screen.



# Your code below
def calculate_average_budget(budget_list):
    # Check if the list is empty
    if len(budget_list) == 0:
        return None

    # Calculate the average budget
    average = sum(budget_list) / len(budget_list)

    # Return the result
    return average


# My marketing budgets from exercise 4.0
budgets = [1200, 850, 1500, 950, 2000, 1100, 750, 1350]


# Test 1: Average of all budgets
result1 = calculate_average_budget(budgets)
print("Average of all budgets:", result1)


# Test 2: Average of the first four budgets
result2 = calculate_average_budget(budgets[:4])
print("Average of the first four budgets:", result2)


# Test 3: Average of the last four budgets
result3 = calculate_average_budget(budgets[4:])
print("Average of the last four budgets:", result3)


# CHECK IT YOURSELF

# Test with an empty list
empty_result = calculate_average_budget([])
print("Average of an empty list:", empty_result)

# The result is None because the list is empty.
# This is acceptable because an empty list has no average.
# It also avoids dividing by zero.

