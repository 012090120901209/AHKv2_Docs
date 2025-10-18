# DriveGetList

Returns a string of letters, one character for each drive letter in the
system.

``` Syntax
List := DriveGetList(DriveType)
```

## Parameters {#Parameters}

DriveType

:   Type: [String](../Concepts.htm#strings)

    If omitted, all drive types are retrieved. Otherwise, specify one of
    the following words to retrieve only a specific type of drive:
    CDROM, REMOVABLE, FIXED, NETWORK, RAMDISK, UNKNOWN.

## Return Value {#Return_Value}

Type: [String](../Concepts.htm#strings)

This function returns the drive letters in the system, depending on
*DriveType*. For example: ACDEZ.

## Related {#Related}

[Drive functions](Drive.htm)

## Examples {#Examples}

See [example #1](Drive.htm#ExAnalyzeDrive) on the [Drive
Functions](Drive.htm) page for a demonstration of this function.
