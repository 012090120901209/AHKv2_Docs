/*
    AutoHotkey v2 Example: Functions
    Documentation: Functions.md
    Category: Core Concepts

    This example demonstrates practical usage of Functions.
    Modify and experiment to learn!
*/


; Define function
Greet(name) {
    MsgBox "Hello " name
}

; Call function
Greet("John")

; Return value
Add(a, b) {
    return a + b
}
result := Add(5, 3)

; Optional parameters
PrintInfo(name, age := 0) {
    if age
        MsgBox name ": " age
    else
        MsgBox name
}

; Variadic function
Sum(numbers*) {
    total := 0
    for num in numbers
        total += num
    return total
}
result := Sum(1, 2, 3, 4, 5)


/*
    For complete documentation, see: Functions.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
