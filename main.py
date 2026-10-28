
# ==============================
# Income Analysis
# ==============================

# Get five income amounts from the user :
income_1 = float(input("Enter income 1: "))
income_2 = float(input("Enter income 2: "))
income_3 = float(input("Enter income 3: "))
income_4 = float(input("Enter income 4: "))
income_5 = float(input("Enter income 5: "))

# Store all income amounts in a list :
income_list = [income_1, income_2, income_3, income_4, income_5]

# Calculate the total income
total_income = sum(income_list)

# Sort incomes from lowest to highest :
income_list.sort()

# Display the income analysis :
print("\n========== INCOME REPORT ==========")
print(f"Total income: {total_income:.2f}")
print(f"Sorted incomes: {income_list}")
print(f"Lowest income: {income_list[0]:.2f}")
print(f"Highest income: {income_list[-1]:.2f}")


# ==============================
# Expense Analysis
# ==============================

# Get five expense amounts from the user :
cost_1 = float(input("Enter expense 1: "))
cost_2 = float(input("Enter expense 2: "))
cost_3 = float(input("Enter expense 3: "))
cost_4 = float(input("Enter expense 4: "))
cost_5 = float(input("Enter expense 5: "))

# Store all expense amounts in a list :
cost_list = [cost_1, cost_2, cost_3, cost_4, cost_5]

# Calculate the total expenses :
total_cost = sum(cost_list)

# Sort expenses from lowest to highest :
cost_list.sort() 

# Display the expense analysis :
print("\n========== EXPENSE REPORT ==========")
print(f"Total expenses: {total_cost:.2f}")
print(f"Sorted expenses: {cost_list}")
print(f"Lowest expense: {cost_list[0]:.2f}")
print(f"Highest expense: {cost_list[-1]:.2f}")


# ==============================
# Final Financial Summary
# ==============================

# Calculate the remaining balance : 
final_balance = total_income - total_cost

# Display the final financial result : 
print("\n========= FINANCIAL SUMMARY =========")
print(f"Total income: {total_income:.2f}")
print(f"Total expenses: {total_cost:.2f}")
print(f"Final balance: {final_balance:.2f}")
print("I’m Farbod, and I completed this project using everything I’ve learned so far ...")
