# MonitorGetWorkArea

Checks if the specified monitor exists and optionally retrieves the
bounding coordinates of its working area.

``` Syntax
ActualN := MonitorGetWorkArea(N, &Left, &Top, &Right, &Bottom)
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
    bounding coordinates of the working area, in pixels.

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers)

This function returns the monitor number (the same as *N* unless *N* was
omitted).

## Error Handling {#Error_Handling}

On failure, an exception is thrown and the output variables are not
modified.

## Remarks {#Remarks}

The working area of a monitor excludes the area occupied by the taskbar
and other registered desktop toolbars.

## Related {#Related}

[MonitorGet](MonitorGet.htm), [SysGet](SysGet.htm), [Monitor
functions](Monitor.htm)

## Examples {#Examples}

See [example #1](Monitor.htm#ExLoopAll) on the [Monitor
Functions](Monitor.htm) page for a demonstration of this function.
