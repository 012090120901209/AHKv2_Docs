# DriveGetSerial

Returns the volume serial number of the specified drive.

``` Syntax
Serial := DriveGetSerial(Drive)
```

## Parameters {#Parameters}

Drive

:   Type: [String](../Concepts.htm#strings)

    The drive letter followed by a colon and an optional backslash, or a
    UNC name such as `"\server1\share1"`.

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers)

This function returns the *Drive*\'s volume serial number. See
[Format](Format.htm) for how to convert it to hexadecimal.

## Error Handling {#Error_Handling}

An exception is thrown on failure.

## Related {#Related}

[Drive functions](Drive.htm)

## Examples {#Examples}

See [example #1](Drive.htm#ExAnalyzeDrive) on the [Drive
Functions](Drive.htm) page for a demonstration of this function.
