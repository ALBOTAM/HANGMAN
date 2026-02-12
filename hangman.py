import random

def choose_word():
    words = ["JAVA", "Kotlin", "Laptop", "Fronted", "Backend","Python"]
    return random.choice(words)

def display(word, guessed_letters):
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    return display_word

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 10

    print("Добро пожаловать в игру Поле Чудес!")
    
    while attempts > 0:
        print("\nСлово:", display(word, guessed_letters))
        guess = input("Введите букву: ").lower()

        if guess in guessed_letters:
            print("Вы уже называли эту букву.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Правильно!")
        else:
            print("Неправильно!")
            attempts -= 1
            print(f"Осталось попыток: {attempts}")

        if all(letter in guessed_letters for letter in word):
            print(f"Поздравляем! Вы отгадали слово: {word}")
            break
    else:
        print(f"Вы проиграли! Загаданное слово было: {word}")

if __name__ == "__main__":
    hangman()
