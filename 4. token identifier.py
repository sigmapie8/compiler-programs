#A program that can count distinct python identifiers and keywords in a txt file
import keyword as k

file=open("document.txt",encoding="utf-8")
content=file.read()
content=content.split()

keyword=set()
identifier=set()
other=set()
print("-----------------------------------------------------------------------")
for i in content:
    if(k.iskeyword(i)):
        print("keyword-{}".format(i))
        keyword.add(i)
    elif(i.isidentifier()):
        print("identifier-{}".format(i))
        identifier.add(i)
    else:
        print("other-{}".format(i))
        other.add(i)
print("-----------------------------------------------------------------------")
print("Keywords={}".format(len(keyword)))
print("Identifiers={}".format(len(identifier)))
print("Others={}".format(len(other)))
