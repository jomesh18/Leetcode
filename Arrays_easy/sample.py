def median_in_stream(arr):
    arr.sort()
    n = len(arr)
    mid = n//2
    if n % 2 == 0:
        print((arr[mid] + arr[mid-1])//2)
        return
    print(arr[mid])
    
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
    median_in_stream(arr)
