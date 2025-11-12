# sales_tuplebased.py

def add_sale(sales):
    print("Enter sale details: ")
    sale_day = input("Enter day of sale: ")
    item_name = input("Enter item name: ")
    quantity = int(input("Enter quantity of item sold: "))
    price_per_unit = float(input("Enter price per unit: "))
    sold = (sale_day, item_name, quantity, price_per_unit)# immutable tuple with values from console
    sales.append(sold)# appended to a list tuples inside a list
    print(f" Sale record added for {item_name} on {sale_day}.")


def view_sales(sales):
    if not sales:
        print("No sales records found.")
        return

    for day, item, qty, price in sales:# tuple unpacking
        print(
            f"Day Sold: {day} | Item: {item} | Qty: {qty} | Price/unit: ₹{price} | Total: ₹{qty * price}"
        )





def main():
    sales = []
    while True:
        print("\n--- 🧾 Sales Tracker ---")
        print("1. Add Sale")
        print("2. View All Sales")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_sale(sales)
        elif choice == "2":
            view_sales(sales)
        elif choice == "3":
            print(" Exiting Sales Tracker.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
