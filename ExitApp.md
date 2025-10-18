# ExitApp

Terminates the script.

``` Syntax
ExitApp ExitCode
```

## Parameters {#Parameters}

ExitCode

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted, it defaults to 0 (zero is traditionally used to indicate
    success). Otherwise, specify an integer between -2147483648 and
    2147483647 that is returned to its caller when the script exits.
    This code is accessible to any program that spawned the script, such
    as another script (via RunWait) or a batch (.bat) file.

## Remarks {#Remarks}

This is equivalent to choosing \"Exit\" from the script\'s tray menu or
main menu.

Any functions registered by [OnExit](OnExit.htm) are called before the
script terminates. If such a function returns a non-zero integer, the
script does not terminate; instead, the current
[thread](../misc/Threads.htm) exits as if [Exit](Exit.htm) was called.

Terminating the script is not the same as exiting each thread. For
instance, [Finally](Finally.htm) blocks are not executed and
[\_\_Delete](../Objects.htm#Custom_NewDelete) is not called for objects
contained by local variables.

ExitApp is often unnecessary in scripts which are not
[persistent](../Scripts.htm#persistent).

## Related {#Related}

[Exit](Exit.htm), [OnExit](OnExit.htm), [Persistent](Persistent.htm)

## Examples {#Examples}

::: {#ExHotkey .ex}
[](#ExHotkey){.ex_number} Press a hotkey to terminate the script.

    #x::ExitApp  ; Win+X
:::
