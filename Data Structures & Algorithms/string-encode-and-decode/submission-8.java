class Solution {

    public String encode(List<String> strs) {
        String words = "";
        String lengths = "|";
        // Gonna sned final string with the words and then also the lenghts of the words
        for (String str : strs) {
            int length = str.length();
            words += str;
            lengths += length;
            lengths += ",";
            

        }
        return words + lengths;
    }

    public List<String> decode(String str) {
        List<String> list = new ArrayList<>();

        int div = 0;
        for (int i = 0; i < str.length(); i++) {
            // how to parse using the lengths
            if (str.charAt(i) == '|') div = i;
        }
        String allLengs = str.substring(div + 1, str.length());
        int endOfWord = 0; // use this to track where I last read from 
        for (int i = 0; i < allLengs.length(); i++) {

            String lengString = "";
            
            while (allLengs.charAt(i) != ',') {
                lengString += allLengs.charAt(i);
                i++;
            }
            int leng = Integer.parseInt(lengString);

            list.add(str.substring(endOfWord, endOfWord + leng)); 
            endOfWord += leng;

        }
        return list;
        
    }
}
