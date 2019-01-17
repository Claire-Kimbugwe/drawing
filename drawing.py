import cs1graphics as cg

paper = cg.Canvas()
sun= cg.Circle()
paper.add(sun)

paper.setBackgroundColor('skyBlue')
paper.setWidth(800)
paper.setHeight(600)
paper.setTitle('My World')


sun.setFillColor('yellow')
sun.setRadius(50)
sun.moveTo(700, 100)

sunCenter = cg.Point(500, 100)



class Circle(cg.FillableShape):

    def __init__(self, radius=10, centerPt =None):
        self.radius= radius
        self.centerPt = centerPt


#instatiate 

sun2 = cg.Circle(50, sunCenter)
sun2.setFillColor('lightYellow')
paper.add(sun2)

facade = cg.Square(200, cg.Point(400, 350))
facade.setFillColor('white')
paper.add(facade)

chimney = cg.Rectangle(50, 70, cg.Point(450, 215))
chimney.setFillColor('red')
paper.add(chimney)

tree = cg.Polygon(cg.Point(150, 220),
cg.Point(120, 380),
cg.Point(180, 380))
tree.setFillColor('darkGreen')
paper.add(tree)


# add more sun rays arround the sun 
sunraySW = cg.Path(cg.Point(660, 140), cg.Point(635, 165))
sunraySW.setBorderColor('yellow')
sunraySW.setBorderWidth(6)
paper.add(sunraySW)

sunraySE = cg.Path(cg.Point(740, 140), cg.Point(765, 165))
sunraySE.setBorderColor('yellow')
sunraySE.setBorderWidth(6)
paper.add(sunraySE)

sunrayNE = cg.Path(cg.Point(740, 60), cg.Point(765, 35))
sunrayNE.setBorderColor('yellow')
sunrayNE.setBorderWidth(6)
paper.add(sunrayNE)

sunrayNW = cg.Path(cg.Point(660, 60), cg.Point(635, 35))
sunrayNW.setBorderColor('yellow')
sunrayNW.setBorderWidth(6)
paper.add(sunrayNW)