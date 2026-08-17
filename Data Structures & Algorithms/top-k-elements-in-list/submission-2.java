class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        
        Map<Integer, Integer> count = new HashMap<>();
        // second either a list of arrs or a map of arrs index/key = freq and element/val will be a int list 
        Map<Integer, List<Integer>> freq = new HashMap<>();

        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }

        for (int i = 1; i <= nums.length; i++) {
            freq.put(i, new ArrayList<>());
        }

        for (Integer num : count.keySet()) { 
            freq.get(count.get(num)).add(num);
        }

        int[] arr = new int[k];
        int index = 0;
        for (int i = nums.length; i > 0; i--) {
            List<Integer> temp = freq.get(i);
            for (int num : temp) {
                arr[index++] = num;
                if (index == k) return arr;
            }
        }
        return arr;
    }
}
