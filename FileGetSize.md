# FileGetSize

Retrieves the size of a file.

``` Syntax
Size := FileGetSize(Filename, Units)
```

## Parameters {#Parameters}

Filename

:   Type: [String](../Concepts.htm#strings)

    If omitted, the current file of the innermost enclosing [file
    loop](LoopFiles.htm) will be used. Otherwise, specify the name of
    the target file, which is assumed to be in
    [A_WorkingDir](../Variables.htm#WorkingDir) if an absolute path
    isn\'t specified.

Units

:   Type: [String](../Concepts.htm#strings)

    If blank or omitted, it defaults to B. Otherwise, specify one of the
    following letters to cause the result to be returned in specific
    units:

    -   B = Bytes
    -   K = Kilobytes
    -   M = Megabytes

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers)

This function returns the size of the specified file (rounded down to
the nearest whole number).

## Error Handling {#Error_Handling}

An [OSError](Error.htm#OSError) is thrown on failure.

[A_LastError](../Variables.htm#LastError) is set to the result of the
operating system\'s GetLastError() function.

## Remarks {#Remarks}

Files of any size are supported, even those over 4 gigabytes, and even
if *Units* is bytes.

If the target file is a directory, the size will be reported as whatever
the OS believes it to be (probably zero in all cases).

To calculate the size of folder, including all its files, follow this
example:

    FolderSize := 0
    WhichFolder := DirSelect()  ; Ask the user to pick a folder.
    Loop Files, WhichFolder "\*.*", "R"
        FolderSize += A_LoopFileSize
    MsgBox "Size of " WhichFolder " is " FolderSize " bytes."

## Related {#Related}

[FileGetAttrib](FileGetAttrib.htm), [FileSetAttrib](FileSetAttrib.htm),
[FileGetTime](FileGetTime.htm), [FileSetTime](FileSetTime.htm),
[FileGetVersion](FileGetVersion.htm), [file loop](LoopFiles.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Retrieves the size in bytes and stores it in
`Size`{.variable}.

    Size := FileGetSize("C:\My Documents\test.doc")
:::

::: {#ExKB .ex}
[](#ExKB){.ex_number} Retrieves the size in kilobytes and stores it in
`Size`{.variable}.

    Size := FileGetSize("C:\My Documents\test.doc", "K")
:::
