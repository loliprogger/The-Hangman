print()
print()
print("Чтобы начать игру нажмите 1.")
print("Если хотите выйти- жмите 2.")
print()
print()
move = input()
print()




import random



words = ["стакан", "мышь", "собака", "кот"]
choice_word = random.choice(words)

if move == "1":
    unknown_word = []
    for i in choice_word:
        unknown_word.append("*")
    print(*(unknown_word))

    lives = 10

    while True:
        positions = []
        letter = input()
        print()
        count = -1
        if letter in unknown_word:
            print("Эта буква уже была введена.")
            print()
            print()
        for i in choice_word:
            count += 1
            if i == letter:
                positions.append(int(count))
        for i in positions:
            unknown_word[int(i)] = letter
        print(*(unknown_word))
        print()



        if "*" not in unknown_word:
            print("Поздравляю! Вы победили!")
            print()
            print()
            quit()
        if letter not in choice_word:
            lives -= 1
            print("Такой буквы нет. Осталось " + str(lives) + " попыток.")
            print()
            print()
        if lives == 0:
            print("Вы проиграли! В следущий раз повезет больше")
            print()
            print()
            quit()

if move == "2":
    quit()

