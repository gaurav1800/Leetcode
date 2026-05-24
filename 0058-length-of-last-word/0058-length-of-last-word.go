import "strings"

func lengthOfLastWord(s string) int {
    s = strings.TrimSpace(s)
    sList := strings.Fields(s)
    return len(sList[len(sList)-1])
}