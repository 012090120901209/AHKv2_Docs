# Thread

Sets the priority or interruptibility of [threads](../misc/Threads.htm).
It can also temporarily disable all [timers](SetTimer.htm).

``` Syntax
Thread SubFunction , Value1, Value2
```

The *SubFunction*, *Value1*, and *Value2* parameters are dependent upon
each other and their usage is described below.

## Sub-functions {#SubFunctions}

For *SubFunction*, specify one of the following:

-   [NoTimers](#NoTimers): Prevents interruptions from any timers.
-   [Priority](#Priority): Changes the priority level of the current
    thread.
-   [Interrupt](#Interrupt): Changes the duration of interruptibility
    for newly launched threads.

### NoTimers {#NoTimers}

Prevents interruptions from any timers.

``` Syntax
Thread "NoTimers" , False
```

This sub-function prevents interruptions from any [timers](SetTimer.htm)
until the [current thread](../misc/Threads.htm) either ends, executes
`Thread "NoTimers", false`, or is interrupted by another thread that
allows timers (in which case timers can interrupt the interrupting
thread until it finishes).

If this setting is not changed by [the auto-execute
thread](../Scripts.htm#auto), all threads start off as interruptible by
timers (though the settings of the [Interrupt](#Interrupt) sub-function
described below will still apply). By contrast, if the auto-execute
thread turns on this setting but never turns it off, every newly
launched [thread](../misc/Threads.htm) (such as a
[hotkey](../Hotkeys.htm), [custom menu item](Menu.htm), or
[timer](SetTimer.htm)) starts off immune to interruptions by timers.

Regardless of the default setting, timers will always operate when the
script has no threads (unless [Pause](Pause.htm) has been turned on).

`Thread "NoTimers"` is equivalent to `Thread "NoTimers", true`. In
addition, since the *False* parameter is an
[expression](../Variables.htm#Expressions), true resolves to 1, and
false to 0. See [Boolean Values](../Concepts.htm#boolean) for details.

### Priority {#Priority}

Changes the priority level of the current thread.

``` Syntax
Thread "Priority", Level
```

Specify for *Level* an integer between -2147483648 and 2147483647 (or an
[expression](../Variables.htm#Expressions)) to indicate the current
thread\'s new priority. This has no effect on other threads. See
[Threads](../misc/Threads.htm) for details.

Due to its ability to buffer events, the function
[Critical](Critical.htm) is generally superior to this sub-function.

On a related note, the OS\'s priority level for the entire script can be
changed via [ProcessSetPriority](ProcessSetPriority.htm). For example:

    ProcessSetPriority "High"

### Interrupt {#Interrupt}

Changes the duration of interruptibility for newly launched threads.

``` Syntax
Thread "Interrupt" , Duration, LineCount
```

**Note:** This sub-function should be used sparingly because most
scripts perform more consistently with settings close to the defaults.

By default, every newly launched thread is uninterruptible for a
*Duration* of 15 milliseconds or a *LineCount* of 1000 script lines,
whichever comes first. This gives the thread a chance to finish rather
than being immediately interrupted by another thread that is waiting to
launch (such as a buffered [hotkey](../Hotkeys.htm) or a series of
[timed subroutines](SetTimer.htm) that are all due to be run).

**Note:** Any *Duration* less than 17 might result in a shorter actual
duration or immediate interruption, since the system tick count has a
minimum resolution of 10 to 16 milliseconds. However, at least one line
will execute before the thread becomes interruptible, allowing the
script to enable [Critical](Critical.htm), if needed.

If either parameter is 0, each newly launched thread is immediately
interruptible. If either parameter is -1, the thread cannot be
interrupted as a result of that parameter. The maximum for both
parameters is 2147483647.

This setting is global, meaning that it affects all subsequent threads,
even if this function was not called by [the auto-execute
thread](../Scripts.htm#auto). However, [interrupted
threads](../misc/Threads.htm) are unaffected because their period of
uninterruptibility has already expired. Similarly, the [current
thread](../misc/Threads.htm) is unaffected except if it is
uninterruptible at the time the *LineCount* parameter is changed, in
which case the new *LineCount* will be in effect for it.

If a [hotkey](../Hotkeys.htm) is pressed or a [custom menu
item](Menu.htm) is selected while the [current
thread](../misc/Threads.htm) is uninterruptible, that event will be
buffered. In other words, it will launch when the current thread
finishes or becomes interruptible, whichever comes first. The exception
to this is when the current thread becomes interruptible before it
finishes, and it is of higher [priority](#Priority) than the buffered
event; in this case the buffered event is unbuffered and discarded.

Regardless of this sub-function, a thread will become interruptible the
moment it displays a [MsgBox](MsgBox.htm), [InputBox](InputBox.htm),
[FileSelect](FileSelect.htm), or [DirSelect](DirSelect.htm) dialog.

Either parameter can be left blank to avoid changing it.

## Remarks {#Remarks}

Due to its greater flexibility and its ability to buffer events, the
function [Critical](Critical.htm) is generally more useful than
`Thread "Interrupt"` and `Thread "Priority"`.

## Related {#Related}

[Critical](Critical.htm), [Threads](../misc/Threads.htm),
[Hotkey](Hotkey.htm), [Menu object](Menu.htm), [SetTimer](SetTimer.htm),
[Process functions](Process.htm)

## Examples {#Examples}

::: {#ExPriority .ex}
[](#ExPriority){.ex_number} Makes the priority of the current thread
slightly above average.

    Thread "Priority", 1
:::

::: {#ExInterrupt .ex}
[](#ExInterrupt){.ex_number} Makes each newly launched thread
immediately interruptible.

    Thread "Interrupt", 0
:::

::: {#ExInterrupt2 .ex}
[](#ExInterrupt2){.ex_number} Makes each thread interruptible after
50 ms or 2000 lines, whichever comes first.

    Thread "Interrupt", 50, 2000
:::
