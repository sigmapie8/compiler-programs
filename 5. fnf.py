
def first_func(g):
    non=g[0:1]
    gram=g[2:]
    first[non]=set([])
    gram=gram.split('|')
    for k in gram:
        temp=k[0:1]
        if(temp.islower()):
            first[non].add(temp)
        elif(temp.isupper()):
            first_func(map_gram[temp])
            first[non].update(first[temp])
        else:
            first[non].add(temp)
            
def follow_func(nt):
    follow[nt]=set([])
    for k in grammer:
        ter=k[0:1]
        k=k[2:]
        if(nt in k):
            temp=k[k.index(nt)+1]
            if(temp.islower()):
                follow[nt].add(temp)
            elif(temp.upper()):
                follow[nt].update(first[temp])
            elif(temp==""):
                follow_func(ter)
                follow[nt].update(follow[ter])
            else:
                follow(nt).add(temp)
                
n=int(input("Enter the number of non-terminals in the grammer:"))
grammer=[]
nonTer=[]
map_gram={}
first={}
follow={}
                
for i in range(n):
    grammer.append(input())
    nonTer.append(grammer[0:1])
    map_gram[grammer[i][0:1]]=grammer[i]

for i in grammer:
    first_func(i)
print(first)
for i in nonTer:
    follow_func(i)
print(follow)
