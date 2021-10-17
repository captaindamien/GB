first_result = int(input("Сколько километров вы пробежали в 1-ый день? "))
final_result = int(input("Какую дистанцию вы хотите преодолеть в итоге? "))
day_number = 1

while first_result < final_result:
    first_result = first_result + first_result * 0.1
    day_number += 1

print(f"На {int(day_number)} день вы достигните желаемого результата")
