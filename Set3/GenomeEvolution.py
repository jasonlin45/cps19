import fileinput

def read():
    sequences = []
    for line in fileinput.input():
        if line == "0":
            return sequences
        else:
            cur = line.split()
            if len(cur) == 1:
                pass
            else:
                sequences.append(line.split())

def calculate(seq1, seq2):
    seq1subsets = []
    seq2subsets = []
    start = 0
    step = 2
    while step < len(seq1):
        while start < len(seq1-2):
            for i in range(start,len(seq1),step):
                sub1 = []
                sub2 = []
                sub1.append(int(seq1[i]))
                sub2.append(int(seq2[i]))
                sub1.sort()
                sub2.sort()
            seq1subsets.append(sub1)
            seq2subsets.append(sub2)
            start+=1
        step+=1

def main():
    sequences = read()
    output = []
    seq1list = []* len(sequences)/2
    seq2list = [] * len(sequences)/2
    for i in range(len(sequences)):
        if (i+1)%2 == 1:
            seq1list = sequences[i]
        else:
            seq2list = sequences[i]
    for i in range(len(seq1list)):
        output.append(calculate(seq1list[i],seq2list[i]))
    for val in output:
        print(val)
if __name__=="__main__":
    main()