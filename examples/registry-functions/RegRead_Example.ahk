/*
    AutoHotkey v2 Example: RegRead
    Documentation: RegRead.md
    Category: Registry Functions

    This example demonstrates practical usage of RegRead.
    Modify and experiment to learn!
*/


; Read registry value
value := RegRead("HKEY_CURRENT_USER\Software\MyApp", "Setting")
MsgBox value

; Error handling
try {
    value := RegRead("HKCU\Software\MyApp", "Key")
} catch Error {
    value := "default"
}


/*
    For complete documentation, see: RegRead.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
