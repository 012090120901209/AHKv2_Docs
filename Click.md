# Click

Clicks a mouse button at the specified coordinates. It can also hold
down a mouse button, turn the mouse wheel, or move the mouse.

``` Syntax
Click Options
```

## Parameters {#Parameters}

Options

:   Specify one or more of the following components:
    `Coords`{.variable}, `WhichButton`{.variable},
    `ClickCount`{.variable}, `DownOrUp`{.variable} and/or
    `Relative`{.variable}. If all components are omitted, a single left
    click is performed at the mouse cursor\'s current position.

    The components may be spread across multiple parameters or combined
    into one or more strings. Each parameter may be either a single
    numeric component or a string containing zero or more components,
    where each component is separated from the next with at least one
    space, tab and/or comma (all within the string). For example,
    `Click 100, 200, "R D"` is equivalent to `Click "100 200 R D"` and
    both are valid. Parameters that are blank or omitted are ignored, as
    are extra commas.

    **Warning:** `Click 100 200` would be equivalent to
    `Click "100200"`, as the two numbers would be
    [concatenated](../Variables.htm#concat) before the function is
    called.

    The components can appear in any order except
    `ClickCount`{.variable}, which must occur somewhere to the right of
    `Coords`{.variable}, if present.

    **Coords:** If omitted, the cursor\'s current position is used.
    Otherwise, specify the X and Y coordinates to which the mouse cursor
    is moved prior to clicking. For example, `Click "100 200"` clicks
    the left mouse button at a specific position. Coordinates are
    relative to the active window\'s client area unless
    [CoordMode](CoordMode.htm) was used to change that.

    **WhichButton:** If omitted, it defaults to Left (the left mouse
    button). Otherwise, specify Left, Right, Middle (or just the first
    letter of each of these); or X1 (fourth button) or X2 (fifth
    button). For example, `Click "Right"` clicks the right mouse button
    at the mouse cursor\'s current position. Left and Right correspond
    to the primary button and secondary button. If the user swaps the
    buttons via system settings, the physical positions of the buttons
    are swapped but the effect stays the same.

    `WhichButton`{.variable} can also be WheelUp or WU to turn the wheel
    upward (away from you), or WheelDown or WD to turn the wheel
    downward (toward you). WheelLeft (or WL) or WheelRight (or WR) may
    also be specified. *ClickCount* is the number of notches to turn the
    wheel. However, some applications do not obey a
    `ClickCount`{.variable} value higher than 1 for the mouse wheel. For
    them, use the Click function multiple times by means such as
    [Loop](Loop.htm).

    **ClickCount:** If omitted, it defaults to 1. Otherwise, specify the
    number of times to click the mouse button or turn the mouse wheel.
    For example, `Click 2` performs a double-click at the mouse
    cursor\'s current position. If `Coords`{.variable} is specified,
    `ClickCount`{.variable} must appear after it. Specify zero (0) to
    move the mouse without clicking; for example, `Click "100 200 0"`.

    **DownOrUp:** If omitted, each click consists of a down-event
    followed by an up-event. Otherwise, specify the word Down (or the
    letter D) to press the mouse button down without releasing it.
    Later, use the word Up (or the letter U) to release the mouse
    button. For example, `Click "Down"` presses down the left mouse
    button and holds it.

    **Relative:** If omitted, the X and Y coordinates will be used for
    absolute positioning. Otherwise, specify the word Rel or Relative to
    treat the coordinates as offsets from the current mouse position. In
    other words, the cursor will be moved from its current position by X
    pixels to the right (left if negative) and Y pixels down (up if
    negative).

## Remarks {#Remarks}

The Click function uses the sending method set by
[SendMode](SendMode.htm). To override this mode for a particular click,
use a specific Send function in combination with
[{Click}](Send.htm#Click), as in this example:
`SendEvent "{Click 100 200}"`.

To perform a shift-click or control-click, [clicking via
Send](Send.htm#Click) is generally easiest. For example:

    Send "+{Click 100 200}"  ; Shift+LeftClick
    Send "^{Click 100 200 Right}"  ; Control+RightClick

Unlike [Send](Send.htm), the Click function does not automatically
release the modifier keys (Ctrl, Alt, Shift, and Win). For example, if
[Ctrl]{.kbd} is currently down, `Click` would produce a control-click
but `Send "{Click}"` would produce a normal click.

The [SendPlay mode](SendMode.htm#Play) is able to successfully generate
mouse events in a broader variety of games than the other modes. In
addition, some applications and games may have trouble tracking the
mouse if it moves too quickly, in which case
[SetDefaultMouseSpeed](SetDefaultMouseSpeed.htm) can be used to reduce
the speed (but only in [SendEvent mode](SendMode.htm#Event)).

The [BlockInput](BlockInput.htm) function can be used to prevent any
physical mouse activity by the user from disrupting the simulated mouse
events produced by the mouse functions. However, this is generally not
needed for the [SendInput](SendMode.htm#Input) and
[SendPlay](SendMode.htm#Play) modes because they automatically postpone
the user\'s physical mouse activity until afterward.

There is an automatic delay after every click-down and click-up of the
mouse (except for [SendInput mode](SendMode.htm#Input) and for turning
the mouse wheel). Use [SetMouseDelay](SetMouseDelay.htm) to change the
length of the delay.

## Related {#Related}

[Send \"{Click}\"](Send.htm#Click), [SendMode](SendMode.htm),
[CoordMode](CoordMode.htm),
[SetDefaultMouseSpeed](SetDefaultMouseSpeed.htm),
[SetMouseDelay](SetMouseDelay.htm), [MouseClick](MouseClick.htm),
[MouseClickDrag](MouseClickDrag.htm), [MouseMove](MouseMove.htm),
[ControlClick](ControlClick.htm), [BlockInput](BlockInput.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Clicks the left mouse button at the mouse
cursor\'s current position.

    Click
:::

::: {#ExCoord .ex}
[](#ExCoord){.ex_number} Clicks the left mouse button at a specific
position.

    Click 100, 200
:::

::: {#ExCoordMove .ex}
[](#ExCoordMove){.ex_number} Moves the mouse cursor to a specific
position without clicking.

    Click 100, 200, 0
:::

::: {#ExCoordRight .ex}
[](#ExCoordRight){.ex_number} Clicks the right mouse button at a
specific position.

    Click 100, 200, "Right"
:::

::: {#ExDouble .ex}
[](#ExDouble){.ex_number} Performs a double-click at the mouse cursor\'s
current position.

    Click 2
:::

::: {#ExDown .ex}
[](#ExDown){.ex_number} Presses down the left mouse button and holds it.

    Click "Down"
:::

::: {#ExUp .ex}
[](#ExUp){.ex_number} Releases the right mouse button.

    Click "Up Right"
:::
