# Exit

Exits the [current thread](../misc/Threads.htm).

``` Syntax
Exit ExitCode
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

The Exit function terminates only the [current
thread](../misc/Threads.htm). In other words, the stack of functions
called directly or indirectly by a [menu](Menu.htm),
[timer](SetTimer.htm), or [hotkey](../Hotkeys.htm) function will all be
returned from as though a [Return](Return.htm) were immediately
encountered in each. If used directly inside such a function \-- or in
[global code](../Language.htm#global-code) \-- Exit is equivalent to
[Return](Return.htm).

If the script is not [persistent](../Scripts.htm#persistent) and this is
the last thread, the script will terminate after the thread exits.

Use [ExitApp](ExitApp.htm) to completely terminate a script that is
[persistent](../Scripts.htm#persistent).

## Related {#Related}

[ExitApp](ExitApp.htm), [OnExit](OnExit.htm),
[Functions](../Functions.htm), [Return](Return.htm),
[Threads](../misc/Threads.htm), [Persistent](Persistent.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} In this example, the Exit function terminates
the call_exit function as well as the calling function.

    #z::
    {
        call_exit
        MsgBox "This MsgBox will never happen because of the Exit."
        call_exit() 
        {
            Exit ; Terminate this function as well as the calling function.
        }
    }
:::
