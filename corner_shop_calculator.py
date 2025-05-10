# Display price of items
Bubblegum = 2
Toffee = 0.2
Ice_ream = 5
Milk_chocolate = 4
Doughnut = 2.5
Pancake = 3.2

print("Prices:")
print("Bubblegum: $", Bubblegum)
print("Toffee: $", Toffee)
print("Ice cream: $", Ice_ream)
print("Milk chocolate: $", Milk_chocolate)
print("Doughnut: $", Doughnut)
print("Pancake: $", Pancake)

print()

# Display income after 1 month shop open
sum_Bubblegum = 202
sum_Toffee = 118
sum_Ice_cream = 2250
sum_Milk_chocolate = 1680
sum_Doughnut = 1075
sum_Pancake = 80
total_income = sum_Bubblegum + sum_Toffee + sum_Ice_cream + sum_Milk_chocolate + sum_Doughnut + sum_Pancake

print("Earned amount:")
print("Bubblegum: $", sum_Bubblegum)
print("Toffee: $", sum_Toffee)
print("Ice cream: $", sum_Ice_cream)
print("Milk chocolate: $", sum_Milk_chocolate)
print("Doughnut: $", sum_Doughnut)
print("Pancake: $", sum_Pancake)


print("Income: $", total_income)

staff_expenses = int(input("Staff expenses: "))
print("Staff expenses: $", staff_expenses)

other_expenses = int(input("Other expenses: "))
print("Other expenses: $", other_expenses)

net_income = total_income - staff_expenses - other_expenses
print("Net income: $", net_income)


