import codesters
from codesters import StageClass
stage = StageClass()

q1 = codesters.Square(100,100,200,'gray')
q2 = codesters.Square(-100,100,200,'black')
q3 = codesters.TriangleRight(-100,-100,-200,-200,'purple')
q4 = codesters.TriangleRight(100,-100,200,-200,'green')
q5 = codesters.Circle(0,0,110,'gold')
q6 = codesters.Circle(0,0,100,'red')


s1 = codesters.Sprite ("PineTree",100,100)
s1.set_size(0.15)
s2 = codesters.Sprite ("cardinal",-75,-50)
s2.set_size(0.25)
s3 = codesters.Sprite ("baseball",75,-50)
s4 = codesters.Sprite ("download (1)",-100,100)
s4.set_size(0.5)
s5 = codesters.Sprite ("Snowflake2",0,0)
s5.set_size (0.09)

stage.set_background("winter")

message1 = codesters.Text("Canon Winkelhake",0,220,"red")
message2 = codesters.Text("Can't right wright",0,-220,"black")