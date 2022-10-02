# Given a string s consisting of words and spaces
# Return the length of the last word
# Word is a maximal substring consisting of non-space characters only

# Example1
#s = "Hello World"
#Output = 5


class Solution():
    def lengthOfLastWord(self, s):
        # Have i start at the back of the list instead of the front
        # This will allow it to skip possible white space first then iterate over the first word
        i = len(s) - 1
        count = 0

        # if there is whitespace at the beginning of the input move the pointer through it
        while s[i] == " ":
            i -= 1

        # Increase the count by 1 if the string still has characters and if there is no blank space
        # if a blank space happens end the loop and return the count
        while i > 0 and s[i] != " ":
            count += 1
        return count


print(Solution().lengthOfLastWord(["Hello World"]))
