/* 1. Дан код:
    var a = 1, b = 1, c, d;
    c = ++a; alert(c);           // 2
    d = b++; alert(d);           // 1
    c = (2+ ++a); alert(c);      // 5
    d = (2+ b++); alert(d);      // 4
    alert(a);                    // 3
    alert(b);                    // 3
Почему код даёт именно такие результаты?
*/

// Разница в том, что ++a инкрементирует, а затем возвращает значение. b++ возвращает значение, а потом инкрементирует.

/* 2. Чему будет равен x в примере ниже?
    var a = 2;
    var x = 1 + (a *= 2);
*/

// x = 5

/* 3. Объявить две целочисленные переменные a и b и задать им произвольные начальные значения.
Затем написать скрипт, который работает по следующему принципу:
    если a и b положительные, вывести их разность;
    если а и b отрицательные, вывести их произведение;
    если а и b разных знаков, вывести их сумму; ноль можно считать положительным числом.
*/

function operations(a, b) {
    if (a > 0 & b > 0) {
        return a - b;
    } else if (a < 0 & b < 0) {
        return a * b;
    } else {
        return a + b;
    }
}

const a = Number(prompt('Введите первое число: ')), b = Number(prompt('Введите 2 число: '));
console.log(operations(a, b));

/* 4. Присвоить переменной а значение в промежутке [0..15]. С помощью оператора switch организовать вывод чисел от a до 15. */

const number = prompt('Введите число от 0 до 15: ');

function fromNto15(number) {
    switch (true) {
        case isNaN(number):
        case number < 0:
            let newNumber = prompt('Введите число от 0 до 15: ');
            return fromNto15(Number(newNumber));
        case number <= 15:
            console.log(number);
            return fromNto15(Number(number + 1));
        case number > 15:
            break;
    }
}

console.log(fromNto15(Number(number)));


/* 5. Реализовать основные 4 арифметические операции в виде функций с двумя параметрами. Обязательно использовать оператор return. */

function addition(a, b) {
    return a + b;
}

function subtraction(a, b) {
    return a - b;
}

function multiplicetion(a, b) {
    return a * b;
}

function division(a, b) {
    return a / b;
}

console.log(addition(10, 10));
console.log(subtraction(10, 10));
console.log(multiplicetion(10, 10));
console.log(division(10, 10));

/* 6. Реализовать функцию с тремя параметрами: function mathOperation(arg1, arg2, operation), где arg1, arg2 – значения аргументов, operation – строка с названием операции.
В зависимости от переданного значения операции выполнить одну из арифметических операций (использовать функции из пункта 5) и вернуть полученное значение (использовать switch).
*/

function mathOperation(arg1, arg2, operation) {
    switch (operation) {
        case '+':
            return addition(arg1, arg2);
        case '-':
            return subtraction(arg1, arg2);
        case '*':
            return multiplicetion(arg1, arg2);
        case '/':
            return division(arg1, arg2);
    }
}

console.log(mathOperation(10, 10, '*'));

/* 7. *Сравнить null и 0. Попробуйте объяснить результат.*/

console.log(null > 0); // false
console.log(null < 0); // false
console.log(null >= 0); // true
console.log(null <= 0); // true
console.log(null == 0); // false
console.log(null === 0); // false

// На очень высоком уровне реляционный оператор >= оценивает так: если null < 0 является false , тогда null >= 0 является true
// Начал про это читать на форумах и убился на час :)

/* 8. *С помощью рекурсии организовать функцию возведения числа в степень.
Формат: function power(val, pow), где val – заданное число, pow – степень.
*/

function power(val, pow) {
    if (pow === 1) return val;
    return power(val += val, pow - 1);
}

console.log(power(2, 4));
