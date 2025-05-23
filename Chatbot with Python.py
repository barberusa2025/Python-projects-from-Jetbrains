def greet(bot_name, birth_year):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")


def remind_name():
    your_name = input("Please, remind me your name.\n")
    # reading a name
    print(f"What a great name you have, {your_name}!")

def guess_age():
    remainder3 = int(input("Enter remainders of dividing your age by 3: "))
    remainder5 = int(input("Enter remainders of dividing your age by 5: "))
    remainder7 = int(input("Enter remainders of dividing your age by 7: "))

    age = int (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    print(f"Your age is {age}; that's a good time to start programming!")

def count():
    number = int(input("Now I will prove to you that I can count to any number you want."))
    i = 0
    while i <= number:
        print(f"{i} !")
        i = i + 1
    print('Completed, have a nice day!')


# Now we can use these functions
greet("Buddy", 2025)
remind_name()
guess_age()
count()