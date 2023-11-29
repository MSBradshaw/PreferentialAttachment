# Homo_sapiens.GRCh38.109.entrez.tsv 
# gene_stable_id	transcript_stable_id	protein_stable_id	xref	db_name	info_type	source_identity	xref_identity	linkage_type
# ENSG00000160072	ENST00000673477	ENSP00000500094	83858	EntrezGene	DEPENDENT	-	-	-
# load Homo_sapiens.GRCh38.109.entrez.tsv as a dictionary that maps gene_stable_id to protein_stable_id (potentially many)
g_id = 0
p_id = 2
gene_to_pro = {}
for line in open('Ensembl/Homo_sapiens.GRCh38.109.entrez.tsv','r'):
    row = line.strip().split('\t')
    if row[g_id] not in gene_to_pro:
        gene_to_pro[row[g_id]] = []
    gene_to_pro[row[g_id]].append(row[p_id])


# get a set of nodes in huri HuRI/HuRI.tsv 
huri_nodes = set()
for line in open('HuRI/HuRI.tsv','r'):
    row = line.strip().split('\t')
    if row[0] in gene_to_pro:
        for n in gene_to_pro[row[0]]:
            huri_nodes.add(n)
    if row[1] in gene_to_pro:
        for n in gene_to_pro[row[1]]:
            huri_nodes.add(n)

print('huri_nodes', len(huri_nodes))
# get the number of edges in STRING exp where both nodes are in huri, and the number of nodes
string_exp_edges = 0
string_exp_nodes = set()

for line in open('String/9606.protein.physical.links.full.v11.5.txt','r'):
    if 'protein1' in line:
        continue
    row = line.strip().split(' ')
    n1 = row[0].split('.')[1]
    n2 = row[1].split('.')[1]
    if n1 in huri_nodes and n2 in huri_nodes:
        string_exp_edges += 1
        string_exp_nodes.add(n1)
        string_exp_nodes.add(n2)

print('HuRI intersect STRING Exp Edges:', string_exp_edges)
print('HuRI intersect STRING Exp Nodes:', len(string_exp_nodes))

