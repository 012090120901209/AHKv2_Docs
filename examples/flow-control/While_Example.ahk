/*
    AutoHotkey v2 Example: While
    Documentation: While.md
    Category: Flow Control

    This example demonstrates practical usage of While.
    Modify and experiment to learn!
*/


; While loop
count := 0
while (count < 10) {
    MsgBox count
    count++
}

; While with break
while true {
    if (A_Index > 5)
        break
    MsgBox A_Index
}


/*
    For complete documentation, see: While.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
