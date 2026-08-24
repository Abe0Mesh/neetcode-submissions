class Solution {
    public boolean isValidSudoku(char[][] board) {
       // Need to parse all 9 sub boxes and check for duplicates
       // probably will use a hashset that resets for each block 
       // Then return false if hashset dup is triggered 
        Set<Character> set1 = new HashSet<>();
        Set<Character> set2 = new HashSet<>();
        Set<Character> set3 = new HashSet<>();
        Set<Character> row = new HashSet<>();
        Set<Character> col = new HashSet<>();




       for (int i = 0; i < board.length; i++) {
        // So Im thinking we go through 3 sub boxes at the same time 

        //row
        for (int r = 0; r < 9; r++) {
            if (board[i][r] == '.') continue;
            if (row.add(board[i][r]) == false) {
                    return false;
            } 
        }
        row.clear();

        // col
        for (int c = 0; c < 9; c++) {
            if (board[c][i] == '.') continue;
            if (col.add(board[c][i]) == false) {
                    return false;
            }

        }
        col.clear();

        // sub box 1
            for (int one = 0; one < 3; one++) {
                if (board[i][one] == '.') continue;
                if (set1.add(board[i][one]) == false) {
                    return false;
                }

            }

        // sub box 2
            for (int two = 3; two < 6; two++) {
                if (board[i][two] == '.') continue;
                if (set2.add(board[i][two]) == false) {
                    return false;
                }
            }


        // sub box 3
            for (int three = 6; three < 9; three++) {
                if (board[i][three] == '.') continue;
                if (set3.add(board[i][three]) == false) {
                    return false;
                }
            }

        if ( (i + 1 ) % 3 == 0) {
            // reset the 3 hashsets here for new subboxes
            set1.clear();
            set2.clear();
            set3.clear();
        }
        
        
       } 


       return true;
    }
}
