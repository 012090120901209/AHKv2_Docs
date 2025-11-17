/*
    AutoHotkey v2 Example: Try
    Documentation: Try.md
    Category: Error Handling

    This example demonstrates practical usage of Try.
    Modify and experiment to learn!
*/


; Try-catch
try {
    result := 10 / 0
} catch Error as err {
    MsgBox "Error: " err.Message
}

; Try-catch-finally
try {
    content := FileRead("file.txt")
} catch Error as err {
    MsgBox "Failed: " err.Message
} finally {
    MsgBox "Cleanup"
}


/*
    For complete documentation, see: Try.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
