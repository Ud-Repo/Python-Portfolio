#  Initialization
customers = {}  # Dictionary to store customers' information

#  Add Customer Function
def add_customer():
    global customers
    name = input("Enter customer name: ")
    contact = input("Enter customer contact number: ")
    customer_id = len(customers) + 1  # Generate a unique customer ID
    customers[customer_id] = {"name": name, "contact": contact, "orders": {}}
    print("Customer added successfully")

#  Place Order Function
def place_order(customer_id, product_name, quantity, unit_price):
    global customers
    if customer_id not in customers:
        print("Customer ID not found")
        return

    order_id = len(customers[customer_id]["orders"]) + 1  # Generate a unique order ID
    total_cost = quantity * unit_price
    order = {
        "product_name": product_name,
        "quantity": quantity,
        "unit_price": unit_price,
        "total_cost": total_cost
    }
    customers[customer_id]["orders"][order_id] = order
    print("Order placed successfully")

#  Generate Customer Report Function
def generate_customer_report(customer_id):
    global customers
    if customer_id not in customers:
        print("Customer ID not found")
        return

    customer = customers[customer_id]
    print(f"Customer ID: {customer_id}")
    print(f"Name: {customer['name']}")
    print(f"Contact: {customer['contact']}")
    
    orders = customer.get('orders')
    if not orders:
        print("No orders found for this customer.")
        return
    
    print("Orders:")
    for order_id, order_details in orders.items():
        print(f"Order ID: {order_id}")
        print(f"Product: {order_details['product_name']}")
        print(f"Quantity: {order_details['quantity']}")
        print(f"Unit Price: {order_details['unit_price']}")
        print(f"Total Cost: {order_details['total_cost']}")
        print("--------------------")

#  Main Loop/Interface
while True:
    print("\n1. Add Customer\n2. Place Order\n3. Generate Customer Report\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_customer()
    elif choice == "2":
        #  user inputs order details here
        place_order(1, "Product A", 2, 15.99)  # Example usage
    elif choice == "3":
        customer_id = int(input("Enter customer ID: "))
        generate_customer_report(customer_id)
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

