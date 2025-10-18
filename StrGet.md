# StrGet

Copies a string from a memory address or buffer, optionally converting
it from a given code page.

``` Syntax
String := StrGet(Source , Length, Encoding)
String := StrGet(Source , Encoding)
```

## Parameters {#Parameters}

Source

:   Type: [Object](../Concepts.htm#objects) or
    [Integer](../Concepts.htm#numbers)

    A [Buffer](Buffer.htm)-like object containing the string, or the
    memory address of the string.

    Any object which implements [Ptr](Buffer.htm#Ptr) and
    [Size](Buffer.htm#Size) properties may be used, but this function is
    optimized for the native [Buffer](Buffer.htm) object. Passing an
    object with these properties ensures that the function does not read
    memory from an invalid location; doing so could cause crashes or
    other unpredictable behaviour.

    The string is not required to be
    [null-terminated](../Concepts.htm#null-termination) if a Buffer-like
    object is provided, or if *Length* is specified.

Length

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted (or when using 2-parameter mode), it defaults to the
    current length of the string, provided the string is
    [null-terminated](../Concepts.htm#null-termination). Otherwise,
    specify the maximum number of
    [characters](../Concepts.htm#character) to read.

    By default, StrGet only copies up to the first binary zero. If
    *Length* is negative, its absolute value indicates the exact number
    of characters to convert, including any binary zeros that the string
    might contain - in other words, the result is always a string of
    exactly that length.

    **Note:** Omitting *Length* when the string is not null-terminated
    may cause an access violation which terminates the program, or some
    other undesired result. Specifying an incorrect length may produce
    unexpected behaviour.

Encoding

:   Type: [String](../Concepts.htm#strings) or
    [Integer](../Concepts.htm#numbers)

    If omitted, the string is simply copied without any conversion
    taking place. Otherwise, specify the source encoding; for example,
    `"UTF-8"`, `"UTF-16"` or `"CP936"`. For numeric identifiers, the
    prefix \"CP\" can be omitted only in 3-parameter mode. Specify an
    empty string or `"CP0"` to use the system default ANSI code page.

## Return Value {#Return_Value}

Type: [String](../Concepts.htm#strings)

This function returns the copied or converted string. If the source
encoding was specified correctly, the return value always uses the
[native encoding](../Concepts.htm#string-encoding). The value is always
[null-terminated](../Concepts.htm#null-termination), but the
null-terminator is not included in its [length](StrLen.htm) except when
*Length* is negative, as described above.

## Error Handling {#Error_Handling}

A [ValueError](Error.htm#ValueError) is thrown if invalid parameters are
detected.

An [OSError](Error.htm#OSError) is thrown if the conversion could not be
performed.

## Remarks {#Remarks}

Note that the return value is always in the [native
encoding](../Concepts.htm#string-encoding) of the current executable,
whereas *Encoding* specifies how to interpret the string read from the
given *Source*. If no *Encoding* is specified, the string is simply
copied without any conversion taking place.

In other words, StrGet is used to retrieve text from a memory address or
buffer, or convert it to a format the script can understand.

If conversion between code pages is necessary, the length of the return
value may differ from the length of the source string.

## Related {#Related}

[String Encoding](../Concepts.htm#string-encoding),
[StrPut](StrPut.htm), [Binary Compatibility](../Compat.htm),
[FileEncoding](FileEncoding.htm), [DllCall](DllCall.htm), [Buffer
object](Buffer.htm), [VarSetStrCapacity](VarSetStrCapacity.htm)

## Examples {#Examples}

::: {#ExNumEnc .ex}
[](#ExNumEnc){.ex_number} Either *Length* or *Encoding* may be specified
directly after *Source*, but in those cases *Encoding* must be
non-numeric.

    str := StrGet(address, "cp0")  ; Code page 0, unspecified length
    str := StrGet(address, n, 0)   ; Maximum n chars, code page 0
    str := StrGet(address, 0)      ; Maximum 0 chars (always blank)
:::
