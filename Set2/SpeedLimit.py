import fileinput

def main():
    i = 0
    speeds = []
    distance = 0
    for line in fileinput.input():
        if line == "-1":
            return
        if len(line) == 2 or len(line) == 3:
            i = int(line)
        else:
            speeds.append(line)
            i -= 1
        if i == 0:
            j = 0
            while(j < len(speeds)):
                if(j is not 0):
                    a, b = speeds[j].split()
                    c, d = speeds[j-1].split()
                    distance += int(a)*(int(b)-int(d))
                else:
                    a, b = speeds[j].split()
                    distance += int(a)*int(b)
                j += 1
            print(str(distance) + " miles")
            i = 0
            speeds = []
            distance = 0

if __name__ == "__main__":
    main()