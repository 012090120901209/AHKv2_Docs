# ComObjFlags

Retrieves or changes flags which control a COM wrapper object\'s
behaviour.

``` Syntax
Flags := ComObjFlags(ComObj , NewFlags, Mask)
```

## Parameters {#Parameters}

ComObj

:   Type: [Object](../Concepts.htm#objects)

    A COM wrapper object. See [ComValue](ComValue.htm) for details.

NewFlags

:   Type: [Integer](../Concepts.htm#numbers)

    New values for the flags identified by *Mask*, or flags to add or
    remove.

Mask

:   Type: [Integer](../Concepts.htm#numbers)

    A bitmask of flags to change.

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers)

This function returns the current flags of the specified COM object
(after applying *NewFlags*, if specified).

## Error Handling {#Error_Handling}

A [TypeError](Error.htm#TypeError) is thrown if *ComObj* is not a COM
wrapper object.

## Flags {#Flags}

+-----------------------------------+-----------------------------------+
| Flag                              | Effect                            |
+===================================+===================================+
| 1                                 | F_OWNVALUE                        |
|                                   |                                   |
|                                   | **SafeArray:** If the flag is     |
|                                   | set, the SafeArray is destroyed   |
|                                   | when the wrapper object is freed. |
|                                   | Since SafeArrays have no          |
|                                   | reference counting mechanism, if  |
|                                   | a SafeArray with this flag is     |
|                                   | assigned to an element of another |
|                                   | SafeArray, a separate copy is     |
|                                   | created.                          |
|                                   |                                   |
|                                   | **BSTR:** If the flag is set, the |
|                                   | BSTR is freed when the wrapper    |
|                                   | object is freed. The flag is set  |
|                                   | automatically when a BSTR is      |
|                                   | allocated as a result of type     |
|                                   | conversion performed by           |
|                                   | [ComValue](ComValue.htm), such as |
|                                   | `ComValue(8, "example")`.         |
+-----------------------------------+-----------------------------------+

## Remarks {#Remarks}

If *Mask* is omitted, *NewFlags* specifies the flags to add (if
positive) or remove (if negative). For example, `ComObjFlags(obj, -1)`
removes the F_OWNVALUE flag. Do not specify any value for *Mask* other
than 0 or 1; all other bits are reserved for future use.

## Related {#Related}

[ComValue](ComValue.htm), [ComObjActive](ComObjActive.htm),
[ComObjArray](ComObjArray.htm)

## Examples {#Examples}

::: {#ExCheck .ex}
[](#ExCheck){.ex_number} Checks for the presence of the F_OWNVALUE flag.

    arr := ComObjArray(0xC, 1)
    if ComObjFlags(arr) & 1
        MsgBox "arr will be automatically destroyed."
    else
        MsgBox "arr will not be automatically destroyed."
:::

::: {#ExRemove .ex}
[](#ExRemove){.ex_number} Changes array-in-array behaviour.

    arr1 := ComObjArray(0xC, 3)
    arr2 := ComObjArray(0xC, 1)
    arr2[0] := "original value"
    arr1[0] := arr2         ; Assign implicit copy.
    ComObjFlags(arr2, -1)   ; Remove F_OWNVALUE.
    arr1[1] := arr2         ; Assign original array.
    arr1[2] := arr2.Clone() ; Assign explicit copy.
    arr2[0] := "new value"
    for arr in arr1
        MsgBox arr[0]

    arr1 := ""
    ; Not valid since arr2 == arr1[1], which has been destroyed: 
    ;  arr2[0] := "foo"
:::
