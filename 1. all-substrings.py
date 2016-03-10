def substring(string):
    for i in range(len(string)):
        print(string[:i+1],end=" ")
        
string=input("Enter the String:")
print("All the substring in the string {} are:".format(string))
for i in range(len(string)):
    substring(string[i:]) #selecting a substring and making substring out of those substring
    print()
