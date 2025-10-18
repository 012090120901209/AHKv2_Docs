# OutputDebug

Sends a string to the debugger (if any) for display.

``` Syntax
OutputDebug Text
```

## Parameters {#Parameters}

Text

:   Type: [String](../Concepts.htm#strings)

    The text to send to the debugger for display. This text may include
    linefeed characters (\`n) to start new lines. In addition, a single
    long line can be broken up into several shorter ones by means of a
    [continuation section](../Scripts.htm#continuation).

## Remarks {#Remarks}

If the script\'s process has no debugger, the system debugger displays
the string. If the system debugger is not active, this function has no
effect.

One example of a debugger is DebugView, which is free and available at
[microsoft.com](https://learn.microsoft.com/sysinternals/downloads/debugview).

See also: [other debugging methods](../Scripts.htm#debug)

## Related {#Related}

[FileAppend](FileAppend.htm), [continuation
sections](../Scripts.htm#continuation)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Sends a string to the debugger (if any) for
display.

    OutputDebug A_Now ': Because the window "' TargetWindowTitle '" did not exist, the process was aborted.'
:::
