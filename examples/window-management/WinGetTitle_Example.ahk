/*
    AutoHotkey v2 Example: WinGetTitle
    Documentation: WinGetTitle.md
    Category: Window Management

    This example demonstrates practical usage of WinGetTitle.
    Modify and experiment to learn!
*/


; Get active window title
title := WinGetTitle("A")
MsgBox title

; Get all window titles
ids := WinGetList()
for id in ids {
    title := WinGetTitle(id)
    if title
        MsgBox title
}


/*
    For complete documentation, see: WinGetTitle.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
