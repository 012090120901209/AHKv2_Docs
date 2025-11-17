/*
    AutoHotkey v2 Example: FileAppend
    Documentation: FileAppend.md
    Category: File Directory

    This example demonstrates practical usage of FileAppend.
    Modify and experiment to learn!
*/


; Append text to file
FileAppend "Log entry`n", "log.txt"

; Append with timestamp
timestamp := FormatTime(, "yyyy-MM-dd HH:mm:ss")
FileAppend timestamp ": Event occurred`n", "events.log"

; Create file if doesn't exist
FileAppend "First line`n", "new.txt"


/*
    For complete documentation, see: FileAppend.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
