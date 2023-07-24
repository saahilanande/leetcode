class Solution {
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {

        // int result = 0;

        // for(List item: items){
        //     if(ruleKey.equals("color") && item.get(1).equals(ruleValue)){
        //         result++;
        //     }
        //     if(ruleKey.equals("type")&& item.get(0).equals(ruleValue)){
        //         result++;
        //     }
        //     if(ruleKey.equals("name")&& item.get(2).equals(ruleValue)){
        //         result++;
        //     }
        // }

        // return result;

        int result = 0;
        HashMap<String, Integer> ruleMap = new HashMap();
        ruleMap.put("type",0);
        ruleMap.put("color",1);
        ruleMap.put("name",2);
        for(List item: items){
            if(item.get(ruleMap.get(ruleKey)).equals(ruleValue)){
                result++;
            }
        }

        return result;
        
    }
}