print("Программа для шифрования и расшифровки методом Цезаря") #Сообщение для пользователя
while True:
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz" #Удвоенный алфавит, если сдвиг выйдет за рамки одного алфавит
    x = int(input("Напишите 1 для зашифровки, и 2 для расшифровки: "))
    if x == 1: #Функция зашифровки
        word = input("Введите слово для зашифровки на английском языке: ")
        try: #Проверка на нужный алфавит
            word[i].isalpha
        except:
            print("Вы ввели неверное слово")
            break
        key = int(input("Введите ключ шифрования диапазоном 1-25: "))
        if key > 25:
            key = key%25
        word = word.lower() #Делает все буквы нижним регистром
        wordX = "" #Отчистка
        for i in word: #Поиск введённого символа в алфавите
            position = alphabet.find(i)
            newPosition = position + key #Добавить к найденному символу наш шаг
            if i in alphabet:
                wordX = wordX + alphabet[newPosition]
            else:
                wordX = wordX + i
        print("Ваше зашифрованное слово:", wordX)
    elif x == 2: #Функция расшифровки
        word = input("Введите слово для расшифровки на английском языке: ")
        try: #Проверка на нужный алфавит
            word[i].isalpha
        except:
            print("Вы ввели неверное слово")
            break
        key = int(input("Введите ключ шифрования диапазоном 1-25: "))
        if key > 25:
            key = key%25
        word = word.lower()
        wordX = ""
        for i in word:
            position = alphabet.find(i)
            newPosition = position - key #Отнимаем наш шаг от найденного символа
            if i in alphabet:
                wordX = wordX + alphabet[newPosition]
            else:
                wordX = wordX + i
        print("Ваше расшифрованное слово", wordX)
    else: #Обработка ошибки ввода комманды
        print("Вы ввели неверную команду, попробуйте снова")