# motif_enrichment
The second project for Introduction to computational biology
It contains two scripts.
First script - E_coli_proteins_finder.py which finds E.Coli proteins in the genome. In this task, genome is included in a fasta file with genes' sequences (genes_e_coli.fa) and desirable proteins are in a fasta file with protein sequences (protein_fragments.fa). Protein fragments need to be matched against DNA sequences, so Blast is performed. The best hits are wrote to .csv file (ecolihits.csv). 
The file in which promoter's sequences is given (proms_e_coli.fa). This file includes promoters from theoretical groups A and B, which should have different regulatory mechanisms. This script identifies 10 sequence motifs present in the promoters associated with group A and 10 motifs associated with group B with length 15. To reach this goal script genrates file fasta files (promotersA.fa and promotersB.fa) as input to MEME-suite.

The output should be changed manually, because of the different MEME suite versions between one implemented in Biopython and one available online. For example:
it was:
PRIMARY SEQUENCES= promotersB.fa
CONTROL SEQUENCES= --none--
it should be:
DATAFILE= promotersB.fa

The second script - motif_enrichment.py parses MEME files and uses the binomial test to identify the motifs that are significantly enriched.
