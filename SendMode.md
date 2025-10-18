# SendMode

Makes [Send](Send.htm) synonymous with SendEvent or SendPlay rather than
the default (SendInput). Also makes Click and MouseMove/Click/Drag use
the specified method.

``` Syntax
SendMode Mode
```

## Parameters {#Parameters}

Mode

:   Type: [String](../Concepts.htm#strings)

    Specify one of the following words:

    **Event:** Switches to the [SendEvent](Send.htm#SendEvent) method
    for [Send](Send.htm), [SendText](Send.htm), [Click](Click.htm),
    [MouseMove](MouseMove.htm), [MouseClick](MouseClick.htm), and
    [MouseClickDrag](MouseClickDrag.htm).

    **Input:** Uses the [SendInput](Send.htm#SendInput) method for
    [Send](Send.htm), [SendText](Send.htm), [Click](Click.htm),
    [MouseMove](MouseMove.htm), [MouseClick](MouseClick.htm), and
    [MouseClickDrag](MouseClickDrag.htm). Known limitations:

    -   Windows Explorer ignores SendInput\'s simulation of certain
        navigational hotkeys such as [Alt]{.kbd}+[←]{.kbd}. To work
        around this, use either `SendEvent "!{Left}"` or
        `SendInput "{Backspace}"`.

    **InputThenPlay:** Same as above except that rather than falling
    back to Event mode when SendInput is
    [unavailable](Send.htm#SendInputUnavail), it reverts to Play mode
    (below). This also causes the [SendInput
    function](Send.htm#SendInput) itself to revert to Play mode when
    SendInput is unavailable.

    **Play:** Switches to the [SendPlay](Send.htm#SendPlay) method for
    [Send](Send.htm), [SendText](Send.htm), [Click](Click.htm),
    [MouseMove](MouseMove.htm), [MouseClick](MouseClick.htm), and
    [MouseClickDrag](MouseClickDrag.htm). Known limitations:

    -   Characters that do not exist in the current keyboard layout
        (such as Ô in English) cannot be sent. To work around this, use
        [SendEvent](Send.htm#SendEvent).
    -   Simulated mouse dragging might have no effect in RichEdit
        controls (and possibly others) such as those of WordPad and
        Metapad. To use an alternate mode for a particular drag, follow
        this example:
        [`SendEvent`](Send.htm#SendEvent)` "{Click 6 52 Down}{Click 45 52 Up}"`.
    -   Simulated mouse wheel rotation produces movement in only one
        direction (usually downward, but upward in some applications).
        Also, wheel rotation might have no effect in applications such
        as MS Word and Notepad. To use an alternate mode for a
        particular rotation, follow this example:
        [`SendEvent`](Send.htm#SendEvent)` "{WheelDown 5}"`.
    -   If `SendMode "Play"` is called during [script
        startup](../Scripts.htm#auto), all remapped keys are affected
        and might lose some of their functionality. See [SendPlay
        remapping limitations](../misc/Remap.htm#SendPlay) for details.
    -   SendPlay does not trigger AutoHotkey\'s hotkeys or hotstrings,
        or global hotkeys registered by other programs or the OS.

## Return Value {#Return_Value}

Type: [String](../Concepts.htm#strings)

This function returns the previous setting; either Event, Input,
InputThenPlay or Play.

## Remarks {#Remarks}

If SendMode is not used, the default mode is *Input*.

Since SendMode also changes the mode of [Click](Click.htm),
[MouseMove](MouseMove.htm), [MouseClick](MouseClick.htm), and
[MouseClickDrag](MouseClickDrag.htm), there may be times when you wish
to use a different mode for a particular mouse event. The easiest way to
do this is via [{Click}](Send.htm#Click). For example:

    SendEvent "{Click 100 200}"  ; SendEvent uses the older, traditional method of clicking.

If SendMode is used during [script startup](../Scripts.htm#auto), it
also affects [keyboard and mouse remapping](../misc/Remap.htm). In
particular, if you use `SendMode "Play"` with remapping, see [SendPlay
remapping limitations](../misc/Remap.htm#SendPlay).

The built-in variable **A_SendMode** contains the current setting.

Every newly launched [thread](../misc/Threads.htm) (such as a
[hotkey](../Hotkeys.htm), [custom menu item](Menu.htm), or
[timed](SetTimer.htm) subroutine) starts off fresh with the default
setting for this function. That default may be changed by using this
function during [script startup](../Scripts.htm#auto).

## Related {#Related}

[Send](Send.htm), [SetKeyDelay](SetKeyDelay.htm),
[SetMouseDelay](SetMouseDelay.htm), [Click](Click.htm),
[MouseClick](MouseClick.htm), [MouseClickDrag](MouseClickDrag.htm),
[MouseMove](MouseMove.htm)

## Examples {#Examples}

::: {#ExInputThenPlay .ex}
[](#ExInputThenPlay){.ex_number} Makes Send synonymous with SendInput,
but falls back to SendPlay if SendInput is not available.

    SendMode "InputThenPlay"
:::
