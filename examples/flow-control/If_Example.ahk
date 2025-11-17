/*
    AutoHotkey v2 Example: If
    Documentation: If.md
    Category: Flow Control

    This example demonstrates practical usage of If.
    Modify and experiment to learn!
*/


; Simple if
if (x > 10)
    MsgBox "Greater"

; If-else
if (x = 0)
    MsgBox "Zero"
else
    MsgBox "Non-zero"

; Multiple conditions
if (x > 0 and x < 100)
    MsgBox "In range"

; Nested
if (x > 0) {
    if (x < 10)
        MsgBox "Single digit"
    else
        MsgBox "Multiple digits"
}


/*
    For complete documentation, see: If.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
