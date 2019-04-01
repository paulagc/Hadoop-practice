#!/usr/bin/python
 
import sys
 
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 26:
        try:
            maximo = max(float(data[2]), float(data[3]), float(data[4]), float(data[5]))
            minimo = min(float(data[2]), float(data[3]), float(data[4]), float(data[5]))
            medio = (float(data[2])+float(data[3])+float(data[4])+float(data[5]))/float(4)
            data.append(maximo)
            data.append(minimo)
            data.append(medio)
        except ValueError:
            continue

    if len(data) == 29:
	    idref, ident, gsm19023, gsd19024, gsd19025, gsd19026, genetitle, genesymbol, geneID, uniGenetitle, uniGenesymbol, uniGeneID, NucleotideTitle, GI, GenBankAccession, PlatformCLONEID, PlatformORF, PlatformSPOTID, Chromosomelocation, Chromosomeannotation, GOFunction,GOProcess, GOComponent, GOFunctionID, GOProcessID, GOComponentID, Max, Min, Avg = data
 
    print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}\t{13}\t{14}\t{15}".format(idref, ident, gsm19023, gsd19024, gsd19025, gsd19026, genetitle, genesymbol, geneID, uniGenetitle, uniGenesymbol, uniGeneID, NucleotideTitle, Max, Min, Avg)

 
