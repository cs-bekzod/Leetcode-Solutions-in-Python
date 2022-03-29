class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.upper() == word or word.lower() == word or (word[0].upper() == word[0] and word[1:] == word[1:].lower()):
            return True
        return False