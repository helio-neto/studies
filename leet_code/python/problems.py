#!/usr/bin/env python
from collections import Counter
from itertools import combinations_with_replacement, product
from typing import List, Optional

from studies.leet_code.python.list_node import SinglyLinkedList


class Problems:
    """Solutions for LeetCode problems using Python."""

    def addBinary(self, a: str, b: str) -> str:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/add-binary/

        Description: Given two binary strings a and b, return their sum as a binary string.
        
        Example 1:
        
        Input: a = "11", b = "1"
        Output: "100"
        
        Example 2:
        
        Input: a = "1010", b = "1011"
        Output: "10101"
        
        Constraints:
        
        1 <= a.length, b.length <= 104
        a and b consist only of '0' or '1' characters.
        Each string does not contain leading zeros except for the zero itself.
        """
        return bin(int(a, 2) + int(b, 2))[2:]
    
    def addStrings(self, num1: str, num2: str) -> str:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/add-strings/

        Description: Given two non-negative integers, num1 and num2 represented as string, return
        the sum of num1 and num2 as a string.
        """
        sys.set_int_max_str_digits(6000)
        return str(sum([int(num1), int(num2)]))
    
    def addTwoNumbers(
        self,
        l1: Optional[SinglyLinkedList],
        l2: Optional[SinglyLinkedList]
    ) -> Optional[SinglyLinkedList]:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/add-two-numbers/

        Description: You are given two non-empty linked lists representing two non-negative integers.
        The digits are stored in reverse order, and each of their nodes contains a single digit.
        Add the two numbers and return the sum as a linked list.

        You may assume the two numbers do not contain any leading zero, except the number 0 itself.

        Example 1:
        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        Explanation: 342 + 465 = 807.

        Example 2:
        Input: l1 = [0], l2 = [0]
        Output: [0]

        Example 3:
        Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
        Output: [8,9,9,9,0,0,0,1]

        Constraints:
        The number of nodes in each linked list is in the range [1, 100].
        0 <= Node.val <= 9
        It is guaranteed that the list represents a number that does not have leading zeros.
        """
        # Create a dummy node to act as the starting point of the result list
        dummy = SinglyLinkedList(0)
        current = dummy
        carry = 0
       
        # Continue looping while there are nodes to process or a leftover carry
        while l1 or l2 or carry:
            # Extract digits, substituting 0 if a list has already finished
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate total sum for the current position
            total = val1 + val2 + carry
            
            # Determine new carry and the digit to store
            carry = total // 10
            digit = total % 10
            
            # Append the new digit node to our result list
            current.next = SinglyLinkedList(digit)
            current = current.next
            
            # Advance pointers if more nodes exist
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next

    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/backspace-string-compare/

        Description: Given two strings s and t, return true if they are equal when both are typed into
        empty text editors. '#' means a backspace character.
        Note that after backspacing an empty text, the text will continue empty.
        """
        backspace_char = "#"
        while backspace_char in s or backspace_char in t:
            s_index = s.find(backspace_char)
            if s_index == 0:
                s = s[1:]
                continue
            if s_index != -1:
                s = s[:s_index-1] + s[s_index+1:]
            t_index = t.find(backspace_char)
            if t_index == 0:
                t = t[1:]
                continue
            if t_index != -1:
                t = t[:t_index-1] + t[t_index+1:]
        return s == t
    
    def calPoints(self, operations: List[str]) -> int:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/baseball-game/

        Description: You are keeping the scores for a baseball game with strange rules.
        At the beginning of the game, you start with an empty record.
        You are given a list of strings operations, where operations[i] is the ith operation you
        must apply to the record and is one of the following:
        An integer x.
        Record a new score of x.
        '+'.
        Record a new score that is the sum of the previous two scores.
        'D'.
        Record a new score that is the double of the previous score.
        'C'.
        Invalidate the previous score, removing it from the record.
        Return the sum of all the scores on the record after applying all the operations.
        """
        records = []
        for operation in operations:
            try:
                records.append(int(operation))
            except ValueError:
                if operation == "+":
                    records.append(sum(records[-2:]))
                elif operation == "D":
                    records.append(2*records[-1])
                else:
                    records.pop()
        return sum(records)

    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/maximum-frequency-sum-of-a-string-after-modifying/

        Description: There is a keyboard with some broken letters. Given a string text and a string
        brokenLetters, return the number of words in text you can fully type using this keyboard.
        """
        splited_words = text.split(" ")
        broken_letters = list(brokenLetters)
        can_be_typed_words = len(splited_words)
        for broken_letter in broken_letters:
            if broken_letter in text:
                can_be_typed_words -= text.count(broken_letter)
        return can_be_typed_words
    
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/ransom-note/

        Description: Given two strings ransomNote and magazine, return true if ransomNote can be
        constructed by using the letters from magazine and false otherwise.
        """
        for ransom_word in ransomNote:
            if ransom_word in magazine:
                magazine = magazine.replace(ransom_word, "", 1)
                continue
            else:
                return False
        return True
    
    def checkRecord(self, s: str) -> bool:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/student-attendance-record-i/

        Description: You are given a string s representing an attendance record for a student where
        each character signifies whether the student was absent, late, or present on that day.
        The record only contains the following three characters:
        'A': Absent.
        'L': Late.
        'P': Present.
        The student is a prize winner if they meet both of the following criteria:
        The student was absent ('A') for strictly fewer than 2 days total.
        The student was never late ('L') for 3 or more consecutive days.
        Return true if the student is a prize winner, or false otherwise.
        """
        start = 0
        late_days = 3
        late_cut = "LLL"
        s_size = len(s)
        # Check for Absence
        if s.count("A") >= 2:
            return False
        # Check for lateness
        while late_days <= s_size:
            if s[start:late_days] == late_cut:
                return False
            start += 1
            late_days += 1
        return True

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Status: WORKING...

        Reference: https://leetcode.com/problems/combination-sum/

        Description: Given an array of distinct integers candidates and a target integer target,
        return a list of all unique combinations of candidates where the chosen numbers sum to target.
        You may return the combinations in any order.
        The same number may be chosen from candidates an unlimited number of times.
        Two combinations are unique if the frequency of at least one of the chosen numbers is different.
        The test cases are generated such that the number of unique combinations that sum up to target is
        less than 150 combinations for the given input.
        """
        unique_combinations = []
        # Loop through all possible lengths of candidates permutations
        for combination_size in range(1, len(candidates) + 2):
            for possible_candidate in combinations_with_replacement(candidates, combination_size):
                if sum(possible_candidate) == target:
                    unique_combinations.append(possible_candidate)
        return unique_combinations

    def compareVersion(self, version1: str, version2: str) -> int:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/compare-version-numbers/

        Description: Compare two version strings, version1 and version2.
        Each version string consists of revisions separated by dots '.'.
        The value of the revision is its integer conversion ignoring leading zeros.
        """
        # Split version strings
        version1_list = [int(v1) for v1 in version1.split(".")]
        version2_list = [int(v2) for v2 in version2.split(".")]
        # Compare, filling missing values with a default (e.g., 'missing')
        zipped_for_comparison = list(zip_longest(version1_list, version2_list, fillvalue=0))
        # You can then check for equality in a more comprehensive way
        versions_equal = all(version1 == version2 for version1, version2 in zipped_for_comparison)
        # Validate and return the result
        if versions_equal:
            return 0
        if version1_list < version2_list:
            return -1
        if version1_list > version2_list:
            return 1
    
    def compress(self, chars: List[str]) -> int:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/string-compression/

        Description: Given an array of characters chars, compress it using the following algorithm:
        Begin with an empty string s.
        For each group of consecutive repeating characters in chars:
        If the group's length is 1, append the character to s.
        Otherwise, append the character followed by the group's length.
        The compressed string s should not be returned separately, but instead, be stored in the input character
        array chars.
        Note that group lengths that are 10 or longer will be split into multiple characters in chars.
        After you are done modifying the input array, return the new length of the array.
        You must write an algorithm that uses only constant extra space.
        """
        if not chars:
            return 0
            
        write_index = 0
        read_index = 0
        n = len(chars)
        
        while read_index < n:
            current_char = chars[read_index]
            count = 1
            # Count consecutive characters
            while read_index + 1 < n and chars[read_index + 1] == current_char:
                read_index += 1
                count += 1
            # Write the character
            chars[write_index] = current_char
            write_index += 1
            # Write the count if greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit
                    write_index += 1
            read_index += 1
        return write_index

    def compress_by_me(self, chars: List[str]) -> int:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/string-compression/

        Description: Given an array of characters chars, compress it using the following algorithm:
        Begin with an empty string s.
        For each group of consecutive repeating characters in chars:
        If the group's length is 1, append the character to s.
        Otherwise, append the character followed by the group's length.
        The compressed string s should not be returned separately, but instead, be stored in the input character
        array chars.
        Note that group lengths that are 10 or longer will be split into multiple characters in chars.
        After you are done modifying the input array, return the new length of the array.
        You must write an algorithm that uses only constant extra space.
        """
        chars_length = len(chars)
        string_builder = ""
        char_count = 1
        previous_item = None

        if chars_length == 1:
            return chars_length

        for index, char in enumerate(chars):
            if char == previous_item:
                string_builder += char

            previous_item = char
            if char == chars[index + 1]:
                char_count += 1
                if index + 1 == chars_length - 1:
                    string_builder += str(char_count)
                    char_count = 1
            else:
                if char_count == 1:
                    continue 
                string_builder += str(char_count)
                char_count = 1

        chars.clear()
        chars.extend(list(string_builder))
        return len(chars)

    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/construct-transformed-array/

        Description: Given a 0-indexed integer array nums of size n, construct and return an integer array
        ans of size n that is the concatenation of array nums with itself.
        """
        ct_index = 0
        nums_size = len(nums)
        result = []
        while ct_index < nums_size:
            array_value = nums[ct_index]
            result.append(nums[(ct_index + array_value) % nums_size])
            ct_index += 1
        return result
    
    def convert(self, s: str, numRows: int) -> str:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/zigzag-conversion/

        Description: The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of
        rows like this: (you may want to display this pattern in a fixed font for better legibility)
        P   A   H   N
        A P L S I I G
        Y   I   R
        And then read line by line: "PAHNAPLSIIGYIR"
        """
        s_size = len(s)
        string_index = 0
        index = 0  # Start at the first character
        direction = 1  # 1 means move forward, -1 means move backwards
        split_rows = [[] for _ in range(numRows)]
        # Edge case: if there is only one row, return the string as is
        if numRows == 1:
            return s
        # Loop runs until the string_index is no longer smaller than the string length
        while string_index < s_size:
            # 1. Add char to it's respective zig zag row/position
            split_rows[index].append(s[string_index])
            # 2. Step forward to the next char on the string
            string_index += 1
            # 3. Step forward or backward onto the zig zag pattern
            index += direction
            # 4. Check if we need to bounce back
            if index == numRows - 1:
                direction = -1  # Hit the zig zag end! Turn back.
            elif index == 0:
                direction = 1  # Hit the zig zag start! Turn back.
        return "".join(["".join(row) for row in split_rows])
    
    def countSegments(self, s: str) -> int:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/number-of-segments-in-a-string/

        Description: Given a string s, return the number of segments in the string.
        """
        string_list = s.split()
        return len(string_list)
    
    def detectCapitalUse(self, word: str) -> bool:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/detect-capital/

        Description: We define the usage of capitals in a word to be right when one of the following cases holds:
        All letters in this word are capitals, like "USA".
        All letters in this word are not capitals, like "leetcode".
        Only the first letter in this word is capital, like "Google".
        """
        if word.islower() or word.isupper() or word.istitle():
            return True
        else:
            return False
    
    def distributeCandies(self, candyType: List[int]) -> int:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/distribute-candies/

        Description: Alice has n candies, where the ith candy is of type candyType[i].
        Alice noticed that she started to gain weight, so she visited a doctor.
        The doctor advised Alice to only eat n / 2 of the candies she has (n is always even).
        Alice likes her candies very much, and she wants to eat the maximum number of different types
        of candies while still following the doctor's advice.
        Given the integer array candyType of length n, return the maximum number of different types of
        candies she can eat if she only eats n / 2 of them.
        """
        max_candies = int(len(candyType)/2)
        unique_candies = set(candyType)
        candy_types = len(unique_candies)

        if candy_types >= max_candies:
            return max_candies
        else:
            return candy_types
    
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/find-the-difference-of-two-arrays/

        Description: Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
        answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
        answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
        Note that the integers in the lists may be returned in any order.
        """
        return [
            list(set([num1 for num1 in nums1 if num1 not in nums2])),
            list(set([num2 for num2 in nums2 if num2 not in nums1]))
        ]
    
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

        Description: Given an array nums of n integers where nums[i] is in the range [1, n], return an array
        of all the integers in the range [1, n] that do not appear in nums.
        """
        num_set = set(nums)
        return [number for number in range(1, len(nums) + 1) if number not in num_set]
    
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/set-mismatch/

        Description: You have a set of integers s, which originally contains all the numbers from 1 to n.
        Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set,
        which results in repetition of one number and loss of another number.
        You are given an integer array nums representing the data status of this set after the error.
        Find the number that occurs twice and the number that is missing and return them in the form of an array.
        """
        desired_list = [i for i in range(1,len(nums)+1)]
        nums_counter = Counter(nums)
        twice_number = [nums_counter.most_common(1)[0][0]]
        missing_number = [number for number in desired_list if number not in nums]
        return twice_number + missing_number

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/maximum-average-subarray-i/

        Description: You are given an integer array nums consisting of n elements, and an integer k.
        Find a contiguous subarray whose length is equal to k that has the maximum average value and return
        this value.
        Any answer with a calculation error less than 10-5 will be accepted.
        """
        n = len(nums)
        if k <= 0 or k > n:
            return 0.0
        # Initial window sum
        window_sum = sum(nums[0:k])
        max_sum = window_sum
        # Slide the window from i=1 to i = n-k
        for i in range(k, n):
            window_sum += nums[i] - nums[i - k]
            if window_sum > max_sum:
                max_sum = window_sum
        # Average = max_sum / k
        return max_sum / k
    
    def findMaxAverageByMe(self, nums: List[int], k: int) -> float:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/maximum-average-subarray-i/

        Description: You are given an integer array nums consisting of n elements, and an integer k.
        Find a contiguous subarray whose length is equal to k that has the maximum average value and return
        this value.
        Any answer with a calculation error less than 10-5 will be accepted.
        
        # this was my first pproach, but it was not efficient
        """
        input_variables = False if not nums or not k else True
        size_fits = False if k < 1 or k > len(nums) else True

        if not input_variables or not size_fits:
            return 0
        
        slice_begin = 0
        slice_end = k
        maximum_average = 0
        while slice_end <= len(nums):
            current_average = sum(nums[slice_begin:slice_end])/k
            if len(nums) == 1 or len(nums) == k:
                return current_average
            maximum_average = current_average if current_average > maximum_average or maximum_average == 0 else maximum_average
            slice_begin += 1
            slice_end += 1
        return maximum_average

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/max-consecutive-ones/

        Description: Given a binary array nums, return the maximum number of consecutive 1's in the array.
        """
        max_ones = [
            sum(1 for _ in group) if key == 1 else 0 for key, group in groupby(nums)]
        return max(max_ones)
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/median-of-two-sorted-arrays/

        Description: Given two sorted arrays nums1 and nums2 of size m and n respectively, return the
        median of the two sorted arrays.
        The overall run time complexity should be O(log (m+n)).
        """
        merged_array = sorted(nums1 + nums2)
        median_value = statistics.median(merged_array)
        return median_value

    def findTheDifference(self, s: str, t: str) -> str:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/find-the-difference/

        Description: You are given two strings s and t.
        String t is generated by random shuffling string s and then add one more letter at a random position.
        Return the letter that was added to t.
        """
        count_s = Counter(s)
        count_t = Counter(t)
        count_diff = count_t - count_s
        return list(count_diff)[0]
    
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/find-words-containing-character/

        Description: You are given a 0-indexed array of strings words and a character x.
        Return an array of indices representing the words that contain the character x.
        Note that the returned array may be in any order.
        """
        words_found = []
        for index, word in enumerate(words):
            if x in word:
                words_found.append(index)
        return words_found
    
    def firstUniqueChar(self, s: str) -> int:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/first-unique-character-in-a-string/

        Description: Given a string s, find the first non-repeating character in it and return its index.
        If it does not exist, return -1.
        """
        for char_index, char in enumerate(s):
            if s.count(char) == 1:
                return char_index
        return -1

    def guessNumber(self, n: int) -> int:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/guess-number-higher-or-lower/

        Description: We are playing the Guess Game. The game is as follows:

        I pick a number from 1 to n. You have to guess which number I picked
        (the number I picked stays the same throughout the game).

        Every time you guess wrong, I will tell you whether the number I picked
        is higher or lower than your guess.

        You call a pre-defined API int guess(int num), which returns three
        possible results:

        -1: Your guess is higher than the number I picked (i.e. num > pick).
        1: Your guess is lower than the number I picked (i.e. num < pick).
        0: your guess is equal to the number I picked (i.e. num == pick).
        Return the number that I picked.

        Example 1:

        Input: n = 10, pick = 6
        Output: 6
        Example 2:

        Input: n = 1, pick = 1
        Output: 1
        Example 3:

        Input: n = 2, pick = 1
        Output: 1
        

        Constraints:

        1 <= n <= 231 - 1
        1 <= pick <= n
        """

        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                right = mid - 1
            else:
                left = mid + 1
        return left
    
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/increasing-triplet-subsequence/

        Description: Given an integer array nums, return true if there exists a triple of
        indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].
        If no such indices exists, return false.
        """
        if len(nums) < 3:
            return False
        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
    
    def isMatch(self, s: str, p: str) -> bool:
        """
        Status: Complete

        Reference: https://leetcode.com/problems/regular-expression-matching/

        Description: Given an input string s and a pattern p, implement regular expression matching
        with support for '.' and '*' where:
        '.' Matches any single character.
        '*' Matches zero or more of the preceding element.
        The matching should cover the entire input string (not partial).
        """
        # dp[i][j] means whether s[:i] matches p[:j]
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True  # empty string matches empty pattern

        # Handle patterns like a*, a*b*, a*b*c* that can match empty string
        for j in range(2, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    # Current chars match
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # Two cases:
                    # 1. '*' means zero occurrence of preceding char
                    dp[i][j] = dp[i][j - 2]
                    # 2. '*' means one or more occurrence of preceding char
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        return dp[len(s)][len(p)]
    
    def isPalindrome(self, x: int) -> bool:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/palindrome-number/

        Description: Given an integer x, return true if x is a palindrome, and false otherwise.
 
        Example 1:

        Input: x = 121
        Output: true
        Explanation: 121 reads as 121 from left to right and from right to left.
        
        Example 2:

        Input: x = -121
        Output: false
        Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is
        not a palindrome.
        
        Example 3:

        Input: x = 10
        Output: false
        Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
        

        Constraints:

        -231 <= x <= 231 - 1

        Follow up challenge: Could you solve it without converting the integer to a string?
        """
        x_as_string = str(x)
        return x_as_string == x_as_string[::-1]

    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/is-subsequence/

        Description: A subsequence of a string is a new string that is formed from the original string
        by deleting some (can be none) of the characters without disturbing the relative
        positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde"
        while "aec" is not).
        """
        if not s:
            return True
        if len(s) > len(t):
            return False

        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
    
        return i == len(s)

    def isValid(self, s: str) -> bool:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/valid-parentheses/

        Description: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine
        if the input string is valid.
        """
        # dictionary of brackets (close: open)
        brackets_dict = {")": "(", "}": "{", "]": "["}
        open_bracket_stack = []
        is_valid = False
        # check input size for odd number of brackets
        if len(s) % 2 != 0:
            return is_valid
        for bracket in s:
            if bracket in brackets_dict.values():
                open_bracket_stack.insert(0, bracket)
                is_valid = False
                continue
            if bracket in brackets_dict.keys():
                match_bracket = brackets_dict.get(bracket)
                if open_bracket_stack and match_bracket == open_bracket_stack[0]:
                    open_bracket_stack.pop(0)
                    is_valid = True
                    continue
                else:
                    return False
        if len(open_bracket_stack) > 0:
            is_valid = False
        return is_valid
    
    def largestAltitude(self, gain: List[int]) -> int:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/find-the-highest-altitude/

        Description: There is a biker going on a road trip. The road trip consists of n + 1 points at
        different altitudes. The biker starts his trip on point 0 with altitude equal 0.

        You are given an integer array gain of length n where gain[i] is the net gain in
        altitude between points i and i + 1 for all (0 <= i < n).
        Return the highest altitude of a point.

        Example 1:

        Input: gain = [-5,1,5,0,-7]
        Output: 1
        Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
        
        Example 2:

        Input: gain = [-4,-3,-2,-1,4,3,2]
        Output: 0
        Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
        """
        if not gain or gain == [0]:
            return 0

        altitude_points = [0]
        index_altitude = index_gain = 0
        while index_altitude < (len(gain) + 1) and index_gain < len(gain):
            new_point = gain[index_gain] + altitude_points[index_altitude]
            altitude_points.append(new_point)
            index_altitude += 1
            index_gain += 1
        return max(altitude_points)
    
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        Status: WORKING...

        Reference: https://leetcode.com/problems/lemonade-change/

        Description: At a lemonade stand, each lemonade costs $5. Customers are standing in a queue
        to buy from you and order one at a time (in the order specified by bills).
        Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.
        You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
        Note that you do not have any change in hand at first.
        Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you
        can provide every customer with the correct change, or false otherwise.
        """
        possible_bills = [5,10,20]
        possible_change_combinations = list(combinations_with_replacement(possible_bills, 2))
        lemonade_cost = 5
        change = []
        change_counter = Counter()
        # --------------------------------------------------------------------------------- #
        print("# --------------------------------------------------------------------------------- #")
        print(f"List of Bills: {bills}")
        for payment in bills:
            payback = payment - lemonade_cost
            print("# --------------------------------------------------------------------------------- #")
            print(f"Payment: {payment}, Payback: {payback}")
            print("# --------------------------------------------------------------------------------- #")
            if payback > sum(change):
                print("#                Not enough change to pay                #")
                return False
            # --------------------------------------------------------------------------------- #
            if payback == 0:
                change.append(payment)
                change_counter.update([payment])
                continue
            # --------------------------------------------------------------------------------- #
            print("# ------------------------------- CHANGE AVAILABLE -------------------------------- #")
            print(f"Change: {change}")
            print(f"Change Sum: {sum(change)}")
            print(f"Counter Elements: {sorted(change_counter.elements())}")
            print(f"Counter Items: {change_counter.items()}")
            print(f"Counter Total: {sum(change_counter.elements())}")
            print("# --------------------------------------------------------------------------------- #")
            if payback in possible_bills:
                change_counter.subtract([payback])
            else:
                print("# ----------------------------- Time to deal with change -------------------------- #")
                possible_change = [Counter(pair) for pair in possible_change_combinations if sum(pair) == payback]
                print(f"Counter Possible Change: {possible_change}")
                print(f"Composite Counter Change Subtract: {possible_change[0].items()}")
                has_payback = possible_change[0] & change_counter
                is_enough = sum(has_payback) >= payback
                print(f"Does Counter has enough bills? {is_enough}")
                change_counter.subtract(possible_change[0])
                print("# --------------------------------------------------------------------------------- #")
            # --------------------------------------------------------------------------------- #
            while payback > 0:
                payback = abs(payback - change[-1])
                change.pop()
            change_counter.update([payment])
            change.append(payment)
            print("# ------------------------------ CHANGE AFTER PAYMENT ---------------------------- #")
            print(f"Change: {change}")
            print(f"Change Sum: {sum(change)}")
            print(f"Counter Elements: {sorted(change_counter.elements())}")
            print(f"Counter Items: {change_counter.items()}")
            print(f"Counter Total: {sum(change_counter.elements())}")
            print("# --------------------------------------------------------------------------------- #")
            # --------------------------------------------------------------------------------- #
        return True
    
    def lengthOfLastWord(self, s: str) -> int:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/length-of-last-word/

        Description: Given a string s consisting of words and spaces, return the length of the last word in the string.
        """
        string_list = s.split()
        return len(string_list[-1])
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Status: WORK IN PROGRESS...
        
        Reference: https://leetcode.com/problems/longest-substring-without-repeating-characters/

        Description: Given a string s, find the length of the longest substring without duplicate characters.

        Example 1:

        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also
        correct answers.

        Example 2:

        Input: s = "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.

        Example 3:

        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
        Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

        Constraints:

        0 <= s.length <= 5 * 104
        s consists of English letters, digits, symbols and spaces.
        """
        pass
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/longest-substring-without-repeating-characters/

        Description: Given a string s, find the length of the longest substring without repeating characters.
        """
        last = {}            # char -> last index seen
        left = 0
        best_len = 0

        for right, ch in enumerate(s):
            if ch in last and last[ch] >= left:
                left = last[ch] + 1
            last[ch] = right

            cur_len = right - left + 1
            if cur_len > best_len:
                best_len = cur_len

        return best_len

    def letterCombinations(self, digits: str) -> List[str]:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

        Description: Given a string containing digits from 2-9 inclusive, return all possible letter
        combinations that the number could represent. Return the answer in any order.
        A mapping of digits to letters (just like on the telephone buttons) is given below.
        Note that 1 does not map to any letters.
        """
        phone_letters = {
            "2": ["abc"],
            "3": ["def"],
            "4": ["ghi"],
            "5": ["jkl"],
            "6": ["mno"],
            "7": ["pqrs"],
            "8": ["tuv"],
            "9": ["wxyz"]
        }
        letter_list = []
        for digit in digits:
            letter_list.extend(phone_letters.get(digit))
        possible_combinations = product(*letter_list)
        letter_combinations = ["".join(letter_combination) for letter_combination in list(possible_combinations)]
        return letter_combinations
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Status: Complete

        Reference: https://leetcode.com/problems/longest-common-prefix/

        Description: Write a function to find the longest common prefix string amongst an array of strings.
        If there is no common prefix, return an empty string "".
        """
        return os.path.commonprefix(strs)
    
    def longestPalindrome(self, s: str) -> str:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/longest-palindromic-substring/

        Description: Given a string s, return the longest palindromic substring in s.
        """
        n = len(s)
        start, maxLen = 0, 1

        for i in range(n):
            # this runs two times for both odd and even 
            # length palindromes. 
            # j = 0 means odd and j = 1 means even length
            for j in range(2):
                low, high = i, i + j
                # expand substring while it is a palindrome
                # and in bounds
                while low >= 0 and high < n and s[low] == s[high]:
                    currLen = high - low + 1
                    if currLen > maxLen:
                        start = low
                        maxLen = currLen
                    low -= 1
                    high += 1

        return s[start:start + maxLen]

    def majorityElement(self, nums: List[int]) -> int:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/majority-element/

        Description: Given an array nums of size n, return the majority element.
        """
        count_elements = Counter(nums)
        return count_elements.most_common(1)[0][0]

    def maxFreqSum(self, s: str) -> int:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/maximum-frequency-sum-of-a-string-after-modifying/ 

        Description: You are given a string s and a positive integer k.
        Select a set of non-overlapping substrings from the string s that satisfy the following conditions:
        The length of each substring is at least k.
        Each substring is a palindrome.
        Return the maximum number of substrings in an optimal selection.
        """
        vowels = "aeiou"
        vowel_count = [s.count(vowel) for vowel in vowels]
        consonant_count = [s.count(letter) if letter not in vowels else 0 for letter in s]
        return max(vowel_count) + max(consonant_count)
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/merge-sorted-array/

        Description: You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
        and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1[:m] + nums2[:n]
        nums1.sort()

    def missingNumber(self, nums: List[int]) -> int:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/missing-number/

        Description: Given an array nums containing n distinct numbers in the range [0, n],
        return the only number in the range that is missing from the array.
        """
        n = len(nums) + 1
        # Find the number not in the nums list
        missing_number = [
            range_number for range_number in range(n) if range_number not in nums
        ]
        return missing_number[0]
    
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/most-common-word/

        Description: Given a string paragraph and a string array of the banned words banned, return the most
        frequent word that is not banned.
        It is guaranteed there is at least one word that is not banned, and that the answer is unique.
        """
        symbols_to_remove = "!?',;."
        clean_paragraph = paragraph.translate({ord(word): " " for word in symbols_to_remove})
        split_words = clean_paragraph.lower().split()
        not_banned_words = [word for word in split_words if word not in banned]
        count_words = Counter(not_banned_words)
        return count_words.most_common(1)[0][0]
    
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/move-zeroes/

        Description: Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        
        zero_counter = nums.count(0)
        if zero_counter < 1:
            return

        for _ in range(0, zero_counter):
            nums.remove(0)

        nums.extend([0]*zero_counter)
    
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/find-smallest-letter-greater-than-target/

        Description: Given a sorted array of characters letters and a character target, return the smallest
        character in letters that is lexicographically greater than target.
        If such a character does not exist, return the first character in letters.
        """
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        target_start = alphabet.index(target)
        greater_letter = [value_letter for value_letter in letters if alphabet.index(value_letter)>target_start]
        if not greater_letter or target_start > alphabet.index(letters[-1]):
            return letters[0]
        return greater_letter[0]

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/number-of-equivalent-domino-pairs/

        Description: Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and
        only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal
        to another domino.
        Return the number of pairs (i, j) (0 <= i < j < dominoes.length) for which dominoes[i] and dominoes[j] are
        equivalent.
        """
        counts = defaultdict(int)
        pairs = 0
        
        for a, b in dominoes:
            key = min(a, b) * 10 + max(a, b)
            pairs += counts[key]
            counts[key] += 1
        
        return pairs
    
    def numEquivDominoPairsByMe(self, dominoes: List[List[int]]) -> int:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/number-of-equivalent-domino-pairs/

        Description: Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and
        only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal
        to another domino.
        Return the number of pairs (i, j) (0 <= i < j < dominoes.length) for which dominoes[i] and dominoes[j] are
        equivalent.
        """
        dominoes_left = 0
        dominoes_right = 1
        number_of_pairs = 0

        while dominoes_right < len(dominoes):
            equal_dominos = dominoes[dominoes_left] == dominoes[dominoes_right]
            reversed_equals = dominoes[dominoes_left] == dominoes[dominoes_right][::-1]
            if equal_dominos or reversed_equals:
                number_of_pairs += 1
            dominoes_right += 1
            if dominoes_right == len(dominoes):
                dominoes_left += 1
                dominoes_right = dominoes_left + 1
        return number_of_pairs
    
    def pivotIndex(self, nums: List[int]) -> int:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/find-pivot-index/

        Description: Given an array of integers nums, calculate the pivot index of this array.

        The pivot index is the index where the sum of all the numbers strictly to the
        left of the index is equal to the sum of all the numbers strictly to the
        index's right.

        If the index is on the left edge of the array, then the left sum is 0 because
        there are no elements to the left. This also applies to the right edge of the
        array.

        Return the leftmost pivot index. If no such index exists, return -1.

        Example 1:

        Input: nums = [1,7,3,6,5,6]
        Output: 3
        Explanation:
        The pivot index is 3.
        Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
        Right sum = nums[4] + nums[5] = 5 + 6 = 11

        Example 2:

        Input: nums = [1,2,3]
        Output: -1
        Explanation:
        There is no index that satisfies the conditions in the problem statement.

        Example 3:

        Input: nums = [2,1,-1]
        Output: 0
        Explanation:

        The pivot index is 0.
        Left sum = 0 (no elements to the left of index 0)
        Right sum = nums[1] + nums[2] = 1 + -1 = 0

        Constraints:

        1 <= nums.length <= 104
        -1000 <= nums[i] <= 1000
        """
        left_sum = 0
        right_sum = 0
        no_index = -1

        if not nums or len(nums) == 0:
            return no_index
        
        if len(nums) == 1:
            return 0

        for index, num in enumerate(nums):
            left_sum += num
            right_sum = sum(nums[index:])
            if left_sum == right_sum:
                return index
            
        return no_index

    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/plus-one/

        Description: You are given a large integer represented as an integer array digits, where each digits[i] is
        the ith digit of the integer.
        The digits are ordered from most significant to least significant in left-to-right order.
        The large integer does not contain any leading 0's.
        """
        full_integer = int("".join(str(digit) for digit in digits))
        full_integer_plus_one = full_integer + 1
        digits_list_after = [int(int_plus) for int_plus in str(full_integer_plus_one)]
        return digits_list_after
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/product-of-array-except-self/

        Description: Given an integer array nums, return an array answer such that answer[i] is equal to the product
        of all the elements of nums except nums[i].
        """
        n = len(nums)
        res = [1] * n

        # Prefix pass
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # Suffix pass
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
    
    def removeAnagrams(self, words: List[str]) -> List[str]:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/remove-anagrams/

        Description: You are given a 0-indexed string array words, where words[i] consists of lowercase English letters.
        In one operation, select any index i such that 0 < i < words.length and words[i - 1] and words[i]
        are anagrams, and delete words[i] from words.
        Keep performing this operation as long as you can select an index that satisfies the conditions.

        Return words after performing all operations. It can be shown that selecting the indices for each
        operation in any arbitrary order will lead to the same result.

        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase
        using all the original letters exactly once. For example, "dacb" is an anagram of "abdc".

        Example 1:

        Input: words = ["abba","baba","bbaa","cd","cd"]
        Output: ["abba","cd"]
        Explanation:
        One of the ways we can obtain the resultant array is by using the following operations:
            - Since words[2] = "bbaa" and words[1] = "baba" are anagrams, we choose index 2 and delete words[2].
        Now words = ["abba","baba","cd","cd"].
            - Since words[1] = "baba" and words[0] = "abba" are anagrams, we choose index 1 and delete words[1].
        Now words = ["abba","cd","cd"].
            - Since words[2] = "cd" and words[1] = "cd" are anagrams, we choose index 2 and delete words[2].
        Now words = ["abba","cd"].
        We can no longer perform any operations, so ["abba","cd"] is the final answer.
        
        Example 2:

        Input: words = ["a","b","c","d","e"]
        Output: ["a","b","c","d","e"]
        Explanation:
            - No two adjacent strings in words are anagrams of each other, so no operations are performed.
 

        Constraints:

        1 <= words.length <= 100
        1 <= words[i].length <= 10
        words[i] consists of lowercase English letters.
        """
        if len(words) <= 1:
            return words

        can_select_index = True

        while can_select_index:
            for index in range(1, len(words)):
                if sorted(words[index]) == sorted(words[index - 1]):
                    words.pop(index)
                    break
            else:
                can_select_index = False
        
        return words

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

        Description: Given a sorted array nums, remove the duplicates in-place such that each element appears only once
        and returns the new length.
        """
        unique_numbers = []
        for number in nums:
            if number not in unique_numbers:
                unique_numbers.append(number)
        nums[:] = unique_numbers
        return len(unique_numbers)

    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/remove-element/

        Description: Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
        The order of the elements may be changed.
        Then return the number of elements in nums which are not equal to val.
        """
        nums[:] = [num for num in nums if num != val]
        return len(nums)
    
    def reverse(self, x: int) -> int:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/reverse-integer/

        Description: Given a signed 32-bit integer x, return x with its digits reversed.
        If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1],
        then return 0.
        Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
        """
        org = x
        x = abs(x)
        res = int(str(x)[::-1])
        if org < 0:
            res *= -1
        if res < -(1 << 31) or res > (1 << 31) - 1:
            return 0
        return res
    
    def reverseList(self, head: Optional[SinglyLinkedList]) -> Optional[SinglyLinkedList]:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/reverse-linked-list/

        Description: Given the head of a singly linked list, reverse the list, and return the reversed list.
        """
        current_value = head
        previous_value = None

        # Iteratively run the nodes of the singly linked List
        while current_value is not None:

            # store next value
            next_node = current_value.next

            # reverse current node's next pointer
            current_value.next = previous_value

            # move pointers one position ahead
            previous_value = current_value
            current_value = next_node

        return previous_value
        
    def reverseString(self, s: List[str]) -> None:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/reverse-string/

        Description: Write a function that reverses a string.
        The input string is given as an array of characters s.
        Do not return anything, modify s in-place instead.
        """
        return s.reverse()

    def reverseWords(self, s: str) -> str:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/reverse-words-in-a-string-iii/

        Description: Given a string s, reverse the order of characters in each word within a
        sentence while still preserving whitespace and initial word order.
        """
        splited_words = s.split()
        reverse_words = list(map(lambda word: word[::-1],splited_words))
        return " ".join(reverse_words)
    
    def rotateString(self, s: str, goal: str) -> bool:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/rotate-string/

        Description: Given two strings s and goal, return true if and only if s can become goal after some
        number of shifts on s.
        A shift on s consists of moving the leftmost character of s to the rightmost position.
        """
        for _ in range(0,len(s)):
            s = s.removeprefix(s[0]) + s[0]
            if s == goal:
                return True
        return False
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/search-insert-position/

        Description: Given a sorted array of distinct integers and a target value, return the index if the target is found.
        If not, return the index where it would be if it were inserted in order.
        """
        insert_index = 0
        try:
            return nums.index(target)
        except ValueError:
            nums_size = len(nums)
            left, right = 0, nums_size
            while left < right:
                if target < nums[left]:
                    return left
                if target > nums[nums_size -1]:
                    return nums_size
                if target > nums[left] and target < nums[left+1]:
                    return left+1
                left += 1

    def singleNumber(self, nums: List[int]) -> int:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/single-number/

        Description: Given a non-empty array of integers nums, every element appears twice except for one.
        Find that single one.
        """
        return 2 * sum(set(nums)) - sum(nums)

    def strStr(self, haystack: str, needle: str) -> int:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

        Description: Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
        or -1 if needle is not part of haystack.
        """
        return haystack.find(needle)
    
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

        Description: You are given two positive integer arrays spells and potions, of length n and m respectively,
        where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.
        """
        # Sort potions for binary search
        potions.sort()
        successful_spells = []
        
        for spell in spells:
            # Calculate minimum potion strength needed
            min_potion_strength = (success + spell - 1) // spell  # Ceiling division
            
            # Binary search for first potion >= min_potion_strength
            left, right = 0, len(potions)
            while left < right:
                mid = (left + right) // 2
                if potions[mid] < min_potion_strength:
                    left = mid + 1
                else:
                    right = mid
            
            # All potions from left to end are successful
            successful_spells.append(len(potions) - left)
    
        return successful_spells

    def successfulPairsFirstVersion(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

        Description: You are given two positive integer arrays spells and potions, of length n and m respectively,
        where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.
        """
        successful_spells = []
        for spell in spells:
            conjured_spells = []
            conjured_spells = [spell * potion for potion in potions if spell * potion >= success]
            successful_spells.append(len(conjured_spells))
        return successful_spells

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Status: Complete

        Reference: https://leetcode.com/problems/3sum/

        Description: Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
        such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
        Notice that the solution set must not contain duplicate triplets.
        """
        nums.sort()
        n = len(nums)
        res: List[List[int]] = []

        for i in range(n - 2):
            # skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            left, right = i + 1, n - 1

            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    res.append([nums[i], nums[left], nums[right]])
                    # advance left and right past duplicates
                    left_val, right_val = nums[left], nums[right]
                    while left < right and nums[left] == left_val:
                        left += 1
                    while left < right and nums[right] == right_val:
                        right -= 1
                elif s < target:
                    left += 1
                else:
                    right -= 1
        return res

    def toGoatLatin(self, sentence: str) -> str:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/goat-latin/

        Description: You are given a string sentence that consist of words separated by spaces.
        Each word consists of lowercase and uppercase letters only.
        We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)
        The rules of Goat Latin are as follows:
        If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
        For example, the word "apple" becomes "applema".
        If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add "ma".
        For example, the word "goat" becomes "oatgma".
        Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
        For example, the first word gets "a" added to the end, the second word gets "aa" added to the end, and so on.
        Return the final sentence representing the conversion from sentence to Goat Latin.
        """
        vowels = ("a", "e", "i", "o", "u")
        split_sentence = sentence.split()
        converted_sentence = []
        for index, word in enumerate(split_sentence):
            if word.lower().startswith(vowels):
                word = word + "ma" + ("a" * (index + 1))
            else:
                word = word[1::] + word[0] + "ma" + ("a" * (index + 1))
            split_sentence[index] = word
        return " ".join(split_sentence)

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/two-sum/

        Description: Given an array of integers nums and an integer target, return indices of the
        two numbers such that they add up to target.

        You may assume that each input would have exactly one solution, and you may not
        use the same element twice.

        You can return the answer in any order.

        Example 1:

        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
        Example 2:

        Input: nums = [3,2,4], target = 6
        Output: [1,2]
        Example 3:

        Input: nums = [3,3], target = 6
        Output: [0,1]

        Constraints:

        2 <= nums.length <= 104
        -109 <= nums[i] <= 109
        -109 <= target <= 109
        Only one valid answer exists.

        Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
        """
        answer_was_found = False
        index_num1 = 0
        index_num2 = 1
        while not answer_was_found:
            if nums[index_num1] + nums[index_num2] == target:
                answer_was_found = True
                return [index_num1,index_num2]
            index_num2 += 1
            if index_num2 == len(nums):
                index_num1 += 1
                index_num2 = index_num1 + 1

    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/uncommon-words-from-two-sentences/

        Description: A sentence is a string of single-space separated words where each word consists only of lowercase letters.
        A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
        Given two sentences s1 and s2, return a list of all the uncommon words.
        You may return the answer in any order.
        """
        s1_word_list = s1.split()
        s2_word_list = s2.split()
        set_s1 = set(s1_word_list)
        set_s2 = set(s2_word_list)
        diff_word_list = list(set_s1 ^ set_s2)
        uncommon_words = [
            word for word in diff_word_list 
            if s1_word_list.count(word) <= 1 and s2_word_list.count(word) <=1
        ]
        return uncommon_words

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/unique-number-of-occurrences/

        Description: Given an array of integers arr, return true if the number of occurrences of each value in the
        array is unique or false otherwise.
        """
        uniques_list = set(arr)
        uniques_count = Counter(item for item in arr if isinstance(item, int))
        uniques_occurrences = set(uniques_count.values())
        return len(uniques_occurrences) == len(uniques_list)

    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Status: COMPLETE

        Reference: https://leetcode.com/problems/word-pattern/

        Description: Given a pattern and a string s, determine if s follows the same pattern.
        A bijection exists if each character in pattern maps to exactly one word in s, and vice versa.
        """
        string_list = s.split()
        pattern_list = list(pattern)
        unique_pattern = list(dict.fromkeys(pattern_list))
        unique_string = list(dict.fromkeys(string_list))
        unique_matches = list(zip_longest(unique_pattern, unique_string))
        matches = list(zip(pattern_list, string_list))
        for match in matches:
            if match not in unique_matches:
                return False
        return True
