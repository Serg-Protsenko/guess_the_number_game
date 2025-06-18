import random

print("Вітаю! Я загадав число від 1 до 100. Спробуйте вгадати його за 7 спроб.")

secret_number = random.randint(1, 100)
max_attempts = 7
attempt = 1

while attempt <= max_attempts:
    try:
        guess = int(input(f"Спроба {attempt}. Введіть Ваше припущення: "))

        if guess < secret_number:
            print("Занадто маленьке!\n")
        elif guess > secret_number:
            print("Занадто велике!\n")
        else:
            print(f"Ви вгадали! Це число {secret_number}.")
            break
        attempt += 1
    except ValueError:
        print("Будь ласка, введіть ціле число.\n")

if attempt > max_attempts:
    print(f"На жаль, Ви не вгадали. Загадане число було: {secret_number}")
