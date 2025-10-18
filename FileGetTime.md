# FileGetTime

Retrieves the datetime stamp of a file or folder.

``` Syntax
Timestamp := FileGetTime(Filename, WhichTime)
```

## Parameters {#Parameters}

Filename

:   Type: [String](../Concepts.htm#strings)

    If omitted, the current file of the innermost enclosing [file
    loop](LoopFiles.htm) will be used. Otherwise, specify the name of
    the target file or folder, which is assumed to be in
    [A_WorkingDir](../Variables.htm#WorkingDir) if an absolute path
    isn\'t specified.

WhichTime

:   Type: [String](../Concepts.htm#strings)

    If blank or omitted, it defaults to M. Otherwise, specify one of the
    following letters to set which timestamp should be retrieved:

    -   M = Modification time
    -   C = Creation time
    -   A = Last access time

## Return Value {#Return_Value}

Type: [String](../Concepts.htm#strings)

This function returns a string of digits in the
[YYYYMMDDHH24MISS](FileSetTime.htm#YYYYMMDD) format. The time is your
own local time, not UTC/GMT. This string should not be treated as a
number, i.e. one should not perform math on it or compare it
numerically.

## Error Handling {#Error_Handling}

An [OSError](Error.htm#OSError) is thrown on failure.

[A_LastError](../Variables.htm#LastError) is set to the result of the
operating system\'s GetLastError() function.

## Remarks {#Remarks}

See [YYYYMMDDHH24MISS](FileSetTime.htm#YYYYMMDD) for an explanation of
dates and times.

## Related {#Related}

[FileSetTime](FileSetTime.htm), [FormatTime](FormatTime.htm),
[FileGetAttrib](FileGetAttrib.htm), [FileSetAttrib](FileSetAttrib.htm),
[FileGetSize](FileGetSize.htm), [FileGetVersion](FileGetVersion.htm),
[file loop](LoopFiles.htm), [DateAdd](DateAdd.htm),
[DateDiff](DateDiff.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Retrieves the modification time and stores it
in `Timestamp`{.variable}.

    Timestamp := FileGetTime("C:\My Documents\test.doc")
:::

::: {#ExC .ex}
[](#ExC){.ex_number} Retrieves the creation time and stores it in
`Timestamp`{.variable}.

    Timestamp := FileGetTime("C:\My Documents\test.doc", "C")
:::
