hexfrom = input("Hex from: ").split()
hexto = input("Hex to: ").split()
hexto1 = input("Hex to: ").split()
hexto2 = input("Hex to: ").split()
hexto3 = input("Hex to: ").split()
hexto4 = input("Hex to: ").split()
hexto5 = input("Hex to: ").split()
hexto6 = input("Hex to: ").split()
data = []

def toint(convert):
    if(len(convert) == 0):
        return
    convert[0] = int(convert[0])
    convert[1] = int(convert[1])
    convert[2] = int(convert[2])

def makeDezList(fr, to):
    if(len(fr) == 0 or len(to) == 0):
        return
    n = abs(fr[0] - to[0])
    if(abs(fr[1] - to[1]) > n):
        n = abs(fr[1] - to[1])
    if(abs(fr[2] - to[2]) > n):
        n = abs(fr[2] - to[2])
    s = 0
    for i in range(n):
        if(fr[0] < to[0]):
            fr[0] += 1
        elif(fr[0] > to[0]):
            fr[0] -= 1
        if(fr[1] < to[1]):
            fr[1] += 1
        elif(fr[1] > to[1]):
            fr[1] -= 1
        if(fr[2] < to[2]):
            fr[2] += 1
        elif(fr[2] > to[2]):
            fr[2] -= 1
        if(s % 5 == 0 or s == 0):
            data.append('#%02x%02x%02x' % (fr[0], fr[1], fr[2]))
        s += 1

def writeToFile():
    i = 1
    for hex in data:
        myfile.write(".rainbow" + str(i) + "::-webkit-scrollbar-thumb{\n  background: " + hex + ";\n}\n")
        i += 1

toint(hexfrom)
toint(hexto)
toint(hexto1)
toint(hexto2)
toint(hexto3)
toint(hexto4)
toint(hexto5)
toint(hexto5)
toint(hexto6)
makeDezList(hexfrom, hexto)
makeDezList(hexto, hexto1)
makeDezList(hexto1, hexto2)
makeDezList(hexto2, hexto3)
makeDezList(hexto3, hexto4)
makeDezList(hexto4, hexto5)
makeDezList(hexto5, hexto6)
myfile = open("generatedCodeHere.txt", "w")
writeToFile()
myfile.close()
