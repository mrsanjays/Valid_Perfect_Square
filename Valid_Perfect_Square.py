class Solution:
    @staticmethod
    def Valid_Perfect_Square(n):
        i=1
        while i*i<=n:
            if i*i==n:
                return "True"
            i+=1
        return "False"
if __name__ == '__main__':
    n=int(input())
    print(Solution().Valid_Perfect_Square(n))