from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Trie-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------


# Class representing a node in the Trie
class TrieNode:

    def __init__(self, letter=None, frequency=None, is_last=False):
        self.letter = letter
        self.frequency = frequency
        self.is_last = is_last
        self.children : dict[str, TrieNode] = {}


class TrieDictionary(BaseDictionary):

    def __init__(self):
        # TO BE IMPLEMENTED
        self.root = TrieNode("")
        
        

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # TO BE IMPLEMENTED
        #build the trie
        curr_node = self.root
        for word_frequency in words_frequencies:
            for letter in word_frequency.word:
                if letter in curr_node.children:
                    curr_node = curr_node.children[letter]
                else:
                    new_node = TrieNode(letter)
                    curr_node.children[letter] = new_node
                    curr_node = new_node
                    
            curr_node.is_last = True
            curr_node.frequency = word_frequency.frequency
            curr_node = self.root
            
            
            
        # curr_node = self.root
        # for letter in word_frequency.word:
        #     if letter in curr_node.children:
        #         curr_node = curr_node.children[letter]
        #         return False
        #     else:
        #         new_node = TrieNode(letter)
        #         curr_node.children[letter] = new_node
        #         curr_node = new_node
        # curr_node.is_last = True
        # curr_node.frequency = word_frequency.frequency
        # return True
            
            
            
        


        

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # TO BE IMPLEMENTED
        curr_node = self.root #start at the root
        for letter in word: #iterate over the word
            if letter in curr_node.children: #if the letter is in the children
                curr_node = curr_node.children[letter] #move to the next node
            else: #if the letter is not in the children
                return 0  #return 0
        if curr_node.is_last: #if the node is the last node
            return curr_node.frequency  #return the frequency
        else:
            return 0 
        

        
        
    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """

        # TO BE IMPLEMENTED\

        
        curr_node = self.root
        for letter in word_frequency.word:
            if letter in curr_node.children:
                curr_node = curr_node.children[letter]
            else:
                new_node = TrieNode(letter)
                curr_node.children[letter] = new_node
                curr_node = new_node
        if curr_node.is_last:
            return False
        else:
            curr_node.is_last = True
            curr_node.frequency = word_frequency.frequency
            return True
        
    

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        
        curr_node = self.root #start at the root
        for letter in word: #iterate over the word
            if letter in curr_node.children: #if the letter is in the children
                curr_node = curr_node.children[letter] #move to the next node
        if curr_node.is_last: #if the
            curr_node.is_last = False #set the node to not be the last node
            curr_node.frequency = None #set the frequency to None
            return True
        
        



    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        autocomplete_list = [] #list to store the words
        curr_node = self.root #start at the root
        for letter in word: #iterate over the word
            if letter in curr_node.children: #if the letter is in the children
                curr_node = curr_node.children[letter] #move to the next node
            else: #if the letter is not in the children
                return autocomplete_list  #return the list
        stack = [(curr_node, word)] #stack to store the nodes
        while stack: #while the stack is not empty
            curr_node, word = stack.pop() #pop the node and the word
            if curr_node.is_last: #if the node is the last node
                autocomplete_list.append(WordFrequency(word, curr_node.frequency)) #append the word to the list
            for child in curr_node.children.values(): #iterate over the children
                stack.append((child, word + child.letter)) #append the child and the word + the child's letter
        autocomplete_list.sort(key=lambda x: x.frequency, reverse=True) #sort the list
        return autocomplete_list[:3] #return the first 3 elements of the list
        
        
        
        
        
                
        
    
    
    # curr_node = self.root #start at the root
    #     for letter in word: #iterate over the word
    #         if letter in curr_node.children: #if the letter is in the children
    #             curr_node = curr_node.children[letter] #move to the next node
    #         else: #if the letter is not in the children
    #             return 0  #return 0
    #     if curr_node.is_last: #if the node is the last node
    #         return curr_node.frequency  #return the frequency
    #     else:
            
        
        
            
                
            
    
    
    
            
            
    
            
    
            
        
        
        
            
    
