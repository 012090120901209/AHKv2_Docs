# #WinActivateForce

Skips the gentle method of activating a window and goes straight to the
forceful method.

``` Syntax
#WinActivateForce
```

Specifying this anywhere in a script will cause built-in functions that
activate a window \-- such as [WinActivate](WinActivate.htm),
[WinActivateBottom](WinActivateBottom.htm), and
[GroupActivate](GroupActivate.htm) \-- to skip the \"gentle\" method of
activating a window and go straight to the more forceful methods.

Although this directive will usually not change how quickly or reliably
a window is activated, it might prevent task bar buttons from flashing
when different windows are activated quickly one after the other.

## Remarks {#Remarks}

Like other directives, #WinActivateForce cannot be executed
conditionally.

## Related {#Related}

[WinActivate](WinActivate.htm),
[WinActivateBottom](WinActivateBottom.htm),
[GroupActivate](GroupActivate.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Enables the forceful method of activating a
window.

    #WinActivateForce
:::
