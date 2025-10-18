# StrLen

Retrieves the count of how many characters are in a string.

``` Syntax
Length := StrLen(String)
```

## Parameters {#Parameters}

String

:   Type: [String](../Concepts.htm#strings)

    The string whose contents will be measured.

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers)

This function returns the length of the specified string.

## Related {#Related}

[InStr](InStr.htm), [SubStr](SubStr.htm), [Trim](Trim.htm),
[StrLower](StrLower.htm), [StrUpper](StrLower.htm),
[StrPut](StrPut.htm), [StrGet](StrGet.htm),
[StrReplace](StrReplace.htm), [StrSplit](StrSplit.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Retrieves and reports the count of how many
characters are in a string.

    StrValue := "The quick brown fox jumps over the lazy dog"
    MsgBox "The length of the string is " StrLen(StrValue) ; Result: 43
:::
