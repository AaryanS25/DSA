class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum1=0
        mul=1
        while n>0:
            num=n%10
            sum1 +=num
            mul *=num
            n=n//10
        return mul-sum1