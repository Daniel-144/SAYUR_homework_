#Fruit vendor has a list of fruits
fruits=['apple','orange','banana','grape']
quantity = None
Fruit_asked = None
numbers = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9
    }
while True:
    # Ask the customer what they want to buy
    customer_input = input("What do you want to buy?")

    # Check if the customer mentioned a quantity and asked fruit from your list
    words = customer_input.split()
    for word in words:
        if word.isdigit() and len(word) == 1:
            quantity = int(word)
        elif word.lower() in fruits:
            Fruit_asked =  word
        elif word in numbers:
            quantity = numbers.get(word.lower(), 0)

#If a fruit is recognized
    if Fruit_asked:
        print(f"You want {quantity} {Fruit_asked}.")
    else:
        print("I didn't understand your request. Please specify a fruit and, if needed, a quantity (e.g., 'two apples').")

    # Check if the customer wants to exit the program
    if customer_input.lower() == "exit":
        print("Fruit vendor: Thank you for shopping!")
        break