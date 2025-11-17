/*
    AutoHotkey v2 Example: Loop
    Documentation: Loop.md
    Category: Flow Control

    This example demonstrates practical usage of Loop.
    Modify and experiment to learn!
*/


; Simple loop
Loop 10
    MsgBox A_Index

; Infinite loop
Loop {
    if (A_Index > 100)
        break
    Sleep 10
}

; Loop through files
Loop Files, "*.txt"
    MsgBox A_LoopFileName


/*
    For complete documentation, see: Loop.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
