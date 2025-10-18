# Number

Converts a numeric string to a pure integer or floating-point number.

``` Syntax
NumValue := Number(Value)
```

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers) or
[Float](../Concepts.htm#numbers)

This function returns the result of converting *Value* to a pure integer
or floating-point number, or *Value* itself if it is already an Integer
or Float value.

## Remarks {#Remarks}

If the value cannot be converted, a [TypeError](Error.htm#TypeError) is
thrown.

To determine if a value can be converted to a number, use the
[IsNumber](Is.htm#number) function.

Number is actually a class, but can be called as a function.
`Value is Number` can be used to check whether a value is a pure number.

## Related {#Related}

[Type](Type.htm), [Float](Float.htm), [Integer](Integer.htm),
[String](String.htm), [Values](../Concepts.htm#values),
[Expressions](../Language.htm#expressions), [Is functions](Is.htm)
