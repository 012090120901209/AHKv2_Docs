# SoundSetVolume

Changes a volume setting of a sound device.

``` Syntax
SoundSetVolume NewSetting , Component, Device
```

## Parameters {#Parameters}

NewSetting

:   Type: [String](../Concepts.htm#strings),
    [Integer](../Concepts.htm#numbers) or
    [Float](../Concepts.htm#numbers)

    A string containing a percentage number between -100 and 100
    inclusive. If the number begins with a plus or minus sign, the
    [current setting]{.underline} will be adjusted up or down by the
    indicated amount. Otherwise, the setting will be set explicitly to
    the level indicated by *NewSetting*.

    If the percentage number begins with a minus sign or is unsigned, it
    does not need to be enclosed in quotation marks.

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

## Error Handling {#Error_Handling}

A [TargetError](Error.htm#TargetError) is thrown if the device or
component could not be found or if the component does not support this
control type. Otherwise, an [OSError](Error.htm#OSError) is thrown on
failure.

## Remarks {#Remarks}

An alternative way to adjust the volume is to have the script send
volume-control keystrokes to change the master volume for the entire
system, such as in the example below:

    Send "{Volume_Up}"  ; Raise the master volume by 1 interval (typically 5%).
    Send "{Volume_Down 3}"  ; Lower the master volume by 3 intervals.

To discover the capabilities of the sound devices installed on the
system \-- such as the names and available components \-- run the
[soundcard analysis script](Sound.htm#ExSoundcard).

SoundSetVolume attempts to preserve the existing balance when changing
the volume level.

Use [SoundGetVolume](SoundGetVolume.htm) to retrieve the current volume
setting.

## Related {#Related}

[Sound Functions](Sound.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Sets the master volume to 50 percent. Quotation
marks can be omitted.

    SoundSetVolume "50"

    SoundSetVolume 50
:::

::: {#ExPlus .ex}
[](#ExPlus){.ex_number} Increases the master volume by 10 percent.
Quotation marks [cannot]{.underline} be omitted.

    SoundSetVolume "+10"
:::

::: {#ExMinus .ex}
[](#ExMinus){.ex_number} Decreases the master volume by 10 percent.
Quotation marks can be omitted.

    SoundSetVolume "-10"

    SoundSetVolume -10
:::

::: {#ExMic .ex}
[](#ExMic){.ex_number} Increases microphone recording volume by 20
percent.

    SoundSetVolume "+20", , "Microphone"
:::
