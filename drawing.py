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