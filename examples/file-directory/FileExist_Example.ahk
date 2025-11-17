/*
    AutoHotkey v2 Example: FileExist
    Documentation: FileExist.md
    Category: File Directory

    This example demonstrates practical usage of FileExist.
    Modify and experiment to learn!
*/


; Check if file exists
if FileExist("config.ini")
    MsgBox "Config file found"

; Get attributes
attr := FileExist("folder")
if InStr(attr, "D")
    MsgBox "It's a directory"


/*
    For complete documentation, see: FileExist.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
