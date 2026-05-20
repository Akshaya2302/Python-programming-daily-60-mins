class FoodOrder:
    def __init__(self, customer_name, food_item, quantity, price):
        """Initializes the food order with required attributes."""
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price
        self.total_amount = 0.0
        self.is_cancelled = False
        
        self.calculate_total()

    def place_order(self):
     
        if self.is_cancelled:
            print(f"Cannot place order. This order for {self.customer_name} was previously cancelled.")
        else:
            print(f"Order placed successfully for {self.customer_name}!")

    def cancel_order(self):
        """Cancels the order."""
        if self.is_cancelled:
            print("This order is already cancelled.")
        else:
            self.is_cancelled = True
            self.total_amount = 0.0  # Reset total since it's cancelled
            print(f"Order for {self.customer_name} has been cancelled.")

    def calculate_total(self):
        """Calculates the total amount based on price and quantity."""
        if not self.is_cancelled:
            self.total_amount = self.price * self.quantity
        return self.total_amount

    def apply_coupon(self, discount):
        """Applies a flat discount amount to the total total_amount."""
        if self.is_cancelled:
            print("Cannot apply coupon. The order is cancelled.")
            return

        if discount < 0:
            print("Invalid discount amount.")
            return

        if discount > self.total_amount:
            print(f"Coupon amount ₹{discount} exceeds total. Setting total to ₹0.")
            self.total_amount = 0.0
        else:
            self.total_amount -= discount
            print(f"Coupon applied! Discounted ₹{discount}. New total: ₹{self.total_amount:.2f}")

    def display_order_details(self): 
        print(f"Customer Name : {self.customer_name}")
        print(f"Food Item     : {self.food_item}")
        print(f"Quantity      : {self.quantity}")
        print(f"Price per Unit: ₹{self.price:.2f}")
        print(f"Total Amount  : ₹{self.total_amount:.2f}")

if __name__ == "__main__":
    print("Successful Order Processing")
   
    order1 = FoodOrder(customer_name="Akshu", food_item="Paneer Butter Masala & Naan", quantity=2, price=250.0)
    order1.place_order()
    order1.display_order_details()
    order1.apply_coupon(discount=50.0)
    order1.display_order_details()

    