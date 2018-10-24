def mergeSort(x):
    if len(x) > 1:
        mid = len(x)//2
        left_x, right_x = x[:mid], x[mid:]
        mergeSort(left_x)
        mergeSort(right_x)

        li, ri, i = 0, 0, 0
        # left값이 right값보다 더 크면 left 값을 return
        while li < len(left_x) and ri < len(right_x):
            if left_x[li] < right_x[ri]:
                x[i] = left_x[li]
                li += 1
            # right값이 left 값보다 더 크면 right 값을 더 뒤쪽에 return
            else:
                x[i] = right_x[ri]
                ri += 1
            i += 1
        x[i:] = left_x[li:] if li != len(left_x) else right_x[ri:]
        return x


insert = [3,5,7,6,8,4,1]
print(mergeSort(insert))