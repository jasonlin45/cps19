import fileinput

def main():
    i = 1
    for line in fileinput.input():
        data = line.rstrip().split()
        if data[1] != "0":
            distance = float(data[0]) * int(data[1]) * 3.1415927 / (5280*12)
            mph = distance / float(data[2]) * 3600
            distance, mph = "{:.2f}".format(distance), "{:.2f}".format(mph)
            print("Trip #" + str(i) + ": " + str(distance) + " " + str(mph))
            i += 1


if __name__ == "__main__":
    main()