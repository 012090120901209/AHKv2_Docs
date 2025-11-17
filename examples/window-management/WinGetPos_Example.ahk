/*
    AutoHotkey v2 Example: WinGetPos
    Documentation: WinGetPos.md
    Category: Window Management

    This example demonstrates practical usage of WinGetPos.
    Modify and experiment to learn!
*/


; Get window position and size
WinGetPos &x, &y, &w, &h, "A"
MsgBox "Position: " x ", " y "`nSize: " w "x" h

; Check if window is off-screen
if (x < 0 or y < 0)
    WinMove 100, 100, , , "A"


/*
    For complete documentation, see: WinGetPos.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
