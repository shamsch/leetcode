ROMAN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0 
        for i in range(len(s)):
            if i>0 and ROMAN[s[i]] > ROMAN[s[i-1]]:
                # if we find a smaller number before, we need to subtract it, here's more details from the problem:
                # the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
                # I can be placed before V (5) and X (10) to make 4 and 9. 
                # X can be placed before L (50) and C (100) to make 40 and 90. 
                # C can be placed before D (500) and M (1000) to make 400 and 900.
                result += ROMAN[s[i]] - ROMAN[s[i-1]]

                # but because we had already added the previous number, we need to subtract it now since that number alone is not valid
                result -= ROMAN[s[i-1]]
            else:
                result += ROMAN[s[i]]
        return result
    