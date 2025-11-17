/*
    AutoHotkey v2 Example: FileMove
    Documentation: FileMove.md
    Category: File Directory

    This example demonstrates practical usage of FileMove.
    Modify and experiment to learn!
*/


; Move/rename file
FileMove "old.txt", "new.txt"

; Move to different directory
FileMove "file.txt", "backup\file.txt"

; Overwrite if exists
FileMove "source.txt", "dest.txt", 1


/*
    For complete documentation, see: FileMove.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
