n = int(input("Введите число от 3 до 20: "))
password = ""
for i in range(1, n):
    for j in range(i + 1, n):
        if(i + j) % n == 0:
            password += str(i) + str(j)
print(password, "Ваш пароль")