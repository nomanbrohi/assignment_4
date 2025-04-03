# Write a program that reads a year from the user and tells whether a given year is a leap year or not.

# A leap year (also known as an intercalary year or bissextile year) is a calendar year that contains an additional day (or, in the case of a lunisolar calendar, a month) added to keep the calendar year synchronized with the astronomical year or seasonal year. In the Gregorian calendar, each leap year has 366 days instead of 365, by extending February to 29 days rather than the common 28.

# In the Gregorian calendar, three criteria must be checked to identify leap years:

# The given year must be evenly divisible by 4;
# If the year can also be evenly divided by 100, it is NOT a leap year; unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# Your code should use the above criteria to check for a leap year and then print either "That's a leap year!" or "That's not a leap year."



def main():
    #Check this requirement for leap year

#     1. if Year is Divisible by 4 (that's a leap year)
#     2. if Year is not Divisible by 100 (that's not a leap year)
#     3. or if Year is also Divisilbe by 400 (that's also a leap year)

#   year % 4 == 0 → Check if the year is divisible by 4
#   year % 100 != 0 → Ensure it is NOT divisible by 100
#   year % 400 == 0 → If it is divisible by 100, then it must also be divisible by 400
    
    while True:
        user_input = input("Please Enter Year or press 'Enter' for exit: ").strip()
        if user_input == "":
            print('progarm exit.')
            break 
        year = int(user_input)
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print(f"{year} is a leap Year.\n")
        else:
            print(f"{year} is not a leap Year.\n")

if __name__ == "__main__":
    main()