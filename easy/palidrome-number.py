class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            y = 0
            z = x
            while z > 0:
                # i.e 123 % 10 = 3 + 0*10 = 3 
                # => 12 % 10 = 2 + 3*10 = 32
                # => i.e 1 % 10 = 1 + 32*10 = 321
                y = y * 10 + z % 10
                z = z // 10
            return x == y
