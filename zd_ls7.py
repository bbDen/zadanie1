

stroka=' Я не знаю что написать    потому будет простой текст '

def changeWord(stroka):
    list_char=[]
    list_char.extend(stroka.split())
    return '*'.join(list_char)
print(changeWord(stroka))
