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
def person_is_seller(name):
    return name[-1] == 'm'

from collections import deque
def search(name):
    search_queue = deque()

if __name__ == "__main__":
    # We must initialize the class to use the methods of this class
    # my_list = [1, 3, 5, 7, 9, 10, 11, 13]
    # bs = BinarySearch()
    # print(bs.search_iterative(my_list, 3))  # => 1
    #
    # # 'None' means nil in Python. We use to indicate that the item wasn't found.
    # print(bs.search_iterative(my_list, -1))  # => None
    # print(bs.search_recursive(my_list, 0, 4, 3))

    my_list = [7, 6, 9, 10, 11, 13, 1, 3, 3, 5, 4]
    # print(findSmallest(my_list))
    # my_list = selectSort(my_list)
    # print(quicksort(my_list))







