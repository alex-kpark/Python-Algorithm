#-*- coding: utf-8 -*-
import time
import random

#http://ejklike.github.io/2017/03/04/sorting-algorithms-with-python.html

def swap(x,i,j):
    x[i], x[j] = x[j], x[i]
    #x : input array

def selectionSort(x):
    for size in reversed(range(len(x))): #range 잡으면 하나 빠짐
        max_i = 0
        for i in range(1, 1+size):
            if x[i] > x[max_i]:
                max_i = i #가장 큰 값으로 지정해줌
        swap(x, max_i, size) #가장 마지막의 값과 교체해줌
    return x
    
def bubblesort(x):
    for size in reversed(range(len(x))): #전체 개수 중에서
        for i in range(size):
            if x[i] > x[i+1]: #size=1 이면 1번, size=2면 2번, size=3면 3번... 반복
                swap(x, i, i+1)
    return x

insert = [3,5,7,6,8,4,1]
print(selectionSort(insert))



