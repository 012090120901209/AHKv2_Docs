# DirDelete

Deletes a folder.

``` Syntax
DirDelete DirName , Recurse
```

## Parameters {#Parameters}

DirName

:   Type: [String](../Concepts.htm#strings)

    Name of the directory to delete, which is assumed to be in
    [A_WorkingDir](../Variables.htm#WorkingDir) if an absolute path
    isn\'t specified.

Recurse

:   Type: [Boolean](../Concepts.htm#boolean)

    If omitted, it defaults to false.

    If **false**, files and subdirectories contained in *DirName* are
    [not]{.underline} removed. In this case, if *DirName* is not empty,
    no action is taken and an exception is thrown.

    If **true**, all files and subdirectories are removed (like the
    Windows command \"rmdir /S\").

## Error Handling {#Error_Handling}

An exception is thrown if an error occurs.

## Related {#Related}

[DirCreate](DirCreate.htm), [FileDelete](FileDelete.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Removes the directory, but only if it is empty.

    DirDelete "C:\Download Temp"
:::

::: {#ExRecurse .ex}
[](#ExRecurse){.ex_number} Removes the directory including its files and
subdirectories.

    DirDelete "C:\Download Temp", true
:::
