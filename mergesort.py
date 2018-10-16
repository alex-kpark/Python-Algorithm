#-*- coding: utf-8 -*-

'''
1-1. 시간복잡도 O(n^2)이 소요되는 정렬 중 하나와 병합 정렬을 각각 구현한다. 분석에 의한 성능 차이를 실제 실험을 통해 확인한다.

 - 제출 내용: 1. 본인 코드 설명, 2. 두 정렬의 동일한 입력과 출력 화면, 3. 두 정렬의 소요 시간 비교 화면, 4. 소스 코드 파일

1-2. 퀵 정렬을 구현한다. 기준(pivot)은 어떤 것이든 상관 없으나 재귀적으로 동일한 기준이어야한다.

 - 제출 내용: 1. 본인 코드 설명, 2. 입력, 출력, 소요 시간 화면, 3. 선택한 기준 값을 정한 이유 , 4. 소스 코드 파일
'''

import time

#MergeSort
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

    mid = len(list) / 2

    leftList = list[:mid]
    rightList = list[mid:]

    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)

    return merge(leftList, rightList)


#Bubble Sort
def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def bubble_sort(x):
    for size in reversed(range(len(x))):
        for i in range(size):
            if x[i] > x[i+1]:
                swap(x, i, i+1)


'''Testing Code'''

list = [100, 12, 100, 1, 1, 12, 100, 1, 12, 100, 1, 1]
print(list)

merge_start = time.time() 
merge_result = merge_sort(list)
merge_end = time.time()

bubble_start = time.time()
bubble_result = bubble_sort(list)
bubble_end = time.time()

bubble_time = int(merge_end - merge_start)
print(merge_sort(list))
print(bubble_start)
print(bubble_end)
print('{:02d}:{:02d}:{:02d}'.format(bubble_time // 3600, (bubble_time % 3600 // 60), bubble_time % 60))