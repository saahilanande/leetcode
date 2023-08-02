class Solution {
    public boolean checkIfPangram(String sentence) {

        if(sentence.length()<26){
            return false;
        }

        Boolean[] charArray = new Boolean[26];
        for(int i = 0;i<sentence.length();i++){
            char c = sentence.charAt(i);
            charArray[c-'a'] = true;
        }

        for(Boolean b: charArray){
            if(b==null){
                return false;
            }
        }

        return true;
        
    }
}