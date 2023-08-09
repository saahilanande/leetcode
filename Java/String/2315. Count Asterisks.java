lass Solution {
    public int countAsterisks(String s) {
        int bcounter = 0;
        int counter= 0;
        for(int i = 0; i<s.length();i++){
            if(s.charAt(i) == '|'){
                bcounter++;
            }
            if(bcounter % 2 == 0){

                if(s.charAt(i)=='*'){
                counter++;
            }

            }

        }

        return counter;
        
    }
}