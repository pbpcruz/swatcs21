"""""
Playing around with objects and the graphics library to draw a cute animal!

Pedro Cruz '25
October 20th, 2021
"""""

from graphics import *

def main():
    win = GraphWin("Pong, the Panda", 500, 500)
    win.setBackground("lightpink")
    win.setCoords(0, 0, 100, 100)

    # body
    ## black part
    body = Circle(Point(50,1), 45)
    body.setFill("black")
    body.draw(win)

    ## white part
    p1 = Point(30, 10)
    p2 = Point(70,-20)
    whiteDetail = Oval(p1,p2)
    whiteDetail.setFill("white")
    whiteDetail.setWidth(8)
    whiteDetail.draw(win)

    #ears
    ## left ear
    leftEar = Circle(Point(25,80),15)
    leftEar.setFill("black")
    leftEar.draw(win)

    ## right ear
    rightEar = leftEar.clone()
    rightEar.move(50,0)
    rightEar.draw(win)

    # head
    head = Circle(Point(50, 50), 35)
    head.setFill("white")
    head.setOutline("black")
    head.setWidth(8)
    head.draw(win)

    # black details around eyes
    ## left eye
    p1 = Point(41, 66)
    p2 = Point(30, 50)

    leftBlackDetail = Oval(p1,p2)
    leftBlackDetail.setFill("black")
    leftBlackDetail.draw(win)

    ## right eye
    rightBlackDetail = leftBlackDetail.clone()
    rightBlackDetail.move(29,0)
    rightBlackDetail.draw(win)

    # lips
    ## black parts
    lip1 = Circle(Point(45, 40), 5)
    lip1.setWidth(5)
    lip1.draw(win)

    lip2 = lip1.clone()
    lip2.move(10,0)
    lip2.draw(win)

    ## cut detail
    rec = Rectangle(Point(39,40.6), Point(61,50))
    rec.setFill("white")
    rec.setOutline("white")
    rec.draw(win)

    # nose
    nose = Polygon([Point(45,45), Point(50,40), Point(55,45)])
    nose.setFill("black")
    nose.draw(win)


    # eyes outline
    ## left eye
    outlineLeftEye = Circle(Point(35.6,60.1), 4.2)
    outlineLeftEye.setFill("white")
    outlineLeftEye.setOutline("black")
    outlineLeftEye.draw(win)

    ## right  eye
    outlineRightEye = outlineLeftEye.clone()
    outlineRightEye.move(28.8,0)
    outlineRightEye.draw(win)

    # eyes
    ## left eye
    leftEye = Circle(Point(36,60), 3)
    leftEye.setFill("black")
    leftEye.draw(win)

    gleamLeft1 = Circle(Point(35.3, 61.4), 0.6)
    gleamLeft1.setFill("white")
    gleamLeft1.draw(win)

    gleamLeft2 = Circle(Point(36.5, 60.5), 0.3)
    gleamLeft2.setFill("white")
    gleamLeft2.draw(win)

    ## right eye
    rightEye = leftEye.clone()
    rightEye.move(28,0)
    rightEye.draw(win)

    gleamRight1 = gleamLeft1.clone()
    gleamRight1.move(30,0)
    gleamRight1.draw(win)

    gleamRight2 = gleamLeft2.clone()
    gleamRight2.move(27.3,0)
    gleamRight2.draw(win)

    win.getMouse()
    win.close()

main()
