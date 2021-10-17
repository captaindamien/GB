/* 1. С помощью цикла while вывести все простые числа в промежутке от 0 до 100.
*/

function simpleNumbers(number) {
    arr = [];

    next:
    for (let el = 2; el <= number; el++) {

        for (let elem = 2; elem < el; elem++) {
            if (el % elem == 0) continue next;
        }

        arr.push(el);
    }
    
    return arr;
}

for (let value of simpleNumbers(100)) {
    console.log(value);
}

/* 2. С этого урока начинаем работать с функционалом интернет-магазина.
Предположим, есть сущность корзины. Нужно реализовать функционал подсчета стоимости корзины в зависимости от находящихся в ней товаров.
Товары в корзине хранятся в массиве. Задачи:
a) Организовать такой массив для хранения товаров в корзине;
b) Организовать функцию countBasketPrice, которая будет считать стоимость корзины.
*/

let products = [];
let basket = [];

function addProducts(name, price, count) {
    return products.push([name, price, count]);
}

function addBasket(product, count) {
    basketProduct = product.slice();
    
    if (count > product[2]) return console.log('Превышает кол-во товара на складе');
    basketProduct[2] = count;

    return basket.push(basketProduct);
}

function countBasketPrice(basket) {
    let sum = 0;

    for (value of basket) {
        sum += value[1] * value[2]
    }

    return sum;
}

addProducts('Компьютерная мышь', 1000, 5);
addProducts('Клавиатура', 1500, 1);
addProducts('Кабель USB Type-C', 300, 50);

addBasket(products[0], 1);
addBasket(products[2], 2);

console.log(products);
console.log(basket);
console.log(`Общая стоимость товаров в корзине: ${countBasketPrice(basket)}`);

/* 3.*Вывести с помощью цикла for числа от 0 до 9, не используя тело цикла. Выглядеть это должно так:
for(…){// здесь пусто}
*/

for (let element = 0; element < 10;  console.log(element), element++) {}

/* 4. *Нарисовать пирамиду с помощью console.log, как показано на рисунке, только у вашей пирамиды должно быть 20 рядов, а не 5:
*/

for (let element = 0; element <= 20; element++) {
    console.log('x'.padEnd(element, 'x'));
}
