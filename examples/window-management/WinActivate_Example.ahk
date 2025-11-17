/*
    AutoHotkey v2 Example: WinActivate
    Documentation: WinActivate.md
    Category: Window Management

    This example demonstrates practical usage of WinActivate.
    Modify and experiment to learn!
*/


; Activate window by title
WinActivate "Untitled - Notepad"

; Activate using window class
WinActivate "ahk_class Notepad"

; Activate most recent window
if WinExist("Chrome")
    WinActivate

; Switch between two windows
F1::
{
    if WinActive("ahk_class Notepad")
        WinActivate "ahk_class Chrome"
    else
        WinActivate "ahk_class Notepad"
}


/*
    For complete documentation, see: WinActivate.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
