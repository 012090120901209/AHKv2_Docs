/*
    AutoHotkey v2 Example: Switch
    Documentation: Switch.md
    Category: Flow Control

    This example demonstrates practical usage of Switch.
    Modify and experiment to learn!
*/


; Switch statement
day := 1
switch day {
    case 1: MsgBox "Monday"
    case 2: MsgBox "Tuesday"
    case 3: MsgBox "Wednesday"
    default: MsgBox "Other day"
}

; Switch with multiple values
color := "red"
switch color {
    case "red", "blue", "green":
        MsgBox "Primary color"
    default:
        MsgBox "Other color"
}


/*
    For complete documentation, see: Switch.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
