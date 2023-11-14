class Rectangle:
    # Initalize the rectangle class with its width and height
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
    
    # Create a string representation of the Rectangle class which provides the width and the height of the rectangle.
    def __repr__(self) -> str:
        return f'Rectangle(width={self.width}, height={self.height})'

    # The set_width method updates the width of the rectangle to the new width specified by the user.
    def set_width(self, new_width: int) -> None:
        self.width = new_width

    # The set_height method updates the height of the rectangle to the new height specified by the user.
    def set_height(self, new_height: int) -> None:
        self.height = new_height

    # The get_area method returns the area of the rectangle which is obtained by multiplying the width by the height.
    def get_area(self):
        return self.height * self.width

    # The get_perimeter method returns the perimeter of the rectangle which is obtained by multiplying 2 by the sum of the width and the height. 
    def get_perimeter(self) -> int:
        return 2 * (self.width + self.height)

    # The get_diagonal method returns the length of the diagonal of the rectangle which is obtained by getting the square root of the sum of the squares of the width and the height.
    def get_diagonal(self) -> float:
        return (self.width**2 + self.height**2)**.5

    # The get_picture method returns a string-represented picture of the object if the width and the height are less than or equal to 50 units. If not, it returns 'Too big for picture.'
    def get_picture(self) -> str:
        if self.height <= 50 and self.width <= 50: 
            picture = []
            for i in range(self.height):
                picture.append('\n'.rjust(self.width + 1, '*'))
            return ''.join(picture)
            
        return 'Too big for picture.'

    # The get_amount_inside method returns the number of rectangles that can fit inside of another rectangle.
    def get_amount_inside(self, other_shape: Rectangle) -> int:
        return self.get_area() // other_shape.get_area()


class Square(Rectangle):
    # Initalize the square class with its side length. The superclass is initialized with both the width and height being equal.
    def __init__(self, side_length: int) -> None:
        super().__init__(side_length, side_length)

    # The set_side method updates the side length of the square to the new side length specified by the user. This is accomplished by employing the superclass's set_width and set_height methods.
    def set_side(self, new_side_length: int) -> None:
        super().set_height(new_side_length)
        super().set_width(new_side_length)

    # Create a string representation of the Square class which provides the length of the sides of the square.
    def __repr__(self) -> str:
        return f'Square(side={self.width})'
    # To maintain the same behavior as the Rectangle superclass, the set_height method is overridden to update both the height and width with the new value entered.
    def set_height(self, new_height: int) -> None:
        super().set_height(new_height)
        super().set_width(new_height)
    # To maintain the same behavior as the Rectangle superclass, the set_width method is overridden to update both the width and height with the new value entered. 
    def set_width(self, new_width: int) -> None:
        super().set_width(new_width)
        super().set_height(new_width)
