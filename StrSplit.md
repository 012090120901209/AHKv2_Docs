# StrSplit

Separates a string into an array of substrings using the specified
delimiters.

``` Syntax
Array := StrSplit(String , Delimiters, OmitChars, MaxParts)
```

## Parameters {#Parameters}

String

:   Type: [String](../Concepts.htm#strings)

    A string to split.

Delimiters

:   Type: [String](../Concepts.htm#strings) or [Array](Array.htm)

    If blank or omitted, each character of the input string will be
    treated as a separate substring.

    Otherwise, specify either a single string or an array of strings
    (case-sensitive), each of which is used to determine where the
    boundaries between substrings occur. Since the delimiters are not
    considered to be part of the substrings themselves, they are never
    included in the returned array. Also, if there is nothing between a
    pair of delimiters within the input string, the corresponding array
    element will be blank.

    For example: `","` would divide the string based on every occurrence
    of a comma. Similarly, `[A_Space, A_Tab]` would create a new array
    element every time a space or tab is encountered in the input
    string.

OmitChars

:   Type: [String](../Concepts.htm#strings)

    If blank or omitted, no characters will be excluded. Otherwise,
    specify a list of characters (case-sensitive) to exclude from the
    beginning and end of each array element. For example, if *OmitChars*
    is `` " `t" ``, spaces and tabs will be removed from the beginning
    and end (but not the middle) of every element.

    If *Delimiters* is blank, *OmitChars* indicates which characters
    should be excluded from the array.

MaxParts

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted, it defaults to -1, which means \"no limit\". Otherwise,
    specify the maximum number of substrings to return. If non-zero, the
    string is split a maximum of *MaxParts*-1 times and the remainder of
    the string is returned in the last substring (excluding any leading
    or trailing *OmitChars*).

## Return Value {#Return_Value}

Type: [Array](Array.htm)

This function returns an array containing the substrings of the
specified string.

## Remarks {#Remarks}

Whitespace characters such as spaces and tabs will be preserved unless
those characters are included in the *Delimiters* or *OmitChars*
parameters. Spaces and tabs can be trimmed from both ends of any
variable by using [Trim](Trim.htm). For example: `Var := Trim(Var)`

To split a string that is in standard CSV (comma separated value)
format, use a [parsing loop](LoopParse.htm) since it has built-in CSV
handling.

To arrange the fields in a different order prior to splitting them, use
the [Sort](Sort.htm) function.

If you do not need the substrings to be permanently stored in memory,
consider using a [parsing loop](LoopParse.htm) \-- especially if
*String* is very large, in which case a large amount of memory would be
saved. For example:

    Colors := "red,green,blue"
    Loop Parse, Colors, ","
        MsgBox "Color number " A_Index " is " A_LoopField

## Related {#Related}

[Parsing loop](LoopParse.htm), [Sort](Sort.htm),
[SplitPath](SplitPath.htm), [InStr](InStr.htm), [SubStr](SubStr.htm),
[StrLen](StrLen.htm), [StrLower](StrLower.htm),
[StrUpper](StrLower.htm), [StrReplace](StrReplace.htm)

## Examples {#Examples}

::: {#ExSpace .ex}
[](#ExSpace){.ex_number} Separates a sentence into an array of words and
reports the fourth word.

    TestString := "This is a test."
    word_array := StrSplit(TestString, A_Space, ".")  ; Omits periods.
    MsgBox "The 4th word is " word_array[4]
:::

::: {#ExComma .ex}
[](#ExComma){.ex_number} Separates a comma-separated list of colors into
an array of substrings and traverses them, one by one.

    colors := "red,green,blue"
    For index, color in StrSplit(colors, ",")
        MsgBox "Color number " index " is " color
:::
