def displayAverage(scores):
    total = 0
    for s in scores:
        total = total + s
    print("The average score is", total / len(scores))


score = [79, 39, 57, 73, 93, 23]
score1 = [38, 49, 95, 82, 28, 34]
displayAverage(score)
displayAverage(score1)
