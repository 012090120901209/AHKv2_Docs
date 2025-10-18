# DriveSetLabel

Changes the volume label of the specified drive.

``` Syntax
DriveSetLabel Drive , NewLabel
```

## Parameters {#Parameters}

Drive

:   Type: [String](../Concepts.htm#strings)

    The drive letter followed by a colon and an optional backslash
    (might also work on UNC paths and mapped drives).

NewLabel

:   Type: [String](../Concepts.htm#strings)

    If omitted, the drive will have no label. Otherwise, specify the new
    label to set.

## Error Handling {#Error_Handling}

An exception is thrown on failure.

## Related {#Related}

[DriveGetLabel](DriveGetLabel.htm), [Drive functions](Drive.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Changes the volume label of the C drive.

    DriveSetLabel "C:", "Seagate200"
:::
