# String

Converts a value to a string.

``` Syntax
StrValue := String(Value)
```

## Return Value {#Return_Value}

Type: [String](../Concepts.htm#strings)

This function returns the result of converting *Value* to a string, or
*Value* itself if it is a string.

If *Value* is a number, the [default decimal
formatting](../Concepts.htm#number-default-format) is used.

If *Value* is an object, the return value is the result of calling
`Value.ToString()`. If the object has no such method, a
[MethodError](Error.htm#MethodError) is thrown. This method is not
implemented by default, so must be defined by the script.

## Related {#Related}

[Type](Type.htm), [Integer](Integer.htm), [Float](Float.htm),
[Values](../Concepts.htm#values),
[Expressions](../Language.htm#expressions), [Is functions](Is.htm)
