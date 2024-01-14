import itertools
import math
 
Puzzle_practice = [[[1],[0],[0],[0],[0]],[[1],[0],[0],[0],[0]]]
Answer_practice = [[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

Puzzle_1 = [[[3],[3],[1,1],[2],[1,2]],[[1],[3,1],[2],[4],[2]]]
Answer_1 = [[1,0,0,0,0],[1,1,1,0,1],[1,1,0,0,0],[0,1,1,1,1],[0,0,0,1,1]]

Puzzle_2 = [[[5],[5],[5],[5],[5]],[[5],[5],[5],[5],[5]]]

Puzzle_3 = [[[3],[1],[0]],[[1],[1],[2]]]

Puzzle_4 = [[[4],[2,1],[1],[1]],[[4],[2],[1],[2]]]

Puzzle_5 = [[[3],[1,1],[3],[2],[1,2]],[[2],[1,1],[4],[3],[1,1]]]

PuzzleOn = Puzzle_5

TopTaskLenghth = len(PuzzleOn[0])
LeftTaskLenghth = len(PuzzleOn[1]);

TaskAnswer = [[],[]]
for i in range(TopTaskLenghth):
    TaskAnswer[0].append([])
for i in range(LeftTaskLenghth):
    TaskAnswer[1].append([])

def CheckAnswer():
    for i in range(TopTaskLenghth):
        key = 0
        for j in range(LeftTaskLenghth):
            if Answer[j][i][0] == 1:
                key += 1
                if j == LeftTaskLenghth -1:
                    TaskAnswer[0][i].append(key)
            else:
                if key != 0:
                    TaskAnswer[0][i].append(key)
                    key = 0
                elif j == TopTaskLenghth -1:
                    if TaskAnswer[0][i] == []:
                        TaskAnswer[0][i].append(0)

    for i in range(LeftTaskLenghth):
        key = 0
        for j in range(TopTaskLenghth):
            if Answer[i][j][0] == 1:
                key += 1
                if j == TopTaskLenghth -1:
                    TaskAnswer[1][i].append(key)
            else:
                if key != 0:
                    TaskAnswer[1][i].append(key)
                    key = 0
                elif j == TopTaskLenghth -1:
                    if TaskAnswer[1][i] == []:
                        TaskAnswer[1][i].append(0)

    if TaskAnswer == PuzzleOn:
        return True
    else:
        TaskAnswer[:] = [[],[]]
        for i in range(TopTaskLenghth):
            TaskAnswer[0].append([])
        for i in range(LeftTaskLenghth):
            TaskAnswer[1].append([])
        return False

Answer = []
for i in range(LeftTaskLenghth):
    Answer.append([])
    for j in range(TopTaskLenghth):
        Answer[i].append([0,0])


#checking cells that we 100% know - column
possibility = 1
for i in range(TopTaskLenghth):
    FillNumber = -1 + len(PuzzleOn[0][i]) + sum(PuzzleOn[0][i])

    #if it is fully filled
    if FillNumber == LeftTaskLenghth:
        Count = 0
        for j in range(len(PuzzleOn[0][i])):
            for k in range(PuzzleOn[0][i][j]):
                Answer[Count][i] = [1, 1]
                Count += 1
            if Count != LeftTaskLenghth:
                Answer[Count][i] = [0, 1]
            Count += 1

    #if it is 0
    elif PuzzleOn[0][i] == [0]:
        for j in range(TopTaskLenghth):
            Answer[j][i] = [0,1]
    
    #count how many possibilities
    # else :
    #     possibility *= math.comb(LeftTaskLenghth-sum(PuzzleOn[0][i])+len(PuzzleOn[0][i]),len(PuzzleOn[0][i])) 
        


#checking cells that we 100% know - row
for i in range(LeftTaskLenghth):
    FillNumber = -1 + len(PuzzleOn[1][i]) + sum(PuzzleOn[1][i])

    if FillNumber == LeftTaskLenghth:
        Count = 0
        for j in range(len(PuzzleOn[1][i])):
            for k in range(PuzzleOn[1][i][j]):
                Answer[i][Count] = [1, 1]
                Count += 1
            if Count != TopTaskLenghth:
                Answer[i][Count] = [0, 1]
            Count += 1

    if PuzzleOn[1][i] == [0] :
        for j in range(TopTaskLenghth):
            Answer[i][j] = [0,1]

#checking all the possible case and find the answer
NumberOfUnknown = 0

for i in range(LeftTaskLenghth):
    for j in range(TopTaskLenghth):
        if Answer[i][j][1]==0:
            NumberOfUnknown += 1
print(NumberOfUnknown)
lst = list(itertools.product([0, 1], repeat=NumberOfUnknown))

for k in range(len(lst)):
    Counting = 0
    for i in range(LeftTaskLenghth):
        for j in range(TopTaskLenghth):
            if Answer[i][j][1]==0:
                Answer[i][j][0]=lst[k][Counting]
                Counting += 1
    if CheckAnswer():
        break

#Convert into diagram
AnswerShow = []
for i in range(LeftTaskLenghth):
    AnswerShow.append([])
    for j in range(TopTaskLenghth):
        if Answer[i][j][0] == 1:
            AnswerShow[i].append("⬛")
        elif  Answer[i][j][0] == 0:
            AnswerShow[i].append("⬜")

for i in AnswerShow:
    print("".join(i))