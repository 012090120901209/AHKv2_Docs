/*
    AutoHotkey v2 Example: WinClose
    Documentation: WinClose.md
    Category: Window Management

    This example demonstrates practical usage of WinClose.
    Modify and experiment to learn!
*/


; Close window by title
WinClose "Calculator"

; Close with confirmation
if WinExist("Notepad") {
    WinActivate
    Send "^s"  ; Try to save first
    Sleep 500
    WinClose
}

; Close all instances
while WinExist("ahk_class Notepad")
    WinClose


/*
    For complete documentation, see: WinClose.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
