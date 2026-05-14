'''
Author: mazezen
Date: 2026-05-14
LastEditors: mazezen
LastEditTime: 2026-05-14
FilePath: /ailearning/0-Pre/opencv/1-quick-guide-to-python/Vehicle.py
Description: 
'''

class Vehicle:
    def __init__(self, year, model, plate_number, current_speed) -> None:
        self.year = year
        self.model = model
        self.plate_number = plate_number
        self.current_speed = current_speed

    def move(self):
        self.current_speed += 1
    
    def accelerate(self, value):
        self.current_speed += value
    
    def vehicle_details(self):
        return self.model + ', ' + str(self.year) + ', ' + self.plate_number
    

