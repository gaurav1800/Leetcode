class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        arr = sentence.split()
        
        for i in range(len(dictionary)):
            for j in range(len(arr)):
                if dictionary[i] == arr[j][:len(dictionary[i])] and len(dictionary[i]) < len(arr[j]):
                    arr[j] = dictionary[i]
        
        return " ".join(arr)