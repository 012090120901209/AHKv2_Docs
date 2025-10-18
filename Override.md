# Overriding or Disabling External Hotkeys

You can disable all built-in Windows hotkeys except
[Win]{.kbd}+[L]{.kbd} and [Win]{.kbd}+[U]{.kbd} by making the following
change to the registry (this should work on all OSes but a reboot is
probably required):

``` no-highlight
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer
NoWinKeys REG_DWORD 0x00000001 (1)
```

But read on if you want to do more than just disable them all.

Hotkeys owned by another application can be overridden or disabled
simply by assigning them to an action in the script. The most common use
for this feature is to change the hotkeys that are built into Windows
itself. For example, if you wish [Win]{.kbd}+[E]{.kbd} (the shortcut key
that launches Windows Explorer) to perform some other action, use this:

    #e::MsgBox "This hotkey is now owned by the script."

In the next example, the [Win]{.kbd}+[R]{.kbd} hotkey, which is used to
open the RUN window, is completely disabled:

    #r::return

Similarly, to disable both [Win]{.kbd}, use this:

    LWin::return
    RWin::return

To disable or change an application\'s non-global hotkey (that is, a
shortcut key that only works when that application is the active
window), consider the following example which disables
[Ctrl]{.kbd}+[P]{.kbd} (Print) only for Notepad, leaving the key in
effect for all other types of windows:

    $^p::
    {
        if WinActive("ahk_class Notepad")
            return  ; i.e. do nothing, which causes Ctrl+P to do nothing in Notepad.
        Send "^p"
    }

In the above example, the \$ prefix is needed so that the hotkey can
\"send itself\" without activating itself (which would otherwise trigger
a warning dialog about an infinite loop). See also: [Context-sensitive
Hotkeys](../Hotkeys.htm#Context).

You can try out any of the above examples by copying them into a new
text file such as \"Override.ahk\", then launching the file.
Alternatively, if your browser supports it, you can download any of them
as a script file by clicking the [↓]{style="font-family: icons;"} button
which appears in the top-right of the code block when you hover your
mouse over it.
