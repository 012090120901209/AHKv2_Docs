# ComObjValue

Retrieves the value or pointer stored in a COM wrapper object.

``` Syntax
Value := ComObjValue(ComObj)
```

## Parameters {#Parameters}

ComObj

:   Type: [Object](../Concepts.htm#objects)

    A wrapper object containing a COM object or typed value. See
    [ComValue](ComValue.htm) for details.

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers)

This function returns a 64-bit signed integer.

## Error Handling {#Error_Handling}

A [TypeError](Error.htm#TypeError) is thrown if *ComObj* is not a COM
wrapper object.

## Remarks {#Remarks}

This function is not intended for general use.

Calling ComObjValue is equivalent to *`variant`*`.llVal`, where *ComObj*
is treated as a [VARIANT
structure](https://learn.microsoft.com/windows/win32/api/oaidl/ns-oaidl-variant).
Any script which uses this function must be aware what [type of
value](ComObjType.htm) the wrapper object contains and how it should be
treated. For instance, if an interface pointer is returned,
[Release](ObjAddRef.htm) should not be called, but
[AddRef](ObjAddRef.htm) may be required depending on what the script
does with the pointer.

## Related {#Related}

[ComObjType](ComObjType.htm), [ComObject](ComObject.htm),
[ComObjGet](ComObjGet.htm), [ComObjActive](ComObjActive.htm)
