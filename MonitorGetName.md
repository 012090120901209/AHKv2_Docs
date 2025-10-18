# MonitorGetName

Returns the operating system\'s name of the specified monitor.

``` Syntax
Name := MonitorGetName(N)
```

## Parameters {#Parameters}

N

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted, the primary monitor will be used. Otherwise, specify the
    monitor number, between 1 and the number returned by
    [MonitorGetCount](MonitorGetCount.htm).

## Return Value {#Return_Value}

Type: [String](../Concepts.htm#strings)

This function returns the operating system\'s name for the specified
monitor.

## Error Handling {#Error_Handling}

An exception is thrown on failure.

## Related {#Related}

[SysGet](SysGet.htm), [Monitor functions](Monitor.htm)

## Examples {#Examples}

See [example #1](Monitor.htm#ExLoopAll) on the [Monitor
Functions](Monitor.htm) page for a demonstration of this function.
