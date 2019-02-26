import fileinput
def main():
    input = []
    matches = []
    scan = True
    counter = 0
    for line in fileinput.input():
        line = line.rstrip()
        if scan:
            input = list(line)
            scan = False
        elif len(line)==len(input):
            cur = list(line)
            for i in range(len(input)):
                if input[i]!=cur[i]:
                    if input[i] != '*':
                        break
                    if i==len(input)-1:
                        counter+=1
                        matches.append(line)
                elif i==len(input)-1:
                    counter += 1
                    matches.append(line)
    print(counter)
    for match in matches:
        print(match)
if __name__ == "__main__":
    main()