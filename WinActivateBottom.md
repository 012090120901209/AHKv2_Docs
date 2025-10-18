# WinActivateBottom

Same as [WinActivate](WinActivate.htm) except that it activates the
bottommost matching window rather than the topmost.

``` Syntax
WinActivateBottom WinTitle, WinText, ExcludeTitle, ExcludeText
```

## Parameters {#Parameters}

WinTitle, WinText, ExcludeTitle, ExcludeText

:   Type: [String](../Concepts.htm#strings),
    [Integer](../Concepts.htm#numbers) or
    [Object](../Concepts.htm#objects)

    At least one of these is required. Specify for *WinTitle* a [window
    title or other criteria](../misc/WinTitle.htm) to identify the
    target window and/or for *WinText* a substring from a single text
    element of the target window (as revealed by the included Window Spy
    utility).

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

## Error Handling {#Error_Handling}

A [TargetError](Error.htm#TargetError) is thrown if the window could not
be found.

## Remarks {#Remarks}

The bottommost window is typically the one least recently used, except
when windows have been reordered, such as with
[WinMoveBottom](WinMoveBottom.htm).

If there is only one matching window, WinActivateBottom behaves
identically to [WinActivate](WinActivate.htm).

[Window groups](GroupAdd.htm) are more advanced than this function, so
consider using them for more features and flexibility.

If the window is minimized and inactive, it is automatically restored
prior to being activated. If *WinTitle* is the letter \"A\" and the
other parameters are omitted, the active window is restored. The window
is restored even if it was already active.

Six attempts will be made to activate the target window over the course
of 60 ms. Thus, it is usually unnecessary to follow it with the
[WinWaitActive](WinWaitActive.htm) function.

Unlike [WinActivate](WinActivate.htm), the [Last Found
Window](../misc/WinTitle.htm#LastFoundWindow) cannot be used because it
might not be the bottommost window. Therefore, at least one of the
parameters must be non-blank.

When a window is activated immediately after another window was
activated, task bar buttons may start flashing on some systems
(depending on OS and settings). To prevent this, use
[#WinActivateForce](_WinActivateForce.htm).

## Related {#Related}

[WinActivate](WinActivate.htm),
[#WinActivateForce](_WinActivateForce.htm),
[SetTitleMatchMode](SetTitleMatchMode.htm),
[DetectHiddenWindows](DetectHiddenWindows.htm),
[WinExist](WinExist.htm), [WinActive](WinActive.htm),
[WinWaitActive](WinWaitActive.htm), [WinWait](WinWait.htm),
[WinWaitClose](WinWaitClose.htm), [GroupActivate](GroupActivate.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Press a hotkey to visit all open browser
windows in order from oldest to newest.

    #i:: ; Win+I
    {
        SetTitleMatchMode 2
        WinActivateBottom "- Microsoft Internet Explorer"
    }
:::
