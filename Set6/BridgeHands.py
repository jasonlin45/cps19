import fileinput
def main():
    output = []
    loc = ""
    suitKey = {"C":0, "D":20, "S":40, "H":60}
    numKey = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, "T":10, "J": 11, "Q": 12, "K": 13, "A": 14}
    first = True
    for line in fileinput.input():
        line = line.rstrip()
        if line == "#":
            for out in output:
                for player in out:
                    outString = player[0][1]
                    for i in range(1, len(player)):
                        outString = outString + " " + player[i][1] + player[i][2]
                    print(outString)
        elif len(line)==1:
            if line=="S":
                loc=0
            elif line=="W":
                loc=1
            elif line=="N":
                loc=2
            else:
                loc=3
        else:
            input = list(line)
            if(first):
                deck = []
                for i in range(0, len(input) - 1, 2):
                    deck.append((suitKey[input[i]] + numKey[input[i + 1]], input[i], input[i + 1]))
                first = False
            else:
                for i in range(0, len(input) - 1, 2):
                    # print(str(i) + " : " + input[i]+input[i+1])
                    # print(str(i) + " : " + str(suitKey[input[i]]))
                    deck.append((suitKey[input[i]] + numKey[input[i + 1]], input[i], input[i + 1]))
                n=[( 0,"N:","")]
                e=[( 0,"E:","")]
                s=[( 0,"S:","")]
                w=[( 0,"W:","")]
                direction = [s , w, n, e]
                players = []
                for i in range(loc,loc+4):
                    players.append(direction[(i+1)%4])
                for i in range(0, len(deck)):
                    players[i%4].append(deck[i])
                for hand in players:
                    hand.sort()
                output.append(direction)
                first = True
if __name__ == "__main__":
    main()