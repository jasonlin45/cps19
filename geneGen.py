output = open("gene.txt", "w+")
gene1 = ""
gene2 = ""
for i in range(3001):
    gene1 = gene1 + " " + str(i)
    gene2 = str(i) + " " + gene2
output.write("3000 \n")
output.write(gene1 + "\n")
output.write(gene2 + "\n")
output.write("0")
