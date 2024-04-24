class Solution:
    def isPalindrome(self, x: int) -> bool:
        isPalindrome = False
        number = str(x)
        if (number == number[::-1]):
            isPalindrome = True
        return isPalindrome