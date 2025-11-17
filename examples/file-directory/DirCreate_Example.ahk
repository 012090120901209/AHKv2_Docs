/*
    AutoHotkey v2 Example: DirCreate
    Documentation: DirCreate.md
    Category: File Directory

    This example demonstrates practical usage of DirCreate.
    Modify and experiment to learn!
*/


; Create directory
DirCreate "NewFolder"

; Create nested directories
DirCreate "Path\To\Deep\Folder"

; Create if doesn't exist
if !DirExist("Output")
    DirCreate "Output"


/*
    For complete documentation, see: DirCreate.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
