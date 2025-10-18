# HasMethod

Returns a non-zero number if the specified value has a method by the
specified name.

``` Syntax
HasMethod := HasMethod(Value , Name, ParamCount)
```

## Parameters {#Parameters}

Value

:   Type: [Any](../Concepts.htm#values)

    Any value, of any type except ComObject.

Name

:   Type: [String](../Concepts.htm#strings)

    If omitted, *Value* itself is checked whether it is callable.
    Otherwise, specify the method name to check for.

ParamCount

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted (or if the parameter count was not verified), a basic
    check is performed for a Call method to verify that the object is
    most likely callable.

    Otherwise, specify the number of parameters that would be passed to
    the method or function. If specified, the method\'s MinParams,
    MaxParams and IsVariadic properties may be queried to verify that it
    can accept this number of parameters. If those properties are not
    present, the parameter count is not verified.

    This count should not include the implicit `this` parameter.

## Return Value {#Return_Value}

Type: [Integer (boolean)](../Concepts.htm#boolean)

This function returns 1 (true) if a method was found and passed
validation (if performed), otherwise 0 (false).

## Remarks {#Remarks}

HasMethod has the same [limitations](GetMethod.htm#Remarks) as
[GetMethod](GetMethod.htm).

This function can be used to estimate whether a value supports a
specific action. For example, values without a Call method cannot be
called or passed to [SetTimer](SetTimer.htm), while values without
either an \_\_Enum method or a Call method cannot be passed to
[For](For.htm). However, the existence of a method does not guarantee
that it can be called, since there are requirements that must be met,
such as parameter count.

When *ParamCount* is specified, the validation this function performs is
equivalent to the validation performed by built-in functions such as
[SetTimer](SetTimer.htm).

A return value of 0 (false) does not necessarily indicate that the
method cannot be called, as the value may have a \_\_Call
[meta-function](../Objects.htm#Meta_Functions). However, \_\_Call is not
triggered in certain contexts, such as when \_\_Enum is being called by
[For](For.htm). If \_\_Call is present, there is no way to detect which
methods it may support.

This function supports [primitive values](../Objects.htm#primitive).

## Related {#Related}

[Objects](../Objects.htm), [HasBase](HasBase.htm),
[HasProp](HasProp.htm), [GetMethod](GetMethod.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Illustrates the use of this function.

    MsgBox HasMethod(0, "HasMethod") ; 1
    MsgBox HasMethod(0, "Call") ; 0
:::
