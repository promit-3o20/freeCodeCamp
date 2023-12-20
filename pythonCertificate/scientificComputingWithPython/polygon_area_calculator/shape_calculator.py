class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
       
    def set_width(self, new_width):
        self.width = new_width
        
    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        dia = (self.width ** 2 + self.height ** 2) ** .5
        return dia

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        pic = '* ' * self.width + '\n'
        pic = pic * self.height
        return pic
    
    def get_amount_inside(self, ob):
        return self.get_area() // ob.get_area()


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f'Square(side={self.width})'
    
    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side

        