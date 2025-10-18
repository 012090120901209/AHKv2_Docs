# StrReplace

Replaces the specified substring with a new string.

``` Syntax
ReplacedStr := StrReplace(Haystack, Needle , ReplaceText, CaseSense, &OutputVarCount, Limit)
```

## Parameters {#Parameters}

Haystack

:   Type: [String](../Concepts.htm#strings)

    The string whose content is searched and replaced.

Needle

:   Type: [String](../Concepts.htm#strings)

    The string to search for.

ReplaceText

:   Type: [String](../Concepts.htm#strings)

    If blank or omitted, *Needle* will be replaced with blank (empty),
    meaning it will be omitted from the return value. Otherwise, specify
    the string to replace *Needle* with.

CaseSense

:   Type: [String](../Concepts.htm#strings) or [Integer
    (boolean)](../Concepts.htm#boolean)

    If omitted, it defaults to *Off*. Otherwise, specify one of the
    following values:

    **On** or **1** (true): The search is case-sensitive.

    **Off** or **0** (false): The search is not case-sensitive, i.e. the
    letters A-Z are considered identical to their lowercase
    counterparts.

    **Locale:** The search is not case-sensitive according to the rules
    of the current user\'s locale. For example, most English and Western
    European locales treat not only the letters A-Z as identical to
    their lowercase counterparts, but also non-ASCII letters like Ä and
    Ü as identical to theirs. *Locale* is 1 to 8 times slower than *Off*
    depending on the nature of the strings being compared.

&OutputVarCount

:   Type: [VarRef](../Concepts.htm#variable-references)

    If omitted, the corresponding value will not be stored. Otherwise,
    specify a reference to the output variable in which to store the
    number of replacements that occurred (0 if none).

Limit

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted, it defaults to -1, which replaces [all]{.underline}
    occurrences of the pattern found in *Haystack*. Otherwise, specify
    the maximum number of replacements to allow. The part of *Haystack*
    to the right of the last replacement is left unchanged.

## Return Value {#Return_Value}

Type: [String](../Concepts.htm#strings)

This function returns the replaced version of the specified string.

## Remarks {#Remarks}

The built-in variables **A_Space** and **A_Tab** contain a single space
and a single tab character, respectively. They are useful when searching
for spaces and tabs alone or at the beginning or end of *Needle*.

## Related {#Related}

[RegExReplace](RegExReplace.htm), [InStr](InStr.htm),
[SubStr](SubStr.htm), [StrLen](StrLen.htm), [StrLower](StrLower.htm),
[StrUpper](StrLower.htm)

## Examples {#Examples}

::: {#ExClipboard .ex}
[](#ExClipboard){.ex_number} Removes all CR-LF pairs from the clipboard
contents.

    A_Clipboard := StrReplace(A_Clipboard, "`r`n")
:::

::: {#ExVar .ex}
[](#ExVar){.ex_number} Replaces all spaces with pluses.

    NewStr := StrReplace(OldStr, A_Space, "+")
:::

::: {#ExRemoveBlankLines .ex}
[](#ExRemoveBlankLines){.ex_number} Removes all blank lines from the
text in a variable.

    Loop
    {
        MyString := StrReplace(MyString, "`r`n`r`n", "`r`n",, &Count)
        if (Count = 0)  ; No more replacements needed.
            break
    }
:::
