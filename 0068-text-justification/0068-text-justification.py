class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        result = []
        currentLine = []
        currentLineSize = 0

        for word in words:
            length = 0
            
            if currentLineSize + len(word) + len(currentLine) > maxWidth:
                for i in range(maxWidth - currentLineSize):
                    currentLine[i % (len(currentLine) - 1 or 1)] += ' '
                result.append(''.join(currentLine))
                currentLine = []
                currentLineSize = 0
            currentLine.append(word)
            currentLineSize += len(word)
        
        result.append(' '.join(currentLine).ljust(maxWidth))
        return result
            