# MonitorGetCount

Returns the total number of monitors.

``` Syntax
Count := MonitorGetCount()
```

## Parameters {#Parameters}

This function has no parameters.

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers)

This function returns the total number of monitors.

## Remarks {#Remarks}

Unlike the SM_CMONITORS system property retrieved via
[`SysGet`](SysGet.htm)`(80)`, the return value includes all monitors,
even those not being used as part of the desktop.

## Related {#Related}

[SysGet](SysGet.htm), [Monitor functions](Monitor.htm)

## Examples {#Examples}

See [example #1](Monitor.htm#ExLoopAll) on the [Monitor
Functions](Monitor.htm) page for a demonstration of this function.
