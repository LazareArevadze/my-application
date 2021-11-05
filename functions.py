x = ([1,2,3,3,3,3,4,5])
y = []

def func():
    for a in x:
        if a not in y:
            y.append(a)
    print(y)
func()