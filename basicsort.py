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

def insertsort(x):
    for size in range(1, len(x)):
        val = x[size] #현재 원소
        i = size #현재 번 째를 의미
        while i>0 and x[i-1]>val: #현재원소보다 마지막 원소가 커질 때 까지
            x[i] = x[i-1] #마지막 원소를 그 전의 원소로 변경
            i -= 1 # i는 하나 빼주면서 계속 다음 것으로 전진
        x[i] = val #마지막 원소를 현재 원소로 지정
    return x


insert = [3,5,7,6,8,4,1]
print(insertsort(insert))



