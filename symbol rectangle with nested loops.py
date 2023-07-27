rows = int(input("Enter the number of rows of the rectangle: "))
columns = int(input("Enter the number of columns of the rectangle: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()