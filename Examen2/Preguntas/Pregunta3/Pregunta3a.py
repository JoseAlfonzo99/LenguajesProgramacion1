# Jose Alfonzo 17-10012 
# Pregunta 3)a)

def misterio(a, b, c, d):
    if c == 0:
        yield a
        for x in misterio(b, a, b, d - 1):
            yield x
    elif d > 0:
        for x in misterio(a, b + 1, c - 1, d):
            yield x 

for x in misterio(0, 1, 0, 6 + 1):
    print(x)



#a = 2 * 0 + 3 * 1 + 2
#b = 4 * 1 + 5 * 2 + 1
#c = 5 * 0 + 2 * 2 + 3
#d = (a + b + c) % 7
#print(a)
#print(b)
#print(c)
#print(d)