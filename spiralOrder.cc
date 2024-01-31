#include <vector>

vector<int> spiralOrder(vector<vector<int>>& matrix) {
    int topEnd = 0;
    int bottomEnd = matrix.size();
    int leftEnd = 0;
    int rightEnd = matrix[0].size();
    int col = 0; 
    int row = 0;
    vector<int> result;
    while ((leftEnd < rightEnd) && (topEnd < bottomEnd)) {
        while (col >= leftEnd && col < rightEnd && row >= topEnd && row < bottomEnd) {
            result.push_back(matrix[row][col]);
            ++col;
        }
        --col;
        ++row;
        ++topEnd;
        while (row >= topEnd && row < bottomEnd && col >= leftEnd && col < rightEnd) {
            result.push_back(matrix[row][col]);
            ++row;
        }
        --row;
        --col;
        --rightEnd;
        while (col >= leftEnd && col < rightEnd && row >= topEnd && row < bottomEnd) {
            result.push_back(matrix[row][col]);
            --col;
        }
        ++col;
        --row;
        --bottomEnd;
        while (row >= topEnd && row < bottomEnd && col >= leftEnd && col < rightEnd) {
            result.push_back(matrix[row][col]);
            --row;
        }
        ++row;
        ++col;
        ++leftEnd;
    }
    return result;
}
