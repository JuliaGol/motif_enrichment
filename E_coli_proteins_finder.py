from Bio.Blast.Applications import NcbitblastnCommandline
from Bio.Blast.Applications import NcbimakeblastdbCommandline
from Bio import SeqIO

file=open("genes_e_coli.fa")
#funkcja obsługująca blast
def blast(query, database, dbtype, title, evalue, outfmt, out):
    #tworzę bazę danych dla blasta
    cline = NcbimakeblastdbCommandline(dbtype=dbtype, input_file=database,title=title)
    cline()
    #wykonuję blasta wobec danej bazy danych
    blastx_cline = NcbitblastnCommandline(query=query, db=database, evalue=evalue, outfmt=outfmt, out=out)
    blastx_cline()

blast("protein_fragments.fa","genes_e_coli.fa","nucl","ecoli",0.001,"6 qseqid sseqid evalue", "ecoli.m6")

#tworze plik csvz pliku tsv który otrzymałąm
def tsvtocsv(filename, newfilename):
    file1=open(filename)
    file2=open(newfilename,"w")
    for line in file1:
        tab=line.split("\t")
        file2.write(tab[0]+","+tab[1]+","+tab[2])

tsvtocsv("ecoli.m6", "ecolihits.csv")


#parsowanie blasta i znalezienie sekwecji do znalezionych id
def readtheblast(blastoutput, promotersfile):
    genesA=[]
    genesB=[]
    namegenesA={}
    namegenesB = {}

    fileblastoutput=open(blastoutput)
    #tworzę słowniki gdzie klucz to nazwa białka a wartość to nazwa genu
    for line in fileblastoutput:
        tab=line.split(",")
        genename=tab[1]
        proteinname=tab[0]
        if "groupA" in proteinname:
            namegenesA[proteinname]=namegenesA.get(proteinname,[])+[genename]
            genesA+=[genename]
        elif "groupB" in proteinname:
            namegenesB[proteinname]=namegenesB.get(proteinname,[])+[genename]
            genesB += [genename]
    with open(promotersfile, "rU") as handle:
        filepromotersA=open("promotersA.fa", "w")
        filepromotersB = open("promotersB.fa", "w")
        for promoter in SeqIO.parse(handle, "fasta"):

            if promoter.id in genesA:
                #tworze plik A z promotorami grupy A
                # szukanie motywów
                filepromotersA.write(">"+str(promoter.id)+"\n"+str(promoter.seq)+"\n")
            elif promoter.id in genesB:
                #tworzę plik B z promotorami grupy B
                filepromotersB.write(">"+str(promoter.id)+"\n"+str(promoter.seq)+"\n")

#pliki te zostały użyte jako input do programu MEME
readtheblast("ecolihits.csv","proms_e_coli_fixed.fa")

