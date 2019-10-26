import statistics

theList = [1,2]

print(str(statistics.median(theList)))
print(str(statistics.median_low(theList)))

charList = ["You", "may", "say", "I'm", "a", "dreamer"]

def count_characters(theList):
    count = 0
    for i in theList:
        for ch in i:
            count +=1

    return count

print(count_characters(charList))


def my_reverse(theList):
    newList = []
    for i in theList:
        newList.insert(0, i)

    return newList

print(my_reverse(charList))

def create_file(fileName, num):
    output = open(fileName, "w")
    for i in range(num):
        output.write(str(i + 1) + "\n")


create_file("jbd.txt", 5)
