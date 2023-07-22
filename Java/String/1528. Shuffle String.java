class Solution {
    public String restoreString(String s, int[] indices) {
        char arrayChar[] = new char[indices.length];
        for(int i :indices){
            arrayChar[indices[i]]= s.charAt(i);
        }

        return new String(arrayChar);
        
    }
}