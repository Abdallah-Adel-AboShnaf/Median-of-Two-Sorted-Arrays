Median of Two Sorted Arrays 📊
Overview 📋
This Python script calculates the median of two sorted arrays (nums1 and nums2) by merging them, sorting the combined array, and determining the median based on whether the total length is odd or even.
Features ✨

Input Handling 🖱️: Prompts the user to input the size and elements of two lists.
Merging Arrays 🔗: Combines the two input arrays into a single array.
Sorting 🔄: Uses bubble sort to sort the merged array.
Median Calculation 📈: Computes the median, returning a single middle element for odd-length arrays or the average of two middle elements for even-length arrays.

Time Complexity ⏱️

Merging arrays: O(m + n), where m and n are the lengths of nums1 and nums2.
Sorting (bubble sort): O((m + n)²).
Median calculation: O(1).
Overall complexity: O((m + n)²) due to the sorting step.

Usage 🚀

Run the script.
Enter the number of elements for the first list (m).
Input m integers for the first list.
Enter the number of elements for the second list (n).
Input n integers for the second list.
The script outputs the median of the combined sorted arrays.

Example 📝
Enter The Elements Of The First List: 2
Enter number 1: 1
Enter number 2: 3
Enter The Elements Of The Second List: 1
Enter number 1: 2
2.0

Explanation: The merged array [1, 3, 2] is sorted to [1, 2, 3], and the median is 2.0.
Notes 📌

The input arrays are assumed to be sorted, but the script sorts the merged array regardless, which may be unnecessary if the inputs are guaranteed sorted.
For better performance, consider using a more efficient algorithm (e.g., binary search) to find the median without sorting, achieving O(log(min(m, n))) complexity.

Requirements 🛠️

Python 3.x

License ⚖️
This project is unlicensed and free to use.
