# DriveGetStatusCD

Returns the media status of the specified CD/DVD drive.

``` Syntax
CDStatus := DriveGetStatusCD(Drive)
```

## Parameters {#Parameters}

Drive

:   Type: [String](../Concepts.htm#strings)

    If omitted, the default CD/DVD drive will be used. Otherwise,
    specify the drive letter followed by a colon.

## Return Value {#Return_Value}

Type: [String](../Concepts.htm#strings)

This function returns the *Drive*\'s media status:

  Status      Meaning
  ----------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  not ready   The drive is not ready to be accessed, perhaps due to being engaged in a write operation. Known limitation: \"not ready\" also occurs when the drive contains a DVD rather than a CD.
  open        The drive contains no disc, or the tray is ejected.
  playing     The drive is playing a disc.
  paused      The previously playing audio or video is now paused.
  seeking     The drive is seeking.
  stopped     The drive contains a CD but is not currently accessing it.

## Error Handling {#Error_Handling}

An exception is thrown on failure.

## Remarks {#Remarks}

This function will probably not work on a network drive or non-CD/DVD
drive. If it fails in such cases or for any other reason, an exception
is thrown.

If the tray was recently closed, there may be a delay before the
function completes.

## Related {#Related}

[DriveEject](DriveEject.htm), [Drive functions](Drive.htm)

## Examples {#Examples}

See [example #1](Drive.htm#ExAnalyzeDrive) on the [Drive
Functions](Drive.htm) page for a demonstration of this function.
