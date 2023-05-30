text = input("Введите слово из 3-х букв: ")

#print ( ord('R') )

first_char = text[0]
second_char = text[1]
third_char = text[2]

print(first_char, second_char, third_char)

first_code = ord(first_char)
second_code = ord(second_char)
third_code = ord(third_char)
code_sum = first_code + second_code + third_code

message1 = "Коды символов: %d, %d, %d" % (first_code, second_code, third_code)
message2 = "Сумма кодов символов: %d" % code_sum

print(message1)
print(message2)


#code_sum = ord(first_char, second_char, third_char)
#print("Сумма кодов символов: ", code_sum)