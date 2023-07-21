class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int x = 0;
        for(String s :operations){
            if(s.charAt(1) == '-'){
                x += -1;
            }
            if(s.charAt(1) == '+'){
                x += 1;
            }
        }

        return x;
        
    }
}