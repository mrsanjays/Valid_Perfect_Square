class Solution:
    @staticmethod
    def Valid_Perfect_Square(num):
        l = 1
        r = num
        while l <= r:
            mid = (l + r) // 2
            if mid * mid == num:
                return "True"
            if mid * mid > num:
                r = mid - 1
            else:
                l = mid + 1
        return "False"
if __name__ == '__main__':
    n=int(input())
    print(Solution().Valid_Perfect_Square(n))
