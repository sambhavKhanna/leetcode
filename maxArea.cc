#include <vector>
using namespace std;

int maxArea(vector<int>& height) {
    int max_area = 0, n = height.size();
    int l = 0, r = n - 1;
    while (l < r) {
        int area = min(height[l], height[r]) * (r - l);
        max_area = max(max_area, area);
        if (height[l] < height[r]) ++l;
        else --r;
    }
    return max_area;
}