from typing import List, Optional
from collections import Counter
from studies.leet_code.python.list_node import ListNode


class Problems:
    """ Solutions for LeetCode problems. """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Status: COMPLETE
        Ref: https://leetcode.com/problems/product-of-array-except-self/
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
    
    def compress(self, chars: List[str]) -> int:
        """
        Status: COMPLETE
        Ref: https://leetcode.com/problems/string-compression/
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
        Ref: https://leetcode.com/problems/string-compression/
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

    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        Status: COMPLETE
        Ref: https://leetcode.com/problems/increasing-triplet-subsequence/
        Description:
        Given an integer array nums, return true if there exists a triple of
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
    
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Status: COMPLETE
        Ref:
        Description:
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        
        zero_counter = nums.count(0)
        if zero_counter < 1:
            return

        for _ in range(0, zero_counter):
            nums.remove(0)

        nums.extend([0]*zero_counter)
    
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Status: COMPLETE
        Ref: https://leetcode.com/problems/is-subsequence/
        Description:
        A subsequence of a string is a new string that is formed from the original string
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

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Status: WORK IN PROGRESS...
        Ref: https://leetcode.com/problems/longest-substring-without-repeating-characters/
        Description:
        Given a string s, find the length of the longest substring without duplicate characters.

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
    
    def largestAltitude(self, gain: List[int]) -> int:
        """
        Status: COMPLETE
        Ref: https://leetcode.com/problems/find-the-highest-altitude/
        Description:
        There is a biker going on a road trip. The road trip consists of n + 1 points at
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
    
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        """
        Status: COMPLETE
        Ref: https://leetcode.com/problems/find-the-difference-of-two-arrays/
        """
        return [
            list(set([num1 for num1 in nums1 if num1 not in nums2])),
            list(set([num2 for num2 in nums2 if num2 not in nums1]))
        ]
    
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
        Status: COMPLETE
        Ref: https://leetcode.com/problems/unique-number-of-occurrences/
        """
        uniques_list = set(arr)
        uniques_count = Counter(item for item in arr if isinstance(item, int))
        uniques_occurrences = set(uniques_count.values())
        return len(uniques_occurrences) == len(uniques_list)

    def singleNumber(self, nums: List[int]) -> int:
        """
        Status: COMPLETE
        Ref: https://leetcode.com/problems/single-number/
        """
        return 2 * sum(set(nums)) - sum(nums)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Status: COMPLETE
        Ref: https://leetcode.com/problems/reverse-linked-list/
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
        
    def pivotIndex(self, nums: List[int]) -> int:
        """
        Status: COMPLETE
        Ref: https://leetcode.com/problems/find-pivot-index/
        Description:
        Given an array of integers nums, calculate the pivot index of this array.

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

    def findMaxAverageByMe(self, nums: List[int], k: int) -> float:
        """
        Status: COMPLETE
        Ref:
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

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Status: COMPLETE
        Ref:
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
    
    def guessNumber(self, n: int) -> int:
        """
        Status: COMPLETE
        Ref: https://leetcode.com/problems/guess-number-higher-or-lower/
        Description:
        We are playing the Guess Game. The game is as follows:

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
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Status: COMPLETE
        Ref: https://leetcode.com/problems/two-sum/
        Description:
        Given an array of integers nums and an integer target, return indices of the
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

    def maxFreqSum(self, s: str) -> int:
        """
        Status: COMPLETE
        Ref: https://leetcode.com/problems/maximum-frequency-sum-of-a-string-after-modifying/ 
        """
        vowels = "aeiou"
        vowel_count = [s.count(vowel) for vowel in vowels]
        consonant_count = [s.count(letter) if letter not in vowels else 0 for letter in s]
        return max(vowel_count) + max(consonant_count)
    
    def numEquivDominoPairsByMe(self, dominoes: List[List[int]]) -> int:
        """
        Status: COMPLETE
        Ref: https://leetcode.com/problems/number-of-equivalent-domino-pairs/ 
        """
        dominoes_left = 0
        dominoes_right = 1
        number_of_pairs = 0
        seen_dominoes = {}
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
    
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        """
        Status: COMPLETE
        Ref:
        """
        counts = defaultdict(int)
        pairs = 0
        
        for a, b in dominoes:
            key = min(a, b) * 10 + max(a, b)
            pairs += counts[key]
            counts[key] += 1
        
        return pairs
    
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        """
        Status: COMPLETE
        Ref: https://leetcode.com/problems/find-words-containing-character/
        """
        words_found = []
        for index, word in enumerate(words):
            if x in word:
                words_found.append(index)
        return words_found
    
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        """
        Status: COMPLETE
        Ref: https://leetcode.com/problems/maximum-frequency-sum-of-a-string-after-modifying/ 
        """
        splited_words = text.split(" ")
        broken_letters = list(brokenLetters)
        can_be_typed_words = len(splited_words)
        for broken_letter in broken_letters:
            if broken_letter in text:
                can_be_typed_words -= text.count(broken_letter)
        return can_be_typed_words
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Status: COMPLETE
        Ref: https://leetcode.com/problems/add-two-numbers/
        Description:
        You are given two non-empty linked lists representing two non-negative integers. The digits are
        stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and
        return the sum as a linked list.

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
        # Base case: empty list or single node
        # Base case: empty list or single node
        if l1 is None:
            return l1
        if l2 is None:
            return l2
        
        # Recursive case: add the two numbers
        l1.val += l2.val
        if l1.val > 9:
            rest_value = l1.val - 9
            l1.val = l1.val - 10
            if l2.next:
                l2.next.val += rest_value
        l1.next = self.addTwoNumbers(l1.next, l2.next)
        return l1
    
    def removeAnagrams(self, words: List[str]) -> List[str]:
        """
        Status: COMPLETE
        Ref: https://leetcode.com/problems/remove-anagrams/
        Description:
        You are given a 0-indexed string array words, where words[i] consists of lowercase English letters.
        In one operation, select any index i such that 0 < i < words.length and words[i - 1] and words[i]
        are anagrams, and delete words[i] from words. Keep performing this operation as long as you can
        select an index that satisfies the conditions.

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

    def isPalindrome(self, x: int) -> bool:
        """
        Status: COMPLETE
        Ref: https://leetcode.com/problems/palindrome-number/

        Given an integer x, return true if x is a palindrome, and false otherwise.
 
        Example 1:

        Input: x = 121
        Output: true
        Explanation: 121 reads as 121 from left to right and from right to left.
        
        Example 2:

        Input: x = -121
        Output: false
        Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
        
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

    def addBinary(self, a: str, b: str) -> str:
        """
        Status: COMPLETE
        Ref: https://leetcode.com/problems/add-binary/
        
        Given two binary strings a and b, return their sum as a binary string.
        
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
    
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        """
        Status: COMPLETE
        Ref: https://leetcode.com/problems/construct-transformed-array/
        """
        ct_index = 0
        nums_size = len(nums)
        result = []
        while ct_index < nums_size:
            array_value = nums[ct_index]
            result.append(nums[(ct_index + array_value) % nums_size])
            ct_index += 1
        return result
    
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """
        Status: COMPLETE
        Ref: https://leetcode.com/problems/find-smallest-letter-greater-than-target/
        """
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        target_start = alphabet.index(target)
        greater_letter = [value_letter for value_letter in letters if alphabet.index(value_letter)>target_start]
        if not greater_letter or target_start > alphabet.index(letters[-1]):
            return letters[0]
        return greater_letter[0]

    def compareVersion(self, version1: str, version2: str) -> int:
        """
        Status: COMPLETE
        ref: https://leetcode.com/problems/compare-version-numbers/
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
    
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        """
        Status: COMPLETE
        ref: https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
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
        ref: https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
        """
        successful_spells = []
        for spell in spells:
            conjured_spells = []
            conjured_spells = [spell * potion for potion in potions if spell * potion >= success]
            successful_spells.append(len(conjured_spells))
        return successful_spells

    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Status: COMPLETE
        ref: https://leetcode.com/problems/remove-element/
        """
        nums[:] = [num for num in nums if num != val]
        return len(nums)
    
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Status: COMPLETE
        ref: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
        """
        return haystack.find(needle)
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Status: COMPLETE
        ref: https://leetcode.com/problems/search-insert-position/
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

    def lengthOfLastWord(self, s: str) -> int:
        """
        Status: COMPLETE
        ref: https://leetcode.com/problems/length-of-last-word/
        """
        string_list = s.split()
        return len(string_list[-1])
    
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Status: COMPLETE
        ref: https://leetcode.com/problems/plus-one/
        """
        full_integer = int("".join(str(digit) for digit in digits))
        full_integer_plus_one = full_integer + 1
        digits_list_after = [int(int_plus) for int_plus in str(full_integer_plus_one)]
        return digits_list_after
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Status: COMPLETE
        ref: https://leetcode.com/problems/merge-sorted-array/
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1[:m] + nums2[:n]
        nums1.sort()

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Status: COMPLETE
        ref: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
        """
        unique_numbers = []
        for number in nums:
            if number not in unique_numbers:
                unique_numbers.append(number)
        nums[:] = unique_numbers
        return len(unique_numbers)

    def isValid(self, s: str) -> bool:
        """
        Status: COMPLETE
        Ref: https://leetcode.com/problems/valid-parentheses/
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
    
    def majorityElement(self, nums: List[int]) -> int:
        """
        Status: COMPLETE
        Ref: https://leetcode.com/problems/majority-element/
        """
        count_elements = Counter(nums)
        return count_elements.most_common(1)[0][0]

    def missingNumber(self, nums: List[int]) -> int:
        """
        Status: COMPLETE
        Ref: https://leetcode.com/problems/missing-number/
        """
        n = len(nums) + 1
        # Find the number not in the nums list
        missing_number = [
            range_number for range_number in range(n) if range_number not in nums
        ]
        return missing_number[0]
    
    def reverseString(self, s: List[str]) -> None:
        """
        Status: COMPLETE
        Ref: https://leetcode.com/problems/reverse-string/
        
        Do not return anything, modify s in-place instead.
        """
        return s.reverse()

    def countSegments(self, s: str) -> int:
        """
        Status: COMPLETE
        Ref: https://leetcode.com/problems/number-of-segments-in-a-string/
        """
        string_list = s.split()
        return len(string_list)
    
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        """
        Status: COMPLETE
        Ref: https://leetcode.com/problems/most-common-word/
        """
        symbols_to_remove = "!?',;."
        clean_paragraph = paragraph.translate({ord(word): " " for word in symbols_to_remove})
        split_words = clean_paragraph.lower().split()
        not_banned_words = [word for word in split_words if word not in banned]
        count_words = Counter(not_banned_words)
        return count_words.most_common(1)[0][0]
    
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Status: COMPLETE
        Ref: https://leetcode.com/problems/ransom-note/
        """
        for ransom_word in ransomNote:
            if ransom_word in magazine:
                magazine = magazine.replace(ransom_word, "", 1)
                continue
            else:
                return False
        return True
