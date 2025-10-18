# MonitorGet

Checks if the specified monitor exists and optionally retrieves its
bounding coordinates.

``` Syntax
ActualN := MonitorGet(N, &Left, &Top, &Right, &Bottom)
```

## Parameters {#Parameters}

N

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted, the primary monitor will be used. Otherwise, specify the
    monitor number, between 1 and the number returned by
    [MonitorGetCount](MonitorGetCount.htm).

&Left, &Top, &Right, &Bottom

:   Type: [VarRef](../Concepts.htm#variable-references)

    If omitted, the corresponding value will not be stored. Otherwise,
    specify references to the output variables in which to store the
    bounding coordinates, in pixels.

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers)

This function returns the monitor number (the same as *N* unless *N* was
omitted).

## Error Handling {#Error_Handling}

On failure, an exception is thrown and the output variables are not
modified.

## Remarks {#Remarks}

The built-in variables [A_ScreenWidth](../Variables.htm#Screen) and
[A_ScreenHeight](../Variables.htm#Screen) contain the dimensions of the
primary monitor, in pixels.

[SysGet](SysGet.htm) can be used to retrieve the bounding rectangle of
all display monitors. For example, this retrieves the width and height
of the virtual screen:

    MsgBox SysGet(78) " x " SysGet(79)

## Related {#Related}

[MonitorGetWorkArea](MonitorGetWorkArea.htm), [SysGet](SysGet.htm),
[Monitor functions](Monitor.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Shows the bounding coordinates of the second
monitor in a message box.

    try
    {
        MonitorGet 2, &Left, &Top, &Right, &Bottom
        MsgBox "Left: " Left " -- Top: " Top " -- Right: " Right " -- Bottom: " Bottom
    }
    catch
        MsgBox "Monitor 2 doesn't exist or an error occurred."
:::

See [example #1](Monitor.htm#ExLoopAll) on the [Monitor
Functions](Monitor.htm) page for another demonstration of this function.
