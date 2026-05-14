'''
Author: mazezen
Date: 2026-05-14
LastEditors: mazezen
LastEditTime: 2026-05-14
FilePath: /ailearning/0-Pre/opencv/1-quick-guide-to-python/truck.py
Description: 
'''

from Vehicle import Vehicle

class Truck(Vehicle):

    def __init__(self, year, model, plate_number, current_speed, current_cargo) -> None:
        super().__init__(year, model, plate_number, current_speed)
        self.current_cargo = current_cargo

    def add_cargo(self, cargo):
        self.current_cargo += cargo
    
    def remove_cargo(self, cargo):
        self.current_cargo -= cargo
