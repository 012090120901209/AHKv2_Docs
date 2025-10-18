# DirCreate

Creates a folder.

``` Syntax
DirCreate DirName
```

## Parameters {#Parameters}

DirName

:   Type: [String](../Concepts.htm#strings)

    Name of the directory to create, which is assumed to be in
    [A_WorkingDir](../Variables.htm#WorkingDir) if an absolute path
    isn\'t specified.

## Error Handling {#Error_Handling}

An [OSError](Error.htm#OSError) is thrown if an error occurs.

[A_LastError](../Variables.htm#LastError) is set to the result of the
operating system\'s GetLastError() function.

## Remarks {#Remarks}

This function will also create all parent directories given in *DirName*
if they do not already exist.

## Related {#Related}

[DirDelete](DirDelete.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Creates a new directory, including its parent
directories if necessary.

    DirCreate "C:\Test1\My Images\Folder2"
:::
