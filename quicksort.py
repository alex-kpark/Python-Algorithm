#-*- coding: utf-8 -*-
import time
import random

'''QuickSort 구현 부분'''

def quick_sorted(arr):
    if len(arr) > 1:
        #성능이 좋지 않은 경우를 상정해서 최악의 리소스 운용을 가정하기 위해, Pivot 오른쪽에 하나의 값만을 갖도록(끝에 Pivot이 할당되게) pivot 위치를 설정했음
        #성능을 높히기 위해서는 pivot의 위치를 무작위로 결정할 수 있도록 해주는 것이 좋다
        pivot = arr[len(arr)-1] #pivot 설정
        left, mid, right = [], [], []
        for i in range(len(arr)-1):
            
            #pivot보다 작은 값 append
            if arr[i] < pivot:
                left.append(arr[i])
            
            #pivot보다 큰 값 append
            elif arr[i] > pivot:
                right.append(arr[i])
            
            #위 2가지 조건에 안들어가는 값 append
            else:
                mid.append(arr[i])
        mid.append(pivot) #빼놓았었던 pivot값 삽입

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

'''실험부분'''

#quick_sorted로 Array를 퀵정렬
quick_start = time.time()
quick_result = quick_sorted(test_list)
quick_end = time.time()

#각 정렬방법의 소요시간 계산
quick_time = quick_end - quick_start #퀵소트 소요시간
print(quick_time) #0.00999, int형으로 약 0에 근사