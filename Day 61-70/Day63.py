# https://www.geeksforgeeks.org/problems/pangram-checking-1587115620/1


class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        #code here
        alphabet = set("abcdefghijklmnopqrstuvwxyz")
        # Convert the input sentence to lowercase and remove non-alphabetic characters
        cleaned_sentence = ''.join(char.lower() for char in s if char.isalpha())
        # Check if the set of unique characters in the cleaned sentence is equal to the alphabet set
        return set(cleaned_sentence) == alphabet
