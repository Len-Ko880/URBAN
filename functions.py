def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()
a = test_function()
print(a) #Выдает результат
b = inner_function()
print(b) #Не выдает результат (ошибка, имя не найдено)
