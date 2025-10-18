# Drive Functions

Functions for retrieving information about the computer\'s drive(s) or
for performing various operations on a drive. Click on a function name
for details.

  Function                                       Description
  ---------------------------------------------- -------------------------------------------------------------------------------------------
  [DriveEject](DriveEject.htm)                   Ejects the tray of the specified CD/DVD drive, or ejects a removable drive.
  [DriveGetCapacity](DriveGetCapacity.htm)       Returns the total capacity of the drive which contains the specified path, in megabytes.
  [DriveGetFileSystem](DriveGetFileSystem.htm)   Returns the type of the specified drive\'s file system.
  [DriveGetLabel](DriveGetLabel.htm)             Returns the volume label of the specified drive.
  [DriveGetList](DriveGetList.htm)               Returns a string of letters, one character for each drive letter in the system.
  [DriveGetSerial](DriveGetSerial.htm)           Returns the volume serial number of the specified drive.
  [DriveGetSpaceFree](DriveGetSpaceFree.htm)     Returns the free disk space of the drive which contains the specified path, in megabytes.
  [DriveGetStatus](DriveGetStatus.htm)           Returns the status of the drive which contains the specified path.
  [DriveGetStatusCD](DriveGetStatusCD.htm)       Returns the media status of the specified CD/DVD drive.
  [DriveGetType](DriveGetType.htm)               Returns the type of the drive which contains the specified path.
  [DriveLock](DriveLock.htm)                     Prevents the eject feature of the specified drive from working.
  [DriveRetract](DriveEject.htm)                 Retracts the tray of the specified CD/DVD drive.
  [DriveSetLabel](DriveSetLabel.htm)             Changes the volume label of the specified drive.
  [DriveUnlock](DriveUnlock.htm)                 Restores the eject feature of the specified drive.

## Error Handling {#Error_Handling}

An exception is thrown on failure.

## Related {#Related}

[List of all functions](index.htm)

## Examples {#Examples}

::: {#ExAnalyzeDrive .ex}
[](#ExAnalyzeDrive){.ex_number} Allows the user to select a drive in
order to analyze it.

    folder := DirSelect( , 3, "Pick a drive to analyze:")
    if not folder
        return
    MsgBox
    (
        "All Drives: " DriveGetList() "
        Selected Drive: " folder "
        Drive Type: " DriveGetType(folder) "
        Status: " DriveGetStatus(folder) "
        Capacity: " DriveGetCapacity(folder) " MB
        Free Space: " DriveGetSpaceFree(folder) " MB
        Filesystem: " DriveGetFilesystem(folder) "
        Volume Label: " DriveGetLabel(folder) "
        Serial Number: " DriveGetSerial(folder)
    )
:::
