object Solution {
    def strStr(haystack: String, needle: String): Int = {


        // simpler
        haystack.indexOf(needle)

        // functional way
        // val n = haystack.length
        // val m = needle.length

        // (0 to n - m).find { i =>
        //     haystack.substring(i, i + m) == needle
        // }.getOrElse(-1)
    }
}