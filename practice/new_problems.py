# Given two sorted lists, return the interesection (ie the common elements b/w the two sorted lists)
# For example given l1 = [1, 2, 3] and l2 = [2, 3, 5, 10] (they can be different sizes)
# return [2, 3]
# LINEAR TIME
# 4
def get_intersection(l1, l2):
    pass

# given two sorted lists l1 and l2, merge them such that the result is also sorted
# use no helper methods
# For example given l1 = [1, 2, 3] and l2 = [2, 3, 5, 10] (they can be different sizes)
# return [1, 2, 2, 3, 3, 5, 10]
# return [1, 2, 3, 5, 10]
# LINEAR TIME
# 5
def merge(l1, l2):
    pass

# return true iff the string has a repeated substring.
# for example: "I ate not so late today" has a repeated substring ate. So it would return true for that
# but if I gave "Have not eaten", it would return false.
# 3
def has_repeated_substring(s):
    pass

# Given a string s, and an index i, return the index of the
# space, or end of string, that terminates the word starting at s[i]. For example given
# s = "monkey ate my banana", i = 0, returns 6. And i = 14 (returns 20)
# 1
def find_word_boundary(s, i):
    pass

# Given a string s that has single-space separated words like "I am a fool"
# Print the words in order, with their characters reversed
# Try not to use any helper methods like split
# For example, the result for "I am a fool" would be "I ma a loof"
# You may consider using the above helper method find_word_boundary
# 2
def reverse_words_in_list(s):
    pass


# Given a 2D array board, that represents a square board of size n
# find if its a winning combination
# ie, that there is either a horizontal, vertical or any of the two diagnols are streams of 1 or 0
# example:
# board[0] = [1, 0, 0], board[1] = [0, 1, 0], board[2] = [0, 0, 1]
# and you call this method with board and n = 3, then it would return true (because there is a diagnol streak of 1)
# 0
def is_winning(board, n):
    pass




# Find two indices i, j in the list (that may be the same) such that l[i] + l[j] == n
# Return that as a tuple
def find_two_nums_summing(l, n):
   pass

# Print the first n fibonacci numbers.
# The numbers are defined as:
# a_1 = 1
# a_2 = 1
# a_n = a_{n-1} + a_{n-2}
def fibonacci(n):
    pass

# a is a 2D matrix (array of arrays). Return true iff n exists in a
def find_element_in_matrix(a, n):
    pass

# Check if the substring sub exists in s. For example, find_substring("hello buffalo", "o b") == True
def find_substring(s, sub):
    pass

# is a string containing just '(' or ')'. For example it could be ((())) or (()()()) or ((() or )(()
# Check if the string contains 'matched' paranthesis (matched as in it would be mathematically correct use of paranthesis). For example the last two examples aren't matched
# Hint: Use the list methods append and pop. You can also read about "Stack datastructure" online
def is_paranthesis_matched(s):
    pass

