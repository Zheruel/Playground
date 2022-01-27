Algo practice from:
https://techinterviewhandbook.org/best-practice-questions/#week-1---sequences

1. Two sum -> https://leetcode.com/problems/two-sum/

Hash map, Time complexity: O(n), Space complexity: O(n),

2. Contains Duplicate -> https://leetcode.com/problems/contains-duplicate/

Hash map, Time complexity: O(n), Space complexity: O(n)

3. Best Time to Buy and Sell Stock -> https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Two pointers, Time complexity: O(n), Space complexity: O(1)

4. Valid Anagram -> https://leetcode.com/problems/valid-anagram/

Hash map, Time complexity: O(n), Space complexity: O(n)

5. Valid Parentheses -> https://leetcode.com/problems/valid-parentheses/

Hash map (stack), Time complexity: O(n), Space complexity: O(n)

6. Product of Array Except Self -> https://leetcode.com/problems/product-of-array-except-self/

Just 2 for loops, Time complexity: O(n), Space complexity: O(1) because you are allowed to ignore the output array in space complexity analysis

7.  Maximum Subarray -> https://leetcode.com/problems/maximum-subarray/

Kadane's algorithm. Time complexity: O(n), Space complexity: O(1)

8. 3Sum -> https://leetcode.com/problems/3sum

Sort array + two pointers, if element not first skip if element is equal to the first element. Do the same for the left pointer when hitting a match.
Time Complexity: O(n^2), Space complexity O(1) but could be O(n) depending of the sort implementation

9. Merge Intervals -> https://leetcode.com/problems/merge-intervals/

Sort array of arrays by first element. Time complexity: O(nlog(n)), Space complexity: O(1) or O(n) depending on the sort implementation.

10. Group Anagrams -> https://leetcode.com/problems/group-anagrams

Use ord to count num of letters in string. Use tuple of string_count as a key for a hash map. Time complexity: O(mn), Space complexity: O(mn)
