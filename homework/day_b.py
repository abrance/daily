# 归并排序

def merge_sort(ls, l, m, r):
    if r-l == 1:
        if ls[r] < ls[l]:
            t = ls[l]
            ls[l] = ls[r]
            ls[r] = t
        return
    # 赋值一份需要排序的部分给b
    b = []
    for item in ls[l: r+1]:
        b.append(item)

    # 两边的已经排序好，需要把l, m 的和 m+1, r 的合并
    j, k = l, m+1
    i = l

    # 修改ls中的值，指针在b上移动
    while j <= m and k <= r:
        if b[j-l] <= b[k-l]:
            ls[i] = b[j-l]
            j += 1
        else:
            ls[i] = b[k-l]
            k += 1
        i += 1
        
    while j<=m:
        ls[i] = b[j-l]
        j += 1
        i += 1
        
    while k<=r:
        ls[i] = b[k-l]
        k += 1
        i += 1

def merge(ls, l, r):
    if l == r:
        return
    m = (l+r)//2
    merge(ls, l, m)
    merge(ls, m+1, r)
    merge_sort(ls, l, m, r)


def main():
    ls = [1, 22, 13, 77, 10, 59, 4, 5]
    merge(ls, 0, 7)
    print(ls)


if __name__ == '__main__':
    main()
