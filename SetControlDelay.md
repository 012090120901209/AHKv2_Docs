# SetControlDelay

Sets the delay that will occur after each control-modifying function.

``` Syntax
SetControlDelay Delay
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

If SetControlDelay is not used, the default delay is 20.

A short delay (sleep) is done automatically after every Control function
that changes a control. This is done to improve the reliability of
scripts because a control sometimes needs a period of \"rest\" after
being changed by one of these functions, so that the control has a
chance to update itself and respond to the next function that the script
may attempt to send to it.

Specifically, SetControlDelay affects the following functions:
[ControlAddItem](ControlAddItem.htm),
[ControlChooseIndex](ControlChooseIndex.htm),
[ControlChooseString](ControlChooseString.htm),
[ControlClick](ControlClick.htm),
[ControlDeleteItem](ControlDeleteItem.htm), [EditPaste](EditPaste.htm),
[ControlFindItem](ControlFindItem.htm),
[ControlFocus](ControlFocus.htm), [ControlHide](ControlHide.htm),
[ControlHideDropDown](ControlHideDropDown.htm),
[ControlMove](ControlMove.htm),
[ControlSetChecked](ControlSetChecked.htm),
[ControlSetEnabled](ControlSetEnabled.htm),
[ControlSetText](ControlSetText.htm), [ControlShow](ControlShow.htm),
[ControlShowDropDown](ControlShowDropDown.htm).

[ControlSend](ControlSend.htm) is not affected; it uses
[SetKeyDelay](SetKeyDelay.htm).

Although a delay of -1 (no delay at all) is allowed, it is recommended
that at least 0 be used, to increase confidence that the script will run
correctly even when the CPU is under load.

A delay of 0 internally executes a Sleep(0), which yields the remainder
of the script\'s timeslice to any other process that may need it. If
there is none, Sleep(0) will not sleep at all.

If the CPU is slow or under load, or if window animation is enabled,
higher delay values may be needed.

The built-in variable **A_ControlDelay** contains the current setting
and can also be assigned a new value instead of calling SetControlDelay.

Every newly launched [thread](../misc/Threads.htm) (such as a
[hotkey](../Hotkeys.htm), [custom menu item](Menu.htm), or
[timed](SetTimer.htm) subroutine) starts off fresh with the default
setting for this function. That default may be changed by using this
function during [script startup](../Scripts.htm#auto).

## Related {#Related}

[Control functions](Control.htm), [SetWinDelay](SetWinDelay.htm),
[SetKeyDelay](SetKeyDelay.htm), [SetMouseDelay](SetMouseDelay.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Causes the smallest possible delay to occur
after each control-modifying function.

    SetControlDelay 0
:::
