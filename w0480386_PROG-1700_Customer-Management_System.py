customers = {}
#Add customer Function
def add_customer(): 
    global customers
    name = input("Enter customer name: ") #Ask customer for name
    contact = input("Enter customers number: ") #Ask customer for contact details
    customer_id = len(customers) + 1 #Generate ID for customer
    customers[customer_id] ={"name": name,"customers":customers,"orders":{}} #store in main customer's dict. using ID as keys
    print("added successfully")

#Add place order function
    def place_order(customer_id, product_name, quantity, unit_price):
        global customers #um, Davis...please throw more light on the 'global' variable.
        order_id = len(customers[customer_id]["orders"]) + 1
        total_cost = quantity * unit_price #calculate total cost 
        order = {"order_id":order_id,"product_name": product_name,"quantity": quantity,"unit_price": unit_price, "total_cost": total_cost} #create dictionary for details
        customers[customer_id]["orders"].append.order #add order dictionary to the specific customer. Use generated order id as key.
        print("order placed successfully!")

        def generate_customer_report(customer_id):
            global customers
            #check if customer exists in dictionary
            if  customer_id not in customers:
                print("order not found , please register first")
                return
            
            customers = customers[customer_id]
            print(f"Customer ID: {customer_id}")
            print(f"name: {name}")
            print(f"contact: {customers[contact]}")

            orders = customers.get("orders")
            if not orders:
                print("oops! you didn't make an order")
                return
            
            print("orders:")
            for order_id,order_details in orders.items():
                print(f"Order ID : {order_id}")
                print(f"Product :{order_details[product_name]}")
                print (f"Quantity: {order_details[quantity]}")
                print(f"Unit Price : {order_details[unit_price]}")
                print(f"Total Cost: {order_details[total_cost]}")
                print("---------------")

                while True:
                    print("What can we do for you today?")
                    print("\n1. Add Customer\n2. Place Order \n3. Generate Customer Report \n4. Exit" )
                    
                    choice = input ("Enter an option to get started:  ")

                    if choice == "1":
                       add_customer
                    elif  choice == "2":
                        place_order(customer_id, product_name, quantity, unit_price)
                    elif choice == "3":
                        customer_id = int(input("Enter Customer ID: "))    
                        generate_customer_report(customer_id)
                    elif choice == "4":
                        print("Thank you for working with us!")
                        print("Now exiting ......")
                        break
                    else :
                        print("invalid input, Please try again")
            

             
            
                

