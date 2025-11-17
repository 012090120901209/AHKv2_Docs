/*
    AutoHotkey v2 Example: StrSplit
    Documentation: StrSplit.md
    Category: String Functions

    This example demonstrates practical usage of StrSplit.
    Modify and experiment to learn!
*/


; Split by delimiter
parts := StrSplit("one,two,three", ",")
for index, part in parts
    MsgBox part

; Split by multiple delimiters
text := "one;two,three"
parts := StrSplit(text, ",;")

; Parse CSV
line := "Name,Age,City"
fields := StrSplit(line, ",")


/*
    For complete documentation, see: StrSplit.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
