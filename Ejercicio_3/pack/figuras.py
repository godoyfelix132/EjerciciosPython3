class Figure:
    _color = 'default'
    _area = 'default'
    _perimeter = 'default'

    def __init__(self, color='default'):
        self._color = color

    def __str__(self):
        return 'Figure(color=' + self._color + ' area=' + str(self._area) + ' perimeter=' + str(self._perimeter) + ')'

    def get_type(self):
        return 'Figure'

    def get_color(self):
        return self._color

    def get_area(self):
        return self._area

    def get_perimeter(self):
        return self._perimeter

    def set_area(self, area):
        self._area = area

    def set_perimeter(self, perimeter):
        self._perimeter = perimeter

    def set_color(self, color):
        self._color = color


class Rectangle(Figure):
    __high = 'default'
    __width = 'default'

    def __init__(self, color='default', high='default', width='default'):
        Figure.__init__(self, color)
        self.__high = high
        self.__width = width

    def __str__(self):
        return 'Figure(color=' + self._color + ' area=' + str(self._area) + ' perimeter=' + str(self._perimeter) + \
               ' high=' + str(self.__high) + ' width=' + str(self.__high) + ')'

    def get_type(self):
        return 'Rectangle'

    def get_high(self):
        return self.__high

    def get_width(self):
        return self.__width

    def set_high(self, high):
        self.__high = high

    def set_width(self, width):
        self.__width = width


class Triangle(Figure):
    __side1 = 'default'
    __side2 = 'default'
    __side3 = 'default'

    def __init__(self, color='default', side1='default', side2='default', side3='default'):
        Figure.__init__(self, color)
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def __str__(self):
        return 'Figure(color=' + self._color + ' area=' + str(self._area) + ' perimeter=' + str(self._perimeter) + \
               ' side1=' + str(self.__side1) + ' side2=' + str(self.__side2) + ' side3=' + str(self.__side3) + ')'

    def get_type(self):
        return 'Triangle'

    def get_side1(self):
        return self.__side1

    def get_side2(self):
        return self.__side2

    def get_side3(self):
        return self.__side3

    def set_side1(self, side1):
        self.__side1 = side1

    def set_side2(self, side2):
        self.__side2 = side2

    def set_side3(self, side3):
        self.__side3 = side3
