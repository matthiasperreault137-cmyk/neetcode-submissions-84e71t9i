class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int ix = 0;
        int iy = 0;
        int jx = 0;
        int jy = matrix.length - 1;
        Integer y = null;
        while(iy <= jy){
            int mid = (iy + jy) / 2;
            int first = matrix[mid][0];
            int last = matrix[mid][matrix[mid].length - 1];
            if(first <= target && last >= target){
                y = mid;
                break;
            }
            else if(last < target){
                iy = mid + 1;
            }
            else{
                jy = mid - 1;
            }
        }
        if(y == null){
            return false;
        }
        jx = matrix[y].length - 1;
        while(ix <= jx){
            int mid = (ix +jx) / 2;
            int cur = matrix[y][mid];
            if(cur == target){
                return true;
            }
            else if(cur < target){
                ix = mid + 1;
            }
            else{
                jx = mid - 1;
            }
        }
        return false;
    }
}