# ComObjArray

Creates a SafeArray for use with COM.

``` Syntax
ArrayObj := ComObjArray(VarType, Count1 , Count2, ... Count8)
```

`ComObjArray` itself is a [class](Class.htm) derived from `ComValue`,
but is used only to create or identify SafeArray wrapper objects.

## Parameters {#Parameters}

VarType

:   Type: [Integer](../Concepts.htm#numbers)

    The base type of the array (the VARTYPE of each element of the
    array). The VARTYPE is restricted to a subset of the variant types.
    Neither the VT_ARRAY nor the VT_BYREF flag can be set. VT_EMPTY and
    VT_NULL are not valid base types for the array. All other types are
    legal.

    See [ComObjType](ComObjType.htm) for a list of possible values.

Count*N*

:   Type: [Integer](../Concepts.htm#numbers)

    The size of each dimension. Arrays containing up to 8 dimensions are
    supported.

## Return Value {#Return_Value}

Type: ComObjArray

This function returns a wrapper object containing a new SafeArray.

## Methods {#Methods}

ComObjArray objects support the following methods:

-   `.MaxIndex(n)`: Returns the upper bound of the *n*th dimension. If
    *n* is omitted, it defaults to 1.
-   `.MinIndex(n)`: Returns the lower bound of the *n*th dimension. If
    *n* is omitted, it defaults to 1.
-   `.Clone()`: Returns a copy of the array.
-   `.__Enum()`: Not typically called by script; allows
    [for-loops](For.htm) to be used with SafeArrays.

## Remarks {#Remarks}

ComObjArray objects may also be returned by COM methods and
[ComValue](ComValue.htm). Scripts may determine if a value is a
ComObjArray as follows:

    ; Check class
    if obj is ComObjArray
        MsgBox "Array subtype: " . ComObjType(obj) & 0xfff
    else
        MsgBox "Not an array."

    ; Check for VT_ARRAY
    if ComObjType(obj) & 0x2000
        MsgBox "obj is a ComObjArray"

    ; Check specific array type
    if ComObjType(obj) = 0x2008
        MsgBox "obj is a ComObjArray of strings"

Arrays with up to 8 dimensions are supported.

Since SafeArrays are not designed to support multiple references, when
one SafeArray is assigned to an element of another SafeArray, a separate
copy is created. However, this only occurs if the wrapper object has the
F_OWNVALUE flag, which indicates it is responsible for destroying the
array. This flag can be removed by using [ComObjFlags](ComObjFlags.htm).

When a function or method called by a COM client returns a SafeArray
with the F_OWNVALUE flag, a copy is created and returned instead, as the
original SafeArray is automatically destroyed.

## Related {#Related}

[ComValue](ComValue.htm), [ComObjType](ComObjType.htm),
[ComObjValue](ComObjValue.htm), [ComObjActive](ComObjActive.htm),
[ComObjFlags](ComObjFlags.htm), [Array Manipulation Functions (Microsoft
Docs)](https://learn.microsoft.com/previous-versions/windows/desktop/automat/array-manipulation-functions)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Simple usage.

    arr := ComObjArray(VT_VARIANT:=12, 3)
    arr[0] := "Auto"
    arr[1] := "Hot"
    arr[2] := "key"
    t := ""
    Loop arr.MaxIndex() + 1
        t .= arr[A_Index-1]
    MsgBox t
:::

::: {#ExMultiDims .ex}
[](#ExMultiDims){.ex_number} Multiple dimensions.

    arr := ComObjArray(VT_VARIANT:=12, 3, 4)

    ; Get the number of dimensions:
    dim := DllCall("oleaut32\SafeArrayGetDim", "ptr", ComObjValue(arr))

    ; Get the bounds of each dimension:
    dims := ""
    Loop dim
        dims .= arr.MinIndex(A_Index) " .. " arr.MaxIndex(A_Index) "`n"
    MsgBox dims

    ; Simple usage:
    Loop 3 {
        x := A_Index-1
        Loop 4 {
            y := A_Index-1
            arr[x, y] := x * y
        }
    }
    MsgBox arr[2, 3]
:::
