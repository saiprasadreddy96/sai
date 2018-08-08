"""
assignment 3
"""
def paying_debt_off_in_a_year(balance, annual_interest_rate):
    """# In short:
    # Monthly interest rate = (Annual interest rate) / 12.0
    # Monthly payment lower bound = Balance / 12
    # Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0
    # Write a program that uses these bounds and bisection search (for more info check
     out the Wikipedia page on bisection search) to find
    # the smallest monthly payment to the cent (no more multiples of $10) such that we
     can pay off the debt within a year. Try it out with
    # large inputs, and notice how fast it is (try the same large inputs in your solution to Problem
     2 to compare!). Produce the same return
    # value as you did in Assignment 2."""
    monthly_interest_rate = (annual_interest_rate) / 12.0
    monthly_payment_lower_bound = balance / 12
    monthly_payment_upper_bound = (balance * (1 + monthly_interest_rate)**12) / 12.0
    new_balance = balance
    epsilon = 0.0001
    guess = (monthly_payment_lower_bound + monthly_payment_upper_bound)/2
    while True:
        month = 1
        while month <= 12:
            new_balance = new_balance - guess
            new_balance = new_balance + (monthly_interest_rate * new_balance)
            month += 1
        if new_balance > 0 and new_balance > epsilon:
            monthly_payment_lower_bound = guess
            new_balance = balance
        elif new_balance < 0 and new_balance < -epsilon:
            monthly_payment_upper_bound = guess
            new_balance = balance
        else:
            return guess

        guess = (monthly_payment_lower_bound + monthly_payment_upper_bound)/2
def main():
    """ it is a main function"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment: " + str(round(paying_debt_off_in_a_year(data[0], data[1]), 2)))
if __name__ == "__main__":
    main()
