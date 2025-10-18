# DateDiff

Compares two [date-time](FileSetTime.htm#YYYYMMDD) values and returns
the difference.

``` Syntax
Result := DateDiff(DateTime1, DateTime2, TimeUnits)
```

## Parameters {#Parameters}

DateTime1, DateTime2

:   Type: [String](../Concepts.htm#strings)

    Date-time stamps in the [YYYYMMDDHH24MISS](FileSetTime.htm#YYYYMMDD)
    format.

    If either is an empty string, the current local date and time
    ([A_Now](../Variables.htm#Now)) is used.

TimeUnits

:   Type: [String](../Concepts.htm#strings)

    Units to measure the difference in. *TimeUnits* may be one of the
    following strings (or just the first letter): Seconds, Minutes,
    Hours or Days.

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers)

This function returns the difference between the two timestamps, in the
units specified by *TimeUnits*. If *DateTime1* is earlier than
*DateTime2*, a negative number is returned.

The result is always rounded [down]{.underline} to the nearest integer.
For example, if the actual difference between two timestamps is 1.999
days, it will be reported as 1 day. If higher precision is needed,
specify Seconds for *TimeUnits* and divide the result by 60.0, 3600.0,
or 86400.0.

## Remarks {#Remarks}

The built-in variable **A_Now** contains the current local time in
[YYYYMMDDHH24MISS](FileSetTime.htm#YYYYMMDD) format.

To precisely determine the elapsed time between two events, use the
[A_TickCount method](../Variables.htm#TickCount) because it provides
millisecond precision.

To add or subtract a certain number of seconds, minutes, hours, or days
from a timestamp, use [DateAdd](DateAdd.htm) (subtraction is achieved by
adding a negative number).

If *DateTime* contains an invalid timestamp or a year prior to 1601, a
[ValueError](Error.htm#ValueError) is thrown.

## Related {#Related}

[DateAdd](DateAdd.htm), [FileGetTime](FileGetTime.htm),
[FormatTime](FormatTime.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Calculates the number of days between two
timestamps and reports the result.

    var1 := "20050126"
    var2 := "20040126"
    MsgBox DateDiff(var1, var2, "days")  ; The answer will be 366 since 2004 is a leap year.
:::
