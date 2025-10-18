# SetDefaultMouseSpeed

Sets the mouse speed that will be used if unspecified in
[Click](Click.htm), [MouseMove](MouseMove.htm),
[MouseClick](MouseClick.htm), and [MouseClickDrag](MouseClickDrag.htm).

``` Syntax
SetDefaultMouseSpeed Speed
```

## Parameters {#Parameters}

Speed

:   Type: [Integer](../Concepts.htm#numbers)

    The speed to move the mouse in the range 0 (fastest) to 100
    (slowest). A speed of 0 will move the mouse instantly.

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers)

This function returns the previous setting.

## Remarks {#Remarks}

If SetDefaultMouseSpeed is not used, the default mouse speed is 2.

SetDefaultMouseSpeed is ignored for the modes
[SendInput](SendMode.htm#Input) and [SendPlay](SendMode.htm#Play); they
move the mouse instantaneously (except when SendInput [reverts to
SendEvent](Send.htm#SendInputUnavail); also,
[SetMouseDelay](SetMouseDelay.htm) has a mode that applies to SendPlay).
To visually move the mouse more slowly \-- such as a script that
performs a demonstration for an audience \-- use
[`SendEvent "{Click 100 200}"`](Send.htm#Click) or
[`SendMode`](SendMode.htm)` "Event"` (optionally in conjuction with
[BlockInput](BlockInput.htm)).

The built-in variable **A_DefaultMouseSpeed** contains the current
setting.

The functions [MouseClick](MouseClick.htm), [MouseMove](MouseMove.htm),
and [MouseClickDrag](MouseClickDrag.htm) all have a parameter to
override the default mouse speed.

Whenever *Speed* is greater than zero,
[SetMouseDelay](SetMouseDelay.htm) also influences the speed by
producing a delay after each incremental move the mouse makes toward its
destination.

Every newly launched [thread](../misc/Threads.htm) (such as a
[hotkey](../Hotkeys.htm), [custom menu item](Menu.htm), or
[timed](SetTimer.htm) subroutine) starts off fresh with the default
setting for this function. That default may be changed by using this
function during [script startup](../Scripts.htm#auto).

## Related {#Related}

[SetMouseDelay](SetMouseDelay.htm), [SendMode](SendMode.htm),
[Click](Click.htm), [MouseClick](MouseClick.htm),
[MouseMove](MouseMove.htm), [MouseClickDrag](MouseClickDrag.htm),
[SetWinDelay](SetWinDelay.htm), [SetControlDelay](SetControlDelay.htm),
[SetKeyDelay](SetKeyDelay.htm), [SetKeyDelay](SetMouseDelay.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Causes the mouse cursor to be moved instantly.

    SetDefaultMouseSpeed 0
:::
