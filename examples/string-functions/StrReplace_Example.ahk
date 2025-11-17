/*
    AutoHotkey v2 Example: StrReplace
    Documentation: StrReplace.md
    Category: String Functions

    This example demonstrates practical usage of StrReplace.
    Modify and experiment to learn!
*/


; Basic replace
text := "Hello World"
new := StrReplace(text, "World", "AHK")
MsgBox new  ; "Hello AHK"

; Replace all occurrences
data := "test test test"
result := StrReplace(data, "test", "demo", , &count)
MsgBox "Replaced " count " times"

; Case-sensitive replace
text := "Test TEST test"
result := StrReplace(text, "test", "demo", true)


/*
    For complete documentation, see: StrReplace.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
