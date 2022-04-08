
from graphics import *


def main():

    top_left_x = 100
    top_left_y = 100
    width = 60
    height = 120
    # num_rows = int(input('Number of rows: '))  # reference: may be useful later
    #num_columns = int(input('Number of columns: '))

    window = GraphWin("On StandBi!", 796, 995)
    top_left_point = Point(100, 0)
    bottom_right_point = Point(160, 398  )
    
    enclosing_rectangle = Rectangle( top_left_point , bottom_right_point )
    enclosing_rectangle.setFill(color_rgb(216,9,126))
    enclosing_rectangle.draw(window)


    top_left_point = Point(100, 398)
    bottom_right_point = Point(160, 597 )
    
    enclosing_rectangle = Rectangle( top_left_point , bottom_right_point )
    enclosing_rectangle.setFill(color_rgb(140,87,156))
    enclosing_rectangle.draw(window)


    top_left_point = Point(100, 597 )
    bottom_right_point = Point(160, 995 )
    
    enclosing_rectangle = Rectangle( top_left_point , bottom_right_point )
    enclosing_rectangle.setFill(color_rgb(36,70,142))
    enclosing_rectangle.draw(window)

    window.getMouse()
    window.close()


if __name__ == "__main__":
   main()
