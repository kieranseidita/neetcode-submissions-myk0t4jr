class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #Step 1: Create the hashmap for count and the frequency list to store the number and their frequency
        hashmap_count = {}

        #This needs to be the same length as the nuumber of elements that are contained within our input array
        freq = [[] for i in range(len(nums)+1)]

        #Step 2: Now we need to iterate through all the numbers that are in numb
        for n in nums:

            #Step 3: We need to now count the frequency of each number within our count hashmap and show the numebr as our keys and the freqneucy as our values
            hashmap_count[n] = 1 + hashmap_count.get(n,0)

        #Step 4: Then we need to look through each number and its count within our hashmap count and look at the key value pairs
        for n, c in hashmap_count.items():
            #Step 5: Then we need to add our number and make the count of the numebr the index of our frequency bucket sorted list
            freq[c].append(n)
        
        #Step 6: Create our result array that we will be displaying for our output
        result = []

        #Step 7: Now we need to go through each index in our frequency starting from the last element and working backwards
        for i in range(len(freq) - 1, 0 , -1):
            #Step 8: Then we need to check each number that is contained within the index(our frequency count)
            for n in freq[i]:
                #Step 9: We then need to add that number contained at a certain index(frequency count) to oru result array
                result.append(n)

                #Step 10: We now need to check if the length of our result array equals k, cause then we will return k elements
                if len(result) == k:
                    return result
        