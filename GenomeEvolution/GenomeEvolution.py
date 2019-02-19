import fileinput

def read():
    sequences = []
    for line in fileinput.input("gene.txt"):
        if line == "0":
            return sequences
        else:
            cur = line.split()
            if len(cur) != 1:
                sequences.append(line.split())

def calculate(seq1, seq2):
    counter = 0
    size = 2
    while size <= len(seq1):
        start = 0
        seq1subsets = []
        seq2subsets = []
        while start <= len(seq1)-size:
            sub1 = []
            sub2 = []
            for i in range(start,start+size,1):
                sub1.append(int(seq1[i]))
                sub2.append(int(seq2[i]))
            sub1.sort()
            sub2.sort()
            seq1subsets.append(sub1)
            seq2subsets.append(sub2)
            start+=1
        for subset1 in seq1subsets:
            for subset2 in seq2subsets:
                if len(subset1)==len(subset2):
                    match = True
                    i=0
                    while match and i<len(subset1):
                        if subset1[i] != subset2[i]:
                            match = False
                        i+=1
                    if match:
                        counter+=1
        size += 1
    return counter


def main():
    sequences = read()
    output = []
    seq1list = []
    seq2list = []
    for i in range(len(sequences)):
        if (i+1)%2 == 1:
            seq1list.append(sequences[i])
        else:
            seq2list.append(sequences[i])
    for i in range(len(seq1list)):
        output.append(calculate(seq1list[i],seq2list[i]))
    for val in output:
        print(val)
if __name__=="__main__":
    main()
