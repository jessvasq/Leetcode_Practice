'''169. Majority Element'''
nums = [2,2,1,1,1,2,2]
print('max', max(nums))

#use the Boyer-Moore Voting Algorithm. The key idea is to cancel out each occurrence of an element with all the other elements that are different from it. This way, the majority element, if it exists, will eventually stand out.
def find_majority(nums):
    x = None
    count = 0
    for i in nums:
        if count == 0:
            x = i
        count += 1 if i == x else -1 
    return x

print(find_majority(nums))
