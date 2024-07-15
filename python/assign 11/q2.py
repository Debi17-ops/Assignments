def find_pos(nums,target,find_first):
    left = 0
    right = len(nums)-1
    position = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
                position = mid
                if find_first:
                     right = mid - 1
                else:
                     left = mid + 1
        elif nums[mid] < target:
             left = mid + 1
        else:
             right = mid - 1
    return position

def count_occurences(nums,target):
     start = find_pos(nums,target,True)         # calculating the start index
     if start == -1:
          return 0
     end = find_pos(nums,target,False)          # calculating the end index
     count = end - start + 1                    # calculating the number of occurences
     return count

     
l1=[8,9,11,11,11,14,99]
target = 11
print(count_occurences(l1,target))