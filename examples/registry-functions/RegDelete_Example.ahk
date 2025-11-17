/*
    AutoHotkey v2 Example: RegDelete
    Documentation: RegDelete.md
    Category: Registry Functions

    This example demonstrates practical usage of RegDelete.
    Modify and experiment to learn!
*/


; Delete registry value
RegDelete "HKCU\Software\MyApp", "OldSetting"

; Delete if exists
try
    RegDelete "HKCU\Software\MyApp", "Setting"


/*
    For complete documentation, see: RegDelete.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
