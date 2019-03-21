import fileinput
#50 mins
def main():
    output = []
    loc = ""
    suitKey = {"C":0, "D":20 "S":40 "H":60}
    numKey = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9 "T":10, "J": 11, "Q": 12, "K": 13, "A": 14}
    for line in fileinput.input():
        line = line.rstrip()
        if line == "#":
            for out in output:
                for player in out:
                    outString = ""
                    for card in player:
                        outString = card[1] + card[2] + " "
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
            deck = []
            n = [(,"N:","")]
            e = [(,"E:","")]
            s = [(,"S:","")]
            w = [(,"W:","")]
            direction = [s , w, n, e]
            players = []
            for i in range(loc,loc+4):
                players.append(direction[(i+1)%4])
            for i in range(0,len(input)-1):

                deck.append((suitKey[input[i]]+numKey[input[i+1]], input[i], input[i+1]))
            for i in range(0, len(deck)):
                players[i%4].append[deck[i]]
            for hand in players:
                hand.sort()
            output.append(direction)
    main()
if __name__ == "__main__":
    main()