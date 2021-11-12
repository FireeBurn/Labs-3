print("Программа для шифрования и расшифровки методом Цезаря")
while True:
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    x = int(input("Напишите 1 для зашифровки, и 2 для расшифровки: "))
    if x == 1:
        word = input("Введите слово для зашифровки на английском языке: ")
        key = int(input("Введите ключ шифрования диапазоном 1-25: "))
        word = word.lower()
        wordX = ""
        for i in word:
            position = alphabet.find(i)
            newPosition = position + key
            if i in alphabet:
                wordX = wordX + alphabet[newPosition]
            else:
                wordX = wordX + i
        print("Ваше зашифрованное слово:", wordX)
    elif x == 2:
        word = input("Введите слово для расшифровки на английском языке: ")
        key = int(input("Введите ключ шифрования диапазоном 1-25: "))
        word = word.lower()
        wordX = ""
        for i in word:
            position = alphabet.find(i)
            newPosition = position - key
            if i in alphabet:
                wordX = wordX + alphabet[newPosition]
            else:
                wordX = wordX + i
        print("Ваше расшифрованное слово", wordX)
    else:
        print("Вы ввели неверную команду, попробуйте снова")