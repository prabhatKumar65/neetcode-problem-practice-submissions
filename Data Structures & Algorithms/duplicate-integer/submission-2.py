class Solution:
    def hasDuplicate(self, nums):
        seen = set() #Empty seen box for nums checks and store. 
        for num in nums:
            if num in seen:  #Check thr num in seen box one by one.
                return True  #If matched the return True.
            seen.add(num)    #Add num in seen box if not matched.
        return False         #If not matched then return False.