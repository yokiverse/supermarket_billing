import pandas as pd
import csv
filename = 'stock.csv'
file = open(filename, 'a', newline='')
writer = csv.writer(file)
if file.tell() == 0:
    header = ['stock name', 'product price', 'available quantity']
    writer.writerow(header)
while True:
    stock_name = input("Enter stock name: ")
    while True:
        try:
            product_price = float(input("Enter product price: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    available_quantity = int(input("Enter available quantity: "))
    writer.writerow([stock_name, product_price, available_quantity])
    add_more = input("Do you want to add more? (yes/no): ").strip().lower()
    if add_more != 'yes':
        break
file.close()
print("Data has been written")
