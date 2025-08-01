# Build class
class ItemToPurchase:
    # attributes
    item_name = "none"
    item_price = 0
    item_quantity = 0

    # Default constructor function
    def __init__(self, item_name=''):
        self.item_name = item_name

    # Method for determining item cost
    def print_item_cost(self):
        self.item_cost = int(self.item_quantity) * float(self.item_price)
        # Defining the print statement in the function based on whether the self.item_cost is an integer or not
        if '.00' in str(self.item_cost):
            # Getting rid of the decimal point and zeroes for the print statement 
            self.item_cost = int(self.item_cost)
            print("{} {} @ ${} = ${}".format(self.item_name, self.item_quantity, self.item_price, self.item_cost))
        # If the self.item_cost does have a cents value, this will ensure the price and cost are printed with 2 decimal places
        else: 
            print("{} {} @ ${:.2f} = ${:.2f}".format(self.item_name, int(self.item_quantity), float(self.item_price), float(self.item_cost)))

# Creating an object of the ItemToPurchase class with the user defining the item_name
item1 = ItemToPurchase(input("Enter the item name: "))
# User defines the item_price of the new item1 object
item1.item_price = input("Enter the item price: ")
# User defines the quantity of the new item1 object
item1.item_quantity = input("Enter the item quantity: ")

# Creating another object of the ItemToPurchase class with the user defining the item_name
item2 = ItemToPurchase(input("Enter the item name: "))
# User defines the item_price of the item2 object
item2.item_price = input("Enter the item price: ")
# User defines the quantity of the item2 object
item2.item_quantity = input("Enter the item quantity: ")

# Creating the first part of the print statement
print("\nTOTAL COST")
# Running the values entered in by the user through the class print_item_cost function above
item1.print_item_cost()   
item2.print_item_cost()  

total_cost = float(item1.item_cost + item2.item_cost)
# Checking if the float has cents (decimal) value of .0 or .00 then converting and printing the value to an integer to get rid of the decimal places
if '.00' in str(total_cost) or '.0' in str(total_cost):
    print("Total: ${}\n".format(int(total_cost)))
# If there is a cents value, this prints the total cost as a float with 2 decimal places
else: 
    print("Total: ${:.2f}\n".format(float(total_cost)))



