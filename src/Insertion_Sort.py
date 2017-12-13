def insertion_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(i + 1, 0, -1):
            if nums[j] < nums[j - 1]:
                tmp = nums[j]
                nums[j] = nums[j - 1]
                nums[j - 1] = tmp
            else:
                break


if __name__ == '__main__':
    nums = [4, 0, 1, 2, 3, 5, 6, 7, 8, 9, 1]
    insertion_sort(nums)
    print(nums)