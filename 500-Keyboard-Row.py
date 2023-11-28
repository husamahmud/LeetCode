class Solution(object):
    def findWords(self, words):
        row1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        row2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        row3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        valid_words = []

        for word in words:
            lowercase_word = word.lower()

            if lowercase_word[0].lower() in row1:
                valid_word = True
                for c in lowercase_word[1:]:
                    if c not in row1:
                        valid_word = False
                        pass
                if valid_word:
                    valid_words.append(word)
            elif lowercase_word[0].lower() in row2:
                valid_word = True
                for c in lowercase_word[1:]:
                    if c not in row2:
                        valid_word = False
                        pass
                if valid_word:
                    valid_words.append(word)
            elif lowercase_word[0].lower() in row3:
                valid_word = True
                for c in lowercase_word[1:]:
                    if c not in row3:
                        valid_word = False
                        pass
                if valid_word:
                    valid_words.append(word)
        return valid_words
