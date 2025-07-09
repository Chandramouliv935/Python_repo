"""BRUTE FORCE METHOD"""
def two_sum(numbers,target):
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [numbers[i],numbers[j]]
            
numbers = [2,7,10,15]
target = 9
x = two_sum(numbers,target)
print(x)
