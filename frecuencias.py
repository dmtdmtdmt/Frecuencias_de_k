from math import sqrt
from random import randint
from decimal import Decimal, getcontext
from datetime import datetime
import subprocess
getcontext().prec = 10000
hora = datetime.now()
a = f"{hora.strftime('Data_%A_%d-%m-%Y_%H:%M:%S-%p')}" 
cantidad = 2
def desv_st(x):
    i = j = k = n = 0
    for i in x:
        k = k + i
        n = n + 1
    k = k / n
    for i in x:
        j = j + (i-k)**2
    j = sqrt(j / n)    
    return j
def mostrar_progreso(actual, total, ancho=50):
    porcentaje = actual / total
    barras_completas = int(ancho * porcentaje)
    barra = "." * barras_completas + " " * (ancho - barras_completas)
    print(f"\r[{barra}] {actual}/{total} ({porcentaje:.1%})", end="", 
    flush=True)
with open(a + '.txt', 'w') as archivo:
    archivo.write("\nIdeal Case\n")
    archivo.write(f"{'='*10}\n")
    archivo.write("Proportions of visits by classes\n")
    archivo.write(f"{'-'*32}\n")
    archivo.write("   d(0)="+ str(1 / 3)+"\n")
    archivo.write("   d(1)="+ str(1 / 6)+"\n")
    archivo.write("   d(2)="+ str(1 / 3)+"\n")
    archivo.write("   d(3)="+ str(1 / 6)+"\n")
    archivo.write("Limit of the sequences\n")
    archivo.write(f"{'-'*22}\n")
    archivo.write("  "+ str(1 / (2**(1 + 2/3 + 1/6) - 3))+"\n")
    archivo.write("\n\nFibonacci Model\n")
    archivo.write(f"{'='*15}\n")
fibonacci = []
fibonacci.append(1)
fibonacci.append(1)
k = 0
while k < 100000:
    k += 1
    fibonacci.append(fibonacci[-1]+fibonacci[-2])
with open(a + '.txt', 'a') as archivo:
    archivo.write("Proportions of visits by classes\n")
    archivo.write(f"{'-'*32}\n")
    archivo.write("   d(0) ="+ str(fibonacci[-2] / (2*fibonacci[-1]))+"\n")
    archivo.write("   d(1) ="+ str(fibonacci[-3] / (2*fibonacci[-1]))+"\n")
    archivo.write("   d(2) ="+ str(fibonacci[-2] / (2*fibonacci[-1]))+"\n")
    archivo.write("   d(3) ="+ str(fibonacci[-3] / (2*fibonacci[-1]))+"\n")
    archivo.write("Limit of the sequences\n")
    archivo.write(f"{'-'*22}\n")
    archivo.write("  "+ str(1 / (2**(1 + (fibonacci[-2] / (fibonacci[-1])) 
    + (fibonacci[-3] / (2*fibonacci[-1])))-3))+"\n")
    archivo.write("\n\nQuasi-Fibonacci Model\n")
    archivo.write(f"{'='*21}\n")
k = k = l = m = i = j = 0
x = 0
x = randint(0,3)
while m < 1000000:
    m += 1
    if x == 0:
        i += 1   #0
        k += 1   #2
    elif x == 1:
        i += 1    #0
    elif x == 2:
        j += 1    #1
        l += 1    #3
    elif x == 3:
        k += 1    #2
    x = randint(0,3)
    mostrar_progreso(m, 1000000)
with open(a + '.txt', 'a') as archivo:
    archivo.write("Proportions of visits by classes\n")
    archivo.write(f"{'-'*32}\n")
    archivo.write("   d(0)="+ str(i / (i + j + k + l))+"\n")
    archivo.write("   d(1)="+ str(j / (i + j + k + l))+"\n")
    archivo.write("   d(2)="+ str(k / (i + j + k + l))+"\n")
    archivo.write("   d(3)="+ str(l / (i + j + k + l))+"\n")
    archivo.write("Limit of the sequences\n")
    archivo.write(f"{'-'*22}\n")
    archivo.write("  "+ str(1 / (2**(1 + ((i + j + k) / (i + j + k + l)))
     - 3))+"\n")
    archivo.write("\n\nReal experiment with a random number\nin "
    "[2^60,10^4000]\n")
    archivo.write(f"{'='*36}\n")
