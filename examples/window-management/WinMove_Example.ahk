/*
    AutoHotkey v2 Example: WinMove
    Documentation: WinMove.md
    Category: Window Management

    This example demonstrates practical usage of WinMove.
    Modify and experiment to learn!
*/


; Move window to top-left
WinMove 0, 0, , , "Notepad"

; Resize window
WinMove , , 800, 600, "A"

; Center window
CenterWindow() {
    WinGetPos , , &w, &h, "A"
    x := (A_ScreenWidth - w) / 2
    y := (A_ScreenHeight - h) / 2
    WinMove x, y, , , "A"
}


/*
    For complete documentation, see: WinMove.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
