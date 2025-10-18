# DriveGetStatus

Returns the status of the drive which contains the specified path.

``` Syntax
Status := DriveGetStatus(Path)
```

## Parameters {#Parameters}

Path

:   Type: [String](../Concepts.htm#strings)

    Any path contained by the drive (might also work on UNC paths and
    mapped drives).

## Return Value {#Return_Value}

Type: [String](../Concepts.htm#strings)

This function returns the status of the drive which contains *Path*:

  Status     Notes
  ---------- ----------------------------------------------------------------------------------
  Unknown    Might indicate unformatted/RAW file system.
  Ready      This is the most common.
  NotReady   Typical for removable drives that don\'t contain media.
  Invalid    *Path* does not exist or is a network drive that is presently inaccessible, etc.

## Error Handling {#Error_Handling}

An exception is thrown on failure.

## Remarks {#Remarks}

In general, *Path* can be any path. Since NTFS supports mounted volumes
and directory junctions, different paths with the same drive letter can
produce different results.

## Related {#Related}

[Drive functions](Drive.htm)

## Examples {#Examples}

See [example #1](Drive.htm#ExAnalyzeDrive) on the [Drive
Functions](Drive.htm) page for a demonstration of this function.
