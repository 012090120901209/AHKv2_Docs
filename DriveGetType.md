# DriveGetType

Returns the type of the drive which contains the specified path.

``` Syntax
DriveType := DriveGetType(Path)
```

## Parameters {#Parameters}

Path

:   Type: [String](../Concepts.htm#strings)

    Any path contained by the drive (might also work on UNC paths and
    mapped drives).

## Return Value {#Return_Value}

Type: [String](../Concepts.htm#strings)

This function returns the type of the drive which contains *Path*:
Unknown, Removable, Fixed, Network, CDROM, or RAMDisk. If *Path* is
invalid (e.g. because the drive does not exist), the return value is an
empty string.

## Remarks {#Remarks}

In general, *Path* can be any path. Since NTFS supports mounted volumes
and directory junctions, different paths with the same drive letter can
produce different results.

## Related {#Related}

[Drive functions](Drive.htm)

## Examples {#Examples}

See [example #1](Drive.htm#ExAnalyzeDrive) on the [Drive
Functions](Drive.htm) page for a demonstration of this function.
