# Ord

Returns the ordinal value (numeric character code) of the first
character in the specified string.

``` Syntax
Number := Ord(String)
```

## Parameters {#Parameters}

String

:   Type: [String](../Concepts.htm#strings)

    The string whose ordinal value is retrieved.

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers)

This function returns the ordinal value of *String*, or 0 if *String* is
empty. If *String* begins with a Unicode supplementary character, this
function returns the corresponding Unicode character code (a number
between 0x10000 and 0x10FFFF). Otherwise it returns a value in the range
0 to 255 (for ANSI) or 0 to 0xFFFF (for Unicode). See [Unicode vs
ANSI](../Compat.htm#Format) for details.

## Related {#Related}

[Chr](Chr.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Both message boxes below show 116, because only
the first character is considered.

    MsgBox Ord("t") 
    MsgBox Ord("test")
:::
