object Solution {
    def longestCommonPrefix(strs: Array[String]): String = {
        
        if (strs.isEmpty) return ""

        strs.reduce((s1, s2) => {
            s1.zip(s2).takeWhile {case(c1, c2) => c1==c2}
            .map(_._1)
            .mkString
    })
    }
}