object Solution {
    def removeElement(nums: Array[Int], `val`: Int): Int = {
        
        if (nums.isEmpty) return 0

        var i = 0
        for (j <- 0 until nums.length) {
            if (nums(j) != `val`) {
                nums(i) = nums(j)
                i += 1
            }
        }
        i
        
        // slower with foldLeft
        // nums.indices.foldLeft(0) {(i, j) =>
        //     if (nums(j) != `val`) {
        //         nums(i) = nums(j)
        //         i + 1
        //     }
        //     else {
        //         i
        //     }
        // }
    }
}