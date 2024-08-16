class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        
        
        vector<int> result;
        
        int rows = matrix.size();
        
        if (rows == 0) {
            return result;
        }
        
        int columns = matrix[0].size();
        
        // sr = start row, er = end row, sc = start column, ec = end column
        
        int sr = 0, sc = 0, er = rows-1, ec = columns-1;
        
        int count = 0;
        
        
        while (sr <= er && sc <= ec) {
            // print sr
            for(int i=sc; i<=ec; i++) {
                result.push_back(matrix.at(sr).at(i));
                count++;
            } 
            sr++;
            
            if (count==rows*columns) return result;
            
            for(int i=sr; i<=er; i++) {
                result.push_back(matrix.at(i).at(ec));
                count++;
            }
            ec--;
            
            if (count==rows*columns) return result;
            
            for(int i = ec; i>=sc; i--) {
                result.push_back(matrix.at(er).at(i));
                count++;
            }
            er--;
            
            if (count==rows*columns) return result;
            
            for(int i=er; i>=sr; i--)  {
                result.push_back(matrix.at(i).at(sc));
                count++;
            }
            sc++;
            
            if (count==rows*columns) return result;
        }
        
        return result;
        
    }
};