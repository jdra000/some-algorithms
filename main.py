# Binary Search

def binary_search(nums, target):
	low = 0
	high = len(nums) - 1

	while low <= high:
		median = (low + high) // 2

		if target == nums[median]:
			return True

		elif target <= nums[median]:
			low += median + 1
		else:
			high += median - 1

	return False

print(binary_search([1,2,4,9,19,56,466,4567,7888], 56))


# Selection Sort
def selection_sort(nums):
    for i in range(len(nums)):
        smallest_idx = i

        for j in range(smallest_idx+1, len(nums)):
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j
                
        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]

    return nums




# Merge Sort

def merge_sort(nums):
	if len(nums) < 2:
		return nums

	mid = len(nums) // 2
	left_half = nums[:mid]
	right_half = nums[mid:]

	sorted_left_side = merge_sort(left_half)
	sorted_right_side = merge_sort(right_half)

	return merge(sorted_left_side, sorted_right_side)


def merge(left, right):
	final = []
	i, j = 0, 0

	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			final.append(left[i])
			i+=1

		else:
			final.append(right[j])
			j+=1

	while i < len(left):
		final.append(left[i])
		i+=1


	while j < len(right):
		final.append(right[j])
		j+=1

	return final

print(merge_sort([1,77,4,56,24,34,56,212,9,2,1111]))



# Insertion Sort
def insertion_sort(nums):
	for index in range(len(nums)):
		j = index 
		while j > 0 and nums[j-1] > nums[j]:
			nums[j], nums[j-1] = nums[j-1], nums[j]
			j-=1

	return nums



# Quick Sort
def quick_sort(nums, low, high):
	if low < high:
		pivot = partition(nums, low, high)

		quick_sort(nums, low, pivot - 1)
		quick_sort(nums, pivot + 1, high)

def partition(nums, low, high):
	pivot = nums[high]
	i = low

	for j in range(low, high):
		if nums[j] < pivot:
			nums[i], nums[j] = nums[j], nums[i]
			i+=1

	nums[i], nums[high] = nums[high], nums[i]
	return i










