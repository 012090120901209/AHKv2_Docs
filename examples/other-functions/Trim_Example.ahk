/*
    AutoHotkey v2 Example: Trim
    Documentation: Trim.md
    Category: Other Functions

    This example demonstrates practical usage of Trim.
    Modify and experiment to learn!
*/


; Remove whitespace from both ends
text := "  Hello World  "
trimmed := Trim(text)
MsgBox trimmed  ; "Hello World"

; Remove from left only
leftTrimmed := LTrim(text)

; Remove from right only
rightTrimmed := RTrim(text)


/*
    For complete documentation, see: Trim.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
