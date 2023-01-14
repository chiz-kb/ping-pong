from turtle import Turtle, update

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.pu()
        
        self.l_score=0
        self.r_score=0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(align='center',arg=f'{self.l_score}',font=('Courier',80,'normal'))
        self.goto(100,200)
        self.write(align='center',arg=f'{self.r_score}',font=('Courier',80,'normal'))
    def l_inc(self):
        self.l_score +=1
        self.update()
    def r_inc(self):
        self.r_score +=1
        self.update()
