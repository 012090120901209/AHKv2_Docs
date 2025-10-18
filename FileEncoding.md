# FileEncoding

Sets the default encoding for [FileRead](FileRead.htm), [Loop
Read](LoopRead.htm), [FileAppend](FileAppend.htm), and
[FileOpen](FileOpen.htm).

``` Syntax
FileEncoding Encoding
```

## Parameters {#Parameters}

Encoding

:   Type: [String](../Concepts.htm#strings) or
    [Integer](../Concepts.htm#numbers)

    Specify one of the following values:

    **CP0** or empty string: The system default ANSI code page. See
    remarks below.

    **UTF-8:** Unicode UTF-8, equivalent to CP65001.

    **UTF-8-RAW:** As above, but no byte order mark is written when a
    new file is created.

    **UTF-16:** Unicode UTF-16 with little endian byte order, equivalent
    to CP1200.

    **UTF-16-RAW:** As above, but no byte order mark is written when a
    new file is created.

    **CP*nnn*:** A code page with numeric identifier *nnn*. See [Code
    Page
    Identifiers](https://learn.microsoft.com/windows/win32/intl/code-page-identifiers).

    ***nnn*:** A numeric code page identifier.

## Return Value {#Return_Value}

Type: [String](../Concepts.htm#strings)

This function returns the previous setting.

## Remarks {#Remarks}

If FileEncoding is not used, the default encoding is CP0.

CP0 does not universally identify a single code page; rather, it
corresponds to the system default ANSI code page, which depends on the
system locale or \"language for non-Unicode programs\" system setting.
To get the actual code page number, call `DllCall("GetACP")`.

The built-in variable **A_FileEncoding** contains the current setting.

Every newly launched [thread](../misc/Threads.htm) (such as a
[hotkey](../Hotkeys.htm), [custom menu item](Menu.htm), or
[timed](SetTimer.htm) subroutine) starts off fresh with the default
setting for this function. That default may be changed by using this
function during [script startup](../Scripts.htm#auto).

The default encoding is not used if a UTF-8 or UTF-16 byte order mark is
present in the file, unless the file is being opened with write-only
access (i.e. the previous contents of the file are being discarded).

## Related {#Related}

[FileOpen](FileOpen.htm), [StrGet](StrGet.htm), [StrPut](StrPut.htm),
[Reading Binary Data](FileRead.htm#Binary)
