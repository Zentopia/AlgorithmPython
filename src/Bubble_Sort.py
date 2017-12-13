def bubble_sort(nums):

    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                tmp = nums[j + 1]
                nums[j + 1] = nums[j]
                nums[j] = tmp


if __name__ == '__main__':
    nums = [2, 1, 4, 5, 3, 7, 8, 6, 9, 0]
    bubble_sort(nums)
    print(nums)