'''
Created on Nov 6, 2020

@author: sidteegela
'''
# Recursion problem
# Backtracking technique


def combinationSum(candidates, target):
    
    result = []
    
    def backtrack(remaining, combination, startIndex):
        # base case. If remaining == 0
        if remaining == 0:
            result.append(list(combination))
            return 
        # base case. If remaining < 0(Exceeded)
        if remaining < 0:
            return 
        
        for i in range(startIndex, len(candidates)):
            # Add current item to combination
            combination.append(candidates[i])
            # Given current item another chance. Duplicates are allowed
            backtrack(remaining - candidates[i], combination, i)
            # Remove item from combination list
            combination.pop()
    
    backtrack(target, [], 0)
    return result

# Time complexity: O(n^(t/m)+1)
# n = No of candidates, t= target, m=min value in candidate
# Space: O(t/m)


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]; target = 7
    print(combinationSum(candidates, target))
    
    candidates = [2, 3, 5]; target = 8
    print(combinationSum(candidates, target))
    
    candidates = [1]; target = 1
    print(combinationSum(candidates, target))
