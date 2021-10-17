user_message = input("Введите любые слова через пробел: ").split()
string_number = 0

for word in user_message:
    string_number += 1
    if len(word) > 10:
        word = word[0:10]
    print(f"{string_number} {word}")
