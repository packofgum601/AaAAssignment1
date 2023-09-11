from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary
import bisect
from timeit import default_timer as timer


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class ArrayDictionary(BaseDictionary):

    def __init__(self, data = []):
        # TO BE IMPLEMENTED
        self.data = data


    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # TO BE IMPLEMENTED
        
        #sort the word frequencies by word

        self.data = words_frequencies
        self.data.sort(key=lambda y: y.word[0])



    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # TO BE IMPLEMENTED


        found = False #if the word has been found
                
        for search in self.data: #iterate over array 
            if word == search.word: #if the word has been found
        #change found to equal true, and return the frequency
                found = True 
                return search.frequency
        if found != True: #if the word is not in the dictionary
            return 0 #return 0

        print("Time to search: ", end - start)
        
        
                

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # TO BE IMPLEMENTED
        
        '''iterate over array
        if the word is already in the dictionary:
            return false, as we do not need to add it to the dictionary
        if after the loop, found is still false:
            append the list to contain the word and resort the list
            return True '''
            


        found = False #if the word has been found
        
        for word in self.data: #iterate over the array
            if word_frequency == word.word: #if the word has been found
                #change found to true and return False, as we do not need to add it to the dictionary
                found = True
 
                return False
        if found != True: #if the word is not in the dictionary
            #add the word to the dictionary and re-sort the list
            #return True
            self.data.append(word_frequency)
            self.data.sort(key=lambda y: y.word[0])

            return True
        
    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        
        # TO BE IMPLEMENTED

        found = False #if the word has been found
        count = 0 
        
        for w in self.data: #iterate over the array
            if word == w.word: #if the word has been found
                self.data.remove(self.data[count]) #remove the word from the dictionary
                found = True #change found to true
                return True
            count += 1
        if found != True: #if the word is not in the dictionary
            return False #return False
        
            
                


    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """

        
        alist = [] #autocomplete list
        for word in self.data: # iterate over the array
            if word.word.startswith(prefix_word): #if the word starts with prefux_word
                #append alist with word
                alist.append(word)
        
        #sort list by frequency then reverse it so the largest frequency is first
        alist.sort(key = lambda y: y.frequency, reverse=True)
        
        #if the list is larger than 3 words, delete everything after the first 3 words
        if len(alist) > 3:
            del alist[3:]
        
        #return the list
        return alist
    