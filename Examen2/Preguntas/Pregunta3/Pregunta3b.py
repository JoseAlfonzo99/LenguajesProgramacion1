# Jose Alfonzo 17-10012 
# Pregunta 3)b)

def misterioCreciente(p):
    if p == []:
        yield []
    else:
        for x in misterioCreciente(p[1:]):
            yield x
            if x==[] or p[0]<= x[0]:
                yield [p[0], *x]

for x in misterioCreciente([1,4,3,2,5]):
    print(x)