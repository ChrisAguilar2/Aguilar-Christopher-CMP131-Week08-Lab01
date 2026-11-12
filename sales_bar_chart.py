#Christopher A
#CMP 131
#Week 8 lab 1



Ast = ""
store = 5
for i in range (5):
    sales = float(input("Enter today's sales for store " + str(i+1)+":"))
    while sales < 0:
        print("Error, sales cannot be negative.")
        sales = float(input("Try again: "))   

    sales = sales/100
    Ast += f"Store {i+1}: "
    for j in range (int(sales)):
        Ast = Ast + "*"
    Ast = Ast + "\n"

print("\n===== SALES BAR CHART =====")
print("Each * represents $100")
print(Ast)
