"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In:
# The user enters a marketing campaign name, a marketing
# channel and a budget in euros.

# 2. Process:
# I check that the name and channel are not empty.
# I check that the budget is a positive number.
# I create the CSV header if the file is new or empty.
# I add each new campaign without deleting previous rows.

# 3. Out, file name and columns:
# The file is named 7.0_marketing_budgets.csv.
# The columns are campaign_name, channel and budget_eur.

# 4. Why these columns, and what this file is for:
# I chose these columns to track marketing campaign spending.
# With 200 rows, I could compare budgets by channel
# and plan future marketing campaigns.



# Your code below
import csv
import math
from pathlib import Path

# Choose the output file
output_file = Path(__file__).resolve().parent / "7.0_marketing_budgets.csv"

columns = ["campaign_name", "channel", "budget_eur"]


# Ask for text and reject empty answers
def ask_text(question):
    while True:
        answer = input(question).strip()

        if answer:
            return answer

        print("Please enter a value. It cannot be empty.")


# Ask for a valid budget
def ask_budget():
    while True:
        answer = input("Budget in euros: ").strip()
        answer = answer.replace(",", ".")

        try:
            budget = float(answer)

        except ValueError:
            print("Please enter a valid number.")
            continue

        if not math.isfinite(budget) or budget <= 0:
            print("The budget must be a positive number.")
            continue

        return budget


# Collect the information
campaign_name = ask_text("Campaign name: ")
channel = ask_text("Marketing channel: ")
budget_eur = ask_budget()


# Check if the file needs a header
needs_header = (
    not output_file.exists()
    or output_file.stat().st_size == 0
)


# Save the information in the CSV file
with output_file.open("a", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    if needs_header:
        writer.writerow(columns)

    writer.writerow([
        campaign_name,
        channel,
        f"{budget_eur:.2f}"
    ])


# Display confirmation
print("Campaign saved to:", output_file.name)


# CHECK IT YOURSELF

# Test 1: Back to School, Instagram, 1200
# Test 2: Winter Sale, Google Search, 850
# Test 3: Newsletter, Email, 1500

# Expected result after three runs:
# The CSV contains 4 lines.
# There is one header and three campaign entries.
# Previous entries are not deleted.
