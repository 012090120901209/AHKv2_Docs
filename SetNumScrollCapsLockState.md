# SetCapsLockState / SetNumLockState / SetScrollLockState

Sets the state of [CapsLock]{.kbd}/[NumLock]{.kbd}/[ScrollLock]{.kbd}.
Can also force the key to stay on or off.

``` Syntax
SetCapsLockState State
SetNumLockState State
SetScrollLockState State
```

## Parameters {#Parameters}

State

:   Type: [String](../Concepts.htm#strings) or
    [Integer](../Concepts.htm#numbers)

    If blank or omitted, the AlwaysOn/Off attribute of the key is
    removed (if present). Otherwise, specify one of the following
    values:

    **On** or 1 ([true](../Variables.htm#True)): Turns on the key and
    removes the AlwaysOn/Off attribute of the key (if present).

    **Off** or 0 ([false](../Variables.htm#False)): Turns off the key
    and removes the AlwaysOn/Off attribute of the key (if present).

    **AlwaysOn:** Forces the key to stay on permanently.

    **AlwaysOff:** Forces the key to stay off permanently.

## Remarks {#Remarks}

Alternatively to [example #3](#ExToggle) below, a key can also be
toggled to its opposite state via the [Send](Send.htm) function, e.g.
`Send "{CapsLock}"`. However, sending {CapsLock} might require
[`SetStoreCapsLockMode`](SetStoreCapsLockMode.htm)` False` beforehand.

Keeping a key *AlwaysOn* or *AlwaysOff* requires the [keyboard
hook](InstallKeybdHook.htm), which will be automatically installed in
such cases.

## Related {#Related}

[SetStoreCapsLockMode](SetStoreCapsLockMode.htm),
[GetKeyState](GetKeyState.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Turns on [NumLock]{.kbd} and removes the
AlwaysOn/Off attribute of the key (if present).

    SetNumLockState True
:::

::: {#ExAlwaysOff .ex}
[](#ExAlwaysOff){.ex_number} Forces [ScrollLock]{.kbd} to stay off
permanently.

    SetScrollLockState "AlwaysOff"
:::

::: {#ExToggle .ex}
[](#ExToggle){.ex_number} Toggles [CapsLock]{.kbd} to its opposite
state.

    SetCapsLockState !GetKeyState("CapsLock", "T")
:::
