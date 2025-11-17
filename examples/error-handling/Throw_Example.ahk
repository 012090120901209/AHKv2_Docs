/*
    AutoHotkey v2 Example: Throw
    Documentation: Throw.md
    Category: Error Handling

    This example demonstrates practical usage of Throw.
    Modify and experiment to learn!
*/


; Throw error
if !FileExist("required.txt")
    throw Error("Required file missing")

; Custom error
ValidateAge(age) {
    if (age < 0 or age > 120)
        throw ValueError("Invalid age: " age)
    return true
}


/*
    For complete documentation, see: Throw.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
