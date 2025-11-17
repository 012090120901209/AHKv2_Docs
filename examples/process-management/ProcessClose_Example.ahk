/*
    AutoHotkey v2 Example: ProcessClose
    Documentation: ProcessClose.md
    Category: Process Management

    This example demonstrates practical usage of ProcessClose.
    Modify and experiment to learn!
*/


; Close process
ProcessClose "notepad.exe"

; Close by PID
pid := ProcessExist("calc.exe")
if pid
    ProcessClose pid


/*
    For complete documentation, see: ProcessClose.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
