# ComObjActive

Retrieves a registered COM object.

``` Syntax
ComObj := ComObjActive(CLSID)
```

## Parameters {#Parameters}

CLSID

:   Type: [String](../Concepts.htm#strings)

    CLSID or human-readable Prog ID of the COM object to retrieve.

## Return Value {#Return_Value}

Type: [ComObject](ComObject.htm)

This function returns a new COM wrapper object with the [variant
type](ComObjType.htm#vt) VT_DISPATCH (9).

## Error Handling {#Error_Handling}

An exception is thrown on failure.

## Related {#Related}

[ComValue](ComValue.htm), [ComObject](ComObject.htm),
[ComObjGet](ComObjGet.htm), [ComObjConnect](ComObjConnect.htm),
[ComObjFlags](ComObjFlags.htm), [ObjAddRef/ObjRelease](ObjAddRef.htm),
[ComObjQuery](ComObjQuery.htm), [GetActiveObject (Microsoft
Docs)](https://learn.microsoft.com/windows/win32/api/oleauto/nf-oleauto-getactiveobject)

## Examples {#Examples}

::: {#ExWord .ex}
[](#ExWord){.ex_number} Displays the active document in Microsoft Word,
if it is running. For details about the COM object and its properties
used below, see [Word.Application object (Microsoft
Docs)](https://learn.microsoft.com/office/vba/api/Word.Application).

    word := ComObjActive("Word.Application")
    if !word
        MsgBox "Word isn't open."
    else
        MsgBox word.ActiveDocument.FullName
:::
