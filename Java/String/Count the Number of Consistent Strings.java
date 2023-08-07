lass Solution {
    public int countConsistentStrings(String allowed, String[] words) {

        int counter = 0;
        HashSet<Character> charMap = new HashSet();
        for(char c: allowed.toCharArray()){
            charMap.add(c);
        }

        for(String s: words){
           for(int i=0; i<s.length();i++){
                if(!charMap.contains(s.charAt(i))){
                    counter++;
                    break;
                }
           }
        }

        return (words.length - counter);
        
    }
}