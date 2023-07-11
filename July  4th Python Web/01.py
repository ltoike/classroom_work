my_file = open("book.txt", encoding="utf-8")
text = my_file.read()
my_file.close()
user_in1 = input("Введите слово, которое вы хотите заменить: ")
user_in2 = input("Введите слово на которое вы хотите заменить: ")
a = text.replace(user_in1.lower(), user_in2.lower())
a = a.replace(user_in1.upper(), user_in2.upper()) #updated a
#capilize function can be used to simplify stroke 6 and 7 
print(a)
