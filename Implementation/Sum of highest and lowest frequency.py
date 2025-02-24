class SumHighestAndLowestFrequency:
    def sumHighestAndLowestFrequency(self, nums):
        my_dict = {}
        for ele in nums:
            my_dict[ele] = (my_dict.get(ele, 0) + 1)
        
        max_freq, min_freq = 0, len(nums)

        for ele, freq in my_dict.items():
            max_freq = max(max_freq, freq)
            min_freq = min(min_freq, freq)
        
        return (max_freq + min_freq)
fn = SumHighestAndLowestFrequency()
print(fn.sumHighestAndLowestFrequency([4, 4, 1, 1, 2]))