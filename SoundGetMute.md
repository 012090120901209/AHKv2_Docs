# SoundGetMute

Retrieves a mute setting of a sound device.

``` Syntax
Setting := SoundGetMute(Component, Device)
```

## Parameters {#Parameters}

Component

:   Type: [String](../Concepts.htm#strings) or
    [Integer](../Concepts.htm#numbers)

    If blank or omitted, it defaults to the master mute setting.
    Otherwise, specify the component\'s display name and/or index, e.g.
    `1`, `"Line in"` or `"Line in:2"`.

    For further details, see [Component (Sound
    Functions)](Sound.htm#component).

Device

:   Type: [String](../Concepts.htm#strings) or
    [Integer](../Concepts.htm#numbers)

    If blank or omitted, it defaults to the system\'s default device for
    playback (which is not necessarily device 1). Otherwise, specify the
    device\'s display name and/or index, e.g. `1`, `"Speakers"`,
    `"Speakers:2"` or `"Speakers (Example HD Audio)"`.

    For further details, see [Device (Sound
    Functions)](Sound.htm#device).

## Return Value {#Return_Value}

Type: [Integer (boolean)](../Concepts.htm#boolean)

This function returns 0 (false) for unmuted or 1 (true) for muted.

## Error Handling {#Error_Handling}

A [TargetError](Error.htm#TargetError) is thrown if the device or
component could not be found or if the component does not support this
control type. Otherwise, an [OSError](Error.htm#OSError) is thrown on
failure.

## Remarks {#Remarks}

To discover the capabilities of the sound devices installed on the
system \-- such as the names and available components \-- run the
[soundcard analysis script](Sound.htm#ExSoundcard).

## Related {#Related}

[Sound Functions](Sound.htm)

## Examples {#Examples}

::: {#ExMasterMute .ex}
[](#ExMasterMute){.ex_number} Checks whether the default playback device
is muted.

    master_mute := SoundGetMute()
    if master_mute
        MsgBox "The default playback device is muted."
    else
        MsgBox "The default playback device is not muted."
:::

::: {#ExLineInMute .ex}
[](#ExLineInMute){.ex_number} Checks whether \"Line In pass-through\" is
muted.

    if SoundGetMute("Line In") = 0
        MsgBox "Line In pass-through is not muted."
:::

::: {#ExMicRecordMute .ex}
[](#ExMicRecordMute){.ex_number} Checks whether the microphone
(recording) is muted.

    if SoundGetMute( , "Microphone") = 0
        MsgBox "The microphone (recording) is not muted."
:::
