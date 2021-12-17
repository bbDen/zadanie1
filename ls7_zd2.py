# дана строка , если в ней встречается пробел заменить его знаком "*" если несколько пробелов подряд, заменить его
# одним знаком * в конце и начале убрать пробелы

stroka=' Я не знаю что написать    потому будет простой текст '

def changeWord(stroka):
    list_char=[]
    list_char.extend(stroka.split())
    return '*'.join(list_char)
print(changeWord(stroka))
