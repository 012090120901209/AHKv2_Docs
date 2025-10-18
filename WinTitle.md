# `WinTitle`{.variable} Parameter & Last Found Window

Various built-in functions have a `WinTitle`{.variable} parameter, used
to identify which window (or windows) to operate on. This parameter can
be the title or partial title of the window, and/or any other criteria
described on this page.

## Table of Contents {#toc}

-   [Window Title & Matching Behaviour](#WinTitle)
-   [A (Active Window)](#ActiveWindow)
-   [ahk\_ Criteria](#ahk_)
    -   [ahk_class (Window Class)](#ahk_class)
    -   [ahk_id (Unique ID / HWND)](#ahk_id)
    -   [ahk_pid (Process ID)](#ahk_pid)
    -   [ahk_exe (Process Name/Path)](#ahk_exe)
    -   [ahk_group (Window Group)](#ahk_group)
-   [Multiple Criteria](#multi)
-   [Last Found Window](#LastFoundWindow)

[]{#Matching}

## Window Title & Matching Behaviour {#WinTitle}

Specify any string for `WinTitle`{.variable} to identify a window by its
title. The title of a window is often visible as text in a title bar at
the top of the window. If invisible or only partially visible, the full
window title can be revealed via [WinGetTitle](../lib/WinGetTitle.htm)
or Window Spy.

The following example activates the calculator:

    WinActivate "Calculator"

[SetTitleMatchMode](../lib/SetTitleMatchMode.htm) controls how a partial
or complete title is compared against the title of each window.
Depending on the setting, `WinTitle`{.variable} can be an exact title,
or it can contain a prefix, a substring which occurs anywhere in the
title, or a [RegEx pattern](RegEx-QuickRef.htm). This setting also
controls whether the [ahk_class](#ahk_class) and [ahk_exe](#ahk_exe)
criteria are interpreted as RegEx patterns.

Window titles are case-sensitive, except when using the [i)
modifier](RegEx-QuickRef.htm#opt_i) in a RegEx pattern.

Hidden windows are only detected if
[DetectHiddenWindows](../lib/DetectHiddenWindows.htm) is turned on,
except with [WinShow](../lib/WinShow.htm), which always detects hidden
windows.

If multiple windows match `WinTitle`{.variable} and any other criteria,
the topmost matching window is used. If the active window matches the
criteria, it usually takes precedence since it is usually above all
other windows. However, if an
[always-on-top](../lib/WinSetAlwaysOnTop.htm) window also matches (and
the active window is not always-on-top), it may be used instead.

In [\[v2.0.6+\]]{.ver}, it is no longer the case that only the first
1023 characters of the specified window title, [ahk_class](#ahk_class)
criterion value, and [ahk_exe](#ahk_exe) criterion value are considered
for matching purposes. Exceeding the length no longer leads to
unexpected results, which rarely occurs, but may be encountered more
often if a very long RegEx pattern is used.

## A (Active Window) {#ActiveWindow}

Use the letter `A` for `WinTitle`{.variable} and omit the other three
window parameters (*WinText*, *ExcludeTitle* and *ExcludeText*), to
operate on the active window.

The following example retrieves and reports the unique ID (HWND) of the
active window:

    MsgBox WinExist("A")

The following example creates a hotkey which can be pressed to maximize
the active window:

    #Up::WinMaximize "A"  ; Win+Up

## ahk\_ Criteria {#ahk_}

Specify one or more of the following ahk\_ criteria (optionally in
addition to a window\'s title), each separated from the next with
exactly [one]{.underline} space or tab (any other spaces or tabs are
treated as a literal part of the previous criterion). An ahk\_ criterion
always consists of an ahk\_ keyword and its criterion value, separated
by zero or more spaces or tabs. For example, `ahk_class Notepad`
identifies a Notepad window.

The ahk\_ keyword and its criterion value do not need to be separated by
spaces or tabs. This is primarily useful when specifying ahk\_ criteria
in combination with variables. For example, you could specify
`"ahk_pid" PID` instead of `"ahk_pid " PID`. In all other cases,
however, it is recommended to use at least one space or tab as a
separation to improve readability.

### ahk_class (Window Class) {#ahk_class}

Use `ahk_class ``ClassName`{.variable} in `WinTitle`{.variable} to
identify a window by its window class.

A window class is a set of attributes that the system uses as a template
to create a window. In other words, the class name of the window
identifies what *type* of window it is. A window class can be revealed
via Window Spy or retrieved by [WinGetClass](../lib/WinGetClass.htm). If
the RegEx [title matching mode](../lib/SetTitleMatchMode.htm) is active,
`ClassName`{.variable} accepts a [regular
expression](RegEx-QuickRef.htm).

Window classes are case-sensitive, except when using the [i)
modifier](RegEx-QuickRef.htm#opt_i) in a RegEx pattern.

The following example activates a console window (e.g. cmd.exe):

    WinActivate "ahk_class ConsoleWindowClass"

The following example does the same as above, but uses a [regular
expression](RegEx-QuickRef.htm) (note that the RegEx [title matching
mode](../lib/SetTitleMatchMode.htm) must be turned on beforehand to make
it work):

    WinActivate "ahk_class ^ConsoleWindowClass$"

### ahk_id (Unique ID / HWND) {#ahk_id}

Each window or control has a unique ID, also known as a HWND (short for
handle to window). This ID can be used to identify the window or control
even if its title or text changes.

Use `ahk_id ``HWND`{.variable} or a pure HWND (as an
[Integer](../Concepts.htm#numbers) or an [Object](../Objects.htm) with a
HWND property) in `WinTitle`{.variable} to identify a window or control
by its unique ID.

When using `ahk_id ``HWND`{.variable},
[DetectHiddenWindows](../lib/DetectHiddenWindows.htm) affects whether
hidden top-level windows are detected, but hidden controls are always
detected. When using pure HWNDs, hidden windows are always detected
regardless of DetectHiddenWindows. [WinWait](../lib/WinWait.htm) and
[WinWaitClose](../lib/WinWaitClose.htm) are an exception, where both
`ahk_id ``HWND`{.variable} and pure HWNDs are affected by
DetectHiddenWindows.

`ahk_id ``HWND`{.variable} can also be combined with other criteria that
the given window must match. For example,
`WinExist("ahk_id " ahwnd " ahk_class " aclass)` returns
`ahwnd`{.variable} if the window is \"detected\" (according to
DetectHiddenWindows) and its window class matches the string contained
by `aclass`{.variable}.

The ID of a window is typically retrieved via
[WinExist](../lib/WinExist.htm) or [WinGetID](../lib/WinGetID.htm). The
ID of a control is typically retrieved via
[ControlGetHwnd](../lib/ControlGetHwnd.htm),
[MouseGetPos](../lib/MouseGetPos.htm), or [DllCall](../lib/DllCall.htm).
[Gui](../lib/Gui.htm) and [GuiControl](../lib/GuiControl.htm) objects
have a `Hwnd` property and therefore can be used directly in
`WinTitle`{.variable}.

The following examples operate on a window by a unique ID stored in
`VarContainingID`{.variable}:

    ; Pass an Integer.
    WinActivate Integer(VarContainingID)
    WinShow A_ScriptHwnd
    WinWaitNotActive WinExist("A")

    ; Pass an Object with a HWND property.
    WinActivate {Hwnd: VarContainingID}
    WinWaitClose myGuiObject

    ; Use the ahk_id prefix.
    WinActivate "ahk_id " VarContainingID

If the object has no HWND property or the property\'s value is not an
integer, a [PropertyError](../lib/Error.htm#PropertyError) or
[TypeError](../lib/Error.htm#TypeError) is thrown.

### ahk_pid (Process ID) {#ahk_pid}

Use `ahk_pid ``PID`{.variable} in `WinTitle`{.variable} to identify a
window belonging to a specific process. The process identifier (PID) is
typically retrieved by [WinGetPID](../lib/WinGetPID.htm),
[Run](../lib/Run.htm) or [Process functions](../lib/Process.htm). The ID
of a window\'s process can be revealed via Window Spy.

The following example activates a window by a process ID stored in
`VarContainingPID`{.variable}:

    WinActivate "ahk_pid " VarContainingPID

### ahk_exe (Process Name/Path) {#ahk_exe}

Use `ahk_exe ``ProcessNameOrPath`{.variable} in `WinTitle`{.variable} to
identify a window belonging to any process with the given name or path.

While the [ahk_pid criterion](#ahk_pid) is limited to one specific
process, the ahk_exe criterion considers all processes with name or full
path matching a given string. If the RegEx [title matching
mode](../lib/SetTitleMatchMode.htm) is active,
`ProcessNameOrPath`{.variable} accepts a [regular
expression](RegEx-QuickRef.htm) which must match the full path of the
process. Otherwise, it accepts a case-insensitive name or full path; for
example, `ahk_exe notepad.exe` covers `ahk_exe C:\Windows\Notepad.exe`,
`ahk_exe C:\Windows\System32\Notepad.exe` and other variations. The name
of a window\'s process can be revealed via Window Spy.

The following example activates a Notepad window by its process name:

    WinActivate "ahk_exe notepad.exe"

The following example does the same as above, but uses a [regular
expression](RegEx-QuickRef.htm) (note that the RegEx [title matching
mode](../lib/SetTitleMatchMode.htm) must be turned on beforehand to make
it work):

    WinActivate "ahk_exe i)\\notepad\.exe$"  ; Match the name part of the full path.

### ahk_group (Window Group) {#ahk_group}

Use `ahk_group ``GroupName`{.variable} in `WinTitle`{.variable} to
identify a window or windows matching the rules contained by a
previously defined [window group](../lib/GroupAdd.htm).

[WinMinimize](../lib/WinMinimize.htm),
[WinMaximize](../lib/WinMaximize.htm),
[WinRestore](../lib/WinRestore.htm), [WinHide](../lib/WinHide.htm),
[WinShow](../lib/WinShow.htm), [WinClose](../lib/WinClose.htm), and
[WinKill](../lib/WinKill.htm) will operate upon [all]{.underline} the
group\'s windows. By contrast, the other windowing functions such as
[WinActivate](../lib/WinActivate.htm) and
[WinExist](../lib/WinExist.htm) will operate only upon the topmost
window of the group.

The following example activates any window matching the criteria defined
by a window group:

    ; Define the group: Windows Explorer windows
    GroupAdd "Explorer", "ahk_class ExploreWClass" ; Unused on Vista and later
    GroupAdd "Explorer", "ahk_class CabinetWClass"

    ; Activate any window matching the above criteria
    WinActivate "ahk_group Explorer"

## Multiple Criteria {#multi}

By contrast with the [ahk_group criterion](#ahk_group) (which broadens
the search), the search may be narrowed by specifying more than one
criterion within the `WinTitle`{.variable} parameter. In the following
example, the script waits for a window whose title contains *My
File.txt* [and]{.underline} whose class is *Notepad*:

    WinWait "My File.txt ahk_class Notepad"
    WinActivate  ; Activate the window it found.

When using this method, the text of the title (if any is desired) should
be listed first, followed by one or more additional criteria. Criteria
beyond the first should be separated from the previous with exactly
[one]{.underline} space or tab (any other spaces or tabs are treated as
a literal part of the previous criterion).

The [ahk_id criterion](#ahk_id) can be combined with other criteria to
test a window\'s title, class or other attributes:

    MouseGetPos ,, &id
    if WinExist("ahk_class Notepad ahk_id " id)
        MsgBox "The mouse is over Notepad."

## Last Found Window {#LastFoundWindow}

This is the window most recently found by
[WinExist](../lib/WinExist.htm), [WinActive](../lib/WinActive.htm),
[WinWait\[Not\]Active](../lib/WinWaitActive.htm),
[WinWait](../lib/WinWait.htm), or
[WinWaitClose](../lib/WinWaitClose.htm). It can make scripts easier to
create and maintain since `WinTitle`{.variable} and `WinText`{.variable}
of the target window do not need to be repeated for every windowing
function. In addition, scripts perform better because they don\'t need
to search for the target window again after it has been found the first
time.

The last found window can be used by all of the windowing functions
except [WinWait](../lib/WinWait.htm),
[WinActivateBottom](../lib/WinActivateBottom.htm),
[GroupAdd](../lib/GroupAdd.htm), [WinGetCount](../lib/WinGetCount.htm),
and [WinGetList](../lib/WinGetList.htm). To use it, simply omit all four
window parameters (`WinTitle`{.variable}, `WinText`{.variable},
`ExcludeTitle`{.variable}, and `ExcludeText`{.variable}).

Each [thread](Threads.htm) retains its own value of the last found
window, meaning that if the [current thread](Threads.htm) is interrupted
by another, when the original thread is resumed it will still have its
original value of the last found window, not that of the interrupting
thread.

If the last found window is a hidden [Gui window](../lib/Gui.htm), it
can be used even when
[DetectHiddenWindows](../lib/DetectHiddenWindows.htm) is turned off.
This is often used in conjunction with the GUI\'s
[+LastFound](../lib/Gui.htm#LastFound) option.

The following example opens Notepad, waits until it exists and activates
it:

    Run "Notepad"
    WinWait "Untitled - Notepad"
    WinActivate ; Use the window found by WinWait.

The following example activates and maximizes the Notepad window found
by WinExist:

    if WinExist("Untitled - Notepad")
    {
        WinActivate ; Use the window found by WinExist.
        WinMaximize ; Same as above.
        Send "Some text.{Enter}"
    }

The following example activates the calculator found by WinExist and
moves it to a new position:

    if not WinExist("Calculator")
    {
        ; ...
    }
    else
    {
        WinActivate ; Use the window found by WinExist.
        WinMove 40, 40 ; Same as above.
    }
