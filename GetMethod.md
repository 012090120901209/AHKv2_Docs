# GetMethod

Retrieves the implementation function of a method.

``` Syntax
Method := GetMethod(Value , Name, ParamCount)
```

## Parameters {#Parameters}

Value

:   Type: [Any](../Concepts.htm#values)

    Any value, of any type except ComObject.

Name

:   Type: [String](../Concepts.htm#strings)

    If omitted, validation is performed on *Value* itself and *Value* is
    returned if successful. Otherwise, specify the name of the method to
    retrieve.

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

Type: [Function Object](../misc/Functor.htm)

This function returns the function object which contains the
implementation of the method, or *Value* itself if *Name* was omitted.

## Errors {#Errors}

If the method is not found or cannot be retrieved without invoking a
property getter, a [MethodError](Error.htm#MethodError) is thrown.

If validation is attempted, exceptions may be thrown as a result of
querying the method\'s properties. A [ValueError](Error.htm#ValueError)
or [MethodError](Error.htm#MethodError) is thrown if validation fails.

## Remarks {#Remarks}

Methods may be defined through one of the following:

-   A dynamic property with a *call* accessor function. This includes:
    -   Any property created by a [method
        definition](../Objects.htm#Custom_Classes_method) within a
        class.
    -   Any property created by passing a descriptor like `{Call: fn}`
        to [DefineProp](Object.htm#DefineProp), where *fn* implements
        the method.
    -   Any predefined/built-in method.
-   An own value property of the object or one of its base objects,
    where the value is a [function object](../misc/Functor.htm).
-   A dynamic property with a getter which returns a function object.
    This case is not supported by GetMethod.
-   Handling within a \_\_Call
    [meta-function](../Objects.htm#Meta_Functions). Methods implemented
    this way cannot be detected and may not even have a corresponding
    function object, so are not supported by GetMethod.

When calling the function object, it is necessary to supply a value for
the normally-hidden *this* parameter. For example,
`Method(Value, Parameters*)`.

Although the standard implementation of GetMethod has limitations as
described above, if `Value.GetMethod(Name)` is used instead of
`GetMethod(Value, Name)`, the object *Value* can define its own
implementation of GetMethod.

`GetMethod(Value, "Call", N)` is not the same as `GetMethod(Value,, N)`,
as the Call method takes the function object itself as a parameter, and
its usage may otherwise differ from that of *Value*. For instance,
`Func.Prototype.Call` is a single method which applies to all built-in
and user-defined functions, and as such must accept any number of
parameters.

## Related {#Related}

[Objects](../Objects.htm), [HasMethod](HasMethod.htm),
[HasBase](HasBase.htm), [HasProp](HasProp.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Retrieves and reports information about the
[GetMethod method](Any.htm#GetMethod).

    method := GetMethod({}, "GetMethod")  ; It's also a method.
    MsgBox method.MaxParams  ; Takes 2 parameters, including 'this'.
    MsgBox method = GetMethod  ; Actually the same object in this case.
:::
