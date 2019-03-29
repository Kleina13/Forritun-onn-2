def Name(name):
    return name[0].upper() + name[1:].lower()

def NameM(name):
    list = []
    x = ' '
    for name in name.split(' '):
        list.append(name[0].upper() + name[1:])
    return x.join(list)

def PrintList(list):
    return ' '.join(list)

def PrintTuple(tup):
    counter = 0
    for i in tup:
        counter += 1
    for i in tup[0:counter]:
        print(i)

def intput(intput):
    intput = int(input(intput))
    return intput
