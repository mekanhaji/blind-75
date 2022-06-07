# [338. Counting Bits](https://leetcode.com/problems/counting-bits/ "LeetCode")
`Dynamic Programming` `Bit Manipulation`
> Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` (`0 <= i <= n`), `ans[i]` is the *__number of__ `1`'__s__* in the binary representation of `i`.

### Example 1 :
    Input: n = 2
    Output: [0,1,1]
    Explanation:
    0 --> 0
    1 --> 1
    2 --> 10
### Example 2 :
    Input: n = 5
    Output: [0,1,1,2,1,2]
    Explanation:
    0 --> 0
    1 --> 1
    2 --> 10
    3 --> 11
    4 --> 100
    5 --> 101
### Constraints :
    0 <= n <= 10^5
