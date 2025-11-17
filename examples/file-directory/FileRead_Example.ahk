/*
    AutoHotkey v2 Example: FileRead
    Documentation: FileRead.md
    Category: File Directory

    This example demonstrates practical usage of FileRead.
    Modify and experiment to learn!
*/


; Read entire file
content := FileRead("config.txt")
MsgBox content

; Read with encoding
content := FileRead("data.json", "UTF-8")

; Error handling
try {
    content := FileRead("file.txt")
} catch Error as err {
    MsgBox "Error reading file: " err.Message
}


/*
    For complete documentation, see: FileRead.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
