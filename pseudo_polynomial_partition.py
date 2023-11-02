import time

def pseudopolynomialPartition(arr):
    sum = 0
    n = len(arr)

    # Step #1: Calculate the sum of the entire values in arr
    for i in range(n):
        sum = sum + arr[i]

    # Step #2: See if the sum can be evenly divided by 2
    if sum % 2 != 0:
        return None
    
    halfSum = sum // 2
    
    # Step #3: Set up the dynamic programming table
    dpTable = [[True for i in range(n + 1)] for j in range(halfSum + 1)]

    for x in range(0, n + 1):
        dpTable[0][i] = True

    for y in range(1, halfSum + 1):
        dpTable[y][0] = False

    # Step #4: Figure out if there's a subset that has a sum equal to the row
    # Example: dpTable[1][4] --> Within the subset of {a0, a1, a2, a3}, does it have a sum that's 
    #                            equal to 1? If it's yes, then dpTable[1][4] equals True. Otherwise,
    #                            it'll equal to False.
    for i in range(1, halfSum + 1):
        for j in range(1, n + 1):
            dpTable[i][j] = dpTable[i][j - 1]
 
            if i >= arr[j - 1]:
                dpTable[i][j] = dpTable[i][j] or dpTable[i - arr[j - 1]][j - 1]

    # Below is printing out what the two set would look like when it's equally partitioned
    # subSum = halfSum
    # a = []
    # b = []
    # i = len(arr)
    # while i > 0:
    #     if dpTable[subSum][i - 1] == False:
    #         a.append(arr[i - 1])
    #         subSum = subSum - arr[i - 1]
    #     else:
    #         b.append(arr[i - 1])

    #     i = i - 1
        
    # print(a)
    # print(b)

    return dpTable[halfSum][n]

def main():
    # arr = [7, 5, 1, 33, 11, 55, 11, 1, 75, 34, 16, 42, 33, 32, 25, 10, 11, 46] --> n = 18
    # arr = [7, 5, 1, 33, 11, 9, 55, 11, 1, 52, 75, 25, 16, 42, 33, 32, 25, 10, 11, 46] --> n = 20
    # arr = [7, 5, 1, 33, 11, 9, 55, 9, 11, 1, 52, 45, 25, 16, 33, 33, 32, 25, 10, 11, 46, 30] --> n = 22
    # arr = [7, 5, 1, 33, 11, 8, 9, 55, 9, 11, 1, 52, 45, 15, 16, 33, 33, 24, 25, 10, 11, 46, 30, 20] --> n = 24
    arr = [7, 5, 1, 33, 11, 9, 36, 9, 21, 27, 11, 1, 19, 1, 52, 45, 25, 16, 33, 14, 32, 25, 10, 10, 25, 3, 19] # n= 27
    start = time.time_ns()
    ret = pseudopolynomialPartition(arr)
    end = time.time_ns()
    print(end - start)

    if ret == None:
        print("No partiton")
    else:
        print("Able to equally partition")

if __name__ == "__main__":
    main()