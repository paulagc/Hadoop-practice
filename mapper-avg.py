#!/usr/bin/python
 
import sys
listaAvg = [0]
for line in sys.stdin:
    data = line.strip().split("\t")
    gsm23 = float(data[2])
    if gsm23 in range(100,1000):
        avg = float(data[15])
        listaAvg.append(avg)

maximo = max(listaAvg)
print maximo


