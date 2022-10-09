class Solution {
    public boolean isPalindrome(String s) {
        if (s == null){
            return false;
        }
        if (s == ""){
            return true;
        }
                
        s = s.toLowerCase(); 
        s = s.replaceAll("[^a-zA-Z0-9]", "");  
        int length = s.length();
        char[] palin = s.toCharArray();
        
        int left = 0;
        int right = length - 1;
        boolean flag = true;
        
        while (left <= right){
            if (palin[left] != palin[right]){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}