import shape_calculator
from unittest import main

rect = shape_calculator.Rectangle(10, 5)
print('Rectangle Area :', rect.get_area())
rect.set_height(3)
print('Rectangle Perimeter :', rect.get_perimeter())
print(rect)
print('Picture:\n'+ rect.get_picture())

sq = shape_calculator.Square(9)
print('Square area: ', sq.get_area())
sq.set_side(4)
print('Square diagonal: ', sq.get_diagonal())
print(sq)
print('Picture:\n' + sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))


# Run unit tests automatically
main(module='test_module', exit=False)