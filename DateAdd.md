# DateAdd

Adds or subtracts time from a [date-time](FileSetTime.htm#YYYYMMDD)
value.

``` Syntax
Result := DateAdd(DateTime, Time, TimeUnits)
```

## Parameters {#Parameters}

DateTime

:   Type: [String](../Concepts.htm#strings)

    A date-time stamp in the
    [YYYYMMDDHH24MISS](FileSetTime.htm#YYYYMMDD) format.

Time

:   Type: [Integer](../Concepts.htm#numbers) or
    [Float](../Concepts.htm#numbers)

    The amount of time to add, as an integer or floating-point number.
    Specify a negative number to perform subtraction.

TimeUnits

:   Type: [String](../Concepts.htm#strings)

    The meaning of the *Time* parameter. *TimeUnits* may be one of the
    following strings (or just the first letter): Seconds, Minutes,
    Hours or Days.

## Return Value {#Return_Value}

Type: [String](../Concepts.htm#strings)

This function returns a string of digits in the
[YYYYMMDDHH24MISS](FileSetTime.htm#YYYYMMDD) format. This string should
not be treated as a number, i.e. one should not perform math on it or
compare it numerically.

## Remarks {#Remarks}

The built-in variable **A_Now** contains the current local time in
[YYYYMMDDHH24MISS](FileSetTime.htm#YYYYMMDD) format.

To calculate the amount of time between two timestamps, use
[DateDiff](DateDiff.htm).

If *DateTime* contains an invalid timestamp or a year prior to 1601, a
[ValueError](Error.htm#ValueError) is thrown.

## Related {#Related}

[DateDiff](DateDiff.htm), [FileGetTime](FileGetTime.htm),
[FormatTime](FormatTime.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Calculates the date 31 days from now and
reports the result in human-readable form.

    later := DateAdd(A_Now, 31, "days")
    MsgBox FormatTime(later)
:::
