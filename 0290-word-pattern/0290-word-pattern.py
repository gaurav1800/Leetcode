class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        array = s.split()

        if len(array) != len(pattern):
            return False

        char_to_word = {}
        word_to_char = {}

        for c, word in zip(pattern, array):
            if c in char_to_word and char_to_word[c] != word:
                return False
            if word in word_to_char and word_to_char[word] != c:
                return False
            char_to_word[c] = word
            word_to_char[word] = c
        
        return True

        