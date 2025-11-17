/*
    AutoHotkey v2 Example: DirDelete
    Documentation: DirDelete.md
    Category: File Directory

    This example demonstrates practical usage of DirDelete.
    Modify and experiment to learn!
*/


; Delete empty directory
DirDelete "EmptyFolder"

; Delete recursively
DirDelete "FolderWithFiles", 1

; Safe delete
if DirExist("OldFolder")
    DirDelete "OldFolder", 1


/*
    For complete documentation, see: DirDelete.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
