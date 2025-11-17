/*
    AutoHotkey v2 Example: Random
    Documentation: Random.md
    Category: Math Functions

    This example demonstrates practical usage of Random.
    Modify and experiment to learn!
*/


; Random number 1-100
num := Random(1, 100)
MsgBox num

; Random float
flt := Random(0.0, 1.0)

; Shuffle array
arr := [1, 2, 3, 4, 5]
Loop 10 {
    i := Random(1, arr.Length)
    j := Random(1, arr.Length)
    temp := arr[i]
    arr[i] := arr[j]
    arr[j] := temp
}


/*
    For complete documentation, see: Random.md
    AutoHotkey v2 Documentation: https://www.autohotkey.com/docs/v2/
*/
