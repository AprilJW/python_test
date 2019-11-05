# 调整单个节点：先选中一个节点i并记录索引（性质5），如果这个节点有左节点，并设左节点为最大索引，
# 判断右节点如果存在并且大于左节点的值，则更新max_index, max_index与i的值进行比较，如果
# max_index的值大，则交换并且i = max_index，如果没有发生交换，则进入下一次循环。
# 生成大顶堆：从低向上，从n//2个节点开始，到第1个节点，使用for循环遍历，每一次遍历都调用
# 调整单个节点
#
def single(i, n):
    pre = 2 ** i
    while pre <= n:
        max_index = pre
        if max:
            pass
