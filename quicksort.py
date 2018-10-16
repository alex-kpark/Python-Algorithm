#-*- coding: utf-8 -*-
import time
import random

def quick_sorted(arr):
    if len(arr) > 1:
        pivot = arr[len(arr)-1] #최악의 경우를 상정하기 위해, Pivot 오른쪽에 하나의 값을 갖도록 pivot 위치를 설정했음
        left, mid, right = [], [], []
        for i in range(len(arr)-1):
            if arr[i] < pivot:
                left.append(arr[i])
            elif arr[i] > pivot:
                right.append(arr[i])
            else:
                mid.append(arr[i])
        mid.append(pivot)
        return quick_sorted(left) + mid + quick_sorted(right)
    else:
        return arr
        
#원활한 실험을 위한 Random Sized Array를 형성하는 함수
def create_array(arr_size):
    arr = []
    for i in range(arr_size):
        num = random.randint(-100,200)
        arr.append(num)
    return arr
    
#크기 5,000짜리의 List 생성
test_list = create_array(5000)    

#quick_sorted로 Array를 퀵정렬
quick_start = time.time()
quick_result = quick_sorted(test_list)
quick_end = time.time()

#각 정렬방법의 소요시간 계산
quick_time = quick_end - quick_start #퀵소트 소요시간
print(quick_time)