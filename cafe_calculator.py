import sys
import csv

# Make sure an input file was given on the command line
if len(sys.argv) < 2:
    print("Usage: python cafe_calculator.py input_file.csv")
    sys.exit(1)

input_file = sys.argv[1]
output_file = "bill_summary.txt"

total_amount = 0.0
item_count = 0

# Read the CSV file
try:
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            # Each row should be: item_name, price, quantity
            name = row[0]
            price = float(row[1])
            quantity = int(row[2])
            total_amount += price * quantity
            item_count += quantity
except Exception as e:
    print(f"Error reading file: {e}")
    sys.exit(1)

# Calculate tax (10%) and grand total
tax = total_amount * 0.10
grand_total = total_amount + tax

# Write results to output file
try:
    with open(output_file, 'w') as file:
        file.write(f"Total items sold: {item_count}\n")
        file.write(f"Subtotal: ${total_amount:.2f}\n")
        file.write(f"Tax (10%): ${tax:.2f}\n")
        file.write(f"Grand Total: ${grand_total:.2f}\n")
except Exception as e:
    print(f"Error writing output: {e}")
    sys.exit(1)

print(f"Bill summary written to {output_file}")
