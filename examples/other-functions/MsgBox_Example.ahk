/*
    AutoHotkey v2 Example: MsgBox
    Documentation: MsgBox.md
    Category: Other Functions

    This example demonstrates practical usage of MsgBox.
    Modify and experiment to learn!
*/


; Simple message
MsgBox "Hello World"

; With title
MsgBox "Message text", "Title"

; Yes/No dialog
result := MsgBox("Continue?", "Confirm", "YesNo")
if (result = "Yes")
    MsgBox "Continuing"

; Icon types
MsgBox "Error occurred", "Error", "Icon!"
MsgBox "Warning", "Warning", "Icon?"


/*
    For complete documentation, see: MsgBox.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
