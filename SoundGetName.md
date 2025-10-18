# SoundGetName

Retrieves the name of a sound device or component.

``` Syntax
Name := SoundGetName(Component, Device)
```

## Parameters {#Parameters}

Component

:   Type: [String](../Concepts.htm#strings) or
    [Integer](../Concepts.htm#numbers)

    If blank or omitted, the name of the device itself will be
    retrieved. Otherwise, specify the component\'s display name and/or
    index, e.g. `1`, `"Line in"` or `"Line in:2"`.

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

Type: [String](../Concepts.htm#strings)

This function returns the name of the device or component, which can be
empty.

## Error Handling {#Error_Handling}

A [TargetError](Error.htm#TargetError) is thrown if the device or
component could not be found. Otherwise, an [OSError](Error.htm#OSError)
is thrown on failure.

## Related {#Related}

[Sound Functions](Sound.htm)

## Examples {#Examples}

::: {#ExNoParams .ex}
[](#ExNoParams){.ex_number} Retrieves and reports the name of the
default playback device.

    default_device := SoundGetName()
    MsgBox "The default playback device is " default_device
:::

::: {#ExDevice .ex}
[](#ExDevice){.ex_number} Retrieves and reports the name of the first
device.

    device1 := SoundGetName( , 1)
    MsgBox "Device 1 is " device1
:::

::: {#ExComponent .ex}
[](#ExComponent){.ex_number} Retrieves and reports the name of the first
component.

    component1 := SoundGetName(1)
    MsgBox "Component 1 is " component1
:::

For a more complex example, see the [soundcard analysis
script](Sound.htm#ExSoundcard).
