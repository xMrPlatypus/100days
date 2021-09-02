if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    a = max(arr)
    lower = []
    for i in arr:
        if a > i:
            lower.append(i)
    
    print(max(lower))