class ShoppingCart:
    # Create constructor with customer_name and date as parameters and intialized with 'none' and 'January 1, 2020'
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date

    # Initializing the cart_items list
    cart_items = []

    # Method for adding an item to shopping cart
    def add_item(self, ItemToPurchase=''):
        self.cart_items.append(ItemToPurchase)
    
    # Method for removing an item from list
    def remove_item(self, item=''):
        if item in self.cart_items:
            self.cart_items.remove(item)
        else:
            print("Item not found in cart. Nothing removed.")
    
    # Initializing lists to contain the data for the cart items' description, price, quantity and cost (price * quantity)
    cart_item_descriptions = []
    cart_item_prices = []
    cart_item_quantities = []
    cart_item_costs = []

    # Method for modifying item in cart and adding data to corresponding lists
    def modify_item(self, item=ItemToPurchase):
        if item in self.cart_items:
            # Obtaining item description and appending it to the respective list
            item_desciption = input("Enter a description for {}: ".format(item))
            self.cart_item_descriptions.append(item_desciption)
            
            # Obtaining item price as a string
            item_price = float(input("Enter price of {}: ".format(item)))
            # Defining the print statement in the function based on whether the self.item_cost is an integer or not
            if '.00' in str(item_price) or '.' not in str(item_price):
                # Getting rid of the decimal point and zeroes for the print statement 
                new_item_price = int(item_price)
            else:
                new_item_price = float(item_price)
            
            # Appending the cart_item_prices list with item_price
            self.cart_item_prices.append(new_item_price)
            
            # Obtaining item quantity and appending it to the respective list
            item_quantity = int(input("Enter quantity of {}: ".format(item)))
            self.cart_item_quantities.append(item_quantity)
            
            # Obtaining item cost (price * quantity) and appending it to the respective list
            item_cost = new_item_price * item_quantity
            self.cart_item_costs.append(item_cost)
            
        
        else:
            print("Items not found in cart. Nothing modified.")    
        

    # Method for retrieving number of objects in cart
    def get_num_items_in_cart(self):
        print('Number of items in cart: ', sum(self.cart_item_quantities))

    def get_cost_of_cart(self):
        # Initialize cost variable
        total_cost = 0
        # Increment through each item in cart and sum it's price to total
        for cost in self.cart_item_costs:
            total_cost = total_cost + cost
        print("Total cost of items in cart: ${:.2f}".format(total_cost))

    def print_total(self):
        if len(self.cart_items) > 0:
            print("\n{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
            print("Number of Items: {}".format(sum(self.cart_item_quantities)))
            for i in range(len(self.cart_items)):
                print("{} {} @ ${:.2f} = ${:.2f}".format(self.cart_items[i], self.cart_item_quantities[i], self.cart_item_prices[i], self.cart_item_costs[i]))
            
            print("Total: ${:.2f}\n".format(sum(self.cart_item_costs)))
        else:
            print("SHOPPING CART IS EMPTY\n")

    def print_descriptions(self):
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
        print("Item Descriptions")
        for i in range(len(self.cart_items)):
            print('{}: {}'.format(self.cart_items[i], self.cart_item_descriptions[i]))
        print('\n')


shopping_cart = ShoppingCart("Mark Lucas", "July 20, 2025")
shopping_cart.add_item("Nike Romaleos")
shopping_cart.add_item("Chocolate Chips")
shopping_cart.add_item("Powerbeats 2 Headphones")
shopping_cart.modify_item("Nike Romaleos")
shopping_cart.modify_item("Chocolate Chips")
shopping_cart.modify_item("Powerbeats 2 Headphones")
shopping_cart.print_total()
shopping_cart.print_descriptions()



def print_menu(shoppingCart=ShoppingCart):
    print("""                   MENU
          a - Add item to cart
          r - Remove item from cart
          c - Change item quantity
          i - Output items' descriptions
          o - Output shopping cart
          q - Quit
          Choose an option:""")
    user_option = input('> ')
    if user_option == 'q':
        return
    while user_option != 'q':
        if user_option == 'a':
            user_input = input("ADD ITEM TO CART\nEnter the item name:\n> ")
            shopping_cart.add_item(user_input)
            user_option = input(f'{user_input} added to cart. Choose new option: ')
            continue
        elif user_option == 'r':
            user_input = input("REMOVE ITEM FROM CART\nEnter name of item to remove:\n> ")
            shoppingCart.remove_item(user_input)
            user_option = input(f'{user_input} removed from cart. Choose new option: ')
            continue
        elif user_option == 'c':
            user_input = input("CHANGE ITEM QUANTITY\nEnter the item name:\n> ")
            index_of_item = shoppingCart.cart_items.index(user_input)
            quantity_change = input("What is the new quantity of {}?\n> ".format(user_input))
            shoppingCart.cart_item_quantities[index_of_item - 1] = int(quantity_change)
            user_option = input(f'You now have {quantity_change} {user_input}(s) in cart. Choose new option: ')
            continue
        elif user_option == 'i':
            print("OUTPUT ITEMS' DESCRIPTIONS")
            shoppingCart.print_descriptions()
            user_option = input('Choose new option: ')
            continue
        elif user_option == 'o':
            print("OUTPUT SHOPPING CART")
            shoppingCart.print_total()
            user_option = input('Choose new option: ')
            continue
        else:
            continue
    

print_menu(shopping_cart)




# Customer inputs their name and today's date
customerName = input("Enter customer's name:\n")  
todaysDate = input("Enter today's date:\n")
print(f'Customer name: {customerName}')
print(f'Today\'s date: {todaysDate}')

new_cart = ShoppingCart(customerName, todaysDate) # New object of class ShoppingCart based on customer input

# Adding new items to new_cart
new_cart.add_item('Milk')
new_cart.add_item('Bagels')

# Adding info about new items added
new_cart.modify_item('Milk')
new_cart.modify_item('Bagels')

print_menu(new_cart)


# Creating new ItemToPurchaseObject
last_item = ItemToPurchase('Popsicles')
last_item.item_price = 0.15
last_item.item_quantity = 80

new_cart.add_item(last_item.item_name)
print(ShoppingCart.cart_item_quantities)
print_menu(new_cart)

