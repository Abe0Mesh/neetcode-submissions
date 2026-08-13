class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> existingNums = new HashSet<>();
        boolean doubleExists;
        for(int num : nums) {// fill the hasset with all unique nums 
            if (existingNums.add(num) == false) return true; // adding duplicate num to hashset w .add returns false
        }
        return false;
    }
}