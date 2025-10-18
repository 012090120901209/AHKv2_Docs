# StrLower / StrUpper / StrTitle

Converts a string to lowercase, uppercase or title case.

``` Syntax
NewString := StrLower(String)
NewString := StrUpper(String)
NewString := StrTitle(String)
```

## Parameters {#Parameters}

String

:   Type: [String](../Concepts.htm#strings)

    The string to convert.

## Return Value {#Return_Value}

Type: [String](../Concepts.htm#strings)

These functions return the newly converted version of the specified
string.

## Remarks {#Remarks}

To detect whether a character or string is entirely uppercase or
lowercase, use the [IsUpper](Is.htm#upper), [IsLower](Is.htm#lower) or
[RegExMatch](RegExMatch.htm) function. For example:

    var := "abc"
    if isUpper(var)
        MsgBox "var is empty or contains only uppercase characters."
    if isLower(var)
        MsgBox "var is empty or contains only lowercase characters."
    if RegExMatch(var, "^[a-z]+$")
        MsgBox "var is not empty and contains only lowercase ASCII characters."
    if !RegExMatch(var, "[A-Z]")
        MsgBox "var does not contain any uppercase ASCII characters."

[Format](Format.htm) can also be used for case conversions, as shown
below:

    MsgBox Format("{:U}, {:L} and {:T}", "upper", "LOWER", "title")

## Related {#Related}

[InStr](InStr.htm), [SubStr](SubStr.htm), [StrLen](StrLen.htm),
[StrReplace](StrReplace.htm)

## Examples {#Examples}

::: {#ExLower .ex}
[](#ExLower){.ex_number} Converts the string to lowercase and stores
\"this is a test.\" in `String1`{.variable}.

    String1 := "This is a test."
    String1 := StrLower(String1)  ; i.e. output can be the same as input.
:::

::: {#ExUpper .ex}
[](#ExUpper){.ex_number} Converts the string to uppercase and stores
\"THIS IS A TEST.\" in `String2`{.variable}.

    String2 := "This is a test."
    String2 := StrUpper(String2)
:::

::: {#ExTitle .ex}
[](#ExTitle){.ex_number} Converts the string to title case and stores
\"This Is A Test.\" in `String3`{.variable}.

    String3 := "This is a test."
    String3 := StrTitle(String3)
:::
