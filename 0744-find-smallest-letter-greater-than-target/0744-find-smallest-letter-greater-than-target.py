class Solution:
    def nextGreatestLetter(self, letters, target):
        left = 0
        right = len(letters)
        while left < right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return letters[left % len(letters)]