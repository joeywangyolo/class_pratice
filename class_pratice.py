#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 16:13:32 2022

@author: wangsiqiao
"""
#父類別
class Chair :
    #初始化
    name='椅子'
    def __init__(self, c : str):
        self.color = c
        
    def seat(self)->None:
        print(self.color, self.name,'的椅子很好坐', self.material,'很舒服')
        # return 'Hello'


#子類別
class Sofa(Chair):
    """c:顏色 m:材質"""
    name = '沙發'
    def __init__(self, c:str, m:str)->None:
        self.material = m
        super().__init__(c)
        
    def lie_down(self):
        print(self.color,'可以躺著')
    
    def seat(self) -> None:
        print('我覆寫了！')
        super().seat()
        
a_sofa = Sofa('黑色','皮革')

b_sofa = Sofa('紅色','金屬')

a_sofa.seat()
b_sofa.seat()
b_sofa.lie_down()

a_chair = Chair('紅色')

b_chair = Chair('綠色')


# print(a_chair.color)
# print(b_chair.color) 

# s=b_chair.seat()
# print(s)