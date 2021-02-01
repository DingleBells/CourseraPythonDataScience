def findLargestPairwise(inlist):
    largest = 0
    secondlargest = 0
    for number in inlist:
        if number > secondlargest:
            if number > largest:
                secondlargest = largest
                largest = number
            else:
                secondlargest = number
    return largest * secondlargest


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(findLargestPairwise(input_numbers))