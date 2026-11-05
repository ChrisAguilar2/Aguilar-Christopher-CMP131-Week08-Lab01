#Christopher A
#CMP 131
#Week 8 lab 1

Ast = ""
store = int(input("Enter number of stores:"))
for i in range (store):
    sales = int(input("Enter today's sales for store " + str(i+1)+":"))
    sales = sales/100
    for j in range (int(sales)):
        Ast = Ast + "*"
    Ast = Ast + "/n"
print(Ast)
