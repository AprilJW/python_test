# 调整单个节点：1，先选中一个节点i并记录索引（性质5:索引依此为1，2，3等），如果这个节点有左节点，
# 并假设左节点索引为最大索引，判断右节点如果存在并且大于左节点的值，则更新max_index,
# 2，max_index与i的值进行比较，如果
# max_index对应的值大于索引i对应的值，则交换max_index与i索引对应的值，并且更新索引i，即i向下移动
# i = max_index, 因为i对应的值已经被跟新了，所以需要进入下一次循环，
# 3，如果没有发生交换，则推出循环。

# 生成大顶堆：1，在第0位添加哨兵位，下面循环中的编号正好与元素在列表中的索引对应
# 2，从低向上开始遍历，从n//2个节点开始（最后一个叶子节点的父节点开始遍历，
# 一共n个节点，最后一个节点的编号为n, 它的父节点的编号为n//2取整），到第1个节点，
# 使用for循环遍历，每一次遍历都调用调整单个节点的函数，循环结束，生成一个大顶堆
# 目前堆中的所有父节点都比两个子节点的数值大

# 排序
# 将大顶堆的堆顶，与大顶堆的最后一个叶子节点，即列表中的第1个元素，与列表中的最后一个元素交换
# 列表中的最后一个元素为最大值，这个值不要动，从索引n-1,到1，重新调整堆中的元素，不需要再构建
# 大顶堆了，直到剩下最后一个元素。

# 为什么不需要再构建大顶堆了呢？
# 因为第1次构建大顶堆，已经把倒数第2大的数，放在了第2层。直接调整就可以获得倒数第2大的数。

# origin = [30, 20, 80, 40, 50, 10, 60, 70, 90]
origin = [19, 5, 3, 23, 12, 1, 15, 10, 8]
origin_new = [0] + origin
n = len(origin)

import math
def print_tree(n, origin, unit_width=2):
    depth = math.ceil(math.log2(n + 1))
    width = 2**depth - 1
    index = 0

    for i in range(depth):
        # i=0 2**0 index=[0:1]  index[count+j, count+j+1]range(1)
        # i=1 2**1 index[1:2] index[2:3]  index[count+j, count+j+1] range(2)
        # i=2 2**2 index[3:4] [4:5] [5:6] [6:7]  count= 3=2 + 1 range(4)
        for j in range(2**i):
            elem = origin[index]
            # print('{:^{}}'.format(elem, width * unit_width), end=' '*unit_width)
            print('{:^{}}'.format(elem, width * unit_width), end='  ')
            index += 1  # 最多打印了多少次2^0 + 2^1 + 2^2 + 2^3 = 13
            if index + 1 > n:
                print()
                return
        width = width // 2
        print()


# n = 30
# print_tree(n, [x+1 for x in range(n)])
# print_tree(9, origin)
# print('*****************')


def adjust_heap(n, i, origin_new):
    while 2 * i <= n:  # 有左孩子才调整
        lchild = 2 * i
        max_index = lchild

        if lchild < n and origin_new[lchild] < origin_new[lchild + 1]:
            max_index = lchild + 1

        if origin_new[i] < origin_new[max_index]:
            origin_new[i], origin_new[max_index] = origin_new[max_index], origin_new[i]
            i = max_index
        else:
            return origin_new[1:]
    return origin_new[1:]

# print_tree(9, adjust_heap(9, 4, origin_new))


def max_heap(n, origin_new:list):
    start = n // 2
    for i in range(start, 0, -1):
        heap = adjust_heap(n, i, origin_new)
        # print(heap)
        # print_tree(n, heap)
        # print('*****************')
    return origin_new[1:]


max_heap(9, origin_new)


def sort(n, origin_new):
    print_tree(9, origin_new[1:])
    print('***********')
    while n > 1:
        origin_new[1], origin_new[n] = origin_new[n], origin_new[1]
        n -= 1
        print_tree(9, adjust_heap(n, 1, origin_new))
        print('****************')
    return origin_new[1:]


sort(9, origin_new)

# max_heap(9, origin)
# print(sort(9, origin))




