class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]: # nums = [5,7,7,8,8,10], target = 8
        unique = sorted(tuple(set(nums))) # [5, 7, 8, 10]
        if target not in unique:
            return [-1,-1]
        first = nums.index(target) # 3
        target_index = unique.index(target) # 2 
        if target_index == len(unique)-1:
            return [first,len(nums)-1]
        last = nums.index(unique[target_index+1]) # 7
        return [first,last-1] # [3,4]
         #[5,7,8,10] , 3 , 2 , [3,4]

