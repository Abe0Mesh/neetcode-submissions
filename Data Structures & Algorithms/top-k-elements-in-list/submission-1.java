class Solution {
    public int[] topKFrequent(int[] nums, int k) {

    Map<Integer, List<Integer>> sortedFreq = new HashMap<>();
    Map<Integer, Integer> freq = new HashMap<>();


    for (int i = 1; i <= nums.length; i++) { 
        sortedFreq.put(i, new ArrayList<>());
    }

    for (int num : nums) {
        freq.put(num, freq.getOrDefault(num, 0) + 1);       
    }

    for (int num : freq.keySet()) {
        int count = freq.get(num);
        sortedFreq.get(count).add(num);
    }

    int[] arr = new int[k];
    int index = 0;
    // need to fill up this arr with all the numbers until its filled up
    for(int i = nums.length; i > 0; i--) {
        List<Integer> temp = sortedFreq.get(i);
        // if (temp.isEmpty()) continue;
        for (int j = 0; j < temp.size(); j++) {
            arr[index] = temp.get(j);
            index++;
            if (index == k) return arr;
        }
    }

    return arr;

    

    }
}
