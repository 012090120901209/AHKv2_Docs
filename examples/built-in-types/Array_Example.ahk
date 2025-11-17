/*
    AutoHotkey v2 Example: Array
    Documentation: Array.md
    Category: Built In Types

    This example demonstrates practical usage of Array.
    Modify and experiment to learn!
*/


; Create array
arr := [1, 2, 3, 4, 5]

; Add elements
arr.Push(6)
arr.InsertAt(1, 0)

; Remove elements
arr.Pop()
arr.RemoveAt(1)

; Iterate
for index, value in arr
    MsgBox value

; Multi-dimensional
matrix := [[1,2], [3,4], [5,6]]
MsgBox matrix[2][1]  ; 3


/*
    For complete documentation, see: Array.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
