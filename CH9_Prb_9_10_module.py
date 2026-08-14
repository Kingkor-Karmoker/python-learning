# code for problem 9.10:
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant's name is {self.restaurant_name}")
        print(f"Restaurant's cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open")
