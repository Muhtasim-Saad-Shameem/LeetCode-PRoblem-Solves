class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Maximum length of product is len(num1) + len(num2)
        result = [0] * (len(num1) + len(num2))
        
        # reversing both num (right to left)
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        #  each digit of num1 x each digit of num2
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit1 = int(num1[i])
                digit2 = int(num2[j])
                product = digit1 * digit2
                
                # Add product
                result[i + j] += product
                
                # we handle the carry 
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10
        
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        
        result.reverse()
            
        return ''.join(map(str, result))
    
    # onek leetcode problem solve korte hobe :) 