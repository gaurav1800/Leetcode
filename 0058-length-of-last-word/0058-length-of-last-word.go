import "strings"

func lengthOfLastWord(s string) int {

    s = strings.TrimSpace(s)
    lastSpace := strings.LastIndex(s, " ")

    return len(s) - 1 - lastSpace    
}