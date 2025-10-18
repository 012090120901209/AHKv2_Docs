# Integer

Converts a numeric string or floating-point value to an integer.

``` Syntax
IntValue := Integer(Value)
```

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers)

This function returns the result of converting *Value* to a pure integer
(having the [type name](Type.htm) \"Integer\"), or *Value* itself if it
is already the correct type.

## Remarks {#Remarks}

Any fractional part of *Value* is dropped, equivalent to
`Value < 0 ? Ceil(Value) : Floor(Value)`.

If the value cannot be converted, a [TypeError](Error.htm#TypeError) is
thrown.

To determine if a value can be converted to an integer, use the
[IsNumber](Is.htm#number) function.

Integer is actually a class, but can be called as a function.
`Value is Integer` can be used to check whether a value is a pure
integer.

## Related {#Related}

[Type](Type.htm), [Float](Float.htm), [Number](Number.htm),
[String](String.htm), [Values](../Concepts.htm#values),
[Expressions](../Language.htm#expressions), [Is functions](Is.htm)
