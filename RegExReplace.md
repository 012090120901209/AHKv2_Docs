# RegExReplace

Replaces occurrences of a pattern (regular expression) inside a string.

``` Syntax
NewStr := RegExReplace(Haystack, NeedleRegEx , Replacement, &OutputVarCount, Limit, StartingPos)
```

## Parameters {#Parameters}

Haystack

:   Type: [String](../Concepts.htm#strings)

    The string whose content is searched and replaced. This may contain
    binary zero.

NeedleRegEx

:   Type: [String](../Concepts.htm#strings)

    The pattern to search for, which is a Perl-compatible regular
    expression (PCRE). The pattern\'s
    [options](../misc/RegEx-QuickRef.htm#Options) (if any) must be
    included at the beginning of the string followed by a
    close-parenthesis. For example, the pattern
    [[i)]{.red}abc.\*123]{.regex} would turn on the case-insensitive
    option and search for \"abc\", followed by zero or more occurrences
    of any character, followed by \"123\". If there are no options, the
    \")\" is optional; for example, [)abc]{.regex} is equivalent to
    [abc]{.regex}.

    Although *NeedleRegEx* cannot contain binary zero, the pattern
    `\x00` can be used to match a binary zero within *Haystack*.

Replacement

:   Type: [String](../Concepts.htm#strings)

    If blank or omitted, *NeedleRegEx* will be replaced with blank
    (empty), meaning it will be omitted from the return value.
    Otherwise, specify the string to be substituted for each match,
    which is plain text (not a regular expression).

    This parameter may include backreferences like \$1, which brings in
    the substring from *Haystack* that matched the first
    [subpattern](../misc/RegEx-QuickRef.htm#subpat). The simplest
    backreferences are \$0 through \$9, where \$0 is the substring that
    matched the entire pattern, \$1 is the substring that matched the
    first subpattern, \$2 is the second, and so on. For backreferences
    greater than 9 (and optionally those less than or equal to 9),
    enclose the number in braces; e.g. \${10}, \${11}, and so on. For
    [named subpatterns](RegExMatch.htm#NamedSubPat), enclose the name in
    braces; e.g. \${SubpatternName}. To specify a literal \$, use \$\$
    (this is the only character that needs such special treatment;
    backslashes are never needed to escape anything).

    To convert the case of a subpattern, follow the \$ with one of the
    following characters: U or u (uppercase), L or l (lowercase), T or t
    (title case, in which the first letter of each word is capitalized
    but all others are made lowercase). For example, both \$U1 and
    \$U{1} transcribe an uppercase version of the first subpattern.

    Nonexistent backreferences and those that did not match anything in
    *Haystack* \-- such as one of the subpatterns in
    [(abc)\|(xyz)]{.regex} \-- are transcribed as empty strings.

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

StartingPos

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted, it defaults to 1 (the beginning of *Haystack*).
    Otherwise, specify 2 to start at the second character, 3 to start at
    the third, and so on. If *StartingPos* is beyond the length of
    *Haystack*, the search starts at the empty string that lies at the
    end of *Haystack* (which typically results in no replacements).

    Specify a negative *StartingPos* to start at that position from the
    right. For example, -1 starts at the last character and -2 starts at
    the next-to-last character. If *StartingPos* tries to go beyond the
    left end of *Haystack*, all of *Haystack* is searched.

    Specify 0 to start at the end of *Haystack*; i.e. the position to
    the right of the last character. This can be used with zero-width
    assertions such as `(?<=a)`.

    Regardless of the value of *StartingPos*, the return value is always
    a complete copy of *Haystack* \-- the only difference is that more
    of its left side might be unaltered compared to what would have
    happened with a *StartingPos* of 1.

## Return Value {#Return_Value}

Type: [String](../Concepts.htm#strings)

This function returns a version of *Haystack* whose contents have been
replaced by the operation. If no replacements are needed, *Haystack* is
returned unaltered.

## Errors {#Errors}

An [Error](Error.htm) is thrown if:

-   the pattern contains a syntax error; or
-   an error occurred during the *execution* of the regular expression.

For details, see [RegExMatch](RegExMatch.htm#Errors).

## Options {#Options}

See [RegEx Quick Reference](../misc/RegEx-QuickRef.htm#Options) for
options such as [[i)]{.red}abc]{.regex}, which turns off
case-sensitivity.

## Performance {#Performance}

To replace simple substrings, use [StrReplace](StrReplace.htm) because
it is faster than RegExReplace.

If you know what the maximum number of replacements will be, specifying
that for the *Limit* parameter improves performance because the search
can be stopped early (this might also reduce the memory load on the
system during the operation). For example, if you know there can be only
one match near the beginning of a large string, specify a limit of 1.

To improve performance, the 100 most recently used regular expressions
are kept cached in memory (in compiled form).

The [study option (S)](../misc/RegEx-QuickRef.htm#Study) can sometimes
improve the performance of a regular expression that is used many times
(such as in a loop).

## Remarks {#Remarks}

Most characters like abc123 can be used literally inside a regular
expression. However, any of the characters in the set `\.*?+[{|()^$`
must be preceded by a backslash to be seen as literal. For example,
[\\.]{.regex} is a literal period and [\\\\]{.regex} is a literal
backslash. Escaping can be avoided by using \\Q\...\\E. For example:
[\\QLiteral Text\\E]{.regex}.

Within a regular expression, special characters such as tab and newline
can be escaped with either an accent (\`) or a backslash (\\). For
example, [\`t]{.regex} is the same as [\\t]{.regex} except when the [x
option](../misc/RegEx-QuickRef.htm#opt_x) is used.

To learn the basics of regular expressions (or refresh your memory of
pattern syntax), see the [RegEx Quick
Reference](../misc/RegEx-QuickRef.htm).

## Related {#Related}

[RegExMatch](RegExMatch.htm), [RegEx Quick
Reference](../misc/RegEx-QuickRef.htm), [Regular Expression
Callouts](../misc/RegExCallout.htm), [StrReplace](StrReplace.htm),
[InStr](InStr.htm)

Common sources of text data: [FileRead](FileRead.htm),
[Download](Download.htm), [A_Clipboard](A_Clipboard.htm), [GUI Edit
controls](GuiControls.htm#Edit)

## Examples {#Examples}

For general RegEx examples, see the [RegEx Quick
Reference](../misc/RegEx-QuickRef.htm).

::: {#ExDollar .ex}
[](#ExDollar){.ex_number} Reports \"abc123xyz\" because the \$ allows a
match only at the end.

    MsgBox RegExReplace("abc123123", "123$", "xyz")
:::

::: {#ExCaseInsens .ex}
[](#ExCaseInsens){.ex_number} Reports \"123\" because a match was
achieved via the case-insensitive option.

    MsgBox RegExReplace("abc123", "i)^ABC")
:::

::: {#ExBackref .ex}
[](#ExBackref){.ex_number} Reports \"aaaXYZzzz\" by means of the \$1
[backreference](#BackRef).

    MsgBox RegExReplace("abcXYZ123", "abc(.*)123", "aaa$1zzz")
:::

::: {#ExOutputVarCount .ex}
[](#ExOutputVarCount){.ex_number} Reports an empty string and stores 2
in `ReplacementCount`{.variable}.

    MsgBox RegExReplace("abc123abc456", "abc\d+", "", &ReplacementCount)
:::
