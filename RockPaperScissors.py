arr=['Rock','Paper','Scissor']
logic={"Rock":[0,-1,1],"Paper":[1,0,-1],"Scissor":[-1,1,0]}

import random
def computerMove():
    index=random.randint(0,2)
    return index
isPlaying=True
prompt="1 for Rock, 2 for Paper, 3 for Scissor,0 to exit and display final score"
point=0
comPoint=0
while isPlaying:
    print(prompt)

    try:
        humanMove=int(input("Enter your move: "))-1
        if humanMove==-1:
            isPlaying==False
            print("The final score is:",point)
            break
        corresponding = arr[humanMove]

    except ValueError or IndexError:
        print("Please enter valid value")

    comMove=computerMove()

    point=point + logic[corresponding][comMove]
    comPoint-=logic[corresponding][comMove]
    print("Human uses", corresponding)
    print("Computer uses",arr[comMove])
    print("Point:",point)
    print("Computer Point:",comPoint)
    print('|---------------------------------------------|')
    print('|----------------New Round--------------------|')
    print('|---------------------------------------------|')

    print('tahmeed')
    print('mahedi')
