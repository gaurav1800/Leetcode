import scala.collection.mutable
import scala.util.boundary, boundary.break

object Solution {
    def isValid(s: String): Boolean = {
        boundary {
            val stack = mutable.Stack[Char]()
            val pairs = Map(')' -> '(', '}' -> '{', ']' -> '[')

            for (char <- s) {
                if (pairs.contains(char)) {
                    if (stack.isEmpty || stack.pop() != pairs(char)) break(false)
                }
                else {
                    stack.push(char)
                }
            }
            stack.isEmpty
        }


        
    }
}