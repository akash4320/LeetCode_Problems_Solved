public class Solution {
    public int AddDigits(int num) {
        int sum = sumDigits(num);
        if(sum/10 == 0) {
            return sum;
        }
        return AddDigits(sum);
    }
    
    public int sumDigits(int num) {
        int sum =0;
        while(num/10 != 0) {
            sum = sum + num%10;
            num = num/10;
        }
        return sum+num;
    }
}