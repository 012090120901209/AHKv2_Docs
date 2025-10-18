# SetStoreCapsLockMode

Whether to restore the state of [CapsLock]{.kbd} after a
[Send](Send.htm).

``` Syntax
SetStoreCapsLockMode Mode
```

## Parameters {#Parameters}

Mode

:   Type: [Boolean](../Concepts.htm#boolean)

    If **true**, [CapsLock]{.kbd} will be restored to its former value
    if [Send](Send.htm) needed to change it temporarily for its
    operation.

    If **false**, the state of [CapsLock]{.kbd} is not changed at all.
    As a result, [Send](Send.htm) will invert the case of the characters
    if [CapsLock]{.kbd} happens to be ON during the operation.

## Return Value {#Return_Value}

Type: [Integer (boolean)](../Concepts.htm#boolean)

This function returns the previous setting; either 0 (false) or 1
(true).

## Remarks {#Remarks}

If SetStoreCapsLockMode is not used, the default setting is 1 (true).

This means that [CapsLock]{.kbd} will not always be turned off for
[Send](Send.htm) and [ControlSend](ControlSend.htm). Even when it is
successfully turned off, it might not get turned back on after the keys
are sent.

This function is rarely used because the default behavior is best in
most cases.

This setting is ignored by [blind mode](Send.htm#blind) and [text
mode](Send.htm#SendText); that is, the state of [CapsLock]{.kbd} is not
changed in those cases.

The built-in variable **A_StoreCapsLockMode** contains the current
setting (1 or 0).

Every newly launched [thread](../misc/Threads.htm) (such as a
[hotkey](../Hotkeys.htm), [custom menu item](Menu.htm), or
[timed](SetTimer.htm) subroutine) starts off fresh with the default
setting for this function. That default may be changed by using this
function during [script startup](../Scripts.htm#auto).

## Related {#Related}

[SetCaps/Num/ScrollLockState](SetNumScrollCapsLockState.htm),
[Send](Send.htm), [ControlSend](ControlSend.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Causes the state of [CapsLock]{.kbd} not to be
changed at all.

    SetStoreCapsLockMode False
:::
