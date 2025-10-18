# GroupActivate

Activates the next window in a window group that was defined with
[GroupAdd](GroupAdd.htm).

``` Syntax
HWND := GroupActivate(GroupName , Mode)
```

## Parameters {#Parameters}

GroupName

:   Type: [String](../Concepts.htm#strings)

    The name of the group to activate, as originally defined by
    [GroupAdd](GroupAdd.htm).

Mode

:   Type: [String](../Concepts.htm#strings)

    If blank or omitted, the function activates the oldest window in the
    series. Otherwise, specify the following letter:

    **R:** The newest window (the one most recently active) is
    activated, but only if no members of the group are active when the
    function is given. \"R\" is useful in cases where you temporarily
    switch to working on an unrelated task. When you return to the group
    via GroupActivate, [GroupDeactivate](GroupDeactivate.htm), or
    [GroupClose](GroupClose.htm), the window you were most recently
    working with is activated rather than the oldest window.

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers)

This function returns the [HWND (unique
ID)](../misc/WinTitle.htm#ahk_id) of the window selected for activation,
or 0 if no matching windows were found to activate. If the current
active window is the only match, the return value is 0.

## Remarks {#Remarks}

This function causes the first window that matches one of the group\'s
window specifications to be activated. Using it a second time will
activate the next window in the series and so on. Normally, it is
assigned to a hotkey so that this window-traversal behavior is automated
by pressing that key.

Each window is evaluated against the window group as a whole, without
distinguishing between window specifications. *Mode* affects the order
of activation across the entire group.

When a window is activated immediately after the activation of some
other window, task bar buttons might start flashing on some systems
(depending on OS and settings). To prevent this, use
[#WinActivateForce](_WinActivateForce.htm).

See [GroupAdd](GroupAdd.htm) for more details about window groups.

## Related {#Related}

[GroupAdd](GroupAdd.htm), [GroupDeactivate](GroupDeactivate.htm),
[GroupClose](GroupClose.htm), [#WinActivateForce](_WinActivateForce.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Activates the newest window (the one most
recently active) in a window group.

    GroupActivate "MyGroup", "R"
:::
