# GroupDeactivate

Similar to [GroupActivate](GroupActivate.htm) except activates the next
window [not]{.underline} in the group.

``` Syntax
GroupDeactivate GroupName , Mode
```

## Parameters {#Parameters}

GroupName

:   Type: [String](../Concepts.htm#strings)

    The name of the target group, as originally defined by
    [GroupAdd](GroupAdd.htm).

Mode

:   Type: [String](../Concepts.htm#strings)

    If blank or omitted, the function activates the oldest non-member
    window. Otherwise, specify the following letter:

    **R:** The newest non-member window (the one most recently active)
    is activated, but only if a member of the group is active when the
    function is given. \"R\" is useful in cases where you temporarily
    switch to working on an unrelated task. When you return to the group
    via [GroupActivate](GroupActivate.htm), GroupDeactivate, or
    [GroupClose](GroupClose.htm), the window you were most recently
    working with is activated rather than the oldest window.

## Remarks {#Remarks}

GroupDeactivate causes the first window that does [not]{.underline}
match any of the group\'s window specifications to be activated. Using
GroupDeactivate a second time will activate the next window in the
series and so on. Normally, GroupDeactivate is assigned to a hotkey so
that this window-traversal behavior is automated by pressing that key.

This function is useful in cases where you have a collection of favorite
windows that are almost always running. By adding these windows to a
group, you can use GroupDeactivate to visit each window that isn\'t one
of your favorites and decide whether to close it. This allows you to
clean up your desktop much more quickly than doing it manually.

GroupDeactivate selects windows in a manner similar to the
[Alt]{.kbd}+[Shift]{.kbd}+[Esc]{.kbd} system hotkey. Specifically:

-   Owned windows, such as certain dialogs and tool windows, are not
    evaluated. However, if the owner window is eligible for activation,
    the most recently active owned window is activated instead, unless
    the owner was active more recently. This is determined by calling
    [GetLastActivePopup](https://learn.microsoft.com/windows/win32/api/winuser/nf-winuser-getlastactivepopup).
-   Windows with the WS_EX_TOPMOST or WS_EX_NOACTIVATE styles are
    skipped.
-   Windows with the WS_EX_TOOLWINDOW style but without the
    WS_EX_APPWINDOW style are skipped. (These windows are generally also
    omitted from Alt-Tab and the taskbar.)
-   Disabled windows are skipped, unless a window it owns (such as a
    modal dialog) was active more recently than the window itself.
-   Hidden or cloaked windows are skipped.
-   The Desktop is skipped.

Although the taskbar is skipped due to the WS_EX_TOPMOST style, it is
activated if there are no other eligible windows and the active window
matches the group.

See [GroupAdd](GroupAdd.htm) for more details about window groups.

## Related {#Related}

[GroupAdd](GroupAdd.htm), [GroupActivate](GroupActivate.htm),
[GroupClose](GroupClose.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Activates the oldest window which is not a
member of a window group.

    GroupDeactivate "MyFavoriteWindows"  ; Visit non-favorite windows to clean up desktop.
:::
