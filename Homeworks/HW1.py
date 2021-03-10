oddList = list(range(0,9,2))
evenList = list(range(1,10,2))
extendedList = [i * 2 for i in oddList + evenList]
for i in extendedList:
    print(type(i))