#-*- coding: utf-8 -*-
import math

def euclidian_distance(rider, driver):
    x_distance = rider['rider_x'] - driver['x']
    y_distance = rider['rider_y'] - driver['y']
    euclidian = (x_distance**2 + y_distance**2) ** 0.5

def direction(driver):
    if driver['x']>0 and driver['y']>0:
        driver_location = 'N'

    if driver['x']>0 and driver['y']<0:
        driver_location = 'E'

    if driver['x']<0 and driver['y']>0:
        driver_location = 'W'

    if driver['x']<0 and driver['y']<0:
        driver_location = 'S'


sample_rider = {
        'rider_x' : 0,
        'rider_y' : 3
        }

sample_driver = {
            'x' : 1,
            'y' : 2,
            'number' : 0,
            'driver' : 'Alex'
            }

potential_drivers = [


                    ]

def find_shortest_eta():

    result_list = []

    if num_son = 0:
        latency = euclidian_distance(sample_rider, sample_driver)
        


    else:
        for i in range(0,num_son):
            find_shortest_eta()
            