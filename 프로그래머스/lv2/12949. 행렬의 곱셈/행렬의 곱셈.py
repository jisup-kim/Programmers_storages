def solution(arr1, arr2):
    array = [[] for i in range(len(arr1))]
    sum = 0
    for x in range(len(arr1)):
        for y in range(len(arr2[0])):
            sum = 0
            for z in range(len(arr2)):
                sum += int(arr1[x][z])*int(arr2[z][y])
            array[x].append(sum)
    print(array)
    return array