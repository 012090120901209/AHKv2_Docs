/*
    AutoHotkey v2 Example: MouseMove
    Documentation: MouseMove.md
    Category: Mouse Functions

    This example demonstrates practical usage of MouseMove.
    Modify and experiment to learn!
*/


; Move to coordinates
MouseMove 500, 500

; Move relative to current
MouseGetPos &x, &y
MouseMove x+50, y+50

; Move slowly
MouseMove 1000, 1000, 50


/*
    For complete documentation, see: MouseMove.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
