class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans=[]
        for i in range(1,n+1):
            if n%3==0 and n%5==0:
                ans.append('FizzBuzz')
            elif n%3==0:
                ans.append('Fizz')
            elif n%5==0:
                ans.append('Buzz')
            else:
                ans.append(str[i])
        