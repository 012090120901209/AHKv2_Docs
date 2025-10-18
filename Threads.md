# Threads

The *current thread* is defined as the flow of execution invoked by the
most recent event; examples include [hotkeys](../Hotkeys.htm), [SetTimer
subroutines](../lib/SetTimer.htm), [custom menu items](../lib/Menu.htm),
and [GUI events](../lib/Gui.htm#Events). The *current thread* can be
executing functions within its own subroutine or within other
subroutines called by that subroutine.

Although AutoHotkey doesn\'t actually use multiple threads, it simulates
some of that behavior: If a second thread is started \-- such as by
pressing another hotkey while the previous is still running \-- the
*current thread* will be interrupted (temporarily halted) to allow the
new thread to become *current*. If a third thread is started while the
second is still running, both the second and first will be in a dormant
state, and so on.

When the *current thread* finishes, the one most recently interrupted
will be resumed, and so on, until all the threads finally finish. When
resumed, a thread\'s settings for things such as
[SendMode](../lib/SendMode.htm) and
[SetKeyDelay](../lib/SetKeyDelay.htm) are automatically restored to what
they were just prior to its interruption; in other words, a thread will
experience no side-effects from having been interrupted (except for a
possible change in the [active window](../lib/WinActivate.htm)).

**Note:** The [KeyHistory](../lib/KeyHistory.htm) function/menu-item
shows how many threads are in an interrupted state and the
[ListHotkeys](../lib/ListHotkeys.htm) function/menu-item shows which
hotkeys have threads.

A single script can have multiple simultaneous
[MsgBox](../lib/MsgBox.htm), [InputBox](../lib/InputBox.htm),
[FileSelect](../lib/FileSelect.htm), and
[DirSelect](../lib/DirSelect.htm) dialogs. This is achieved by launching
a new thread (via [hotkey](../Hotkeys.htm), [timed
subroutine](../lib/SetTimer.htm), [custom menu item](../lib/Menu.htm),
etc.) while a prior thread already has a dialog displayed.

By default, a given [hotkey](../Hotkeys.htm) or
[hotstring](../Hotstrings.htm) subroutine cannot be run a second time if
it is already running. Use
[#MaxThreadsPerHotkey](../lib/_MaxThreadsPerHotkey.htm) to change this
behavior.

**Related:** The [Thread](../lib/Thread.htm) function sets the priority
or interruptibility of threads.

## Thread Priority {#Priority}

Any thread ([hotkey](../Hotkeys.htm), [timed
subroutine](../lib/SetTimer.htm), [custom menu item](../lib/Menu.htm),
etc.) with a priority lower than that of the *current thread* cannot
interrupt it. During that time, such timers will not run, and any
attempt by the user to create a thread (such as by pressing a
[hotkey](../Hotkeys.htm) or [GUI button](../lib/GuiControls.htm#Button))
will have no effect, nor will it be buffered. Because of this, it is
usually best to design high priority threads to finish quickly, or use
[Critical](../lib/Critical.htm) instead of making them high priority.

The default priority is 0. All threads use the default priority unless
changed by one of the following methods:

-   A timed subroutine is given a specific priority via
    [SetTimer](../lib/SetTimer.htm).
-   A hotkey is given a specific priority via the
    [Hotkey](../lib/Hotkey.htm) function.
-   A [hotstring](../Hotstrings.htm) is given a specific priority when
    it is defined, or via the [#Hotstring](../lib/_Hotstring.htm)
    directive.
-   A custom menu item is given a specific priority via the
    [Menu.Add](../lib/Menu.htm#Add) method.
-   The *current thread* sets its own priority via the
    [Thread](../lib/Thread.htm) function.

The [OnExit](../lib/OnExit.htm) callback function (if any) will always
run when called for, regardless of the *current thread*\'s priority.

## Thread Interruptibility {#Interrupt}

For most types of events, new threads are permitted to launch only if
the current thread is *interruptible*. A thread can be *uninterruptible*
for a number of reasons, including:

-   The thread has been marked as *critical*.
    [Critical](../lib/Critical.htm) may have been called by the thread
    itself or by [the auto-execute thread](../Scripts.htm#auto).
-   The thread has not been running long enough to meet the conditions
    for becoming interruptible, as set by [Thread
    Interrupt](../lib/Thread.htm#Interrupt).
-   One of the script\'s menus is being displayed (such as the [tray
    icon](../Program.htm#tray-icon) menu or a menu bar).
-   A delay is being performed by [Send](../lib/Send.htm) (most often
    due to [SetKeyDelay](../lib/SetKeyDelay.htm)),
    [WinActivate](../lib/WinActivate.htm), or a
    [Clipboard](../lib/A_Clipboard.htm) operation.
-   An [OnExit](../lib/OnExit.htm) thread is executing.
-   A warning dialog is being displayed due to the
    [A_MaxHotkeysPerInterval](../lib/A_MaxHotkeysPerInterval.htm) limit
    being reached, or due to a problem activating the keyboard or mouse
    hook (very rare).

### Behavior of Uninterruptible Threads {#Behave}

Unlike high-priority threads, events that occur while the thread is
uninterruptible are not discarded. For example, if the user presses a
[hotkey](../Hotkeys.htm) while the current thread is uninterruptible,
the hotkey is buffered indefinitely until the current thread finishes or
becomes interruptible, at which time the hotkey is launched as a new
thread.

Any thread may be interrupted in emergencies. Emergencies consist of:

-   An [OnExit](../lib/OnExit.htm) callback.
-   Any [OnMessage](../lib/OnMessage.htm) function that monitors a
    message which is not [buffered](../lib/OnMessage.htm#buffering).
-   Any [callback](../lib/CallbackCreate.htm) indirectly triggered by
    the thread itself (e.g. via [SendMessage](../lib/PostMessage.htm) or
    [DllCall](../lib/DllCall.htm)).

To avoid these interruptions, temporarily disable such functions.

A [critical](../lib/Critical.htm) thread becomes interruptible when a
[MsgBox](../lib/MsgBox.htm) or other dialog is displayed. However,
unlike [Thread Interrupt](../lib/Thread.htm#Interrupt), the thread
becomes critical (and therefore uninterruptible) again after the user
dismisses the dialog.
