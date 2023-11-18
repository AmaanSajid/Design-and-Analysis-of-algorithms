#include <stdio.h>

int binarySearch(int array[], int x, int low, int high) {
  while (low <= high) {
    int mid = low + (high - low) / 2;

    if (array[mid] == x)
      return mid;

    if (array[mid] < x)
      low = mid + 1;

    else
      high = mid - 1;
  }

  return -1;
}

int main() {

    int  n ;
    printf("type the size of arr :\n");
    scanf("%d",&n);
    printf("give the array : \n");
    int arr[n];
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    int x ;
    scanf("%d",&x);
    int result = binarySearch(arr, x, 0, n - 1);
    if (result == -1)
      printf("Not found");
    else
      printf("Element is found at index %d", result);
    return 0;
}