# IniDelete

Deletes a value from a standard format .ini file.

``` Syntax
IniDelete Filename, Section , Key
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

    If omitted, the entire section will be deleted. Otherwise, specify
    the key name in the .ini file.

## Error Handling {#Error_Handling}

An [OSError](Error.htm#OSError) is thrown on failure.

Regardless of whether an exception is thrown,
[A_LastError](../Variables.htm#LastError) is set to the result of the
operating system\'s GetLastError() function.

## Remarks {#Remarks}

A standard ini file looks like:

    [SectionName]
    Key=Value

## Related {#Related}

[IniRead](IniRead.htm), [IniWrite](IniWrite.htm),
[RegDelete](RegDelete.htm), [RegDeleteKey](RegDeleteKey.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Deletes a key and its value located in section2
from a standard format .ini file.

    IniDelete "C:\Temp\myfile.ini", "section2", "key"
:::
