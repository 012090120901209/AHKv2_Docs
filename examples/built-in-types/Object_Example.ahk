/*
    AutoHotkey v2 Example: Object
    Documentation: Object.md
    Category: Built In Types

    This example demonstrates practical usage of Object.
    Modify and experiment to learn!
*/


; Create object
person := {name: "John", age: 25, city: "NYC"}

; Access properties
MsgBox person.name

; Add property
person.email := "john@example.com"

; Check property
if person.HasOwnProp("age")
    MsgBox person.age

; Iterate properties
for prop, value in person.OwnProps()
    MsgBox prop ": " value


/*
    For complete documentation, see: Object.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
