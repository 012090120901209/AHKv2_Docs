/*
    AutoHotkey v2 Example: Send
    Documentation: Send.md
    Category: Keyboard Hotkeys

    This example demonstrates practical usage of Send.
    Modify and experiment to learn!
*/


; Send text
Send "Hello World"

; Send keys
Send "{Enter}"
Send "^s"  ; Ctrl+S
Send "+{Tab}"  ; Shift+Tab

; Send raw text
SendText "This {is} sent literally"

; Type slowly
SendInput "{Text}Slow typing"


/*
    For complete documentation, see: Send.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
