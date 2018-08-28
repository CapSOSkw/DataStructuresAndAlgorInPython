def binary_search(data, target, low, high):
    if low > high:
        return False

    else:
        mid = (low + high) // 2
        if target == data.__getitem__(mid):
            return True

        elif target < data.__getitem__(mid):
            return binary_search(data, target, low, mid-1)

        else:
            return binary_search(data, target, mid+1, high)




if __name__ == '__main__':
    data = [1, 2, 3, 4, 10, 21, 23, 42, 123, 12, 643]
    target = 3

    res = binary_search(data, target, 0, len(data)-1)
    print(res)


'''
二分法搜索，O(logn)
'''