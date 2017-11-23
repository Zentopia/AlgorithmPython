
def quick_sort(left, right, nums):

    if left >= right:
        return

    # 选择最左边的元素为基准元素
    pivot = nums[left]
    move_left = left
    move_right = right

    while move_left < move_right:

        while nums[move_right] < pivot and move_left < move_right:
            move_right -= 1

        while nums[move_left] >= pivot and move_left < move_right:
            move_left += 1

        if move_left < move_right:
            temp = nums[move_left]
            nums[move_left] = nums[move_right]
            nums[move_right] = temp

    nums[left] = nums[move_left]
    nums[move_left] = pivot

    quick_sort(left, move_left - 1, nums)
    quick_sort(move_left + 1, right, nums)


if __name__ == '__main__':
    nums = [4, 0, 1, 2, 3, 5, 6, 7, 8, 9]
    quick_sort(0, len(nums) - 1, nums)
    print(nums)