/*

Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
    Input: s = ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]
Example 2:
    Input: s = ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]
*/
public class ReverseString {

    public static void reverserString(char[] s) {
        
        int right = s.length - 1;
        int left = 0;
        while (right > left) {
            char k = s[left];
            s[left] = s[right];
            s[right] = k;
            left++; 
            right--;
        }
    }

    public static void main(String[] args) {
        char[] s1 = {'h','e','l','l','o'};
        char[] s2 = {'b','r','o','t','h','e','r'};
        System.out.println(reverserString(s1));
        System.out.println(reverserString(s2));
    }
}