/*
    AutoHotkey v2 Example: WinExist
    Documentation: WinExist.md
    Category: Window Management

    This example demonstrates practical usage of WinExist.
    Modify and experiment to learn!
*/


; Check if window exists
if WinExist("Notepad")
    MsgBox "Notepad is running"

; Get window ID
id := WinExist("Calculator")
if id
    MsgBox "Window ID: " id


/*
    For complete documentation, see: WinExist.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
