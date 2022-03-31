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

    def search_recursive(self, list, low, high, item):  # low high 参数超出报错
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

# 杨辉三角的规律：
# 1、第n行有n个数字
# 2、每行的前后，都是“1”
# 3、第n行的第L[i]的值，等于第n-1行第L[i]+L[i+1]的值
def triangles():
    L = [1]              #定义L为一个只包含一个元素的列表
    while True:
        yield L          #定义为生成器函数
        L =[1] + [L[n] + L[n-1] for n in range(1, len(L))] + [1]
def print_triangle():
    n = 0
    for t in triangles():
        print(t)
        n = n + 1
        if n == 5:
            break


# 吃1到2个豆子，台阶问题
def eat(n):
    if n < 5:
        return n
    f = [0] * (n + 1)
    for i in range(5):
        f[i] = i
    for i in range(5, n + 1):
        f[i] = f[i - 1] + f[i - 3]
    # print(f)
    return f[-1]


# 动态规划
def backpack():
    w = [1, 2, 3, 4]
    v = [1, 1, 2, 3]
    dp = [[0 for i in range(len(v))] for j in w]




from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)




# class definition
class Bar(object):
  def __init__(self, a):
    self.a = a

class BarSlotted(object):
    __slots__ = "a",
    def __init__(self, a):
        self.a = a

# __slots__当你事先知道class的attributes的时候，建议使用slots来节省memory以及获得更快的attribute access
bar = Bar(1)
bar_slotted = BarSlotted(1)


class Animal:

    def __init__(self, color="白色"):
        Animal.color = color

    def get_color(self):
        print("Animal的颜色为", Animal.color)


class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        pass


# cat = Cat()
# cat.get_color()


lis = ['apple','lemon','pear','peach']

def fn(x):
    return x[::-1]
# lis.sort(key=fn)    # ['apple', 'peach', 'lemon', 'pear'] ehrn
lis.sort(key=fn, reverse=True)
# print(lis)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # 当前指针，结果链表
        result = curr = ListNode()
        # 进位项
        remainder = 0

        # 非空满足循环条件
        while l1 or l2 :
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + remainder

            curr.next = ListNode(total%10)
            remainder = total//10

            # 🚩防止某一链表已经为空，空链表.next会报错
            if l1 : l1 = l1.next
            if l2 : l2 = l2.next
            curr = curr.next

        if remainder: curr.next = ListNode(remainder)
        return result.next


#最大利润
def maxProfit(prices):
    cost, profit = float('+inf'), 0
    for price in prices:
        cost = min(cost, price)
        profit = max(profit, price - cost)

    return profit


if __name__ == "__main__":
    # We must initialize the class to use the methods of this class
    # my_list = [1, 3, 5, 7, 9, 10, 11, 13]
    bs = BinarySearch()
    # print(bs.search_iterative(my_list, 3))  # => 1
    #
    # # 'None' means nil in Python. We use to indicate that the item wasn't found.
    # print(bs.search_iterative(my_list, -1))  # => None
    # print(bs.search_recursive(my_list, 0, 19, 13))

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

    # print_triangle()


    import asyncio


    def bottom():
        """返回yield表达式来允许值通过调用栈进行传递"""
        return (yield 42)


    def middle():
        return (yield from bottom())


    def top():
        return (yield from middle())

    # gen = middle()
    # value = next(gen)
    # print(value)  # Prints '42'
    #
    # try:
    #     value = gen.send(value * 2)
    # except StopIteration as exc:
    #     print("Error!")  # Prints 'Error!'
    #     value = exc.value
    # print(value)
    #
    # class Person:
    #     def __init__(self):
    #         pass
    #
    #     def getAge(self):
    #         print(__name__)
    # p = Person()
    # p.getAge()
    def twoSum(nums, target):
        hashmap = {}
        for i,num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return (i, hashmap.get(target - num))
            hashmap[num] = i


    def isPrime(n):
        # Write your code here
        if n < 3:
            return 1
        for i in range(2, n):
            if n % i == 0:
                return i
        return 1


    # def selectStock(saving, currentValue, futureValue):
    #     # Write your code here
    #     same_stock = list(zip(currentValue, futureValue))
    #     profit_list = list(map(lambda x, y: y - x, same_stock))
    #     current_profit = zip(currentValue, profit_list)
    #     max_profit = sorted(current_profit, key=lambda x: x[1], reverse=True)
    #     print(max_profit)
    #
    #
    # selectStock(1, [1,2,3], [2,3,5])

    print(maxProfit([2,3,5,1]))


    class Resource():
        def __enter__(self):
            print('===connect to resource===')
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            print('===close resource connection===')

        def operate(self):
            print('===in operation===')

    import socket
    import socketserver





