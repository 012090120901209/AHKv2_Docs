# SoundPlay

Plays a sound, video, or other supported file type.

``` Syntax
SoundPlay Filename , Wait
```

## Parameters {#Parameters}

Filename

:   Type: [String](../Concepts.htm#strings)

    The name of the file to be played, which is assumed to be in
    [A_WorkingDir](../Variables.htm#WorkingDir) if an absolute path
    isn\'t specified.

    To produce standard system sounds, specify an asterisk followed by a
    number as shown below (note that the *Wait* parameter has no effect
    in this mode):

    -   \*-1 = Simple beep. If the sound card is not available, the
        sound is generated using the speaker.
    -   \*16 = Hand (stop/error)
    -   \*32 = Question
    -   \*48 = Exclamation
    -   \*64 = Asterisk (info)

Wait

:   Type: [Integer (boolean)](../Concepts.htm#boolean) or
    [String](../Concepts.htm#strings)

    If blank or omitted, it defaults to 0 (false). Otherwise, specify
    one of the following values:

    **0** (false): The [current thread](../misc/Threads.htm) will move
    on to the next statement(s) while the file is playing.

    **1** (true) or **Wait**: The current thread waits until the file is
    finished playing before continuing. Even while waiting, new threads
    can be launched via [hotkey](../Hotkeys.htm), [custom menu
    item](Menu.htm), or [timer](SetTimer.htm).

    Known limitation: If the *Wait* parameter is not used, the system
    might consider the playing file to be \"in use\" until the script
    closes or until another file is played (even a nonexistent file).

## Error Handling {#Error_Handling}

An exception is thrown on failure.

## Remarks {#Remarks}

All Windows systems should be able to play .wav files. However, other
file types (.mp3, .avi, etc.) might not be playable if the right codecs
or features aren\'t installed on the system.

Due to a quirk in Windows, .wav files with a path longer than 127
characters will not be played. To work around this, use other file types
such as .mp3 (with a path length of up to 255 characters) or use 8.3
short paths (see [A_LoopFileShortPath](LoopFiles.htm#LoopFileShortPath)
how to retrieve such paths).

If a file is playing and the current script plays a second file, the
first file will be stopped so that the second one can play. On some
systems, certain file types might stop playing even when an entirely
separate script plays a new file.

To stop a file that is currently playing, use SoundPlay on a nonexistent
filename as in this example: `try SoundPlay "Nonexistent.avi"`.

If the script is exited, any currently-playing file that it started will
stop.

## Related {#Related}

[SoundBeep](SoundBeep.htm), [Sound Functions](Sound.htm),
[MsgBox](MsgBox.htm), [Threads](../misc/Threads.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Plays a .wav file located in the Windows
directory.

    SoundPlay A_WinDir "\Media\ding.wav"
:::

::: {#ExStandardSound .ex}
[](#ExStandardSound){.ex_number} Generates a simple beep.

    SoundPlay "*-1"
:::
