/*
    AutoHotkey v2 Example: WinKill
    Documentation: WinKill.md
    Category: Window Management

    This example demonstrates practical usage of WinKill.
    Modify and experiment to learn!
*/


; Force close unresponsive window
WinKill "Frozen Application"

; Force close with confirmation
if WinExist("Application") {
    WinClose
    WinWaitClose , , 3
    if WinExist()
        WinKill
}


/*
    For complete documentation, see: WinKill.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
