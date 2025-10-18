# Throw

Signals the occurrence of an error. This signal can be caught by a
[Try](Try.htm)-[Catch](Catch.htm) statement.

``` Syntax
Throw Value
```

## Parameters {#Parameters}

Value

:   A value to throw; typically an [Error](Error.htm) object. For
    example:

        throw ValueError("Parameter #1 invalid", -1, theBadParam)

    Values of all kinds can be thrown, but if [Catch](Catch.htm) is used
    without specifying a class (or [Try](Try.htm) is used without
    [Catch](Catch.htm) or [Finally](Finally.htm)), it will only catch
    instances of the [Error](Error.htm) class.

    While execution is within a [Catch](Catch.htm), *Value* can be
    omitted to re-throw the caught value (avoiding the need to specify
    an output variable just for that purpose). This is supported even
    within a nested *Try-Finally*, but not within a nested *Try-Catch*.
    The line with `throw` does not need to be physically contained by
    the *Catch* statement\'s body; it can be used by a called function.

## Remarks {#Remarks}

The space or tab after `throw` is optional if the expression is enclosed
in parentheses, as in `throw(Error())`.

A thrown value or runtime error can be *caught* by
[Try](Try.htm)-[Catch](Catch.htm). In such cases, execution is
transferred into the *catch* statement or to the next statement after
the *try*. If a thrown value is not caught, the following occurs:

-   Any active [OnError](OnError.htm) callbacks are called. Each
    callback may inspect *Value* and either suppress or allow further
    callbacks and default handling.
-   By default, an error message is displayed based on what was thrown.
    If *Value* is an [Object](Object.htm) and owns a value property
    named *Message*, its value is used as the message. If *Value* is a
    non-numeric string, it is used as the message. In any other case, a
    default message is used. If *Value* is numeric, it is shown below
    the default message.
-   The thread exits. Note that this does not necessarily occur for
    continuable errors, but *throw* is never continuable.

## Related {#Related}

[Error Object](Error.htm), [Try](Try.htm), [Catch](Catch.htm),
[Finally](Finally.htm), [OnError](OnError.htm)

## Examples {#Examples}

See [Try](Try.htm#Examples).
