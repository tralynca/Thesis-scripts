#!/usr/bin/python

# ---------------------------------------------------------------------------
#                   import libraries and specify paths
#----------------------------------------------------------------------------

import sys
import glob


path_1000gen = "/home/tracey/Desktop/MASTERS_2014/1000_genomes/somatic_variants_1000genomes/input_files/Variants*"
path_variants = "/home/tracey/Desktop/MASTERS_2014/ICGC/Regulome_annotations/Results/Annotations_from_web_interface/regulome_annotation_matched_to_original_variant/173_ccRCC_genes/173_ccRCC_regulome_annotation_CDS_sv.txt"
#Format non-disease  and CDS: 173_non_disease_genes/non_disease_regulome_annotation_CDS_sv.txt"
#Format non-disease and non-coding: 173_non_disease_genes/combined_non_disease_non_coding_regulome_annot_of_sv.txt"
#Format ccRCC disease genes: 173_ccRCC_genes/combined_non_coding_regulome_annotation_of_sv_UNIQ_positions.txt"


  
## Format input file: 
## ABCA6	17	67080155	67080155	DO46885	SA507332	T	T	C	introns	ENSG00000154262	7

#gen_path = open(path_1000gen)
gen_path = glob.glob(path_1000gen)
variants_file = open(path_variants)
#sys.stdout = open('/home/tracey/Desktop/MASTERS_2014/ICGC/1000genomes/173_ccRCC_genes/ccRCC_CDS_AFs.txt', 'w')
#Format non-disease and CDS: 173_non_disease_genes/non_disease_genes_CDS_AFs.txt', 'w')
#Format non-disease and non-coding: 173_non_disease_genes/non_disease_genes_non_coding_AFs.txt', 'w'
#Format ccRCC disease genes: 173_cccRCC_genes/cRCC_non_coding_AFs.txt', 'w')

# ---------------------------------------------------------------------------
#                                  create maf list
#----------------------------------------------------------------------------

var_list = []

for line in variants_file:
    column = line.strip().split('\t')
    var_gene = column[0]
    var_chrm = column[1]
    var_start = column[2]
    donor_ID = column[4]
    ref_allele = column[6]
    from_allele = column[7]
    to_allele = column[8]
    UCSC_anno = column[9]
    ensembl_gene = column[10]
    regulome_score = column[11]
    var_list.append([var_gene, var_chrm, var_start, ref_allele, from_allele, to_allele, donor_ID, UCSC_anno, ensembl_gene, regulome_score])
#variants_file.close()
#print var_list

# ---------------------------------------------------------------------------
#                            create 1000_genomes list
#----------------------------------------------------------------------------
## Format input file:
##2	65555432	rs57485869	G	C	100	PASS	LDAF=0.0398;RSQ=0.9871;AA=G;AN=2184;VT=SNP;THETA=0.0056;SNPSOURCE=LOWCOV;AC=86;ERATE=0.0003;AVGPOST=0.9982;AF=0.04;AMR_AF=0.01;AFR_AF=0.17


for file_genome in gen_path:
    genome_list = []
    input_1000gen = open(file_genome)
    sys.stderr.write(file_genome)
    for line in input_1000gen:
        #sys.stderr.write('.')
        if line.strip().startswith('#'):
            continue
        columns = line.strip().split('\t')
        chrm = columns[0]
        #print chrm
        position = columns[1]
        #print position
        rsID = columns[2]
        ref_allele = columns[3]
        alt_allele = columns[4]
        qualit = columns[5]
        info = columns[7] #.strip().split(';')
        #info.sort()
        #print info
        genome_list.append([rsID, chrm, position, ref_allele, alt_allele , info])
        #print genome_list

# ---------------------------------------------------------------------------
#             check allele frequency of variant across super populations
#----------------------------------------------------------------------------
    
    for var_item in var_list:
        for gen_item in genome_list:
            if var_item[1] == gen_item[1] and var_item[2] == gen_item[2] and var_item[4] == gen_item[3] and var_item[5] == gen_item[4]:
                print  var_item[0] + '\t' + var_item[1] + '\t' +  var_item[2] + '\t' +  var_item[3] + '\t' +  var_item[4] + '\t' +  var_item[5] + '\t' +  var_item[6] + '\t' +  var_item[7] + '\t' +  var_item[8] + '\t' +  var_item[9]  + '\t' +  gen_item [0] + '\t' +  gen_item[5] 






