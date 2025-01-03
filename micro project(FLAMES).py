def fun_flames():
    # Input names
    name1 = input("Enter the first name: ").lower().replace(" ", "")
    name2 = input("Enter the second name: ").lower().replace(" ", "")
    print("Relationship between",name1,"and",name2,"is :...")
    # Remove common characters from both names
    for char in name1:  
        if char in name2:
            name1 = name1.replace(char, "")
            name2 = name2.replace(char, "")

    # Total remaining letters after removing common ones
    letters_count = len(name1) + len(name2)

    # FLAMES string
    flames = ['F', 'L', 'A', 'M', 'E', 'S']

    i = 0
    counter = 0

    # FLAMES game logic
    while len(flames) > 1:
        counter = (counter + letters_count - 1)
         # Properly handle index
        counter%= len(flames) 
        del flames[counter]

    # Output the result
    result = flames[0]

    # Print the result 
    if result == 'F':
        print("Friends")
    elif result == 'L':
        print("Love")
    elif result == 'A':
        print("Affection")
    elif result == 'M':
        print("Marriage")
    elif result == 'E':
        print("Enemies")
    elif result == 'S':
        print("Siblings")

# Call the function
fun_flames()
