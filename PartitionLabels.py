class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        '''
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        x = {}
        for i in range(len(S)-1,-1,-1):
            if(S[i] not in x):
                x[S[i]] = i
        
        
        o = []
        def partition(start):
            if(start==len(S)):
                return
            i=start
            j=x[S[i]]
            while(i<j):
                if(x[S[i]]>j):
                    j = x[S[i]]
                i+=1
            
            nonlocal o
            o.append(j-start+1)
            if(j<len(S)-1):
                partition(j+1)
        
        partition(0)
        return o
