int maxArea(int* height, int heightSize) {
    int area = 0;
    int i = 0;
    int j = heightSize - 1;

    while (i < j) {
        int h = (height[i] < height[j]) ? height[i] : height[j];
        int width = j - i;
        int area1 = h * width;

        if (area1 > area) {
            area = area1;
        }

   
        if (height[i] < height[j]) {
            i++;
        } else {
            j--;
        }
    }

    return area;
}
