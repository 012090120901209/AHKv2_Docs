# CoordMode

Sets coordinate mode for various built-in functions to be relative to
either the active window or the screen.

``` Syntax
CoordMode TargetType , RelativeTo
```

## Parameters {#Parameters}

TargetType

:   Type: [String](../Concepts.htm#strings)

    Specify one of the following words to indicate the type of target to
    affect:

    **ToolTip:** Affects [ToolTip](ToolTip.htm).

    **Pixel:** Affects [PixelGetColor](PixelGetColor.htm),
    [PixelSearch](PixelSearch.htm), and [ImageSearch](ImageSearch.htm).

    **Mouse:** Affects [MouseGetPos](MouseGetPos.htm),
    [Click](Click.htm), [MouseMove](MouseMove.htm),
    [MouseClick](MouseClick.htm), and
    [MouseClickDrag](MouseClickDrag.htm).

    **Caret:** Affects [CaretGetPos](CaretGetPos.htm).

    **Menu:** Affects the [Menu.Show](Menu.htm#Show) method when
    coordinates are specified for it.

RelativeTo

:   Type: [String](../Concepts.htm#strings)

    If omitted, it defaults to *Screen*. Otherwise, specify one of the
    following words to indicate the area to which *TargetType* should be
    relative:

    **Screen:** Coordinates are relative to the desktop (entire screen).

    **Window:** Coordinates are relative to the active window.

    **Client:** Coordinates are relative to the active window\'s client
    area, which excludes the window\'s title bar, menu (if it has a
    standard one) and borders. Client coordinates are less dependent on
    OS version and theme.

## Return Value {#Return_Value}

Type: [String](../Concepts.htm#strings)

This function returns the previous setting; either Screen, Window or
Client.

## Remarks {#Remarks}

If CoordMode is not used, the default mode is *Client*; that is, all
built-in functions except those documented otherwise (e.g.
[WinMove](WinMove.htm) and [InputBox](InputBox.htm)) use coordinates
that are relative to the active window\'s client area.

Every newly launched [thread](../misc/Threads.htm) (such as a
[hotkey](../Hotkeys.htm), [custom menu item](Menu.htm), or
[timed](SetTimer.htm) subroutine) starts off fresh with the default
setting for this function. That default may be changed by using this
function during [script startup](../Scripts.htm#auto).

The built-in [A_CoordMode variables](../Variables.htm#CoordMode) contain
the current settings.

## Related {#Related}

[Click](Click.htm), [MouseMove](MouseMove.htm),
[MouseClick](MouseClick.htm), [MouseClickDrag](MouseClickDrag.htm),
[MouseGetPos](MouseGetPos.htm), [PixelGetColor](PixelGetColor.htm),
[PixelSearch](PixelSearch.htm), [ToolTip](ToolTip.htm),
[Menu.Show](Menu.htm)

## Examples {#Examples}

::: {#ExToolTipScreen .ex}
[](#ExToolTipScreen){.ex_number} Places tooltips at absolute screen
coordinates.

    CoordMode "ToolTip", "Screen"
:::

::: {#ExToolTip .ex}
[](#ExToolTip){.ex_number} Same effect as the above because \"Screen\"
is the default.

    CoordMode "ToolTip"
:::
