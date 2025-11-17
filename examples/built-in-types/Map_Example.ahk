/*
    AutoHotkey v2 Example: Map
    Documentation: Map.md
    Category: Built In Types

    This example demonstrates practical usage of Map.
    Modify and experiment to learn!
*/


; Create map
ages := Map("John", 25, "Jane", 30)

; Add/update
ages["Bob"] := 35

; Access
MsgBox ages["John"]

; Check if key exists
if ages.Has("Alice")
    MsgBox ages["Alice"]

; Iterate
for name, age in ages
    MsgBox name ": " age

; Delete key
ages.Delete("Bob")


/*
    For complete documentation, see: Map.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
