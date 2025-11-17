/*
    AutoHotkey v2 Example: For
    Documentation: For.md
    Category: Flow Control

    This example demonstrates practical usage of For.
    Modify and experiment to learn!
*/


; Loop through array
arr := [1, 2, 3, 4, 5]
for index, value in arr
    MsgBox value

; Loop through map
ages := Map("John", 25, "Jane", 30)
for name, age in ages
    MsgBox name ": " age

; Loop through object
person := {name: "John", age: 25}
for prop, value in person.OwnProps()
    MsgBox prop ": " value


/*
    For complete documentation, see: For.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
