/*
    AutoHotkey v2 Example: WinWait
    Documentation: WinWait.md
    Category: Window Management

    This example demonstrates practical usage of WinWait.
    Modify and experiment to learn!
*/


; Wait for window to appear
Run "notepad.exe"
WinWait "Untitled - Notepad", , 5
if WinExist()
    WinActivate
else
    MsgBox "Notepad didn't open"


/*
    For complete documentation, see: WinWait.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
