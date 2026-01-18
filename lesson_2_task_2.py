def is_year_leap(year):
    if year % 4 == 0:
        return True # год високосный
    else:
        return False # год не високосный

num = int(input("Введите год: "))
result = is_year_leap(num)
print(f"год {num} делится на 4: {result}")
#Введите год: 2023
#год 2023 делится на 4: False

#Введите год: 1788
#год 1788 делится на 4: True

#Введите год: 1676
#год 1676 делится на 4: True
