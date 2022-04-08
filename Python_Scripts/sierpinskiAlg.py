from graphics import *

def sierpinskiT(points,level,win):

	colormap = ['blue','red','green','white', 'yellow','violet','orange']
	p = Polygon(points)
	p.setFill(colormap[level % len(colormap)])
	p.draw(win)
	if level > 0:
		sierpinskiT([points[0], getMid(points[0], points[1]), getMid(points[2], points[0])], level - 1, win)
		sierpinskiT([points[1], getMid(points[1], points[0]), getMid(points[1], points[2])], level - 1, win)
		sierpinskiT([points[2], getMid(points[2], points[1]), getMid(points[2], points[0])], level - 1, win)
		pass

def getMid(pt1,pt2):
	return Point( (pt1.getX()+pt2.getX())/2.0, (pt1.getY()+pt2.getY())/2.0 )

if __name__ == "__main__":
	win = GraphWin("st",500,500)
	win.setCoords(20,-10,80,50)
	myPoints = [Point(25,0), Point(50,43.3), Point(75,0)]
	sierpinskiT(myPoints,6,win)
