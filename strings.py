for x in "banana":
    print(x)

length_and_slice = "Hello World"
print(len(length_and_slice)) #Length

 # Slicing
print(length_and_slice[2:5])
print(length_and_slice[:5])
print(length_and_slice[2:])

#String present or not
present_or_not = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. " \
"Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. " \
"It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
if "type " in present_or_not:
    print("Yes type is present")

if "zzzz" not in present_or_not:
    print("Yes zzzz is not present")

#Remove Whitespace
remove_whitespace = "   Remove White Space    "
print(remove_whitespace.strip())

#Replace String
replace_string = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. " \
"Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. " \
"It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
print(replace_string.replace('Lorem','AAA'))

#Split
spliting = "Hello World"
print(spliting.split(" "))

#Modifier
price = 68
modifier = f"Price of the item is Rs {price:.2f}."
modifier_2 = f"Price of the item is Rs {30*price:.2f}."
print(modifier)
print(modifier_2)
print(modifier.encode())
