#!usr/bin/python

## Extract gene expression data for ccRCC tissues only from the gene expression file that already contains only the gene expression data for my GOIs

# ---------------------------------------------------------------------------
#               import libraries and specify paths
#----------------------------------------------------------------------------
import sys
file_gene_exp_ccRCC = open('/home/tracey/Desktop/MASTERS_2014/ICGC/Gene_expression_ICGC_and_COSMIC/COSMIC_gene_exp_173_non-disease.txt')
#Format ccRCC disease genes: COSMIC_gene_exp_175_GOI.txt')
file_tissue_code = open('/home/tracey/Desktop/MASTERS_2014/ICGC/TCGA_tissue_codes.txt')


# ---------------------------------------------------------------------------
#               place tissue codes into a list
#----------------------------------------------------------------------------
tissue_list=[]
for tissues in file_tissue_code:
    tissue = tissues.strip('\n')
    tissue_list.append(tissue.strip())
#file_tissue_code.close()
#print tissue_list


# ---------------------------------------------------------------------------
#               place gene expression data into a list
#----------------------------------------------------------------------------
sys.stdout = open('/home/tracey/Desktop/MASTERS_2014/ICGC/Gene_expression_ICGC_and_COSMIC/gene_exp_data_for_ccRCC_tissue_AND_non_disease_genes.txt', 'w')
#Format ccRCC disease genes: gene_exp_data_for_ccRCC_andGOI.txt', 'w')
gene_exp_list = []
# Format gene expression file:
# EZH2	TCGA-02-2483-01	over	2.247
for line in file_gene_exp_ccRCC:
    
    gene = line.split('\t')[0]
    patient_ID = line.split('\t')[1]
    regulation = line.split('\t')[2]
    z_score = line.split('\t')[3].strip('\n')
    gene_exp_list.append([gene, patient_ID, regulation, z_score])
    #print gene_exp_list
    #file_gene_exp_ccRCC.close()
    for code in tissue_list:
       if code in patient_ID:
            print gene + '\t' + patient_ID + '\t' + regulation + '\t' + z_score

        


