# StrCompare

Compares two strings alphabetically.

``` Syntax
Result := StrCompare(String1, String2 , CaseSense)
```

## Parameters {#Parameters}

String1, String2

:   Type: [String](../Concepts.htm#strings)

    The strings to be compared.

CaseSense

:   Type: [String](../Concepts.htm#strings) or [Integer
    (boolean)](../Concepts.htm#boolean)

    If omitted, it defaults to *Off*. Otherwise, specify one of the
    following values:

    **On** or **1** (true): The comparison is case-sensitive.

    **Off** or **0** (false): The comparison is not case-sensitive, i.e.
    the letters A-Z are considered identical to their lowercase
    counterparts.

    **Locale:** The comparison is not case-sensitive according to the
    rules of the current user\'s locale. For example, most English and
    Western European locales treat not only the letters A-Z as identical
    to their lowercase counterparts, but also non-ASCII letters like Ä
    and Ü as identical to theirs. *Locale* is 1 to 8 times slower than
    *Off* depending on the nature of the strings being compared.

    **Logical:** Like *Locale*, but digits in the strings are considered
    as numerical content rather than text. For example, `"A2"` is
    considered less than `"A10"`. However, if two numbers differ only by
    the presence of a leading zero, the string with leading zero may be
    considered [less]{.underline} than the other string. The exact
    behavior may differ between OS versions.

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers)

To indicate the relationship between *String1* and *String2*, this
function returns one of the following:

-   0, if *String1* is identical to *String2*
-   a positive integer, if *String1* is greater than *String2*
-   a negative integer, if *String1* is less than *String2*

To check for a specific relationship between the two strings, compare
the result to 0. For example:

    a_less_than_b := StrCompare(a, b) < 0
    a_greater_than_or_equal_to_b := StrCompare(a, b) >= 0

## Remarks {#Remarks}

This function is commonly used for [sort callbacks](Sort.htm#callback).

## Related {#Related}

[Sort](Sort.htm), [VerCompare](VerCompare.htm)

## Examples {#Examples}

::: {#ExCaseSens .ex}
[](#ExCaseSens){.ex_number} Demonstrates the difference between a
case-insensitive and case-sensitive comparison.

    MsgBox StrCompare("Abc", "abc") ; Returns 0
    MsgBox StrCompare("Abc", "abc", true) ; Returns -1
:::
