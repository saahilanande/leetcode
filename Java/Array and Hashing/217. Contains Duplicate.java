class Solution {
    public boolean containsDuplicate(int[] nums) {

    Set<Integer> intSet = new HashSet<>();
    for(int i:nums){
        if(intSet.contains(i)){
            return true;
        }else{
            intSet.add(i);
        }
    }

    return false;
        
    }
}