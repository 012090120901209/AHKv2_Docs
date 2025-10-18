# SoundBeep

Emits a tone from the PC speaker.

``` Syntax
SoundBeep Frequency, Duration
```

## Parameters {#Parameters}

Frequency

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted, it defaults to 523. Otherwise, specify the frequency of
    the sound, a number between 37 and 32767.

Duration

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted, it defaults to 150. Otherwise, specify the duration of
    the sound, in milliseconds.

## Remarks {#Remarks}

The script waits for the sound to finish before continuing. In addition,
system responsiveness might be reduced during sound production.

If the computer lacks a sound card, a standard beep is played through
the PC speaker.

To produce the standard system sounds instead of beeping the PC Speaker,
see the asterisk mode of [SoundPlay](SoundPlay.htm).

## Related {#Related}

[SoundPlay](SoundPlay.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Plays the default pitch and duration.

    SoundBeep
:::

::: {#ExParams .ex}
[](#ExParams){.ex_number} Plays a higher pitch for half a second.

    SoundBeep 750, 500
:::
