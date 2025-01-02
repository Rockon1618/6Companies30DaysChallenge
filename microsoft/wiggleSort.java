import java.util.Arrays;
class Solution {
    public void wiggleSort(int[] nums) {
        int n = nums.length; 
        int[] temp = nums.clone();

        Arrays.sort(temp);

        int mid = (n-1) / 2;

        for(int i = 0; i < n; i++){
            if(i % 2 == 0){
                nums[i] = temp[mid-i/2];
            }
            else{
                nums[i] = temp[n-1-i/2];
            }
        }
    }
}