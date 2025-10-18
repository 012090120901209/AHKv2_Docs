# ComObjGet

Returns a reference to an object provided by a COM component.

``` Syntax
ComObj := ComObjGet(Name)
```

## Parameters {#Parameters}

Name

:   Type: [String](../Concepts.htm#strings)

    The display name of the object to be retrieved. See
    [MkParseDisplayName (Microsoft
    Docs)](https://learn.microsoft.com/windows/win32/api/objbase/nf-objbase-mkparsedisplayname)
    for more information.

## Return Value {#Return_Value}

Type: [ComObject](ComObject.htm)

This function returns a new COM wrapper object with the [variant
type](ComObjType.htm#vt) VT_DISPATCH (9).

## Error Handling {#Error_Handling}

An exception is thrown on failure.

## Related {#Related}

[ComObject](ComObject.htm), [ComObjActive](ComObjActive.htm),
[ComObjConnect](ComObjConnect.htm), [ComObjQuery](ComObjQuery.htm),
[CoGetObject (Microsoft
Docs)](https://learn.microsoft.com/windows/win32/api/objbase/nf-objbase-cogetobject)

## Examples {#Examples}

::: {#exwmi .ex}
[](#exwmi){.ex_number} Press [Shift]{.kbd}+[Esc]{.kbd} to show the
command line which was used to launch the active window\'s process. For
Win32_Process, see [Microsoft
Docs](https://learn.microsoft.com/windows/win32/cimwin32prov/win32-process).

    +Esc::
    {
        pid := WinGetPID("A")
        ; Get WMI service object.
        wmi := ComObjGet("winmgmts:")
        ; Run query to retrieve matching process(es).
        queryEnum := wmi.ExecQuery(""
            . "Select * from Win32_Process where ProcessId=" . pid)
            ._NewEnum()
        ; Get first matching process.
        if queryEnum(&proc)
            MsgBox(proc.CommandLine, "Command line", 0)
        else
            MsgBox("Process not found!")
    }
:::
