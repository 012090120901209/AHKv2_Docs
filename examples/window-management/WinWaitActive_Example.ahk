/*
    AutoHotkey v2 Example: WinWaitActive
    Documentation: WinWaitActive.md
    Category: Window Management

    This example demonstrates practical usage of WinWaitActive.
    Modify and experiment to learn!
*/


; Wait for window to become active
Run "calc.exe"
WinWaitActive "Calculator", , 3
if ErrorLevel
    MsgBox "Calculator didn't activate"
else
    Send "2+2="


/*
    For complete documentation, see: WinWaitActive.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
