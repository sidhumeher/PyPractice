

def letterCombinations(digits):
    
    combinations = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'],
                    '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'],
                    '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}

    result = []

    def helper(current, remainingDigits):
        if len(remainingDigits) == 0:
            result.append(current)
            return
        else:
            for char in combinations[remainingDigits[0]]:
                helper(current + char, remainingDigits[1:])

    if len(digits) == 0:
        return []
    else:
        helper("", digits)
        return result

# Time complexity: O(3^m*4^m), n=No of digits in input with 3 letters and m=No of digits with 4 letters
# Space: O(3^n * 4^m)

 
if __name__ == '__main__':

    digits = '23'
    result = letterCombinations(digits)
    print(result)
    
