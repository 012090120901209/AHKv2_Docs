# SoundGetVolume

Retrieves a volume setting of a sound device.

``` Syntax
Setting := SoundGetVolume(Component, Device)
```

## Parameters {#Parameters}

Component

:   Type: [String](../Concepts.htm#strings) or
    [Integer](../Concepts.htm#numbers)

    If blank or omitted, it defaults to the master volume setting.
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

Type: [Float](../Concepts.htm#numbers)

This function returns a floating point number between 0.0 and 100.0.

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

::: {#ExMasterVol .ex}
[](#ExMasterVol){.ex_number} Retrieves and reports the master volume.

    master_volume := SoundGetVolume()
    MsgBox "Master volume is " master_volume " percent."
:::

::: {#ExMicListenVol .ex}
[](#ExMicListenVol){.ex_number} Retrieves and reports the microphone
listening volume.

    mic_volume := SoundGetVolume("Microphone")
    MsgBox "Microphone listening volume is " mic_volume " percent."
:::

::: {#ExMicRecordVol .ex}
[](#ExMicRecordVol){.ex_number} Retrieves and reports the microphone
recording volume.

    mic_volume := SoundGetVolume( , "Microphone")
    MsgBox "Microphone recording volume is " mic_volume " percent."
:::
