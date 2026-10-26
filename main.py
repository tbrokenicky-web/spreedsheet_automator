
import csv

# a list that cant have any of the same 
seen_customer = set()
duplicate_customer = set()

print("Program started!")

with open("sales.csv", "r", newline="") as file:
    print("CSV file opened!")

    reader = csv.DictReader(file)
   

    print("Column names:", reader.fieldnames)

    for row in reader:
        customer = str(row["Customer"])
        product = str(row["Product"])
        price = float(row["Price"])
        quantity = int(row["Quantity"])

        total = price * quantity
        # if the customer is in seen list it adds it to duplicate 
        if customer in seen_customer:
            duplicate_customer.add(customer)
        else: # else it just adds them to te see list
            seen_customer.add(customer)
        
            
        if customer not in duplicate_customer:
             print(f"{customer}: {total}")
        else:
            print("found duplicate" + str(duplicate_customer))








