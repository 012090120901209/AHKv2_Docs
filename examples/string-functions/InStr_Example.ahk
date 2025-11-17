/*
    AutoHotkey v2 Example: InStr
    Documentation: InStr.md
    Category: String Functions

    This example demonstrates practical usage of InStr.
    Modify and experiment to learn!
*/


; Find substring
pos := InStr("Hello World", "World")
MsgBox "Found at position: " pos

; Case-sensitive search
pos := InStr("Test", "test", true)
if !pos
    MsgBox "Not found"

; Find from right
pos := InStr("test test test", "test", , -1)


/*
    For complete documentation, see: InStr.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
