/*
    AutoHotkey v2 Example: Round
    Category: Math Functions

    This example demonstrates the usage of Round with practical code.
*/

; ===== Basic Usage =====
result := Round(3.14159, 2)  ; 3.14

; ===== Advanced Usage =====
rounded := Round(12.5)  ; 13

; ===== Error Handling =====
if IsNumber(value)
    result := Round(value, 2)

; ===== Practical Example =====
; Calculate percentage
total := 150
part := 47
percentage := Round((part / total) * 100, 1) "%"

/*
    For more information, see the official documentation:
    https://www.autohotkey.com/docs/v2/
*/
