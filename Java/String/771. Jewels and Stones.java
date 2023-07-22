class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        int counter = 0;
        for (int i = 0;i<stones.length();i++){
            if(jewels.indexOf(stones.charAt(i)) >= 0 ){
                counter++;
            }
        }
        return counter;
    }
}