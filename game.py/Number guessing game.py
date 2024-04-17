import random

while True:
    Computer_number = random.randint(1, 1200)
    user_input = int(input("Enter a number: "))

    if user_input > Computer_number:
        print("Your guess is too high")
        print("You are the winner! Your guess:", user_input, "Computer's number:", Computer_number)
    elif user_input < Computer_number:
        print("Your guess is too low")
        print("Computer wins this game. Your guess:", user_input, "Computer's number:", Computer_number)
    else:
        print("Both of them have the same number")
        print("Computer's number and your guess:", Computer_number, user_input)

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break
