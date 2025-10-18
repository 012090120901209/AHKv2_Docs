# #MaxThreadsPerHotkey

Sets the maximum number of simultaneous [threads](../misc/Threads.htm)
per [hotkey](../Hotkeys.htm) or [hotstring](../Hotstrings.htm).

``` Syntax
#MaxThreadsPerHotkey Value
```

## Parameters {#Parameters}

Value

:   Type: [Integer](../Concepts.htm#numbers)

    The maximum number of [threads](../misc/Threads.htm) that can be
    launched for a given hotkey/hotstring subroutine (limit 255).

## Remarks {#Remarks}

If this directive is unspecified in the script, it will behave as though
set to 1.

This setting is used to control how many \"instances\" of a given
[hotkey](../Hotkeys.htm) or [hotstring](../Hotstrings.htm) subroutine
are allowed to exist simultaneously. For example, if a hotkey has a max
of 1 and it is pressed again while its subroutine is already running,
the press will be ignored. This is helpful to prevent accidental
double-presses. However, if you wish these keypresses to be buffered
rather than ignored \-- perhaps to increase the responsiveness of the
keyboard\'s auto-repeat feature \-- use
[#MaxThreadsBuffer](_MaxThreadsBuffer.htm).

Unlike [#MaxThreads](_MaxThreads.htm), this setting is [not]{.underline}
global. Instead, position it before the first hotkey you wish to have
affected by it, which will result in all subsequent hotkeys using that
value until another instance of this directive is encountered.

The setting of [#MaxThreads](_MaxThreads.htm) \-- if lower than this
setting \-- takes precedence.

Like other directives, #MaxThreadsPerHotkey cannot be executed
conditionally.

## Related {#Related}

[#MaxThreads](_MaxThreads.htm),
[#MaxThreadsBuffer](_MaxThreadsBuffer.htm), [Critical](Critical.htm),
[Threads](../misc/Threads.htm), [Hotkey](Hotkey.htm),
[A_MaxHotkeysPerInterval](A_MaxHotkeysPerInterval.htm),
[ListHotkeys](ListHotkeys.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Allows a maximum of 3 simultaneous threads
instead of 1 per hotkey or hotstring.

    #MaxThreadsPerHotkey 3
:::
