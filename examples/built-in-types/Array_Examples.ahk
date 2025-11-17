/*
    AutoHotkey v2 Array Examples
    Demonstrates all major Array methods and properties

    Topics Covered:
    - Creating arrays
    - Adding/removing elements
    - Accessing elements
    - Array iteration
    - Array methods (Push, Pop, InsertAt, RemoveAt, etc.)
    - Array properties (Length, Capacity)
*/

; ===== Creating Arrays =====

; Empty array
emptyArray := []
MsgBox "Empty array length: " emptyArray.Length

; Array with initial values
numbers := [1, 2, 3, 4, 5]
MsgBox "Numbers: " ArrayToString(numbers)

; Array with mixed types
mixed := ["text", 42, true, {key: "value"}]
MsgBox "Mixed array length: " mixed.Length

; ===== Accessing Elements =====

; Access by index (1-based in AHK)
fruits := ["apple", "banana", "orange"]
MsgBox "First fruit: " fruits[1]  ; "apple"
MsgBox "Last fruit: " fruits[-1]  ; "orange" (negative index from end)

; ===== Adding Elements =====

; Push - add to end
colors := ["red", "green"]
colors.Push("blue")
MsgBox "After Push: " ArrayToString(colors)  ; ["red", "green", "blue"]

; InsertAt - insert at specific position
colors.InsertAt(2, "yellow")
MsgBox "After InsertAt(2): " ArrayToString(colors)  ; ["red", "yellow", "green", "blue"]

; ===== Removing Elements =====

; Pop - remove from end
removed := colors.Pop()
MsgBox "Popped: " removed "`nRemaining: " ArrayToString(colors)

; RemoveAt - remove at specific position
colors.RemoveAt(1)
MsgBox "After RemoveAt(1): " ArrayToString(colors)

; Delete - remove by index
colors.Delete(1)
MsgBox "After Delete(1): " ArrayToString(colors)

; ===== Array Methods =====

; Clone - create a shallow copy
original := [1, 2, 3]
copy := original.Clone()
copy[1] := 99
MsgBox "Original: " ArrayToString(original) "`nCopy: " ArrayToString(copy)

; Has - check if index exists
arr := [10, 20, 30]
MsgBox "Has index 2? " arr.Has(2)  ; true
MsgBox "Has index 10? " arr.Has(10)  ; false

; Length property
MsgBox "Array length: " arr.Length

; Capacity property
MsgBox "Array capacity: " arr.Capacity

; ===== Iteration =====

; For loop
animals := ["cat", "dog", "bird", "fish"]
result := "Animals:`n"
for index, animal in animals {
    result .= index ": " animal "`n"
}
MsgBox result

; ===== Multi-dimensional Arrays =====

; 2D array (matrix)
matrix := [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
MsgBox "Element [2][3]: " matrix[2][3]  ; 6

; ===== Practical Example: Todo List =====

todos := []

; Add todos
todos.Push({task: "Buy groceries", done: false})
todos.Push({task: "Write code", done: false})
todos.Push({task: "Exercise", done: false})

; Mark first task as done
todos[1].done := true

; Display todos
output := "Todo List:`n"
for index, todo in todos {
    status := todo.done ? "[X]" : "[ ]"
    output .= index ". " status " " todo.task "`n"
}
MsgBox output

; ===== Advanced: Filter array =====

allNumbers := [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenNumbers := []

for num in allNumbers {
    if (Mod(num, 2) = 0)
        evenNumbers.Push(num)
}
MsgBox "Even numbers: " ArrayToString(evenNumbers)

; ===== Advanced: Map array =====

prices := [10, 20, 30]
discountedPrices := []

for price in prices {
    discountedPrices.Push(price * 0.9)  ; 10% discount
}
MsgBox "Original: " ArrayToString(prices) "`nDiscounted: " ArrayToString(discountedPrices)

; Helper function to convert array to string
ArrayToString(arr) {
    result := "["
    for index, value in arr {
        if (index > 1)
            result .= ", "
        result .= value
    }
    result .= "]"
    return result
}
