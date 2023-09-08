class Solution {
    public int maximumNumberOfStringPairs(String[] words) {
        int counter = 0;
        for(int i = 0; i<words.length; i ++){
            for(int j = i +1; j<words.length; j++){
                if(words[j].charAt(0)==(words[i]).charAt(1) && words[j].charAt(1)==(words[i]).charAt(0)){
                    counter++;
                }   
            }
        }
        return counter;
    }
}