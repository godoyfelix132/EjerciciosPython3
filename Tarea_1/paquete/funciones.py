def sort_list(list_sort):
    for j in range(len(list_sort)-1,0,-1):
        for i in range(j):
            if list_sort[i]>list_sort[i+1]:
                temp = list_sort[i]
                list_sort[i] = list_sort[i+1]
                list_sort[i+1] = temp
    return list_sort
