# DriveGetFileSystem

Returns the type of the specified drive\'s file system.

``` Syntax
FileSystem := DriveGetFileSystem(Drive)
```

## Parameters {#Parameters}

Drive

:   Type: [String](../Concepts.htm#strings)

    The drive letter followed by a colon and an optional backslash, or a
    UNC name such as `"\server1\share1"`.

## Return Value {#Return_Value}

Type: [String](../Concepts.htm#strings)

This function returns the type of *Drive*\'s file system. The possible
values are defined by the system; they include (but are not limited to)
the following: NTFS, FAT32, FAT, CDFS (typically indicates a CD), or UDF
(typically indicates a DVD).

## Error Handling {#Error_Handling}

An exception is thrown on failure, such as if the drive does not contain
formatted media.

## Related {#Related}

[Drive functions](Drive.htm)

## Examples {#Examples}

See [example #1](Drive.htm#ExAnalyzeDrive) on the [Drive
Functions](Drive.htm) page for a demonstration of this function.
