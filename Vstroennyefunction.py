# Представьте Вы хотите взять какой-то набор данных и переконвертировать его в SET для удаления дубликатов,
# возьмите values и проверьте каждый ли элемент доступен для конвертации. Создайте список.
# Проитерируйте values. Если объект в списке можно переконвертировать добавьте True в новый список
# иначе добавьте False. После, с помощью функции all() скажите можно ли конвертировать values в SET?

lists = [1, 2, "yes", 3, 3, 2, True, {1, 1, 2}]
for i in lists:
    try:
        sets = set(lists[i])
    except:
        print('ошибка')
    else:
        print(f'(ok для {lists[i]})')

print(all(lists))


userNumber = input(range(5))

# s = set(lists)
# for i in s:
#     print(i)

# try:
#     sets = set(list)
# except:
#     print('чета нет')
# finally:
#     print('ок')
