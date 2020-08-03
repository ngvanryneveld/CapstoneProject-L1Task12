
# this is used to import math functions into the program
import math

# request user input of which calculation they are wanting with an explanation of both options
calculation_needed = input("""Choose either 'investment' or 'bond' from the menu below to proceed:
investment\t - to calculate the amount of interest you'll earn on investments
bond \t\t - to calculate the amount you'll have to pay monthy on a home loan

""")


# this while statement means that if anything other than the two options offered are inputted, the user will be asked to input until they input the words correctly,
# the input is not case sensitive as the lowercase function is made us of in the while statement
while calculation_needed.lower() != "investment" and calculation_needed.lower() != "bond":
    calculation_needed = input("You have not entered from the menu below. Please enter your choice again: ")

# lowercase the input in order to allow the user to input without causing an error because of case sensitivity in running the program
calculation_needed = calculation_needed.lower()

# first if statement to capture if investment is the option selected
if calculation_needed == "investment":

# using while true, try and except ValueError to ensure that the inputted value is indeed a figure and not other characters that would cause an error in running the program
    while True:
        principal_amount = input("Enter the deposit amount (in R): ")
        try:
            principal_amount = float(principal_amount)
            break;
        except ValueError:
            print("This is an invalid deposit.")

# using while true, try and except ValueError to ensure that the inputted value is indeed a figure and not other characters that would cause an error in running the program
    while True:
        interest_rate = input("Enter the interest rate (as percentage): ")
        try:
            interest_rate = float(interest_rate)
            interest_rate = interest_rate / 100
            break;
        except ValueError:
            print("This is an invalid interest rate.")

# using while true, try and except ValueError to ensure that the inputted value is indeed a figure and not other characters that would cause an error in running the program
    while True:
        number_of_years = input("Enter the number of years you plan to invest for: ")
        try:
            number_of_years = float(number_of_years)
            break;
        except ValueError:
            print("This is an invalid number of years.")

# this interest variable will affect which calculation occurs between simple and compound, when doing the investment total return
    interest = input("Enter your preference between 'simple' and 'compound' interest: ")
    while interest.lower() != "simple" and interest.lower() != "compound":
        interest = input("Please enter only either 'simple' or 'compound'")
    
    interest = interest.lower()

# this nested if and elif statements are two options that can be further selected thorugh inputs from the user and are the two different investment options and presents approapriate message
    if interest == "simple":
        total_investment_return = principal_amount * (1 + interest_rate * number_of_years)
        print("Your total simple investment return at the end of " + str(int(number_of_years)) + " years is R" + str(round(total_investment_return, 2)))

    elif interest == "compound":
        total_investment_return = principal_amount * math.pow((1 + interest_rate), number_of_years)
        print("Your total compound investment return at the end of " + str(int(number_of_years)) + " years is R" + str(round(total_investment_return, 2)))

# this elif statement occurs when the option of bond is inputted by the user
elif calculation_needed == "bond":

# using while true, try and except ValueError to ensure that the inputted value is indeed a figure and not other characters that would cause an error in running the program
    while True:
        house_present_value = input("Enter the present value of the house (in R): ")
        try:
            house_present_value = float(house_present_value)
            break;
        except ValueError:
            print("This is an invalid present value of the house.")

# using while true, try and except ValueError to ensure that the inputted value is indeed a figure and not other characters that would cause an error in running the program
    while True:
        interest_rate = input("Enter the monthly interest rate (as percentage): ")
        try:
            interest_rate = float(interest_rate)
            interest_rate = interest_rate / 100
            break;
        except ValueError:
            print("This is an invalid interest rate.")

# using while true, try and except ValueError to ensure that the inputted value is indeed a figure and not other characters that would cause an error in running the program
    while True:
        number_of_months_repayment = input("Enter the number of months planned for repayment: ")
        try:
            number_of_months_repayment = float(number_of_months_repayment)
            break;
        except ValueError:
            print("This is an invalid number of months for repayment.")

# this is the calculation used in order to determine the monthly bond repayments with the approapriate varaibles being inputted and appropriate message being outputted
    monthly_bond_repayments = (interest_rate * house_present_value) / (1 - math.pow((1 + interest_rate), -number_of_months_repayment))
    print("Your monthly bond repayments will be R" + str(round(monthly_bond_repayments, 2)) + " for " + str(int(number_of_months_repayment)) + " months")
