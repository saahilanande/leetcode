lass Solution {
    public String sortSentence(String s) {

        String[] word = s.split(" ");
        String[] temp = new String[word.length];
        int index; 
        for(String j : word){
            index = j.charAt(j.length()-1) - '0';
            temp[index-1] = j.substring(0, j.length()-1);
        }
        return String.join(" ", temp);
    }
}