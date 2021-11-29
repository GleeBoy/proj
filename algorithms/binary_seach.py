class BinarySearch():

    def search_iterative(self, list, item):
        # low and high keep track of which part of the list you'll search in.
        low = 0
        high = len(list) - 1

        # While you haven't narrowed it down to one element ...
        while low <= high:
            # ... check the middle element
            mid = (low + high) // 2
            guess = list[mid]
            # Found the item.
            if guess == item:
                return mid
            # The guess was too high.
            if guess > item:
                high = mid - 1
            # The guess was too low.
            else:
                low = mid + 1

        # Item doesn't exist
        return None

    def search_recursive(self, list, low, high, item):
        # Check base case
        if high >= low:

            mid = (high + low) // 2
            guess = list[mid]

            # If element is present at the middle itself
            if guess == item:
                return mid

                # If element is smaller than mid, then it can only
            # be present in left subarray
            elif guess > item:
                return self.search_recursive(list, low, mid - 1, item)

                # Else the element can only be present in right subarray
            else:
                return self.search_recursive(list, mid + 1, high, item)

        else:
            # Element is not present in the array
            return None


# 选择排序， O(n*n)
def findSmallest(arr):
    smallest = arr[0]
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
    return smallest

def selectSort(arr):
    sort_arr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        sort_arr.append(smallest)
        arr.remove(smallest)
    print(sort_arr)
    return sort_arr


# 快速排序，分而治之, 平均O(n log2 n) 最糟O(n*n), 最快之一
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


# 合并排序
from typing import List
def merge(arr1: List[int], arr2: List[int]):
    result = []
    while arr1 and arr2:
        if arr1[0] < arr2[0]:
            result.append(arr1.pop(0))
        else:
            result.append(arr2.pop(0))
    if arr1:
        result += arr1
    if arr2:
        result += arr2
    return result

def merge_sort(arr:List[int]):
    """
    归并排序
    :param arr: 待排序的List
    :return: 排好序的List
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


# 广度优先搜索
graph = {}  # 数据
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def person_is_seller(name):
    return name[-1] == 'm'

from collections import deque
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()  # 取出第一个人
        if person not in searched:
            if person_is_seller(person):
                print(person + 'is a mange seller!')
                return True
            else:
                # 你需要按加入顺序检查搜索列表中的人，否则找到的就不是最短路径，因此搜索列表必须是队列。
                search_queue += graph[person]  # 把这个人朋友加入队列
                searched.append(person)
    return False


# 拓扑排序 把图排序成有序列表
# 树
class Node(object):
    """节点类"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    """树类"""
    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        if self.root.elem == -1:  # 如果树是空的，则对根节点赋值
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]  # 此结点的子树还没有齐。
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)  # 如果该结点存在右子树，将此结点丢弃。

    def front_digui(self, root):
        """利用递归实现树的先序遍历"""
        if root == None:
            return
        print(root.elem)
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)

    def middle_digui(self, root):
        """利用递归实现树的中序遍历"""
        if root == None:
            return
        self.middle_digui(root.lchild)
        print(root.elem)
        self.middle_digui(root.rchild)

    def later_digui(self, root):
        """利用递归实现树的后序遍历"""
        if root == None:
            return
        self.later_digui(root.lchild)
        self.later_digui(root.rchild)
        print(root.elem)


if __name__ == "__main__":
    # We must initialize the class to use the methods of this class
    # my_list = [1, 3, 5, 7, 9, 10, 11, 13]
    bs = BinarySearch()
    # print(bs.search_iterative(my_list, 3))  # => 1
    #
    # # 'None' means nil in Python. We use to indicate that the item wasn't found.
    # print(bs.search_iterative(my_list, -1))  # => None
    # print(bs.search_recursive(my_list, 0, 4, 3))

    my_list = [7, 6, 9, 10, 11, 13, 1, 3, 3, 5, 4]
    # print(findSmallest(my_list))
    # my_list = selectSort(my_list)
    # print(quicksort(my_list))

    # print(search('you'))

    # elems = range(10)  # 生成十个数据作为树节点
    # tree = Tree()  # 新建一个树对象
    # for elem in elems:
    #     tree.add(elem)
    # # print(tree.myQueue)
    # print('\n\n递归实现先序遍历:')
    # tree.front_digui(tree.root)
    # print('\n递归实现中序遍历:')
    # tree.middle_digui(tree.root)
    # print('\n递归实现后序遍历:')
    # tree.later_digui(tree.root)

    # def task():
    #     # begin = yield
    #     # print("begin", begin)
    #     yield 1
    #     for x in range(10):
    #         yield x
    #
    # f = task()
    # # f.send(None)
    # r = next(f)
    # print(r)
    # print(f.send(2))



