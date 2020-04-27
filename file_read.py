#           для чтения данных из текстового файла используется команда "open".
#           в скобках указывается 'имя файла', 'режим открытия' (r - чтение, w - запись),
#           encoding - кодировка, чаще всего используется 'utf8'
info = open('file_read.txt', 'r', encoding='utf8') # показали откуда читаем
out = open('file_out.txt', 'w', encoding='utf8')   # показали куда записываем
a = int(info.readline())       # readline() - считывание построчно
b = int(info.readline())       # readlines() - считывание всего содержимого
print(a + b)
file = open('file_read.txt', 'r', encoding='utf8') # нельзя повторно считать теже строки
c = file.readlines()    # readlines() - считывание всего содержимого, в память
print(c)
for i in c[:-1]:    #   удалили символ переноса строки и печатаем поимвольно не включая
    i = i.strip()   #   последний элемент
    print(i, end='a')
print(c[-1])        #   печатаем последний элемент отдельно

file2 = open('file_read.txt', 'r', encoding='utf8')
for i in file2:                 #   данный метод позволяет считывать построчно
    print(int(i), end=' ')      #   не переполняя память, при больших  объемах

file3 = open('file_read.txt', 'r', encoding='utf8')
s = file3.read()                #   добавляет все содержимое файла в один str
print('\n', [s], sep='')

file4 = open('file_read.txt', 'r', encoding='utf8')
print(sum(map(int, file4.readlines())), file=out)  # через принт при помощи 'file='
                                                   # вывели ответ не в консоль, а в файл
#
#
#
#
#
#
#
#
#
#
#