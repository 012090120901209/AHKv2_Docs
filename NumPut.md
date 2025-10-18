# NumPut

Stores one or more numbers in binary format at the specified
address+offset.

``` Syntax
NumPut Type, Number, Type2, Number2, ... Target , Offset
```

## Parameters {#Parameters}

Type

:   Type: [String](../Concepts.htm#strings)

    One of the following strings: UInt, UInt64, Int, Int64, Short,
    UShort, Char, UChar, Double, Float, Ptr or UPtr

    For all integer types, or when passing pure integers, signed vs.
    unsigned does not affect the result due to the use of two\'s
    complement to represent signed integers.

    For details see [DllCall Types](DllCall.htm#types).

Number

:   Type: [Integer](../Concepts.htm#numbers)

    The number to store.

Target

:   Type: [Object](../Concepts.htm#objects) or
    [Integer](../Concepts.htm#numbers)

    A [Buffer](Buffer.htm)-like object or memory address.

    Any object which implements [Ptr](Buffer.htm#Ptr) and
    [Size](Buffer.htm#Size) properties may be used, but this function is
    optimized for the native [Buffer](Buffer.htm) object. Passing an
    object with these properties ensures that the function does not
    write to an invalid memory location; doing so could cause crashes or
    other unpredictable behaviour.

Offset

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted, it defaults to 0. Otherwise, specify an offset in bytes
    which is added to *Target* to determine the target address.

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers)

This function returns the address to the right of the last item written.
This can be used when writing a non-contiguous sequence of numbers, such
as in a structure for use with [DllCall](DllCall.htm), where some fields
are not being set. However, in many cases it is simpler and more
efficient to specify multiple *Type*, *Number* pairs instead. Passing
the address back to NumPut is less safe than passing a Buffer-like
object with an updated *Offset*.

## General Remarks {#General_Remarks}

A sequence of numbers can be written by repeating *Type* and *Number*
any number of times after the first *Number*. Each number is written at
the next byte after the previous number, with no padding. When creating
a structure for use with [DllCall](DllCall.htm), be aware that some
fields may need explicit padding added due to data alignment
requirements.

If an integer is too large to fit in the specified *Type*, its most
significant bytes are ignored; e.g. `NumPut("Char", 257, buf)` would
store the number 1.

An exception may be thrown if the target address is invalid. However,
some invalid addresses cannot be detected as such and may cause
unpredictable behaviour. Passing a [Buffer](Buffer.htm) object instead
of an address ensures that the target address can always be validated.

## Related {#Related}

[NumGet](NumGet.htm), [DllCall](DllCall.htm), [Buffer
object](Buffer.htm), [VarSetStrCapacity](VarSetStrCapacity.htm)
