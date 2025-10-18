# SetKeyDelay

Sets the delay that will occur after each keystroke sent by
[Send](Send.htm) or [ControlSend](ControlSend.htm).

``` Syntax
SetKeyDelay Delay, PressDuration, "Play"
```

## Parameters {#Parameters}

Delay

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted, the current delay is retained. Otherwise, specify the
    time in milliseconds. Specify -1 for no delay at all or 0 for the
    smallest possible delay (however, if the *Play* parameter is
    present, both 0 and -1 produce no delay).

PressDuration

:   Type: [Integer](../Concepts.htm#numbers)

    Certain games and other specialized applications may require a delay
    inside each keystroke; that is, after the press of the key but
    before its release.

    If omitted, the current press duration is retained. Otherwise,
    specify the time in milliseconds. Specify -1 for no delay at all or
    0 for the smallest possible delay (however, if the *Play* parameter
    is present, both 0 and -1 produce no delay).

    **Note:** *PressDuration* also produces a delay after any change to
    the modifier key state (Ctrl, Alt, Shift, and Win) needed to support
    the keys being sent.

Play

:   Type: [String](../Concepts.htm#strings)

    If blank or omitted, the delay and press duration are applied to the
    traditional SendEvent mode. Otherwise, specify the word **Play** to
    apply both to the [SendPlay mode](Send.htm#SendPlayDetail). If a
    script never uses this parameter, both are always -1 for SendPlay.

## Remarks {#Remarks}

If SetKeyDelay is not used, the default delay is 10 for the traditional
SendEvent mode and -1 for [SendPlay mode](Send.htm#SendPlayDetail). The
default press duration is -1 for both modes.

SetKeyDelay is not obeyed by [SendInput](Send.htm#SendInputDetail);
there is no delay between keystrokes in that mode. This same is true for
[Send](Send.htm) when [SendMode Input](SendMode.htm#Input) is in effect.

A short delay (sleep) is done automatically after every keystroke sent
by [Send](Send.htm) or [ControlSend](ControlSend.htm). This is done to
improve the reliability of scripts because a window sometimes can\'t
keep up with a rapid flood of keystrokes.

During the delay (sleep), the current thread is made
[uninterruptible](../misc/Threads.htm#Interrupt).

Due to the granularity of the OS\'s time-keeping system, delays might be
rounded up to the nearest multiple of 10 or 15.

For Send/SendEvent mode, a delay of 0 internally executes a Sleep(0),
which yields the remainder of the script\'s timeslice to any other
process that may need it. If there is none, Sleep(0) will not sleep at
all. By contrast, a delay of -1 will never sleep. For better
reliability, 0 is recommended as an alternative to -1.

When the delay is set to -1, a script\'s process-priority becomes an
important factor in how fast it can send keystrokes when using the
traditional [SendEvent mode](SendMode.htm#Event). To raise a script\'s
priority, use [`ProcessSetPriority`](ProcessSetPriority.htm)` "High"`.
Although this typically causes keystrokes to be sent faster than the
[active window](WinActivate.htm) can process them, the system
automatically buffers them. Buffered keystrokes continue to arrive in
the target window after the [Send](Send.htm) function completes (even if
the window is no longer active). This is usually harmless because any
subsequent keystrokes sent to the same window get queued up behind the
ones already in the buffer.

The built-in variable **A_KeyDelay** contains the current setting of
*Delay* for Send/SendEvent mode. **A_KeyDuration** contains the setting
for *PressDuration*, while **A_KeyDelayPlay** and **A_KeyDurationPlay**
contain the settings for [SendPlay](Send.htm#SendPlayDetail).

Every newly launched [thread](../misc/Threads.htm) (such as a
[hotkey](../Hotkeys.htm), [custom menu item](Menu.htm), or
[timed](SetTimer.htm) subroutine) starts off fresh with the default
setting for this function. That default may be changed by using this
function during [script startup](../Scripts.htm#auto).

## Related {#Related}

[Send](Send.htm), [ControlSend](ControlSend.htm),
[SendMode](SendMode.htm), [SetMouseDelay](SetMouseDelay.htm),
[SetControlDelay](SetControlDelay.htm), [SetWinDelay](SetWinDelay.htm),
[Click](Click.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Causes the smallest possible delay to occur
after each keystroke sent via [Send](Send.htm) or
[ControlSend](ControlSend.htm).

    SetKeyDelay 0
:::
