#!/home/anirudha/anaconda3/bin/python
## Problem Statement ##
'''
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-.-....-", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
Note:

The length of words will be at most 100.
Each words[i] will have length in range [1, 12].
words[i] will only consist of lowercase letters.

## My Python3 code ##
'''

import string
class Solution:
    def uniqueMorseRepresentations(self, words):
        output = set()
        # Sets store unique values...
        values = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        keys = string.ascii_lowercase ## from string library
        ## now create a dictionary from 2 lists
        # learn dict and zip operators...
        dictionary = dict(zip(keys,values))
        for word in words:
            new_str = ''
            for letter in word:
                new_str += dictionary[letter]
            output.add(new_str)
        return len(output)

        """
        :type words: List[str]
        :rtype: int
        """
### Better sol: no need to use dictionaries...97 is where lower letter start...transformation += transformations[(ord(letter) - 97)]
        ## ord returns unicode code point  
