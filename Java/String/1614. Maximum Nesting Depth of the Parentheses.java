class Solution {
    public int maxDepth(String s) {
        int maxi=Integer.MIN_VALUE;
        int counter = 0;
        for(int i =0;i<s.length();i++){
            if(s.charAt(i)=='('){
                counter++;
            }
            if(s.charAt(i)==')'){
                counter--;
            }

            maxi = Math.max(maxi,counter);

        }

        return maxi;
        
    }
}