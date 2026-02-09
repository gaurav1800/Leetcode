object Solution {
    def mergeAlternately(word1: String, word2: String): String = {
        
        val result = new StringBuilder()
        val n1 = word1.length
        val n2 = word2.length
        val maxLength = math.max(n1, n2)

        for (i <- 0 until maxLength) {
            if (i < n1) result.append(word1(i))
            if (i < n2) result.append(word2(i))
        }

        result.toString()
    }
}