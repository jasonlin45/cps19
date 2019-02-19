import fileinput

class courses:
    def __init__(self, name, semester, prereque_count, prereques):
        self.name = name
        self.semester = semester
        self.prereque_count = prereque_count
        self.prereques = prereques


def main():

    courses = [None]
    maxCourses = 0
    skip = False
    isInt = False
    counter = 0
    classesTaken = []
    semesterCount = 0
    semesterCourses = 0

    for line in fileinput.input("Problem2Input.txt"):
        try:
            int(line[0])
            isInt = True
        except:
            isInt = False

        if (isInt and line == "-1 -1"):
            return

        data = line.split(' ')

        if (isInt):
            courses = [None]*int(data[0])
            maxCourses = int(data[1])
            skip = True
        elif !(skip):


        skip = False

    semesterCount = 0
    semesterCourses = 0

    while (len(classesTaken) < len(courses)):
        semesterCount += 1
        isfall = not isfall
        semesterCourses = 0










if __name__=="__main__":
    main()