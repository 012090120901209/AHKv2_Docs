/*
    AutoHotkey v2 Example: WinMaximize
    Documentation: WinMaximize.md
    Category: Window Management

    This example demonstrates practical usage of WinMaximize.
    Modify and experiment to learn!
*/


; Maximize active window
WinMaximize "A"

; Maximize specific window
if WinExist("Notepad") {
    WinActivate
    WinMaximize
}


/*
    For complete documentation, see: WinMaximize.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
