# SoundSetMute

Changes a mute setting of a sound device.

``` Syntax
SoundSetMute NewSetting , Component, Device
```

## Parameters {#Parameters}

NewSetting

:   Type: [Integer](../Concepts.htm#numbers)

    One of the following values:

    -   `1` or `True` turns on the setting
    -   `0` or `False` turns off the setting
    -   `-1` toggles the setting (sets it to the opposite of its current
        state)

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

## Error Handling {#Error_Handling}

A [TargetError](Error.htm#TargetError) is thrown if the device or
component could not be found or if the component does not support this
control type. Otherwise, an [OSError](Error.htm#OSError) is thrown on
failure.

## Remarks {#Remarks}

An alternative way to toggle the master mute setting of the default
playback device is to have the script send a keystroke, such as in the
example below:

    Send "{Volume_Mute}"  ; Mute/unmute the master volume.

To discover the capabilities of the sound devices installed on the
system \-- such as the names and available components \-- run the
[soundcard analysis script](Sound.htm#ExSoundcard).

Use [SoundGetMute](SoundGetMute.htm) to retrieve the current mute
setting.

## Related {#Related}

[Sound Functions](Sound.htm)

## Examples {#Examples}

::: {#ExMuteOn .ex}
[](#ExMuteOn){.ex_number} Turns on the master mute.

    SoundSetMute true
:::

::: {#ExMuteOff .ex}
[](#ExMuteOff){.ex_number} Turns off the master mute.

    SoundSetMute false
:::

::: {#ExMuteToggle .ex}
[](#ExMuteToggle){.ex_number} Toggles the master mute (sets it to the
opposite of its current state).

    SoundSetMute -1
:::

::: {#ExMuteLineIn .ex}
[](#ExMuteLineIn){.ex_number} Mutes Line In.

    SoundSetMute true, "Line In"
:::

::: {#ExMuteMicRecord .ex}
[](#ExMuteMicRecord){.ex_number} Mutes microphone recording.

    SoundSetMute true,, "Microphone"
:::
