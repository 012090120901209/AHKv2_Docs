# VerCompare

Compares two version strings.

``` Syntax
Result := VerCompare(VersionA, VersionB)
```

## Parameters {#Parameters}

VersionA

:   Type: [String](../Concepts.htm#strings)

    The first version string to be compared.

VersionB

:   Type: [String](../Concepts.htm#strings)

    The second version string to be compared, optionally prefixed with
    one of the following operators: `<`, `<=`, `>`, `>=` or `=`.

## Return Value {#Return_Value}

Type: [Integer (boolean)](../Concepts.htm#boolean) or
[Integer](../Concepts.htm#numbers)

If *VersionB* begins with an operator symbol, this function returns 1
(true) or 0 (false).

Otherwise, this function returns one of the following to indicate the
relationship between *VersionA* and *VersionB*:

-   0 if *VersionA* is equal to *VersionB*
-   a positive integer if *VersionA* is greater than *VersionB*
-   a negative integer if *VersionA* is less than *VersionB*

To check for a specific relationship between the two strings, compare
the result to 0. For example:

    a_less_than_b := VerCompare(a, b) < 0
    a_greater_than_or_equal_to_b := VerCompare(a, b) >= 0

## Remarks {#Remarks}

Version strings are compared according to the same rules as
[#Requires](_Requires.htm#compare).

This function should correctly compare [Semantic Versioning
2.0.0](https://semver.org/spec/v2.0.0.html) version strings, but the
parameters are not required to be valid SemVer strings.

This function can be used in a [sort callback](Sort.htm#callback).

## Related {#Related}

[#Requires](_Requires.htm), [Sort](Sort.htm),
[StrCompare](StrCompare.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Checks the version of AutoHotkey in use.

    if VerCompare(A_AhkVersion, "2.0") < 0
        MsgBox "This version < 2.0; possibly a pre-release version."
    else
        MsgBox "This version is 2.0 or later."
:::

::: {#ExStr .ex}
[](#ExStr){.ex_number} Shows one difference between VerCompare and
StrCompare.

    MsgBox VerCompare("1.20.0", "1.3")  ; Returns 1
    MsgBox StrCompare("1.20.0", "1.3")  ; Returns -1
:::

::: {#ExPre .ex}
[](#ExPre){.ex_number} Demonstrates comparison with pre-release
versions.

    MsgBox VerCompare("2.0-a137", "2.0-a136")  ; Returns 1
    MsgBox VerCompare("2.0-a137", "2.0")  ; Returns -1
    MsgBox VerCompare("10.2-beta.3", "10.2.0")  ; Returns -1
:::

::: {#ExPreRange .ex}
[](#ExPreRange){.ex_number} Demonstrates a range check.

    MsgBox VerCompare("2.0.1", ">=2.0") && VerCompare("2.0.1", "<2.1")  ; Returns 1
:::
