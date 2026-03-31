class Solution {
    public int search(int[] nums, int target) {
        int i = 0;
        int j = nums.length - 1;
        while (i <= j){
            int mid = (i + j) / 2;
            int cur = nums[mid]; 
            if(cur == target){
                return mid;
            }
            else if(cur < target){
                i = mid + 1;
            }
            else if(cur > target){
                j = mid - 1;
            }
        }
        return -1;
    }
}
