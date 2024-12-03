class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        current_word = 1
        curr_ind = 0
        l_sen = len(sentence)
        while curr_ind <  l_sen:
            while curr_ind < l_sen and sentence[curr_ind] == " ":
                curr_ind +=1
                current_word +=1

            match = 0
            while curr_ind < l_sen and match<len(searchWord) and sentence[curr_ind] == searchWord[match]:
                curr_ind += 1
                match += 1

            if match == len(searchWord):
                return current_word
            while curr_ind < l_sen and sentence[curr_ind] != " ":
                curr_ind +=1

        return -1



        
