class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]: 
        unique = sorted(tuple(set(nums))) 
        if target not in unique:
            return [-1,-1]
        first = nums.index(target) 
        target_index = unique.index(target) 
        if target_index == len(unique)-1:
            return [first,len(nums)-1]
        last = nums.index(unique[target_index+1]) 
        return [first,last-1] 
         

