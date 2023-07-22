class Solution {
    public int mostWordsFound(String[] sentences) {
        int result = 0;
        for(String s:sentences){
            int words = 1;

            for(int i = 0;i<s.length(); i++){
                if(s.charAt(i)==' '){
                    words++;
                }
            }

            result = Math.max(result,words);
        }
        return result;
    }
}