# IniRead

Reads a value, section or list of section names from a standard format
.ini file.

``` Syntax
Value := IniRead(Filename, Section, Key , Default)
Section := IniRead(Filename, Section)
SectionNames := IniRead(Filename)
```

## Parameters {#Parameters}

Filename

:   Type: [String](../Concepts.htm#strings)

    The name of the .ini file, which is assumed to be in
    [A_WorkingDir](../Variables.htm#WorkingDir) if an absolute path
    isn\'t specified.

Section

:   Type: [String](../Concepts.htm#strings)

    The section name in the .ini file, which is the heading phrase that
    appears in square brackets (do not include the brackets in this
    parameter).

Key

:   Type: [String](../Concepts.htm#strings)

    The key name in the .ini file.

Default

:   Type: [String](../Concepts.htm#strings)

    If omitted, an [OSError](Error.htm#OSError) is thrown on failure.
    Otherwise, specify the value to return on failure, such as if the
    requested key, section or file is not found.

## Return Value {#Return_Value}

Type: [String](../Concepts.htm#strings)

This function returns the actual value of the specified key. If the
value cannot be retrieved, the default value indicated by the *Default*
parameter is returned.

If the *Key* parameter is omitted, this function returns an entire
section. Comments and empty lines are omitted. Only the first 65,533
characters of the section are retrieved.

If the *Key* and *Section* parameters are omitted, this function returns
a linefeed (`` `n ``) delimited list of section names.

## Error Handling {#Error_Handling}

An [OSError](Error.htm#OSError) is thrown on failure, but only if
*Default* is omitted.

Regardless of whether an exception is thrown,
[A_LastError](../Variables.htm#LastError) is set to the result of the
operating system\'s GetLastError() function.

## Remarks {#Remarks}

The operating system automatically omits leading and trailing
spaces/tabs from the retrieved string. To prevent this, enclose the
string in single or double quote marks. The outermost set of single or
double quote marks is also omitted, but any spaces inside the quote
marks are preserved.

Values longer than 65,535 characters are likely to yield inconsistent
results.

A standard ini file looks like:

    [SectionName]
    Key=Value

**Unicode:** IniRead and IniWrite rely on the external functions
[GetPrivateProfileString](https://learn.microsoft.com/windows/win32/api/winbase/nf-winbase-getprivateprofilestring)
and
[WritePrivateProfileString](https://learn.microsoft.com/windows/win32/api/winbase/nf-winbase-writeprivateprofilestringa)
to read and write values. These functions support Unicode only in UTF-16
files; all other files are assumed to use the system\'s default ANSI
code page.

## Related {#Related}

[IniDelete](IniDelete.htm), [IniWrite](IniWrite.htm),
[RegRead](RegRead.htm), [file-reading loop](LoopRead.htm),
[FileRead](FileRead.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Reads the value of a key located in section2
from a standard format .ini file and stores it in `Value`{.variable}.

    Value := IniRead("C:\Temp\myfile.ini", "section2", "key")
    MsgBox "The value is " Value
:::
