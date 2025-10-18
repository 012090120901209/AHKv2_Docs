# Chr

Returns the string (usually a single character) corresponding to the
character code indicated by the specified number.

``` Syntax
String := Chr(Number)
```

## Parameters {#Parameters}

Number

:   Type: [Integer](../Concepts.htm#numbers)

    A Unicode character code between 0 and 0x10FFFF.

## Return Value {#Return_Value}

Type: [String](../Concepts.htm#strings)

The string corresponding to *Number*. This is always a single Unicode
character, but for practical reasons, Unicode supplementary characters
(where *Number* is in the range 0x10000 to 0x10FFFF) are counted as two
characters. That is, the length of the return value as reported by
[StrLen](StrLen.htm) may be 1 or 2. For further explanation, see [String
Encoding](../Concepts.htm#string-encoding).

If *Number* is 0, the return value is a string containing a binary null
character, not an empty (zero-length) string. This can be safely
assigned to a variable, passed to a function or concatenated with
another string. However, some built-in functions may \"see\" only the
part of the string preceding the first null character.

## Remarks {#Remarks}

The range and meaning of character codes depends on which [string
encoding](../Concepts.htm#string-encoding) is in use. Currently all
AutoHotkey v2 executables are built for Unicode, so this function always
accepts a Unicode character code and returns a Unicode (UTF-16) string.

Common character codes include 9 (tab), 10 (linefeed), 13 (carriage
return), 32 (space), 48-57 (the digits 0-9), 65-90 (uppercase A-Z), and
97-122 (lowercase a-z).

## Related {#Related}

[Ord](Ord.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Reports the string corresponding to the
character code 116.

    MsgBox Chr(116) ; Reports "t".
:::
