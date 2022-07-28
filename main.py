# -*- coding: utf-8 -*-
# 核心方法，随手脚本，都写在这里测试

# 第一章 算法简介

# 1.2 二分查找
def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low + high) // 2
        #print("测试 mid={},high={},low={}".format(mid, high, low) )
        guess = list[mid]
        if (guess == item):
            return mid
        if (guess > item):
            high = mid - 1
        else:
            low = mid + 1
    return None

# 第二章 选择排序

# 2.3 选择排序
def findSmallesetIndex(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if (arr[i] < smallest):
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        smallest = findSmallesetIndex(arr)
        sorted_arr.append(arr.pop(smallest))
    return sorted_arr

# 第四章 快速排序

# 4.1 分而治之
# 习题1 编写sum函数的代码
def sum41(num, arr):
    l = len(arr)
    if (l == 0):
        return num
    if (l == 1):
        return num + arr[0]
    arr.pop(0)
    return sum41(num+arr[0], arr)

class ListNode:
    def __init__(self, val, next_node):
        self.next = next_node
        self.val = val

# 习题2 计算列表包含的元素
def custom_count_len(list_root):
    if (list_root == None):
        return 0
    if (list_root.next == None):
        return 1
    return custom_count_len(list_root.next) + 1

    

if __name__ == '__main__':
    list_root = ListNode(1, None)
    tmp = list_root
    tmp.next = ListNode(3, None)
    tmp = tmp.next
    tmp.next = ListNode(2, None)
    tmp = tmp.next
    tmp.next = ListNode(4, None)
    tmp = tmp.next
    tmp.next = ListNode(5, None)
    print(str(custom_count_len(list_root)))
    #my_list = [1,33,7,93,5]
    #print(str(sum41(0, my_list))) # => 1
    #print(str(binary_search(my_list, 3))) # => 1
    #print(binary_search(my_list, -1)) # => None
    #print('测试python-Lucius')