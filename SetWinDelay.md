# SetWinDelay

Sets the delay that will occur after each windowing function, such as
[WinActivate](WinActivate.htm).

``` Syntax
SetWinDelay Delay
```

## Parameters {#Parameters}

Delay

:   Type: [Integer](../Concepts.htm#numbers)

    Time in milliseconds. Specify -1 for no delay at all or 0 for the
    smallest possible delay.

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers)

This function returns the previous setting.

## Remarks {#Remarks}

If SetWinDelay is not used, the default delay is 100.

A short delay (sleep) is done automatically after every windowing
function except [WinActive](WinActive.htm) and [WinExist](WinExist.htm).
This is done to improve the reliability of scripts because a window
sometimes needs a period of \"rest\" after being created, activated,
minimized, etc. so that it has a chance to update itself and respond to
the next function that the script may attempt to send to it.

Although a delay of -1 (no delay at all) is allowed, it is recommended
that at least 0 be used, to increase confidence that the script will run
correctly even when the CPU is under load.

A delay of 0 internally executes a Sleep(0), which yields the remainder
of the script\'s timeslice to any other process that may need it. If
there is none, Sleep(0) will not sleep at all.

If the CPU is slow or under load, or if window animation is enabled,
higher delay values may be needed.

The built-in variable **A_WinDelay** contains the current setting.

Every newly launched [thread](../misc/Threads.htm) (such as a
[hotkey](../Hotkeys.htm), [custom menu item](Menu.htm), or
[timed](SetTimer.htm) subroutine) starts off fresh with the default
setting for this function. That default may be changed by using this
function during [script startup](../Scripts.htm#auto).

## Related {#Related}

[SetControlDelay](SetControlDelay.htm), [SetKeyDelay](SetKeyDelay.htm),
[SetMouseDelay](SetMouseDelay.htm), [SendMode](SendMode.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Causes a delay of 10 ms to occur after each
windowing function.

    SetWinDelay 10
:::
