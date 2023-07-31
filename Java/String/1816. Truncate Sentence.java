class Solution {
    public String truncateSentence(String s, int k) {

        String res = "";

        String [] stringArray = s.split(" ");

        for(int i =0; i<k; i++){
            res +=stringArray[i]+" ";
        }

        return res.trim();
        
    }
}