import fileinput


def solution(a, b, c, d):
    x = int(a)
    y = int(b)
    paper_x = int(c)
    paper_y = int(d)
    if y < x:
        temp = x
        x = y
        y = temp
    if paper_y < paper_x:
        temp = paper_x
        paper_x = paper_y
        paper_y = temp
    if (x <= paper_x and y <= paper_y):
        return 100
    else:
        return int(min(paper_x/x*100, paper_y/y*100))


def main():
    for line in fileinput.input("Problem3Input.txt"):
        if line == "0 0 0 0":
            return
        a, b, c, d = line.split()
        print(str(solution(a, b, c, d)) + "%")


if __name__ == "__main__":
    main()
