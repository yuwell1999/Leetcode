class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        dict = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
                ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        set = {"".join
               (dict[ord(c) - ord('a')] for c in word)
               for word in words
               }

        return len(set)
