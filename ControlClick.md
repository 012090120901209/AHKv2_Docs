# ControlClick

Sends a mouse button or mouse wheel event to a control.

``` Syntax
ControlClick Control-or-Pos, WinTitle, WinText, WhichButton, ClickCount, Options, ExcludeTitle, ExcludeText
```

## Parameters {#Parameters}

Control-or-Pos

:   Type: [String](../Concepts.htm#strings),
    [Integer](../Concepts.htm#numbers) or
    [Object](../Concepts.htm#objects)

    If omitted, the target window itself will be clicked. Otherwise, use
    one of the following modes.

    **Mode 1 (Position):** Specify the X and Y coordinates relative to
    the upper left corner of the target window\'s [client
    area](CoordMode.htm#Client). The X coordinate must precede the Y
    coordinate and there must be at least one space or tab between them.
    For example: `"X55 Y33"`. If there is a control at the specified
    coordinates, it will be sent the click-event at those exact
    coordinates. If there is no control, the target window itself will
    be sent the event (which might have no effect depending on the
    nature of the window).

    **Note:** In mode 1, the X and Y option letters of the *Options*
    parameter are ignored.

    **Mode 2 (Control):** Specify the control\'s ClassNN, text or HWND,
    or an object with a `Hwnd` property. For details, see [The Control
    Parameter](Control.htm#Parameter).

    By default, mode 2 takes precedence over mode 1. For example, in the
    unlikely event that there is a control whose text or ClassNN has the
    format \"Xnnn Ynnn\", it would be acted upon by mode 2. To override
    this and use mode 1 unconditionally, specify the word Pos in
    *Options* as in the following example:
    `ControlClick "x255 y152", WinTitle,,,, "Pos"`.

WinTitle, WinText, ExcludeTitle, ExcludeText

:   Type: [String](../Concepts.htm#strings),
    [Integer](../Concepts.htm#numbers) or
    [Object](../Concepts.htm#objects)

    If each of these is blank or omitted, the [Last Found
    Window](../misc/WinTitle.htm#LastFoundWindow) will be used.
    Otherwise, specify for *WinTitle* a [window title or other
    criteria](../misc/WinTitle.htm) to identify the target window and/or
    for *WinText* a substring from a single text element of the target
    window (as revealed by the included Window Spy utility).

    *ExcludeTitle* and *ExcludeText* can be used to exclude one or more
    windows by their title or text. Their specification is similar to
    *WinTitle* and *WinText*, except that *ExcludeTitle* does not
    recognize any criteria other than the window title.

    Window titles and text are case-sensitive. By default, hidden
    windows are not detected and hidden text elements are detected,
    unless changed with [DetectHiddenWindows](DetectHiddenWindows.htm)
    and [DetectHiddenText](DetectHiddenText.htm); however, when using
    [pure HWNDs](../misc/WinTitle.htm#ahk_id), hidden windows are always
    detected regardless of DetectHiddenWindows. By default, a window
    title can contain *WinTitle* or *ExcludeTitle* anywhere inside it to
    be a match, unless changed with
    [SetTitleMatchMode](SetTitleMatchMode.htm).

WhichButton

:   Type: [String](../Concepts.htm#strings)

    If blank or omitted, it defaults to Left (the left mouse button).
    Otherwise, specify the button to click or the rotate/push direction
    of the mouse wheel.

    **Button:** Left, Right, Middle (or just the first letter of each of
    these); or X1 (fourth button) or X2 (fifth button).

    **Mouse wheel:** Specify WheelUp or WU to turn the wheel upward
    (away from you); specify WheelDown or WD to turn the wheel downward
    (toward you). Specify WheelLeft (or WL) or WheelRight (or WR) to
    push the wheel left or right, respectively. *ClickCount* is the
    number of notches to turn the wheel.

ClickCount

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted, it defaults to 1. Otherwise, specify the number of times
    to click the mouse button or turn the mouse wheel.

Options

:   Type: [String](../Concepts.htm#strings)

    If blank or omitted, each click consists of a down-event followed by
    an up-event, and occurs at the center of the control when mode 2 is
    in effect. Otherwise, specify a series of one or more of the
    following options. For example: `"d x50 y25"`.

    **NA:** May improve reliability. See [reliability](#Reliability)
    below.

    **D:** Press the mouse button down but do not release it (i.e.
    generate a down-event). If both the D and U options are absent, a
    complete click (down and up) will be sent.

    **U:** Release the mouse button (i.e. generate an up-event). This
    option should not be present if the D option is already present (and
    vice versa).

    **Pos:** Specify the word Pos anywhere in *Options* to
    unconditionally use the X/Y positioning mode as described in the
    *Control-or-Pos* parameter above.

    **X***n*: Specify for *n* the X position to click at, relative to
    the control\'s upper left corner. If unspecified, the click will
    occur at the horizontal-center of the control.

    **Y***n*: Specify for *n* the Y position to click at, relative to
    the control\'s upper left corner. If unspecified, the click will
    occur at the vertical-center of the control.

    Use decimal (not hexadecimal) numbers for the X and Y options.

## Error Handling {#Error_Handling}

An exception is thrown in the following cases:

-   [TargetError](Error.htm#TargetError): The target window could not be
    found.
-   [TargetError](Error.htm#TargetError): The target control could not
    be found and *Control-or-Pos* does not specify a valid position.
-   [OSError](Error.htm#OSError) (very rare): the X or Y position is
    omitted and the control\'s position could not be determined.
-   [ValueError](Error.htm#ValueError) or
    [TypeError](Error.htm#TypeError): Invalid parameters were detected.

## Reliability {#Reliability}

To improve reliability \-- especially during times when the user is
physically moving the mouse during the ControlClick \-- one or both of
the following may help:

1\) Use [`SetControlDelay`](SetControlDelay.htm)` -1` prior to
ControlClick. This avoids holding the mouse button down during the
click, which in turn reduces interference from the user\'s physical
movement of the mouse.

2\) Specify the string NA anywhere in the sixth parameter (*Options*) as
shown below:

    SetControlDelay -1
    ControlClick "Toolbar321", WinTitle,,,, "NA"

The NA option avoids marking the target window as active and avoids
merging its input processing with that of the script, which may prevent
physical movement of the mouse from interfering (but usually only when
the target window is not active). However, this method might not work
for all types of windows and controls.

## Remarks {#Remarks}

Not all applications obey a *ClickCount* higher than 1 for turning the
mouse wheel. For those applications, use a loop to turn the wheel more
than one notch as in this example, which turns it 5 notches:

    Loop 5
        ControlClick Control, WinTitle, WinText, "WheelUp"

## Related {#Related}

[SetControlDelay](SetControlDelay.htm), [Control
functions](Control.htm), [Click](Click.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Clicks the OK button.

    ControlClick "OK", "Some Window Title"
:::

::: {#ExCoord .ex}
[](#ExCoord){.ex_number} Clicks at a set of coordinates. Note the lack
of a comma between X and Y.

    ControlClick "x55 y77", "Some Window Title"
:::

::: {#ExReliability .ex}
[](#ExReliability){.ex_number} Clicks in NA mode at coordinates that are
relative to a named control.

    SetControlDelay -1  ; May improve reliability and reduce side effects.
    ControlClick "Toolbar321", "Some Window Title",,,, "NA x192 y10"
:::
