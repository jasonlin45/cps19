import fileinput

def read():
    output = []
    p = []
    q = []
    pc = -1
    qc = -1
    for line in fileinput.input("StylishTest.txt"):
        if line == "0 0":
            output.append(p)
            output.append(q)
            return output
        else:
            try:
                cur = line.split()
                pc = int(cur[0])
                qc = int(cur[1])
                output.append(p)
                output.append(q)
            except(ValueError):
                if pc>0:
                    p.append(line)
                    pc=pc-1
                elif qc>0:
                    q.append(line)
                    qc=qc-1
                else:
                    raise Exception("FAT ERROR in p count, q count")

if __name__ == "__main__":
    print(read())