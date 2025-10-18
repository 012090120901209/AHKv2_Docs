# DetectHiddenWindows

Determines whether invisible windows are \"seen\" by the script.

``` Syntax
DetectHiddenWindows Mode
```

## Parameters {#Parameters}

Mode

:   Type: [Boolean](../Concepts.htm#boolean)

    If **true**, hidden windows are detected.

    If **false**, hidden windows are not detected, except by the
    [WinShow](WinShow.htm) function.

## Return Value {#Return_Value}

Type: [Integer (boolean)](../Concepts.htm#boolean)

This function returns the previous setting; either 0 (false) or 1
(true).

## Remarks {#Remarks}

If DetectHiddenWindows is not used, the default setting is 0 (false).

Turning on DetectHiddenWindows can make scripting harder in some cases
since some hidden system windows might accidentally match the title or
text of another window you\'re trying to work with. So most scripts
should leave this setting turned off. However, turning it on may be
useful if you wish to work with hidden windows directly without first
using [WinShow](WinShow.htm) to unhide them.

All windowing functions except [WinShow](WinShow.htm) are affected by
this setting, including [WinActivate](WinActivate.htm),
[WinActive](WinActive.htm), [WinWait](WinWait.htm) and
[WinExist](WinExist.htm). By contrast, [WinShow](WinShow.htm) will
always unhide a hidden window even if hidden windows are not being
detected.

Turning on DetectHiddenWindows is not necessary in the following cases:

-   When using a [pure HWND](../misc/WinTitle.htm#ahk_id) (as an
    [Integer](../Concepts.htm#numbers) or an [Object](../Objects.htm)
    with a HWND property), as in `WinShow(A_ScriptHwnd)` or
    `WinMoveTop(myGui)`, except with [WinWait](WinWait.htm) or
    [WinWaitClose](WinWaitClose.htm).
-   When accessing a control or child window via the [ahk_id
    method](../misc/WinTitle.htm#ahk_id) or as the
    [last-found-window](../misc/WinTitle.htm#LastFoundWindow).
-   When accessing GUI windows via the [+LastFound](Gui.htm#LastFound)
    option.

Cloaked windows are also considered hidden. Cloaked windows, introduced
with Windows 8, are windows on a non-active virtual desktop or UWP apps
which have been suspended to improve performance, or more precisely to
reduce their memory consumption. On Windows 10, the processes of those
are indicated with a green leaf in the Task Manager. Such windows are
hidden from view, but might still have the WS_VISIBLE window style.

The built-in variable **A_DetectHiddenWindows** contains the current
setting (1 or 0).

Every newly launched [thread](../misc/Threads.htm) (such as a
[hotkey](../Hotkeys.htm), [custom menu item](Menu.htm), or
[timed](SetTimer.htm) subroutine) starts off fresh with the default
setting for this function. That default may be changed by using this
function during [script startup](../Scripts.htm#auto).

## Related {#Related}

[DetectHiddenText](DetectHiddenText.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Turns on the detection of hidden windows.

    DetectHiddenWindows true
:::
