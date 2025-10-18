# #MaxThreads

Sets the maximum number of simultaneous [threads](../misc/Threads.htm).

``` Syntax
#MaxThreads Value
```

## Parameters {#Parameters}

Value

:   Type: [Integer](../Concepts.htm#numbers)

    The maximum total number of [threads](../misc/Threads.htm) that can
    exist simultaneously. Specifying a number higher than 255 is the
    same as specifying 255.

## Remarks {#Remarks}

If this directive is unspecified in the script, it will behave as though
set to 10.

This setting is global, meaning that it needs to be specified only once
(anywhere in the script) to affect the behavior of the entire script.

Although a value of 1 is allowed, it is not recommended because it would
prevent new [hotkeys](../Hotkeys.htm) from launching whenever the script
is displaying a [message box](MsgBox.htm) or other dialog. It would also
prevent [timers](SetTimer.htm) from running whenever another
[thread](../misc/Threads.htm) is sleeping or waiting.

The [OnExit](OnExit.htm) callback function will always launch regardless
of how many threads exist.

If this setting is lower than
[#MaxThreadsPerHotkey](_MaxThreadsPerHotkey.htm), it effectively
overrides that setting.

Like other directives, #MaxThreads cannot be executed conditionally.

## Related {#Related}

[#MaxThreadsPerHotkey](_MaxThreadsPerHotkey.htm),
[Threads](../misc/Threads.htm),
[A_MaxHotkeysPerInterval](A_MaxHotkeysPerInterval.htm),
[ListHotkeys](ListHotkeys.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Allows a maximum of 2 instead of 10
simultaneous threads.

    #MaxThreads 2
:::
