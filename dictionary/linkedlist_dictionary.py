from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency


class ListNode:
    '''
    Define a node in the linked list
    '''

    def __init__(self, word_frequency: WordFrequency):
        self.word_frequency = word_frequency
        self.next = None
        
    # getters and setters
    def get_word_frequency(self):
        return self.word_frequency
    
    def get_word(self):
        return self.word_frequency.word
    
    def get_frequency(self):
        return self.word_frequency.frequency
    
    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next
        
    def set_word_frequency(self, word_frequency):
        self.word_frequency = word_frequency
    
    

# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class LinkedListDictionary(BaseDictionary):

    def __init__(self):
        # TO BE IMPLEMENTED
        self.head = None
        self.length = 0


    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # TO BE IMPLEMENTED
        
        # create for loop 
        # iterate while moving the haad down on
        # make new line the head of the dictionary
        
        for word in words_frequencies:
            node = ListNode(word)
            if not self.head:
                self.head = node
            else:
                node.set_next(self.head)
                self.head = node
            self.length += 1
        


    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """

        # TO BE IMPLEMENTED
        #     create for loop
        #     iterate over list
        #     if current node is == word
        #     return the frequency
        #     if not
        #     return 0
        
        node = self.head
        #print('self.head:' ,self.head)
        for i in range(self.length):
            if node is not None:
                cur_node = node.get_word_frequency()
                if cur_node.word == word:
                    return cur_node.frequency
                node = node.get_next()
            else:
                break
            
        return 0
        
            
        

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """

        # TO BE IMPLEMENTED
        # '''
        # search for word
        # if word not found
        #     add word as head
        #     increase length
        # '''
        
        new_node = ListNode(word_frequency)
        word = word_frequency.word
        search = self.search(word)
        
        if search == 0: #if not found
            if not self.head: #if not head
                self.head = new_node 
            else : #if head
                new_node.set_next(self.head)
                self.head = new_node
            self.length += 1
            return True
        else: #if word is already in the dictionary
            return False
                

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """

        #TO BE IMPLEMENTED
        found  = False
        
        # if the dictionary is empty, that means there is no word to delete, so automatically return False
        if self.length == 0: 
            return False
        
        #set the current node as the head, and previous node
        cur_node = self.head
        prev_node = None
        
        #checks if word is the head of the dictionary before starting a loop
        if cur_node.get_word() == word:
            self.head = cur_node.get_next()
            prev_node.set_next(cur_node.get_next())
            cur_node = None
            self.length -= 1
            return True
        
        #if word is not head, then set the current node as the next node, and the previous node as the former current node and start loop
        prev_node = cur_node
        
        while cur_node:
            if cur_node.get_word() == word: #if word is found
                prev_node.set_next(cur_node.get_next())
                cur_node = None
                return True
        #if word is not found, then move cur_node to next node and set previous node as the former cur_node
            prev_node = cur_node
            cur_node = cur_node.get_next()
        return False #if word not found
            
        
        
        
        
        


    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """

        
        #define list of autocompleted words as an empty list. and set the current node to be the head of the linked list
        alist = []
        cur_node = self.head
        
        #loop over list
        for i in range(self.length):
            if cur_node is not None:
        #define search as the word we are searching for and word_frequency as the word frequency pair of the current node
                search = cur_node.word_frequency.word
                word_frequency = cur_node.word_frequency
        #if search starts with word, add to autocompleted list
                if search.startswith(word):
                    alist.append(word_frequency)
        #set the current node as the next node
                cur_node = cur_node.next
            else:
                break
        #sort the autocompleted list by frequency and reverse
        alist.sort(key = lambda y: y.frequency, reverse=True)
        #if list is longer than 3 words, delete everything other than the first 3 nodes
        if len(alist) > 3:
            del alist[3:]
        #return the list
        return alist
            
        
        
        
        
        
        
        
        
#         ''' array
#         alist = [] #autocomplete list
#         for word in self.data:
#             if word.word.startswith(prefix_word):
#                 alist.append(word)
        
#         alist.sort(key = lambda y: y.frequency, reverse=True)
#         if len(alist) > 3:
#             del alist[3:]
            
        
        
        
        
#         return alist
# '''
        



