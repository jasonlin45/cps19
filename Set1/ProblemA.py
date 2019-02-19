import fileinput
import math

def solution(arr):
    numColors = int(arr[0])
    grayGoal = int(arr[len(arr)-1])
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    colors = sorted(arr[1:len(arr)-1], reverse = True)  # Sorted in descending order
    sets = math.ceil(int(colors[0])/50)
    paints = [50*sets] * len(colors)
    gray = 0 # Amount of Gray
    # Calculate leftover paint
    for i in range(0, len(colors)):
        paints[i] = paints[i] - colors[i]

    paints = sorted(paints, reverse = True)

    while gray < grayGoal:
        newGray = paints[2]//2
        while newGray != 0:
            gray += newGray
            if gray >= grayGoal:
                return sets
            for i in range(0,3):
                paints[i] = paints[i]-newGray
            paints = sorted(paints, reverse = True)
            if paints[2] == 1:
                newGray = 1
            else:
                newGray = paints[2]//50

        sets += 1
        for i in range(len(paints)):
            paints[i] = paints[i] + 50


    return sets







def main():
    for line in fileinput.input():
        input = line.split()
        if int(input[0]) == 0:
            return
        print(str(solution(input)))


if __name__ == "__main__":
    main()