#-*- coding: utf-8 -*-

import time
import random

'''MergeSort 구현 부분'''

# 두 리스트를 합치는 함수 구현
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

# Mergesort 부분
def merge_sort(list):

    # 정렬할 데이터의 크기가 1보다 작거나 같으면 그대로 return (정렬할 것이 없음)
    if len(list) <= 1:
        return list

    # 중간에 정렬할 middle 값을 설정하고, 나누어떨어지지 않는 경우 int형으로 처리
    mid = int(len(list) / 2)

    # middle 값을 기준으로 작은 값, 큰 값을 분리
    leftList = list[:mid]
    rightList = list[mid:]

    # 재귀적으로 전반부, 후반부를 정렬
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)

    # 정렬한 이후 merging 해주면서 결과값을 return
    return merge(leftList, rightList)


'''Bubble Sort 구현 부분'''

# 인접한 두 자료들의 위치를 바꾸어주는 swap 함수
def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def bubble_sort(x):
    # 데이터의 크기에 따라서 반복해줌
    for size in reversed(range(len(x))):
        for i in range(size):
            # 크기가 더 크면 swap함수를 통해 더 큰 것을 뒤로 보내줌
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