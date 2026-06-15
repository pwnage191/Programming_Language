'''2. Personal Expense Tracker
Scenario
You want to track your daily expenses.

Requirements
Add expenses:
    Food
    Travel
    Shopping
    Others
Store all expenses.
    Display total spending.
    Find the highest expense.
    Search expenses by category.
Concepts
✅ Lists
✅ Dictionaries
✅ Functions
✅ Loops
✅ Conditions  '''

# Get the total number of items 
n=int(input("Enter the total number of items: "))

print('''-------- Categories ------------
      1.Food
      2.Travel
      3.Shop
      4.Others
-----------------------------------''')

# Get the items with category
expenses=[]
for i in range(n):
    valid_categories = ["food", "travel", "shop", "others"]
    while True:
        ctg = input("Enter the category: ").strip().lower()
        if ctg in valid_categories:
            break
        print("Invalid category! Try again")           # Strip is used to remove the extra spaces
    amo=int(input("Enter the amount: "))               # lower is used to handle convert different types of inputs into same format
    expenses.append({"Category":ctg, "Amount":amo})

# Display the expenses
print("---------------- Expenses -----------------")
for i in expenses:
    print(i)
print("-------------------------------------------")

# Total, Avg
total=0
for expense in expenses:
    total+=expense["Amount"]
print("Total expense: ",total)
print("Average: ", total/n)

# Highest & Lowest expenses
high=max(expenses, key=lambda expense: expense["Amount"])
low=min(expenses, key=lambda expense: expense["Amount"])
print(high)
print(low)
print(
    "Highest Expense:",
    high["Category"],
    "-",
    high["Amount"]
)

print(
    "Lowest Expense:",
    low["Category"],
    "-",
    low["Amount"]
)
print("----------------------------------------------")

# Category wise highest and lowest expenses
''' 
NORMAL METHOD
food,travel,shop,others=0,0,0,0
for exp in expenses:
    if (exp["Category"]=="Food"):
        food+=exp["Amount"]
    elif exp["Category"] == "Travel":
        travel += exp["Amount"]

    elif exp["Category"] == "Shopping":
        shop += exp["Amount"]

    else:
        others += exp["Amount"] '''

#  Category-wise total expenses (Efficient method)
category_values={
    "food":0,
    "travel":0,
    "shop":0,
    "others":0 
}

for ex in expenses:
    category=ex["Category"]
    amount=ex["Amount"]
    category_values[category]+=amount

print("-------------------------------------------")
print("Food Expenses: ",category_values["food"])
print("Travel Expense: ", category_values["travel"])
print("Shopping Expenses: ",category_values["shop"])
print("Other Expenses: ", category_values["others"])
print("---------------------------------------------")

print("--------------- Search the amount by category-----------------")
print("valid_categories: food,travel,shop,others")
valid_categories = ["food", "travel", "shop", "others"]
while True:
        i=input("Enter the category to search: ").strip().lower()
        if i in valid_categories:
            break  
        print("Invalid category, Try again!!")
print("------------------- Expenses -------------------------")
for ex in expenses:
        if(ex["Category"]==i):
            print(ex["Category"]," --> ",ex["Amount"])
print("-------------------------------------------------------")




    


