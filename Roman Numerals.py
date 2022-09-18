from ast import Str


class Roman:
    # Allow the text to be inputted in the print command
    def RomanNumerals(self, s):
        # Initialize a dictionary with the values corresponding to each letter
        numerals = {'I': 1, 'V': 5, 'X': 10,
                    'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        WordValue = 0
        # Length of the for loop is the inputted value
        for i in range(len(s)):
            if i > 0 and numerals[s[i]] > numerals[s[i-1]]:
                WordValue += numerals[s[i]] - 2 * numerals[s[i-1]]
            else:
                WordValue += numerals[s[i]]

        return WordValue


print(Roman().RomanNumerals('MMCMX'))
