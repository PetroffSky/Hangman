import engine

# Вывод графики:
def gallows(error):
    str1 = ' ___  '
    str2 = '|    | '
    str3 = '|    '
    str4 = '|    '
    str5 = '|    '
    str6 = '|'

    if error == 1:
        print(str1, str2, str3, str4, str5, str6, sep='\n')
        return ' '
    if error == 2:
        er1 = str3 + 'o'
        print(str1, str2, er1, str4, str5, str6, sep='\n')
        return ' '
    if error == 3:
        er1 = str3 + 'o'
        er2 = str4 + '|'
        print(str1, str2, er1, er2, str5, str6, sep='\n')
        return ' '
    if error == 4:
        er1 = str3 + 'o'
        er3 = ('|   /|')
        print(str1, str2, er1, er3, str5, str6, sep='\n')
        return ' '
    if error == 5:
        er1 = str3 + 'o'
        er4 = '|   /|\\'
        print(str1, str2, er1, er4, str5, str6, sep='\n')
        return ' '
    if error == 6:
        er1 = str3 + 'o'
        er4 = '|   /|\\'
        er5 = '|   /'
        print(str1, str2, er1, er4, er5, str6, sep='\n')
        return ' '
    if error == 7:
        er1 = str3 + 'o'
        er4 = '|   /|\\'
        er5 = '|   / \\'
        print(str1, str2, er1, er4, er5, str6, sep='\n')
        return ' '


# print(gallows(1))
# print()
# print(gallows(7))