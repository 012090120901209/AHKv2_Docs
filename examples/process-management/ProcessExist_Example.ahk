/*
    AutoHotkey v2 Example: ProcessExist
    Documentation: ProcessExist.md
    Category: Process Management

    This example demonstrates practical usage of ProcessExist.
    Modify and experiment to learn!
*/


; Check if process exists
if ProcessExist("notepad.exe")
    MsgBox "Notepad is running"

; Get process ID
pid := ProcessExist("chrome.exe")
if pid
    MsgBox "Chrome PID: " pid


/*
    For complete documentation, see: ProcessExist.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
