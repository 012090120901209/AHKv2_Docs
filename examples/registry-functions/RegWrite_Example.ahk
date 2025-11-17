/*
    AutoHotkey v2 Example: RegWrite
    Documentation: RegWrite.md
    Category: Registry Functions

    This example demonstrates practical usage of RegWrite.
    Modify and experiment to learn!
*/


; Write string value
RegWrite "MyValue", "REG_SZ", "HKCU\Software\MyApp", "Setting"

; Write number
RegWrite 42, "REG_DWORD", "HKCU\Software\MyApp", "Number"


/*
    For complete documentation, see: RegWrite.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
