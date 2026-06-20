class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #make the result hashtable
        result = {}

        #go through every word in strs
        for word in strs:
            #make a list for freq of char
            alphabet = [0] * 26
            #check every char in that specific word
            for char in word:
                #count letter appearances
                alphabet[ord(char) - ord('a')] +=1
            
            #create the tuple for the key
            key = tuple(alphabet)

            if key not in result:
                #forgot this part
                result[key]=[]
            
            result[key].append(word)

        return list(result.values())