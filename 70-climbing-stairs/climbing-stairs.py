class Solution:
    def factorial(self, n:int) -> int:
        if n == 0:
            return 1
        return n * self.factorial(n-1)

    def climbStairs(self, n: int) -> int:
        if n%2 == 0:
            two_cnt = n//2
            one_cnt = 0
        else:
            two_cnt = (n-1)//2
            one_cnt = 1

        combination = 0

        while two_cnt != 0:
            combination += self.factorial(two_cnt + one_cnt)//(self.factorial(two_cnt)*self.factorial(one_cnt))
            two_cnt -= 1
            one_cnt += 2

        return combination + self.factorial(two_cnt + one_cnt)//(self.factorial(two_cnt)*self.factorial(one_cnt)) 