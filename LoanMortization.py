import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import MaxNLocator

# Function to calculate loan amortization details
def calculate_amortization_schedule(loan_amount, loan_term, annual_interest_rate):
    monthly_interest_rate = annual_interest_rate / 1200
    monthly_payment = loan_amount * ((monthly_interest_rate*(1+monthly_interest_rate)**(loan_term))/((1+monthly_interest_rate)**(loan_term) - 1))
    
    amortization_schedule = []
    remaining_balance = loan_amount
    total_payments = 0
    
    for month in range(1, loan_term + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        remaining_balance -= principal_payment
        total_payments += monthly_payment
        amortization_schedule.append((month, remaining_balance, interest_payment, principal_payment, monthly_payment))
    
    return amortization_schedule, monthly_payment, total_payments

def amortization_table(amortization_schedule): 
    print("\nAmortization Schedule: ")
    print(f"{'Month' :<6} {'Remaining Balance' :<20} {'Interest Payment':<18} {'Principal':<20} {'Monthly Payment':<15}")
    for month, remaining, interest, total, payment in amortization_schedule:
        print(f"{month:<6} {remaining:20.2f} {interest:18.2f} {total: 20.2f} {payment:15.2f}")

def plot_amortization_graph(amortization_schedule): 
    months, remaining_balances, interest_payments, principal_payments, monthly_payment = zip(*amortization_schedule)
    accumulated_payments = [sum(monthly_payment[:i+1]) for i in range(len(monthly_payment))]
    accumulated_interest = [sum(interest_payments[:i+1]) for i in range(len(interest_payments))]
    
    plt.figure(figsize=(14, 10))
    plt.plot(months, remaining_balances, '-o', label = 'Remaining Balance', markersize = 4, linewidth = 1)
    plt.plot(months, accumulated_interest, '-s', label = 'Interest Payment', markersize = 1, linestyle = '--', linewidth = 1)
    plt.plot(months, accumulated_payments, '-^', label = 'Accumulated Payment', markersize=4, linestyle='-.', linewidth = 1)
    
    plt.title('Loan Amortization Schedule', fontsize = 16)
    plt.xlabel('Month', fontsize =14)
    plt.ylabel('Amount ($)', fontsize = 14)
    plt.legend(fontsize=12)
    plt.grid(False)
    plt.xlim(0, len(months))
    plt.ylim(0, max(max(remaining_balances), max(interest_payments), max(total_payments)) * 1.1)

    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(int(len(months)/10)))
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True, nbins=10, prune='lower'))

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def payment_details(monthly_payment, loan_term, loan_amount, interest_payments):
    monthly_detail = monthly_payment[-1] if monthly_payment else 0
    accumulated_interest = [sum(interest_payments[:i+1]) for i in range(len(interest_payments))]
    total_interest = accumulated_interest[-1] if accumulated_interest else 0
    total_paid = monthly_detail * loan_term

    print(f"\nLoan Summary: ")
    print(f"Total Loan Amount: ${loan_amount:,.2f}")
    print(f"Total Interest Paid: ${total_interest:,.2f}")
    print(f"Monthly Payment: ${monthly_detail:,.2f}")
    print(f"Total Paid: ${total_paid:,.2f}")

# Ask user for input values
loan_amount = float(input("Enter the total loan amount: ")) 
loan_term = int(input("Enter the length of the loan in months: "))
annual_interest_rate = float(input("Enter the annual interest rate (as a percent): "))

amortization_schedule, total_payments, monthly_payments = calculate_amortization_schedule(loan_amount, loan_term, annual_interest_rate)
months, remaining_balances, interest_payments, total_payments, monthly_payment = zip(*amortization_schedule)


while True:
    print("\nHow would you like to display the data: ")
    print("1. Table")
    print("2. Line Graph")
    print("3. Display loan details")
    user_choice = input("Enter your selection(0 to quit): ")
    if user_choice == "1":
        amortization_table(amortization_schedule)
    elif user_choice == "2":
        plot_amortization_graph(amortization_schedule)
    elif user_choice == "3":
        payment_details(monthly_payment, loan_term, loan_amount, interest_payments)
    elif user_choice =="0":
        print("Exiting Program")
        break
    else:
        print("Invalid Choice. Select an option 1, 2, 3, or 4")