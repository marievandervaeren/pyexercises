"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# My program receives a list of marketing budgets.
# I use the same budgets as in exercise 4.0.


# 2. Process, function by function:
# The first function calculates the average budget.
# The second function selects budgets above the average.
# The third function adds the selected budgets.
# The fourth function uses these three functions together.


# 3. Out:
# The program returns the total of the marketing
# budgets that are above the average.


# 4. The question my fourth function answers:
# What is the total of the budgets above the average?
# I use three small functions because each has one job.
# This makes the code easier to understand and test.
# I can check each function separately.


# Your code below


# My marketing budgets from exercise 4.0
budgets = [1200, 850, 1500, 950, 2000, 1100, 750, 1350]


# FUNCTION 1: Calculate the average budget
def calculate_average(budget_list):
    # Check if the list is empty
    if len(budget_list) == 0:
        return None

    # Calculate the average
    average = sum(budget_list) / len(budget_list)
    return average


# FUNCTION 2: Select budgets above the average
def select_high_budgets(budget_list, average):
    # Create a list of budgets above the average
    high_budgets = []

    for budget in budget_list:
        if budget > average:
            high_budgets.append(budget)

    return high_budgets


# FUNCTION 3: Calculate the total budget
def calculate_total(budget_list):
    # Add all budgets in the list
    total = sum(budget_list)
    return total


# CHECK IT YOURSELF
# Test each small function separately


# Test 1: Calculate the average
# Input: [1200, 2000]
# Expected output: 1600.0
test1 = calculate_average([1200, 2000])
print("Test 1 - Average:", test1)


# Test 2: Select budgets above the average
# Input: [1200, 850, 1500], average = 1000
# Expected output: [1200, 1500]
test2 = select_high_budgets([1200, 850, 1500], 1000)
print("Test 2 - High budgets:", test2)


# Test 3: Calculate the total
# Input: [1500, 2000, 1350]
# Expected output: 4850
test3 = calculate_total([1500, 2000, 1350])
print("Test 3 - Total:", test3)


# FUNCTION 4: Use the three functions together
def total_above_average(budget_list):

    # Step 1: Calculate the average
    average = calculate_average(budget_list)

    # Check if the list is empty
    if average is None:
        return 0

    # Step 2: Select budgets above the average
    high_budgets = select_high_budgets(budget_list, average)

    # Step 3: Calculate their total
    total = calculate_total(high_budgets)

    # Return the final result
    return total


# FINAL TEST: Use the fourth function
result = total_above_average(budgets)

print("Total of budgets above the average:", result)


# The average marketing budget is 1212.5.
# The budgets above the average are 1500, 2000 and 1350.
# Their total is 4850.
# The program gives the expected result.
