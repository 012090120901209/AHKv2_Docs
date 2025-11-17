/*
    AutoHotkey v2 Example: Hotkey
    Documentation: Hotkey.md
    Category: Keyboard Hotkeys

    This example demonstrates practical usage of Hotkey.
    Modify and experiment to learn!
*/


; Create hotkey dynamically
Hotkey "^!t", (*) => MsgBox("Ctrl+Alt+T pressed")

; Enable/disable hotkey
Hotkey "F1", "Off"
Hotkey "F1", "On"

; Toggle hotkey
toggle := true
Hotkey "F2", (*) => ToggleFeature()
ToggleFeature() {
    global toggle
    toggle := !toggle
    MsgBox "Feature " (toggle ? "On" : "Off")
}


/*
    For complete documentation, see: Hotkey.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
