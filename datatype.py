#tuple
point = (12,20)
x= point[0]
y= point[1]

print(f"X: {x}, Y: {y}")

#set
numbers = [1,2,10,9,56,20,6,2,9,56,77,77,1,1,69,77,69]
foods = ["pizza", "burger", "sushi", "pasta", "salad", "tacos", "ramen", "pizza", "curry", "sandwich", "burger", "pizza", "sushi", "tacos", "pasta"]

unique_numbers = set(numbers)
unique_foods = set(foods)

print(unique_numbers)
print( unique_foods)

north_indian = {"butter chicken", "dal makhani", "naan", "biryani", "chole bhature", "samosa"}
south_indian = {"dosa", "idli", "vada", "sambar", "rasam", "pongal", "biryani"}

print("\nIndian Foods:", north_indian | south_indian)
print("Common Indian Foods:", north_indian & south_indian)


# Create frozensets
immutable_permissions = frozenset(["read", "write"])
immutable_permission = frozenset(["read"])
# Use frozenset as dictionary key
access_control = {
    frozenset(["read"]): "Read Only Access",
    frozenset(["read", "write"]): "Read/Write Access"
}

print(access_control[immutable_permissions])
print(access_control)



