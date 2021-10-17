user_input = int(input("Введите количество секунд: "))

hour = (user_input // 60) // 60
minute = user_input // 60

if minute >= 60:
    minute = minute % 60
second = user_input % 60

print(f"{user_input} секунд = {'%02d:%02d:%02d' % (hour, minute, second)}")

if hour >= 24:
    hour = hour % 24
    print(f"Если нужно, чтобы результат не выходил за рамки 24 формата: "
          f"{'%02d:%02d:%02d' % (hour, minute, second)}")
