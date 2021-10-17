def user_title(words):
    new_words = []
    for elements in words:
        new_words.append(elements.title())
    print(*new_words)


user_words = input("Введите любое количество строк через пробел: ").split()
user_title(user_words)
