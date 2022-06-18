class Rectangle:
    #howdy
    height = 0
    width = 0

    def __init__(self,w,h):
        self.height = h
        self.width = w

    def set_height(self,h):
        self.height = h

    def set_width(self,w):
        self.width = w
    
    # Returns area
    def get_area(self):
        area = self.height * self.width
        return area

    # Returns perimeter
    def get_perimeter(self):
        perimeter = (2*self.height) + (2*self.width)
        return perimeter
    
    # Returns diagonal
    def get_diagonal(self):
        d = ((self.height ** 2) + (self.width ** 2)) ** .5
        return d
    
    # Returns 'Too big for picture.' if height/width > 50
    def get_picture(self):
        picture = ''
        wCounter = 0
        hCounter = 0

        if self.height > 50 or self.width > 50:
            picture = 'Too big for picture.'
        else:
            for x in range(self.height):
                for y in range(self.width):
                    picture += '*'
                    wCounter += 1

                picture += '\n'
                hCounter += 1
        return picture
    
    # def get_amount_inside(self):

class Square(Rectangle):
    def __init__(self, s):
        super().__init__(s, s)

    def set_side(self, s):
        self.set_height(s)
        self.set_width(s)
