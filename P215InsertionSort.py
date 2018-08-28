def insertion_sort(S):
    for i in range(1, len(S)):
        current = S[i]
        j = i

        while j > 0 and S[j - 1] > current:
            S[j] = S[j - 1]
            j -= 1

        S[j] = current

    return S

'''
插入排序
Time Complexity:
Best: O(n), Average: O(n^2), Worst: O(n^2)

Algo:
    for i from 1 to n-1 DO:
        Insert A[i] at its proper location

插入排序对少量元素的排序非常有效。
工作机制就像打牌一样，为了将牌插入到已排好序的牌中，需要将牌与手中的牌从右向左进行比较。
'''

if __name__ == '__main__':
    s = [3, 2, 1, 4, 5, 7, 6]
    print(insertion_sort(s))

