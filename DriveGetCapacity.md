# DriveGetCapacity

Returns the total capacity of the drive which contains the specified
path, in megabytes.

``` Syntax
Capacity := DriveGetCapacity(Path)
```

## Parameters {#Parameters}

Path

:   Type: [String](../Concepts.htm#strings)

    Any path contained by the drive (might also work on UNC paths and
    mapped drives).

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers)

This function returns the total capacity of the drive which contains
*Path*, in megabytes.

## Error Handling {#Error_Handling}

An exception is thrown on failure.

## Remarks {#Remarks}

In general, *Path* can be any path. Since NTFS supports mounted volumes
and directory junctions, different paths with the same drive letter can
produce different amounts of capacity.

## Related {#Related}

[DriveGetSpaceFree](DriveGetSpaceFree.htm), [Drive functions](Drive.htm)

## Examples {#Examples}

See [example #1](Drive.htm#ExAnalyzeDrive) on the [Drive
Functions](Drive.htm) page for a demonstration of this function.
