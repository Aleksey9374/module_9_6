'''Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор,
при каждой итерации которого будет возвращаться подпоследовательности переданной строки.

Пункты задачи:
функция-генератор all_variants(text).
внутри функции all_variants циклами for перебираем требуемые срезы и возвращаем их в объекте генератора
Вызываем функцию all_variants и выполняем итерации генератора.'''

import itertools
def all_variants(text):
    for x in range(len(text)):
        for y in range(len(text) - x):
            yield text[y:1 + y + x]

a = all_variants("abc")
for i in a:
    print(i)
