# [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/ "LeedCode")
`Array` `Hash Table` `Sorting` `String`

> Given an array of strings `strs`, group ____the anagrams____ together. You can return the answer in ____any order____.
>
> An ____Anagram____ is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Example 1 :
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

### Example 2 :
    Input: strs = [""]
    Output: [[""]]

### Example 3 :
    Input: strs = ["a"]
    Output: [["a"]]

### Constraints :
    1 <= strs.length <= 10^4
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.
