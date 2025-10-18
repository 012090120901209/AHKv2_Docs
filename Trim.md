# Trim / LTrim / RTrim

Trims characters from the beginning and/or end of a string.

``` Syntax
NewString :=  Trim(String , OmitChars)
NewString := LTrim(String , OmitChars)
NewString := RTrim(String , OmitChars)
```

## Parameters {#Parameters}

String

:   Type: [String](../Concepts.htm#strings)

    Any string value or variable. Numbers are not supported.

OmitChars

:   Type: [String](../Concepts.htm#strings)

    If omitted, spaces and tabs will be removed. Otherwise, specify a
    list of characters (case-sensitive) to exclude from the beginning
    and/or end of *String*.

## Return Value {#Return_Value}

Type: [String](../Concepts.htm#strings)

These functions return the trimmed version of the specified string.

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Trims all spaces from the left and right side
of a string.

    text := "  text  "
    MsgBox
    (
        "No trim:`t'" text "'
        Trim:`t'" Trim(text) "'
        LTrim:`t'" LTrim(text) "'
        RTrim:`t'" RTrim(text) "'"
    )
:::

::: {#ExTrimZeros .ex}
[](#ExTrimZeros){.ex_number} Trims all zeros from the left side of a
string.

    MsgBox LTrim("00000123", "0")
:::
