/*
    AutoHotkey v2 Example: InputBox
    Documentation: InputBox.md
    Category: Other Functions

    This example demonstrates practical usage of InputBox.
    Modify and experiment to learn!
*/


; Get user input
result := InputBox("Enter your name:")
if (result.Result = "OK")
    MsgBox "Hello " result.Value

; With default value
result := InputBox("Enter age:", "Age Input", , "25")

; Password input
result := InputBox("Password:", "Login", "Password")


/*
    For complete documentation, see: InputBox.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
