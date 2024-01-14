import pygame

pygame.font.init()

white = (255,255,255)
CorrectGreen = (51, 255, 51)
WrongRed = (220, 20, 40)
CellSize = 30
ScreenWidth = 500
ScreanHeight = 500
font = pygame.font.SysFont('Comic Sans Ms', CellSize-5)
FinalFont = pygame.font.SysFont('Comic Sans Ms', int(max(ScreenWidth,ScreanHeight)/10))

Puzzel_practice = [[[1],[0],[0],[0],[0]],[[1],[0],[0],[0],[0]],"Puzzel_practice"]
Answer_practice = [[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

Puzzel_1 = [[[3],[3],[1,1],[2],[1,2]],[[1],[3,1],[2],[4],[2]],"Puzzel_1"]
Answer_1 = [[1,0,0,0,0],[1,1,1,0,1],[1,1,0,0,0],[0,1,1,1,1],[0,0,0,1,1]]

PuzzelOn = Puzzel_1
AnswerOn = Answer_1

TopTaskLenghth = len(PuzzelOn[0])
LeftTaskLenghth = len(PuzzelOn[1])
TopMaxNumberTasks = max(len(PuzzelOn[0][x]) for x in range(TopTaskLenghth))
LeftMaxNumberTasks = max(len(PuzzelOn[1][x]) for x in range(TopTaskLenghth))

AnswerFile = []
for i in range(LeftTaskLenghth):
    AnswerFile.append([])
    for n in range(TopTaskLenghth):
        AnswerFile[i].append(0)

AnswerX = ScreenWidth/2-(TopTaskLenghth+LeftMaxNumberTasks)*CellSize/2 + CellSize*LeftMaxNumberTasks
AnswerY = ScreanHeight/2-(LeftTaskLenghth+TopMaxNumberTasks)*CellSize/2 + CellSize*TopMaxNumberTasks -30

screen = pygame.display.set_mode([ScreenWidth,ScreanHeight])

running = True

for row in range(TopTaskLenghth):
    for column in range(LeftTaskLenghth):
            pygame.draw.rect(screen, white, (AnswerX + CellSize*row, AnswerY + CellSize*column, CellSize, CellSize), 1)
            
for i in range(TopTaskLenghth):
    pygame.draw.line(screen, white, (AnswerX + CellSize*i, AnswerY - TopMaxNumberTasks*CellSize ), 
                                    (AnswerX + CellSize*i, AnswerY))
    for j in range(len(PuzzelOn[0][i])):
        screen.blit(font.render(" " + str(PuzzelOn[0][i][-j-1]), False, white), (AnswerX + CellSize*i + 2, AnswerY - CellSize*(j+1)))

            
for i in range(LeftTaskLenghth):
    pygame.draw.line(screen, white, (AnswerX - TopMaxNumberTasks*CellSize, AnswerY + CellSize*i), 
                                        (AnswerX , AnswerY + CellSize*i) )
    for j in range(len(PuzzelOn[1][i])):
        screen.blit(font.render(" " + str(PuzzelOn[1][i][-j-1]), False, white), (AnswerX - CellSize*(j+1), AnswerY + CellSize*i ))

pygame.draw.rect(screen, white, pygame.Rect(ScreenWidth/2 - 2.5*CellSize, 
                                            ScreanHeight/2 - 0.5*CellSize + (LeftTaskLenghth+TopMaxNumberTasks)*CellSize/2,
                                            5*CellSize, CellSize)) 
screen.blit(font.render(' submit', False, (0,0,0)), (ScreenWidth/2 - 1.5*CellSize,
                                                    ScreanHeight/2 - 0.5*CellSize + (LeftTaskLenghth+TopMaxNumberTasks)*CellSize/2))

screen.blit(font.render(PuzzelOn[2], False, white), (ScreenWidth/2 - 1.5*CellSize,
                                                    ScreanHeight/2 - 0.5*CellSize - (LeftTaskLenghth+TopMaxNumberTasks)*CellSize))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for i in range(LeftTaskLenghth):
                for j in range(TopTaskLenghth):
                    if pos[0] > AnswerX+ CellSize*i and pos[0] < AnswerX+ CellSize*i + CellSize:
                        if pos[1] > AnswerY+CellSize*j and pos[1] < AnswerY+CellSize*j + CellSize: 
                            if event.button == 1:
                                if AnswerFile[j][i] == 1:
                                    AnswerFile[j][i] = 0
                                    pygame.draw.rect(screen, (0,0,0), pygame.Rect(AnswerX+ CellSize*i+1, AnswerY+CellSize*j+1 ,CellSize-2,CellSize-2)) 
                                else:    
                                    AnswerFile[j][i] = 1
                                    pygame.draw.rect(screen, white, pygame.Rect(AnswerX+ CellSize*i, AnswerY+CellSize*j ,CellSize,CellSize))
                            elif event.button == 3:
                                AnswerFile[j][i] = 0
                                pygame.draw.rect(screen, (0,0,0), pygame.Rect(AnswerX+ CellSize*i+1, AnswerY+CellSize*j+1 ,CellSize-2,CellSize-2)) 
                                screen.blit(font.render(' X', False, white), (AnswerX+ CellSize*i, AnswerY+CellSize*j))
                        pygame.draw.rect(screen, white, pygame.Rect(ScreenWidth/2 - 2.5*CellSize, 
                                            ScreanHeight/2 - 0.5*CellSize + (LeftTaskLenghth+TopMaxNumberTasks)*CellSize/2,
                                            5*CellSize, CellSize)) 
                        screen.blit(font.render(' submit', False, (0,0,0)), (ScreenWidth/2 - 1.5*CellSize,
                                                    ScreanHeight/2 - 0.5*CellSize + (LeftTaskLenghth+TopMaxNumberTasks)*CellSize/2))

            
            if pos[0] > ScreenWidth/2 - 2.5*CellSize and pos[0] < ScreenWidth/2 + 2.5*CellSize:
                if pos[1] > ScreanHeight/2 - 0.5*CellSize + (LeftTaskLenghth+TopMaxNumberTasks)*CellSize/2 and\
                      pos[1] < ScreanHeight/2 - 0.5*CellSize + (LeftTaskLenghth+TopMaxNumberTasks)*CellSize/2 + CellSize:
                    if AnswerFile == AnswerOn:
                        pygame.draw.rect(screen, CorrectGreen, pygame.Rect(0, 0 ,ScreenWidth, ScreanHeight)) 
                        screen.blit(FinalFont.render('GOOD JOB!!', False, white), (ScreenWidth/2-130, ScreanHeight/2-30))
                    else:
                        pygame.draw.rect(screen, WrongRed, pygame.Rect(ScreenWidth/2 - 2.5*CellSize, 
                                            ScreanHeight/2 - 0.5*CellSize + (LeftTaskLenghth+TopMaxNumberTasks)*CellSize/2,
                                            5*CellSize, CellSize)) 
                        screen.blit(font.render('  wrong', False, (0,0,0)), (ScreenWidth/2 - 1.5*CellSize,
                                                    ScreanHeight/2 - 0.5*CellSize + (LeftTaskLenghth+TopMaxNumberTasks)*CellSize/2))
                        
    pygame.display.flip()
pygame.quit()
