print("Let's count together: {}, them goes {}, and then {}".format("one", "two", "three")) #Конкатация строк в пайтон
# Но существетт и более современный метод.
# Для использования возможностей f-strings нужно указывать символ f перед строкой
# в таком формате: f"ваша строка {my_var}". В фигурных скобках указывается имя переменной,
# значение которой надо подставить в строку, или выражение,
# результат исполнения которого также требуется подставить в вашу строку.
str1 = "one"
str2 = "two"
str3 = "three"
print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")
print(f"{2+3}")
