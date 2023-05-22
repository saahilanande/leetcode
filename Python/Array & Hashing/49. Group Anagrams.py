class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

    # n.m

        result = collections.defaultdict(list) #mapping Key as character counter list and value as the words

        for word in strs:
            count = [0] * 26 #Initializing a list with 26 zero as place for all alphabets

            for letter in word:
                count[ord(letter)-ord("a")] += 1 #increasing count by 1 in the count list
            
            #Since List is mutable and keys in dict cant be, we convert it to tuple
            result[tuple(count)].append(word) #Adding word with same list of Count
        
        return result.values()
        
    #n^2logn
        
        result = {}
        
        for index in range(len(strs)):
            sort = ''.join(sorted(strs[index]))
            
            if sort in result:
                result[sort].append(strs[index])
            else:
                result[sort] = [strs[index]]
                
        return result.values()