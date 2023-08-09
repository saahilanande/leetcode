lass Solution {
    public String removeOuterParentheses(String s) {

        String res = "";
        int counter = 1;
        for(int i =1; i<s.length();i++){

            if(s.charAt(i)=='('){
                counter++;
                if(counter >1){
                    res += "(";
                }
                
            }
            if(s.charAt(i)==')'){
                if(counter > 1){
                    res+= ")";
                }
                counter--;
            }

            


        }

        return res;
        
    }
}