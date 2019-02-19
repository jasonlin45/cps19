import fileinput

def main():
    curWidth = 0
    curHeight = 0
    width = 0
    height = 0
    maxWidth = 0
    output = []
    for line in fileinput.input("WindowSizeInput.txt"):
        if line == "0":
            for item in output:
                print(item)
        else:
            if line == "-1 -1\n":
                output.append(str(width) + ' x ' + str(height))
                curWidth = 0
                curHeight = 0
                width = 0
                height = 0
                maxWidth = 0
            if len(line.split()) == 1:
                maxWidth = int(line)
            else:
                cur = line.split()
                w = int(cur[0])
                h = int(cur[1])
                if curWidth + w > maxWidth:
                    height += curHeight
                    curWidth = w
                    curHeight = h
                else:
                    curWidth += w
                    if curWidth > width:
                        width = curWidth
                    if h > curHeight:
                        curHeight = h
if __name__ == "__main__":
    main()