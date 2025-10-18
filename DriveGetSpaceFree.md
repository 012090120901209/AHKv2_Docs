# DriveGetSpaceFree

Returns the free disk space of the drive which contains the specified
path, in megabytes.

``` Syntax
FreeSpace := DriveGetSpaceFree(Path)
```

## Parameters {#Parameters}

Path

:   Type: [String](../Concepts.htm#strings)

    Any path contained by the drive (might also work on UNC paths and
    mapped drives).

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers)

This function returns the free disk space of the drive which contains
*Path*, in megabytes (rounded down to the nearest megabyte).

## Error Handling {#Error_Handling}

An exception is thrown on failure.

## Remarks {#Remarks}

In general, *Path* can be any path. Since NTFS supports mounted volumes
and directory junctions, different paths with the same drive letter can
produce different amounts of free space.

## Related {#Related}

[DriveGetCapacity](DriveGetCapacity.htm), [Drive functions](Drive.htm)

## Examples {#Examples}

::: {#ExPath .ex}
[](#ExPath){.ex_number} Retrieves and reports the free disk space of the
drive which contains [A_MyDocuments](../Variables.htm#MyDocuments).

    FreeSpace := DriveGetSpaceFree(A_MyDocuments)
    MsgBox FreeSpace " MB"
:::

See [example #1](Drive.htm#ExAnalyzeDrive) on the [Drive
Functions](Drive.htm) page for another demonstration of this function.
