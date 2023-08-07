class Solution {
    public String reverseWords(String s) {
        String[] stringArrya = s.split(" ");
        String res = "";

        for(String w: stringArrya){
            for(int i=w.length()-1;i>=0;i--){
                res += w.charAt(i);
            }
            res += " ";
        }

        return res.trim();
    }
}