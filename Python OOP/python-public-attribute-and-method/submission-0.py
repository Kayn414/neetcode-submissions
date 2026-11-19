class StoreItem:
    def __init__(self, name: str, price: int):
        # Add: name, price
        self.name = name
        self.price = price
        

chips = StoreItem("Chips", 1.99) # Don't modify this line

# TODO: Access the attributes of the chips object and display them
chip_name = chips.name
chip_price = chips.price

print(chip_name)
print(chip_price)

