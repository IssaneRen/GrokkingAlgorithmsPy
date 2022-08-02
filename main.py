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

# 习题3 找出列表中最大的元素
def find_max(val1, val2):
    if (not val1):
        return val2
    if (not val2):
        return val1
    return max(val1, val2)

def custom_count_max(list_root, cur_max):
    if (list_root == None):
        return cur_max
    if (list_root.next == None):
        return find_max(cur_max, list_root.val)
    return custom_count_max(list_root.next, find_max(cur_max, list_root.val))

    
# 4.2 快速排序
def quick_sort(array):
    if (len(array) <= 1):
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if (i <= pivot)]
        more = [i for i in array[1:] if (i > pivot)]
        return quick_sort(less) + [pivot] + quick_sort(more)


    #arr = [22,1,5,81,5,78,546,1,84,44]
    #print(str(quick_sort(arr)))
    #list_root = ListNode(1, None)
    #tmp = list_root
    #tmp.next = ListNode(3, None)
    #tmp = tmp.next
    #tmp.next = ListNode(12, None)
    #tmp = tmp.next
    #tmp.next = ListNode(4, None)
    #tmp = tmp.next
    #tmp.next = ListNode(5, None)
    #print(str(custom_count_max(list_root, None)))
    #my_list = [1,33,7,93,5]
    #print(str(sum41(0, my_list))) # => 1
    #print(str(binary_search(my_list, 3))) # => 1
    #print(binary_search(my_list, -1)) # => None
    #print('测试python-Lucius')

# 第七章 狄克斯特拉算法

# 7.1 构建示例DAG 有向无环图
def generate_dag():
    diagram = {}
    diagram["start"] = {}
    diagram["start"]["A"] = 6
    diagram["start"]["B"] = 2
    diagram["A"] = {}
    diagram["A"]["end"] = 1
    diagram["B"] = {}
    diagram["B"]["A"] = 3
    diagram["B"]["end"] = 5
    diagram["end"] = {}
    return diagram
    
# 7.5 狄克斯特拉算法 实现

def add_init_nodes(diagram, node, costs):
    for n in diagram[node].keys():
        costs[n] = diagram[node][n]
    for n in diagram.keys():
        if (n not in costs):
            costs[n] = float("inf")

def find_lowest_cost_node(costs, known_nodes):
    min_cost = float("inf")
    lowest_cost_node = None
    for node in costs.keys():
        if (node not in known_nodes and node in costs and costs[node] < min_cost):
            min_cost = costs[node]
            lowest_cost_node = node
    return lowest_cost_node, min_cost

def dijkstra_alg(diagram, start, end):
    # 1. 消耗时间
    costs = {}
    # 2. 父节点
    parents = {}
    parents["start"] = 0
    # 3. 已经遍历过的内容
    known_nodes = []
    add_init_nodes(diagram, start, costs)
    current_node, current_cost = find_lowest_cost_node(costs, known_nodes)
    while current_node != None:
        print("正在查找 " + current_node + " 节点...")
        known_nodes.append(current_node)
        for n in diagram[current_node].keys():
            if ((n in costs and (costs[n] > (current_cost + diagram[current_node][n]))) or n not in costs):
                costs[n] = current_cost + diagram[current_node][n]
                parents[n] = current_node
        current_node, current_cost = find_lowest_cost_node(costs, known_nodes)
    # 退出循环表示完全遍历完成，现在找到路径
    final_cost = float("inf")
    if (end in costs):
        final_cost = costs[end]
    return final_cost

def test_dijkstra():
    diagram = generate_dag()
    print(str(dijkstra_alg(diagram, "start", "end")))

if __name__ == '__main__':
    # 测试 7.5
    test_dijkstra()