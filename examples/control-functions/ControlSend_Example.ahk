/*
    AutoHotkey v2 Example: ControlSend
    Documentation: ControlSend.md
    Category: Control Functions

    This example demonstrates practical usage of ControlSend.
    Modify and experiment to learn!
*/


; Send keys to control
ControlSend "Hello", "Edit1", "Notepad"

; Send special keys
ControlSend "^a", "Edit1", "Notepad"
ControlSend "{Delete}", "Edit1", "Notepad"


/*
    For complete documentation, see: ControlSend.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
