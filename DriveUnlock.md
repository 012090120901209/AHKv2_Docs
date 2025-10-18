# DriveUnlock

Restores the eject feature of the specified drive.

``` Syntax
DriveUnlock Drive
```

## Parameters {#Parameters}

Drive

:   Type: [String](../Concepts.htm#strings)

    The drive letter followed by a colon and an optional backslash
    (might also work on UNC paths and mapped drives).

## Error Handling {#Error_Handling}

An exception is thrown on failure.

## Remarks {#Remarks}

This function needs to be called multiple times if the drive was locked
multiple times (at least for some drives). For example, if
`DriveLock("D:")` was called three times, `DriveUnlock("D:")` might need
to be called three times to unlock it. Because of this and the fact that
there is no way to determine whether a drive is currently locked, it is
often useful to keep track of its lock-state in a
[variable](../Variables.htm).

## Related {#Related}

[DriveLock](DriveLock.htm), [Drive functions](Drive.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Unlocks the D drive.

    DriveUnlock "D:"
:::
