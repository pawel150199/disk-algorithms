import os
import math

class Algorithms(object):
    """Algorytm wyznaczania scieżek na dysku"""

    def __init__(self, s, start, row):
        self.s = s
        self.start = start
        self.row = row

    def FCFS(self):
        print("Algorytm FCFS")
        print()
        print(f"Wynik:  {self.row}")
        print()

    def SSFT(self):
        print("Algorytm SSFT")
        print()
        l = int(start)
        xd = []
        temp = []
        length=len(self.row)
        exch=[]
        for i in range(0, length):
            exch.append(self.row[i])

        for i in range(0, length):
            xd.append(0)

        for x in range(0, length):
            for i in range(0, length):
                xd[i] = abs(l-int(exch[i]))
            ix = xd.index(min(xd))
            l = int(exch[ix])
            temp.append(exch[ix])
            exch[ix]=100000000000

        print(f"Wyniki:  {temp}")
        print()

    def SCAN(self):
        print("Algorytm SCAN")
        print()
        temp=[]
        xd=[]
        for i in range(0,len(self.row)):
            if int(start)<int(self.row[i]):
                xd.append(int(self.row[i]))

        xd.sort() 
        for i in range(0,len(self.row)):
            if int(start)>int(self.row[i]):
                temp.append(int(self.row[i]))
        temp.sort(reverse=True) 
        temp.append(0)
        for i in range(0,len(xd)):
            temp.append(xd[i])
        temp.append(int(self.s))
    
        print(f"Wynik: {temp}")
        print()
    def CSCAN(self):
        print("Algorytm CSCAN")
        print()
        temp=[]
        xd=[]
        for i in range(0,len(self.row)):
            if int(start)<int(self.row[i]):
                xd.append(int(self.row[i]))

        xd.sort()
        xd.append(int(self.s))
        for i in range(0,len(self.row)):
            if int(start)>int(self.row[i]):
                temp.append(int(self.row[i]))
        temp.sort()
        xd.append(0)
        for i in range(0,len(temp)):
            xd.append(temp[i])
        
    
        print(f"Wynik: {xd}")
        print()
    def LOOK(self):
        print("Algorytm LOOK")
        print()
        temp=[]
        xd=[]
        for i in range(0,len(self.row)):
            if int(start)<int(self.row[i]):
                xd.append(int(self.row[i]))

        xd.sort() 
        for i in range(0,len(self.row)):
            if int(start)>int(self.row[i]):
                temp.append(int(self.row[i]))
        temp.sort(reverse=True) 
        for i in range(0,len(xd)):
            temp.append(xd[i])

        print(f"Wynik: {temp}")
        print()

    def CLOOK(self):
        print("Algorytm CLOOK")
        print()
        temp=[]
        xd=[]
        for i in range(0,len(self.row)):
            if int(start)<int(self.row[i]):
                xd.append(int(self.row[i]))

        xd.sort()
        for i in range(0,len(self.row)):
            if int(start)>int(self.row[i]):
                temp.append(int(self.row[i]))
        temp.sort()
        for i in range(0,len(temp)):
            xd.append(temp[i])
        
    
        print(f"Wynik: {xd}")
        print()





row = []
print("Wprowadz dane: ")
print()
s = input("Podaj liczbe sektorów: ")
start = input("Podaj numer sektoru startowego:  ")
c = input("Podaj liczbe odwołań do sektorów: ")
for i in range(0, int(c)):
    row.append(input("Podaj numer sektoru: "))

xd = Algorithms(s, start, row)
xd.FCFS()
xd.SSFT()
xd.SCAN()
xd.CSCAN()
xd.LOOK()
xd.CLOOK()


