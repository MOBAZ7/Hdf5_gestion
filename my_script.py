import numpy as np
import pandas as pd
import h5py

f = h5py.File("mouse_matrix.h5", mode = "r")

#Permet d'aller chercher pour chaque gene de notre liste son indice dans le dataset genes du fichier
j = 0
ind = []
genes_list = ['Cnr1','Cnr2','Gpr18','Gpr55','Adgrf1','Gpr110','Gpr119','Trpa1','Trpv1','Trpv2','Trpv4',
             'Trpm8','Ppara','Pparg','Cacna1h','Ptgfr','Cacna1b','Glyatl3','Mogat1','Pla2g4e','Hrasls5',
             'Napepld','Abhd4','Dagla','Daglb','Gde1','Gdpd1','Ptpn22','Inpp5d','Ptgs2','Alox12','Alox15',
             'Ces1d','Ces2h','Ppt1','Pla1a','Faah','Naaa','Mgll','Magl','Abhd6','Abhd12','Abhd16a','Comt',
             'Agk','Dgke','PAM','Plcb1','Enpp2','Pla2g5','Pla2g10','Akr1b3','Fam213b','Ptges','Hprt','Gapdh',
             'Tbp','Rps13']
while j <= 32543:
    for g in genes_list:
        if g == f['meta/genes'][j]:
            ind.append([g,j])
    j = j + 1

#Permets d'aller chercher les expressions des genes dans le dataset expression du fichier hdf5 
#en utilisant les indices récupérés précédemment et écrire le résultat dans un fichier tsv
j = 0
genes_to_find = ['Cnr1','Cnr2','Gpr18','Gpr55','Adgrf1','Gpr110','Gpr119','Trpa1','Trpv1','Trpv2','Trpv4',
             'Trpm8','Ppara','Pparg','Cacna1h','Ptgfr','Cacna1b','Glyatl3','Mogat1','Pla2g4e','Hrasls5',
             'Napepld','Abhd4','Dagla','Daglb','Gde1','Gdpd1','Ptpn22','Inpp5d','Ptgs2','Alox12','Alox15',
             'Ces1d','Ces2h','Ppt1','Pla1a','Faah','Naaa','Mgll','Magl','Abhd6','Abhd12','Abhd16a','Comt',
             'Agk','Dgke','PAM','Plcb1','Enpp2','Pla2g5','Pla2g10','Akr1b3','Fam213b','Ptges','Hprt','Gapdh',
             'Tbp','Rps13']
fh = open("Genes_expression.tsv", "w+")
while j <= 135211:
    for i in ind:
        fh.write('{}'.format(f['meta/Sample_geo_accession'][j]))
        fh.write("\t")
        fh.write(i[0])
        fh.write("\t")
        fh.write('{}'.format(f['data/expression'][j][i[1]]))
        fh.write('\n')
    j = j + 1
