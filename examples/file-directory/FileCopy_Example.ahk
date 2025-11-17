/*
    AutoHotkey v2 Example: FileCopy
    Documentation: FileCopy.md
    Category: File Directory

    This example demonstrates practical usage of FileCopy.
    Modify and experiment to learn!
*/


; Copy file
FileCopy "source.txt", "backup.txt"

; Overwrite existing
FileCopy "file.txt", "copy.txt", 1

; Copy with error handling
try {
    FileCopy "important.doc", "backup.doc"
} catch Error as err {
    MsgBox "Copy failed: " err.Message
}


/*
    For complete documentation, see: FileCopy.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
