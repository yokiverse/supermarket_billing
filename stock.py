import pandas as pd
import csv
with open('stock.csv', 'a', newline='') as file:
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
         add = input("Do you want to add more? (yes/no): ").lower()
         if add != 'yes':
             break
print("Data has been written.")

