def separator(string, c):
    size = len(string)
    k = 0
    for i in range(size):
        string = string[:k+1] + c + string[k+1:]
        k = 2 * (len(string) - size)
    print(string)


person_input = input("Введи строку: ")
print("Получившиеся варианты:")
separator(person_input, ' ')
separator(person_input, '@')
separator(person_input, '#')
