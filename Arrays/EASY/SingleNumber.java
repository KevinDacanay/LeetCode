/*

Given a non-empty array of integers nums, every element appears 
twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity 
and use only constant extra space.

Example 1:
    Input: nums = [2,2,1]
    Output: 1

Example 2:
    Input: nums = [4,1,2,1,2]
    Output: 4

Example 3:
    Input: nums = [1]
    Output: 1
 */

public class SingleNumber {
    public static int singleNumber(int[] nums) {
        
        if (nums.length == 1) {
            return nums[0];
        }
        int num = 0;
        for (int x : nums) {
            num ^= x;
        }
        return num;
    }

    public static void main(String[] args) {
        int[] n1 = {4,1,2,1,2};
        int[] n2 = {2,2,1};
        int[] n3 = {1};
        System.out.println(singleNumber(n1));
        System.out.println(singleNumber(n2));
        System.out.println(singleNumber(n3));
    }
}
