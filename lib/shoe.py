#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand="Nike", size=9):
        self.brand = brand
        self.size = size
        self.condition = "Used"
        
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            print('size must be an integer')
        self._size = size
        
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        if not isinstance(brand, str):
            raise ValueError('Brand must be a string')
        self._brand = brand
        
        
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = 'New'