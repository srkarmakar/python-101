#Create Tuple With One Item
thistuple = ("Mari Gold",)
print(type(thistuple))

#NOT a tuple
thistuple = ("Mari Gold")
print(type(thistuple))

flowers = ["Rose", "Tulip", "Daisy", "Lily", "Sunflower"]
regular_boquet = tuple(flowers)
print("Type :",type(regular_boquet))
print("Regular Boquet :",regular_boquet)
print("Type Flowers :",len(regular_boquet))
print("First Flower in the row:",regular_boquet[1])