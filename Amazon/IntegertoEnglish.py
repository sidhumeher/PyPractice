'''
Created on Dec 14, 2020

@author: sidteegela
'''


def numberToWords(num):
    
    if not num:
        return 'Zero'
    
    result = ''
    
    ones = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', \
            6:'six', 7:'seven', 8:'eight', 9:'nine'}
    tens = {2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', \
                    6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}
    
    uniques = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', \
               16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}

    def twoDigits(num):
        
        if not num:
            return ''
        elif num < 10:
            return ones[num]
        elif num < 20:
            return uniques[num]
        else:
            ten = num // 10
            # print('ten:', ten)
            rest = num % 10
            # print('rest:', rest)
            return tens[ten] + ' ' + ones[rest] if rest else tens[ten]
            
    def threeDigits(num):
        
        if not num:
            return ''
        hundred = num // 100
        rest = num % 100
        
        if hundred and rest:
            return ones[hundred] + ' hundred ' + twoDigits(rest)
        elif not hundred and rest:
            return twoDigits(rest)
        elif hundred and not rest:
            return ones[hundred] + ' hundred '
    
    billion = num // 1000000000
    million = (num - billion * 1000000000) // 1000000
    thousand = (num - billion * 1000000000 - million * 1000000) // 1000
    rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000
    
    if billion:
        result = threeDigits(billion) + ' Billion '
    if million:
        result += ' ' if result else ''
        result += threeDigits(million) + ' Million '
    if thousand:
        result += ' ' if result else ''
        result += threeDigits(thousand) + ' Thousand '
    if rest:
        result += ' ' if result else ''
        result += threeDigits(rest)
    
    return result

# Time complexity:O(n)            


if __name__ == '__main__':
    
    num = 12
    print(numberToWords(num))
    
    num = 123
    print(numberToWords(num))
    
    num = 12345
    print(numberToWords(num))
    
    num = 123456
    print(numberToWords(num))
    
    num = 1234567
    print(numberToWords(num))
    
    num = 12345678
    print(numberToWords(num))
    
    num = 123456789
    print(numberToWords(num))
    
    num = 1234567890
    print(numberToWords(num))
