/*
    AutoHotkey v2 Example: SubStr
    Documentation: SubStr.md
    Category: String Functions

    This example demonstrates practical usage of SubStr.
    Modify and experiment to learn!
*/


; Get first 5 characters
text := "Hello World"
first := SubStr(text, 1, 5)  ; "Hello"

; Get last 5 characters
last := SubStr(text, -5)  ; "World"

; Extract middle
middle := SubStr("ABCDEFGH", 3, 4)  ; "CDEF"


/*
    For complete documentation, see: SubStr.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
