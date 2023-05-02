import java.util.Arrays;
class Solution {
    public int minPairSum(int[] nums) {
        Arrays.sort(nums);
        int sum = 0;
        for(int i=0; i<nums.length/2; i++){
            if(sum < (nums[i]+nums[nums.length-(i+1)])){
                sum=nums[i]+nums[nums.length-(i+1)];
            }
        }
        return sum;
    }
}