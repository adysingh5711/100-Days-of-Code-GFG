#https://www.geeksforgeeks.org/problems/wildcard-string-matching1126/1


import re

class Solution:
    def match(self, wildcard, text_to_match):
        # Convert the wildcard pattern to a regular expression pattern
        regex_pattern = '^' + wildcard.replace('?', '.').replace('*', '.*') + '$'

        # Use re.fullmatch to check if the entire text matches the regular expression pattern
        return True if re.fullmatch(regex_pattern, text_to_match) else False
