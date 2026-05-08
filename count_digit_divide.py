class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        temp = num
        count = 0
        
        while temp > 0:
            digit = temp % 10            
            if num % digit == 0:
                count += 1
            temp //= 10
            
        return count