k = i = j = k = l = m = 0
x = 1
x = randint(2**60,10**4000)
while m < 1:
    m += 1
    while x > 10**16:
        if x % 4 == 0:
            x = x // 2
            i += 1
        elif x % 4 == 1:
            x = 3 * x + 1
            j += 1
        elif x % 4 == 2:
            x = x // 2
            k += 1
        elif x % 4 == 3:
            x = 3 * x + 1
            l += 1
    x = randint(2**60,10**4000)
with open(a + '.txt', 'a') as archivo:
    archivo.write("Proportions of visits by classes\n")
    archivo.write(f"{'-'*32}\n")
    archivo.write("   d(0)="+ str(i / (i + j + k + l))+"\n")
    archivo.write("   d(1)="+ str(j / (i + j + k + l))+"\n")
    archivo.write("   d(2)="+ str(k / (i + j + k + l))+"\n")
    archivo.write("   d(3)="+ str(l / (i + j + k + l))+"\n")
    archivo.write("Limit of the sequences\n")
    archivo.write(f"{'-'*22}\n")
    archivo.write("  "+ str(1 / (2**(1 + ((i + j + k) / (i + j + k + l))) 
    - 3))+"\n")
    archivo.write("\n\nReal Experiment with "+str(cantidad)+" random"
    " numbers\nin [2^60,10^4000]\n")
    archivo.write(f"{'='*39}\n")
k = i = j = k = l = m = 0
x = 1
fibi = []
fibj = []
fibk = []
fibl = []
x = randint(2**60,10**4000)
print("Processing ",cantidad," random numbers in [2^60,10^4000]\n")
while m < cantidad:
    m += 1
    while x > 10**16:
        if x % 4 == 0:
            x = x // 2
            i += 1
        elif x % 4 == 1:
            x = 3 * x + 1
            j += 1
        elif x % 4 == 2:
            x = x // 2
            k += 1
        elif x % 4 == 3:
            x = 3 * x + 1
            l += 1
    x = randint(2**60,10**4000)
    fibi.append(i / (i + j + k + l))
    fibj.append(j / (i + j + k + l))
    fibk.append(k / (i + j + k + l))
    fibl.append(l / (i + j + k + l))
    mostrar_progreso(m, cantidad)
with open(a + '.txt', 'a') as archivo:
    archivo.write("Proportions of visits by classes\n")
    archivo.write(f"{'-'*33}\n")
    archivo.write("   d(0)="+ str(sum(fibi) / len(fibi))+"\n")
    archivo.write("   d(1)="+ str(sum(fibj) / len(fibj))+"\n")
    archivo.write("   d(2)="+ str(sum(fibk) / len(fibk))+"\n")
    archivo.write("   d(3)="+ str(sum(fibl) / len(fibl))+"\n")
    archivo.write("Standard deviations\n")
    archivo.write(f"{'-'*33}\n")
    archivo.write("   s(0)="+ str(desv_st(fibi))+"\n")
    archivo.write("   s(1)="+ str(desv_st(fibj))+"\n")
    archivo.write("   s(2)="+ str(desv_st(fibk))+"\n")
    archivo.write("   s(3)="+ str(desv_st(fibl))+"\n")
    archivo.write("Limit of the sequences\n")
    archivo.write(f"{'-'*24}\n")
    archivo.write("  "+ str(1 / (2**(1 + ((i + j + k) / (i + j + k + l))) 
    - 3))+"\n")
print('\nResults saved in ---'+ a + '.txt---', )
subprocess.call(["open",a + '.txt'])
