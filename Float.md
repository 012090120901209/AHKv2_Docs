# Float

Converts a numeric string or integer value to a floating-point number.

``` Syntax
FltValue := Float(Value)
```

## Return Value {#Return_Value}

Type: [Float](../Concepts.htm#numbers)

This function returns the result of converting *Value* to a pure
floating-point number (having the [type name](Type.htm) \"Float\"), or
*Value* itself if it is already the correct type.

## Remarks {#Remarks}

If the value cannot be converted, a [TypeError](Error.htm#TypeError) is
thrown.

To determine if a value can be converted to a floating-point number, use
the [IsNumber](Is.htm#number) function.

Float is actually a class, but can be called as a function.
`Value is Float` can be used to check whether a value is a pure
floating-point number.

## Related {#Related}

[Type](Type.htm), [Integer](Integer.htm), [Number](Number.htm),
[String](String.htm), [Values](../Concepts.htm#values),
[Expressions](../Language.htm#expressions), [Is functions](Is.htm)
