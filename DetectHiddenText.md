# DetectHiddenText

Determines whether invisible text in a window is \"seen\" for the
purpose of finding the window. This affects windowing functions such as
[WinExist](WinExist.htm) and [WinActivate](WinActivate.htm).

``` Syntax
DetectHiddenText Mode
```

## Parameters {#Parameters}

Mode

:   Type: [Boolean](../Concepts.htm#boolean)

    If **true**, hidden text is detected.

    If **false**, hidden text is not detected.

## Return Value {#Return_Value}

Type: [Integer (boolean)](../Concepts.htm#boolean)

This function returns the previous setting; either 0 (false) or 1
(true).

## Remarks {#Remarks}

If DetectHiddenText is not used, the default setting is 1 (true).

\"Hidden text\" is a term that refers to those controls of a window that
are not visible. Their text is thus considered \"hidden\". Turning off
DetectHiddenText can be useful in cases where you want to detect the
difference between the different panes of a multi-pane window or
multi-tabbed dialog. Use Window Spy to determine which text of the
currently-active window is hidden. All built-in functions that accept a
*WinText* parameter are affected by this setting, including
[WinActivate](WinActivate.htm), [WinActive](WinActive.htm),
[WinWait](WinWait.htm), and [WinExist](WinExist.htm).

The built-in variable **A_DetectHiddenText** contains the current
setting (1 or 0).

Every newly launched [thread](../misc/Threads.htm) (such as a
[hotkey](../Hotkeys.htm), [custom menu item](Menu.htm), or
[timed](SetTimer.htm) subroutine) starts off fresh with the default
setting for this function. That default may be changed by using this
function during [script startup](../Scripts.htm#auto).

## Related {#Related}

[DetectHiddenWindows](DetectHiddenWindows.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Turns off the detection of hidden text.

    DetectHiddenText false
:::
