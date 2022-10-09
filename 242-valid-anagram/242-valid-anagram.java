class Solution {
    public boolean isAnagram(String s, String t) {
     char[] str1 = s.toCharArray();
     char[] str2 = t.toCharArray();
     Arrays.sort(str1);
     Arrays.sort(str2);  
     String res1 = new String(str1);
     String res2 = new String(str2);
     return res1.equals(res2);
    }
}