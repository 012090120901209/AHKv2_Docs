# FileRecycleEmpty

Empties the recycle bin.

``` Syntax
FileRecycleEmpty DriveLetter
```

## Parameters {#Parameters}

DriveLetter

:   Type: [String](../Concepts.htm#strings)

    If omitted, the recycle bin for all drives is emptied. Otherwise,
    specify a drive letter such as `"C:\"`.

## Error Handling {#Error_Handling}

An [OSError](Error.htm#OSError) is thrown on failure.

## Related {#Related}

[FileRecycle](FileRecycle.htm), [FileDelete](FileDelete.htm),
[FileCopy](FileCopy.htm), [FileMove](FileMove.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Empties the recycle bin of the C drive.

    FileRecycleEmpty "C:\"
:::
