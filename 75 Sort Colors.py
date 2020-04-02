for i in range(len(nums)):
            if 0 in nums[i:]:
                nums[nums.index(0,i)] = nums[i]
                nums[i] = 0
            elif 1 in nums[i:]:
                nums[nums.index(1,i)] = nums[i]
                nums[i] = 1
            else:
                nums[nums.index(2,i)] = nums[i]
                nums[i] = 2
