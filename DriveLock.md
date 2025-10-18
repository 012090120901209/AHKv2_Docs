# DriveLock

Prevents the eject feature of the specified drive from working.

``` Syntax
DriveLock Drive
```

## Parameters {#Parameters}

Drive

:   Type: [String](../Concepts.htm#strings)

    The drive letter followed by a colon and an optional backslash
    (might also work on UNC paths and mapped drives).

## Error Handling {#Error_Handling}

An exception is thrown on failure, such as if *Drive* does not exist or
does not support the locking feature.

## Remarks {#Remarks}

Most drives cannot be \"locked open\". However, locking the drive while
it is open will probably result in it becoming locked the moment it is
closed.

This function has no effect on drives that do not support locking (such
as most read-only drives).

To unlock a drive, call [DriveUnlock](DriveUnlock.htm). If a drive is
locked by a script and that script exits, the drive will stay locked
until another script or program unlocks it, or the system is restarted.

## Related {#Related}

[DriveUnlock](DriveUnlock.htm), [Drive functions](Drive.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Locks the D drive.

    DriveLock "D:"
:::
