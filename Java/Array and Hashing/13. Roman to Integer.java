class Solution {
    public int romanToInt(String s) {
        
        int res = 0;
        Map<String, Integer> roman = new HashMap<>();

        roman.put("I",1);
        roman.put("V",5);
        roman.put("X",10);
        roman.put("L",50);
        roman.put("C",100);
        roman.put("D",500);
        roman.put("M",1000);

        for( int i = 0 ; i < s.length() ; i++){
            
            if(i + 1 < s.length() && roman.get(String.valueOf(s.charAt(i))) < roman.get(String.valueOf(s.charAt(i + 1)))){
                res = res - roman.get(String.valueOf(s.charAt(i)));
            }else{
                res = res + roman.get(String.valueOf(s.charAt(i)));
            }
        }
        
    return res;
    }
}
