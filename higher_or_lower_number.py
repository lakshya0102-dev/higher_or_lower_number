import random


def generate_number(min_val=1, max_val=100):
    return random.randint(min_val, max_val)


def play_game():
    n = generate_number(1, 100)
    guess = 0
    a = -1
    print("Welcome to Higher or Lower!")
    while a != n:
        guess += 1
        try:
            a = int(input("Enter your guess (between 1 and 100): "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if a < n:
            print("Higher!")
        elif a > n:
            print("Lower!")
        else:
            print(f"Congratulations! You've guessed the number {n} in {guess} guesses!")


def main():
    play_game()


if __name__ == "__main__":
    main()
        