
# Christopher Aguilar
# CMP 131
# Week 8 Lab 1
# Loop Patterns
# Date: 11/11/2026

print("===== LOOP PATTERNS =====")


print("\nPattern A")

for i in range(1, 11):
    for j in range(i):
        print("+", end="")
    print()


print("\nPattern B")

for i in range(10, 0, -1):
    for j in range(i):
        print("+", end="")
    print()

print("\n===== END OF PROGRAM =====")
