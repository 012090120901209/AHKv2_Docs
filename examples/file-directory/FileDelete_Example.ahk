/*
    AutoHotkey v2 Example: FileDelete
    Documentation: FileDelete.md
    Category: File Directory

    This example demonstrates practical usage of FileDelete.
    Modify and experiment to learn!
*/


; Delete single file
FileDelete "temp.txt"

; Delete with pattern
FileDelete "*.tmp"

; Safe delete
if FileExist("old.txt")
    FileDelete "old.txt"


/*
    For complete documentation, see: FileDelete.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
