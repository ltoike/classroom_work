name = "._.шубадуба \n "

a = name.casefold #локализованное чем a = name.lower()

a = name.replace("дуб", "береза", 3)
print(a)

a = name.rjust(30, "-")
a = name.rjust(30) #пробел по умолчанию
a = name.center(30, "-")

a = name.split("дуб")
a = name.partition("дуб")
a = name.strip()
a = name.rstrip()
a = name.lstrip(".-")

name = "белая береза Под Моим Окном"

a = name.upper()
a = name.lower()
a = name.capitalize()
a = name.title()

a = name.zfill(60)

a = name.isupper()
a = name.islower()
a = name.istitle()
a = name.isdigit()
a = name.isdecimal()
a = name.isalnum()

name = name.encode('koi8-r')
print(name)

print(a)