/*
    AutoHotkey v2 Example: WinSetTitle
    Documentation: WinSetTitle.md
    Category: Window Management

    This example demonstrates practical usage of WinSetTitle.
    Modify and experiment to learn!
*/


; Change window title
WinSetTitle "New Title", "Notepad"

; Add timestamp to title
title := WinGetTitle("A")
WinSetTitle title " - " A_Now, "A"


/*
    For complete documentation, see: WinSetTitle.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
