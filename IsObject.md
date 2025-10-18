# IsObject

Returns a non-zero number if the specified value is an object.

``` Syntax
Boolean := IsObject(Value)
```

## Parameters {#Parameters}

Value

:   Type: [Any](../Concepts.htm#values)

    The value to check.

## Return Value {#Return_Value}

Type: [Integer (boolean)](../Concepts.htm#boolean)

This function returns 1 (true) if *Value* is an object, otherwise 0
(false).

## Remarks {#Remarks}

Any value which is not a primitive value (number or string) is
considered to be an object, including those which do not derive from
[Object](Object.htm), such as COM wrapper objects. This distinction is
made because objects share several common traits in contrast to
primitive values:

-   Each object is dynamically allocated and
    [reference-counted](../Objects.htm#Reference_Counting). Any number
    of variables, properties or array elements may refer to the same
    object. For immutable values this distinction isn\'t important, but
    objects can have mutable properties.
-   Each object has a [unique address](../Objects.htm#ObjPtr) which is
    also an interface pointer compatible with
    [IDispatch](https://learn.microsoft.com/windows/win32/api/oaidl/nn-oaidl-idispatch).
-   An object compares equal to another value only if it is the same
    object.
-   An object cannot be implicitly converted to a string or number.

## Related {#Related}

[Objects](../Objects.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Reports \"This is an object.\" because the
value is an object.

    obj := {key: "value"}

    if IsObject(obj)
        MsgBox "This is an object."
    else
        MsgBox "This is not an object."
:::
