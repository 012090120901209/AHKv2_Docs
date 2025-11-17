/*
    AutoHotkey v2 Example: MouseGetPos
    Documentation: MouseGetPos.md
    Category: Mouse Functions

    This example demonstrates practical usage of MouseGetPos.
    Modify and experiment to learn!
*/


; Get mouse position
MouseGetPos &x, &y
MsgBox "Mouse at: " x ", " y

; Get window under mouse
MouseGetPos , , &id
title := WinGetTitle(id)
MsgBox "Window: " title

; Get control under mouse
MouseGetPos , , , &ctrl
MsgBox "Control: " ctrl


/*
    For complete documentation, see: MouseGetPos.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
