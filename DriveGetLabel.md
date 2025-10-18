# DriveGetLabel

Returns the volume label of the specified drive.

``` Syntax
Label := DriveGetLabel(Drive)
```

## Parameters {#Parameters}

Drive

:   Type: [String](../Concepts.htm#strings)

    The drive letter followed by a colon and an optional backslash, or a
    UNC name such as `"\server1\share1"`.

## Return Value {#Return_Value}

Type: [String](../Concepts.htm#strings)

This function returns the *Drive*\'s volume label.

## Error Handling {#Error_Handling}

An exception is thrown on failure.

## Related {#Related}

[DriveSetLabel](DriveSetLabel.htm), [Drive functions](Drive.htm)

## Examples {#Examples}

See [example #1](Drive.htm#ExAnalyzeDrive) on the [Drive
Functions](Drive.htm) page for a demonstration of this function.
