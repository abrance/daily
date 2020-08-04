# 归并排序

def merge_sort(ls, l, m, r):
    if r-l == 1:
        if ls[r] < ls[l]:
            t = ls[l]
            ls[l] = ls[r]
            ls[r] = t
        return
    b = []
    # 两边的已经排序好，需要把l, m 的和 m+1, r 的合并
    j, k = l, m+1
    i = l
    while j <= m and k <= r:
        if ls[j] <= ls[k]:
            b.append(ls[j])
            j += 1
        else:
            b.append(ls[k])
            k += 1
        if j == m+1:
            b += ls[k:]
            break
        elif k == r+1:
            b += ls[j:m+1]
            break
    if len(ls) > r+1:
        ls = b+ls[r+1:]

def merge(ls, l, r):
    if l == r:
        return
    m = (l+r)//2
    merge(ls, l, m)
    merge(ls, m+1, r)
    merge_sort(ls, l, m, r)


def main():
    ls = [1, 22, 13, 4, 5]
    merge(ls, 0, 4)
    print(ls)


if __name__ == '__main__':
    main()
