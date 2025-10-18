# MouseMove

Moves the mouse cursor.

``` Syntax
MouseMove X, Y , Speed, Relative
```

## Parameters {#Parameters}

X, Y

:   Type: [Integer](../Concepts.htm#numbers)

    The X and Y coordinates to move the mouse to. Coordinates are
    relative to the active window\'s client area unless
    [CoordMode](CoordMode.htm) was used to change that.

Speed

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted, the default speed (as set by
    [SetDefaultMouseSpeed](SetDefaultMouseSpeed.htm) or 2 otherwise)
    will be used. Otherwise, specify the speed to move the mouse in the
    range 0 (fastest) to 100 (slowest). A speed of 0 will move the mouse
    instantly.

    *Speed* is ignored for the modes [SendInput](SendMode.htm#Input) and
    [SendPlay](SendMode.htm#Play); they move the mouse instantaneously
    (though [SetMouseDelay](SetMouseDelay.htm) has a mode that applies
    to SendPlay). To visually move the mouse more slowly \-- such as a
    script that performs a demonstration for an audience \-- use
    [`SendEvent "{Click 100 200}"`](Send.htm#Click) or
    [`SendMode`](SendMode.htm)` "Event"` (optionally in conjuction with
    [BlockInput](BlockInput.htm)).

Relative

:   Type: [String](../Concepts.htm#strings)

    If blank or omitted, the X and Y coordinates will be used for
    absolute positioning. Otherwise, specify the following letter:

    **R:** The X and Y coordinates will be treated as offsets from the
    current mouse position. In other words, the cursor will be moved
    from its current position by X pixels to the right (left if
    negative) and Y pixels down (up if negative).

## Remarks {#Remarks}

This function uses the sending method set by [SendMode](SendMode.htm).

The [SendPlay mode](SendMode.htm#Play) is able to successfully generate
mouse events in a broader variety of games than the other modes. In
addition, some applications and games may have trouble tracking the
mouse if it moves too quickly. The *Speed* parameter or
[SetDefaultMouseSpeed](SetDefaultMouseSpeed.htm) can be used to reduce
the speed (in [SendEvent mode](SendMode.htm#Event) only).

The [BlockInput](BlockInput.htm) function can be used to prevent any
physical mouse activity by the user from disrupting the simulated mouse
events produced by the mouse functions. However, this is generally not
needed for the modes [SendInput](SendMode.htm#Input) and
[SendPlay](SendMode.htm#Play) because they automatically postpone the
user\'s physical mouse activity until afterward.

There is an automatic delay after every movement of the mouse (except
for [SendInput mode](SendMode.htm#Input)). Use
[SetMouseDelay](SetMouseDelay.htm) to change the length of the delay.

The following is an alternate way to move the mouse cursor that may work
better in certain multi-monitor configurations:

    DllCall("SetCursorPos", "int", 100, "int", 400)  ; The first number is the X-coordinate and the second is the Y (relative to the screen).

On a related note, the mouse cursor can be temporarily hidden via the
[hide-cursor example](DllCall.htm#ExHideCursor).

## Related {#Related}

[CoordMode](CoordMode.htm), [SendMode](SendMode.htm),
[SetDefaultMouseSpeed](SetDefaultMouseSpeed.htm),
[SetMouseDelay](SetMouseDelay.htm), [Click](Click.htm),
[MouseClick](MouseClick.htm), [MouseClickDrag](MouseClickDrag.htm),
[MouseGetPos](MouseGetPos.htm), [BlockInput](BlockInput.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Moves the mouse cursor to a new position.

    MouseMove 200, 100
:::

::: {#ExAdvanced .ex}
[](#ExAdvanced){.ex_number} Moves the mouse cursor slowly (speed 50 vs.
2) by 20 pixels to the right and 30 pixels down from its current
location.

    MouseMove 20, 30, 50, "R"
:::
