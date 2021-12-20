# list_ = [1, 1, 3, 2, 1, 3, 4,99]
# result = {}
#
#
# def count_repeat_items(list_):
#     for num in list_:
#         if result.get(num):
#             result[num] = result[num] + 1
#         else:
#             result[num] = 1
#
# count_repeat_items(list_)
# print(result)
# напишите прорамму которая прнимает имя файла и выводит его расширение.Если расширение  у файла определить невозможно
# то выбросите исключение
# дана строка , если в ней встречается пробел заменить его знаком "*" если несколько пробелов подряд, заменить его
# одним знаком * в конце и начале убрать пробелы

stroka=' Я не знаю что написать    потому будет простой текст '

def changeWord(stroka):
    list_char=[]
    list_char.extend(stroka.split())
    return '*'.join(list_char)
print(changeWord(stroka))
