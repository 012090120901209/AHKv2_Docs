# DriveEject / DriveRetract

Ejects or retracts the tray of the specified CD/DVD drive. DriveEject
can also eject a removable drive.

``` Syntax
DriveEject Drive
DriveRetract Drive
```

## Parameters {#Parameters}

Drive

:   Type: [String](../Concepts.htm#strings)

    If omitted, it defaults to the first CD/DVD drive found by iterating
    from A to Z (an exception is thrown if no drive is found).
    Otherwise, specify the drive letter optionally followed by a colon
    or a colon and backslash. For example, `"D"`, `"D:"` or `"D:\"`.

    This can also be a device path in the form `"\\?\Volume{...}"`,
    which can be discovered by running
    [mountvol](https://learn.microsoft.com/windows-server/administration/windows-commands/mountvol)
    at the command line. In this case the drive is not required to be
    assigned a drive letter.

## Error Handling {#Error_Handling}

An exception is thrown on failure, if detected.

These functions will probably not work on a network drive or any drive
lacking the \"Eject\" option in Explorer. The underlying system
functions do not always report failure, so an exception may or may not
be thrown.

## Remarks {#Remarks}

This function waits for the ejection or retraction to complete before
allowing the script to continue.

It may be possible to detect the previous tray state by measuring the
time the function takes to complete, as in [the example
below](#ExToggle).

Ejecting a removable drive is generally equivalent to using the
\"Eject\" context menu option in Explorer, except that no warning is
shown if files are in use. Unlike the Safely Remove Hardware option,
this only dismounts the volume identified by the *Drive* parameter, not
the overall device.

DriveEject and DriveRetract correspond to the
[IOCTL_STORAGE_EJECT_MEDIA](https://learn.microsoft.com/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_eject_media)
and
[IOCTL_STORAGE_LOAD_MEDIA](https://learn.microsoft.com/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_load_media)
control codes, which may also have an effect on drive types other than
CD/DVD, such as tape drives.

## Related {#Related}

[DriveGetStatusCD](DriveGetStatusCD.htm), [Drive functions](Drive.htm)

## Examples {#Examples}

::: {#ExEject .ex}
[](#ExEject){.ex_number} Ejects (opens) the tray of the first CD/DVD
drive.

    DriveEject()
:::

::: {#ExRetract .ex}
[](#ExRetract){.ex_number} Retracts (closes) the tray of the first
CD/DVD drive.

    DriveRetract()
:::

::: {#ExEjectAll .ex}
[](#ExEjectAll){.ex_number} Ejects all removable drives (except CD/DVD
drives).

    Loop Parse DriveGetList("REMOVABLE")
    {
        if MsgBox("Eject " A_LoopField ":, even if files are open?",, "y/n") = "yes"
            DriveEject(A_LoopField)
    }
    else
        MsgBox "No removable drives found."
:::

::: {#ExToggle .ex}
[](#ExToggle){.ex_number} Defines a hotkey which toggles the tray to the
opposite state (open or closed), based on the time the function takes to
complete.

    #c::
    {
        DriveEject
        ; If the function completed quickly, the tray was probably already ejected.
        ; In that case, retract it:
        if (A_TimeSinceThisHotkey < 1000)  ; Adjust this time if needed.
            DriveRetract
    }
:::
