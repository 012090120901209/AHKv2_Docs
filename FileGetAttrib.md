# FileGetAttrib

Reports whether a file or folder is read-only, hidden, etc.

``` Syntax
AttributeString := FileGetAttrib(Filename)
```

## Parameters {#Parameters}

Filename

:   Type: [String](../Concepts.htm#strings)

    If omitted, the current file of the innermost enclosing [file
    loop](LoopFiles.htm) will be used. Otherwise, specify the name of
    the target file, which is assumed to be in
    [A_WorkingDir](../Variables.htm#WorkingDir) if an absolute path
    isn\'t specified. Unlike [FileExist](FileExist.htm) and
    [DirExist](DirExist.htm), this must be a true filename, not a
    pattern.

## Return Value {#Return_Value}

Type: [String](../Concepts.htm#strings)

This function returns the attributes of the file or folder. This string
is a subset of `RASHNDOCTL`, where each letter means the following:

-   R = READONLY
-   A = ARCHIVE
-   S = SYSTEM
-   H = HIDDEN
-   N = NORMAL
-   D = DIRECTORY
-   O = OFFLINE
-   C = COMPRESSED
-   T = TEMPORARY
-   L = REPARSE_POINT (typically a symbolic link)

## Error Handling {#Error_Handling}

An [OSError](Error.htm#OSError) is thrown on failure.

[A_LastError](../Variables.htm#LastError) is set to the result of the
operating system\'s GetLastError() function.

## Remarks {#Remarks}

To check if a particular attribute is present in the retrieved string,
see [example #2](#ExIf) below.

On a related note, to retrieve a file\'s 8.3 short name, follow this
example:

    Loop Files, "C:\My Documents\Address List.txt"
        ShortPathName := A_LoopFileShortPath  ; Will yield something similar to C:\MYDOCU~1\ADDRES~1.txt

A similar method can be used to get the long name of an 8.3 short name.

## Related {#Related}

[FileExist](FileExist.htm), [DirExist](DirExist.htm),
[FileSetAttrib](FileSetAttrib.htm), [FileGetTime](FileGetTime.htm),
[FileSetTime](FileSetTime.htm), [FileGetSize](FileGetSize.htm),
[FileGetVersion](FileGetVersion.htm), [file loop](LoopFiles.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Stores the attribute letters of a directory in
`OutputVar`{.variable}. Note that existing directories always have the
attribute letter D.

    OutputVar := FileGetAttrib("C:\New Folder")
:::

::: {#ExIf .ex}
[](#ExIf){.ex_number} Checks if the Hidden attribute is present in the
retrieved string.

    if InStr(FileGetAttrib("C:\My File.txt"), "H")
        MsgBox "The file is hidden."
:::
