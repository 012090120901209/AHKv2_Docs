/*
    AutoHotkey v2 Example: WinRestore
    Documentation: WinRestore.md
    Category: Window Management

    This example demonstrates practical usage of WinRestore.
    Modify and experiment to learn!
*/


; Restore minimized window
WinRestore "Calculator"

; Toggle maximize/restore
^F11::
{
    if WinActive("A") {
        WinGetMinMax &state, "A"
        if (state = 1)
            WinRestore "A"
        else
            WinMaximize "A"
    }
}


/*
    For complete documentation, see: WinRestore.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
