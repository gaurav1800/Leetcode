object Solution {
    def removeDuplicates(nums: Array[Int]): Int = {
        
        if (nums.isEmpty) return 0

        val result = (1 until nums.length).foldLeft(0) {(i, j) =>
            if (nums(j) != nums(i)) {
                val nextI = i + 1
                nums(nextI) = nums(j)
                nextI
            }
            else {
                i
            }
        }
        result + 1
    }
}