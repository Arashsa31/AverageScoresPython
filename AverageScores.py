#@author Arash
#Write a program that reads in exam scores and displays the average score. 
# (Extra credit +2 display the highest score)
#You should first ask the user how many exams there are. 
#Your program must work for any number of exams.

# How many exams? 5
# Enter a score: 74
# Enter a score: 91
# Enter a score: 87
# Enter a score: 93
# Enter a score: 89
# The average score is 86.8. (and the high score is 93. Extra credit)

#input
print("How many exams? ")
n = int(input())

tempValue = 0
combinedScore = 0
tempScore = 0
highestScore = 0

while(tempValue < n):
    print("Enter a score: ")
    tempScore = float(input())
    tempValue += 1

    #check score validity
    while(tempScore<0 or tempScore>100):
        print("Enter a score between 0 and 100: ")
        tempScore = float(input())

    #adds all the scores into one variable
    combinedScore += tempScore

    #captures the highest score
    if(tempScore > highestScore):
        highestScore = tempScore

#calculations
combinedScore /=n

#output
print("The average score is {:.2f}. (and the high score is {:.2f}.Extra credit)".format(combinedScore, highestScore))