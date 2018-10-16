#-*- coding: utf-8 -*-

'''
1-1. 시간복잡도 O(n^2)이 소요되는 정렬 중 하나와 병합 정렬을 각각 구현한다. 분석에 의한 성능 차이를 실제 실험을 통해 확인한다.

 - 제출 내용: 1. 본인 코드 설명, 2. 두 정렬의 동일한 입력과 출력 화면, 3. 두 정렬의 소요 시간 비교 화면, 4. 소스 코드 파일

1-2. 퀵 정렬을 구현한다. 기준(pivot)은 어떤 것이든 상관 없으나 재귀적으로 동일한 기준이어야한다.

 - 제출 내용: 1. 본인 코드 설명, 2. 입력, 출력, 소요 시간 화면, 3. 선택한 기준 값을 정한 이유 , 4. 소스 코드 파일
'''

import time
import random

#MergeSort 구현 부분
def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]

            else:
                result.append(right[0])
                right = right[1:]

        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]

        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

def merge_sort(list):
    if len(list) <= 1:
        return list

    mid = int(len(list) / 2)

    leftList = list[:mid]
    rightList = list[mid:]

    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)

    return merge(leftList, rightList)


#Bubble Sort 구현 부분
def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def bubble_sort(x):
    for size in reversed(range(len(x))):
        for i in range(size):
            if x[i] > x[i+1]:
                swap(x, i, i+1)
    return x


#원활한 실험을 위한 Random Sized Array를 형성하는 함수
def create_array(arr_size):
    arr = []
    for i in range(arr_size):
        num = random.randint(-100,200)
        arr.append(num)
    return arr

#크기 5,000의 random array로 구성된 배열(리스트)
test_list = create_array(5000)

'''실험부분'''
#MergeSort로 Array를 병합정렬
merge_start = time.time() 
merge_result = merge_sort(test_list)
merge_end = time.time()

#BubbleSort로 Array를 버블정렬
bubble_start = time.time()
bubble_result = bubble_sort(test_list)
bubble_end = time.time()

#각 정렬방법의 소요시간 계산
merge_time = merge_end - merge_start #MergeSort 소요시간
bubble_time = bubble_end - bubble_start #BubbleSort 소요시간

print(merge_time) #0.06996011734008789, int형으로 약 0s에 근사
print(bubble_time) #2.838104486465454, int형으로 약 2s에 근사