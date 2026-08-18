class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> group = new HashMap<>();
        // key will be string of arr of all letters and val the words taht match it

        for (String str : strs) {
            int[] arr = new int[26]; // one spot for each letter and val = count of letter
            for (int i = 0; i < str.length(); i++){
                int index = str.charAt(i) - 'a';
                arr[index] = arr[index] + 1;
            }
            String key = Arrays.toString(arr); // then add this to map key
            group.computeIfAbsent(key, k -> new ArrayList<>());
            // group.put(key, group.get(key).add(str));
            group.get(key).add(str);

        }
        List<List<String>> vals = new ArrayList<>(group.values());
        return vals;
    }
}
