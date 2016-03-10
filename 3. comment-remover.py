#A python program to remove any comment in a c/c++ program

file = open("document.txt",encoding="utf-8")
content= file.read()
newfile=open("new_document.txt",mode="a",encoding="utf-8")
file.seek(0)

for i in file:
    serial=i;
    if('//' in serial):
        copy=serial[:serial.index('//')]
        newfile.write(copy)
    if('/*' in serial):
        copy=serial[:serial.index('/*')]
        newfile.write(copy)
        print(copy)
        while('*/' not in serial):
            serial=next(file)
        copy=serial[serial.index('*/')+3:]
        newfile.write(copy)
        print(copy)
    if('//' not in serial and '/*' not in serial and '*/' not in serial):
        copy=serial
        newfile.write(copy)
        print(copy)
            
