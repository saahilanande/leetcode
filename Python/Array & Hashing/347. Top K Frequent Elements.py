class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #K.nlogn

        counter = {} #keys as nums in the list and values a repetition of that number
        result = [] 

        for num in nums:
            counter[num] = 1 + counter.get(num,0) #Incrementing if number found

        sortedList = sorted(counter.items(), key=lambda x:x[1], reverse=True) #Sorting the Dict

        for i in range(k):
            result.append(sortedList[i][0])

        return result

        #Without Using Sorting Function

        count = {} # dic for counting occurances
        
        freq = [[] for x in range(len(nums) + 1)]
                
        for i in nums:
                count[i] = 1 + count.get(i,0)
                
        for ele , c in  count.items():
            freq[c].append(ele) #arrange then based on the how many times the element occurs
            
        res = []
        
        for n in range(len(freq)-1,0,-1): #iterating the freq in reverse
            for i in freq[n]:
                res.append(i)
                if len(res) == k: #if the list is appended to the k element we 
                    return res
