import shelve
for i in dir(shelve.Shelf):
    if i[0]!='_':
        print(i,end=' ')
