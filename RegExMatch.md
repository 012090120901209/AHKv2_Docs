# RegExMatch

Determines whether a string contains a pattern (regular expression).

``` Syntax
FoundPos := RegExMatch(Haystack, NeedleRegEx , &OutputVar, StartingPos)
```

## Parameters {#Parameters}

Haystack

:   Type: [String](../Concepts.htm#strings)

    The string whose content is searched. This may contain binary zero.

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

&OutputVar

:   Type: [VarRef](../Concepts.htm#variable-references)

    If omitted, no output variable will be used. Otherwise, specify a
    reference to the output variable in which to store a [match
    object](#MatchObject), which can be used to retrieve the position,
    length and value of the overall match and of each [captured
    subpattern](../misc/RegEx-QuickRef.htm#subpat), if any are present.

    If the pattern is not found (that is, if the function returns 0),
    this variable is made blank.

StartingPos

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted, it defaults to 1 (the beginning of *Haystack*).
    Otherwise, specify 2 to start at the second character, 3 to start at
    the third, and so on. If *StartingPos* is beyond the length of
    *Haystack*, the search starts at the empty string that lies at the
    end of *Haystack* (which typically results in no match).

    Specify a negative *StartingPos* to start at that position from the
    right. For example, -1 starts at the last character and -2 starts at
    the next-to-last character. If *StartingPos* tries to go beyond the
    left end of *Haystack*, all of *Haystack* is searched.

    Specify 0 to start at the end of *Haystack*; i.e. the position to
    the right of the last character. This can be used with zero-width
    assertions such as `(?<=a)`.

    Regardless of the value of *StartingPos*, the return value is always
    relative to the first character of *Haystack*. For example, the
    position of \"abc\" in \"123abc789\" is always 4.

## Return Value {#Return_Value}

Type: [Integer](../Concepts.htm#numbers)

This function returns the position of the leftmost occurrence of
*NeedleRegEx* in the string *Haystack*. Position 1 is the first
character. Zero is returned if the pattern is not found.

## Errors {#Errors}

**Syntax errors:** If the pattern contains a syntax error, an
[Error](Error.htm) is thrown with a message in the following form:
*Compile error N at offset M: description*. In that string, *N* is the
PCRE error number, *M* is the position of the offending character inside
the regular expression, and *description* is the text describing the
error.

**Execution errors:** If an error occurs during the *execution* of the
regular expression, an [Error](Error.htm) is thrown. The *Extra*
property of the error object contains the PCRE error number. Although
such errors are rare, the ones most likely to occur are \"too many
possible empty-string matches\" (-22), \"recursion too deep\" (-21), and
\"reached match limit\" (-8). If these happen, try to redesign the
pattern to be more restrictive, such as replacing each \* with a ?, +,
or a limit like {0,3} wherever feasible.

## Options {#Options}

See [RegEx Quick Reference](../misc/RegEx-QuickRef.htm#Options) for
options such as [[i)]{.red}abc]{.regex}, which turns off
case-sensitivity.

## Match Object (RegExMatchInfo) {#MatchObject}

If a match is found, an object containing information about the match is
stored in *OutputVar*. This object has the following methods and
properties:

**Match.Pos**, **Match.Pos\[N\]** or **Match.Pos(N)**: Returns the
position of the overall match or a captured subpattern.

**Match.Len**, **Match.Len\[N\]** or **Match.Len(N)**: Returns the
length of the overall match or a captured subpattern.

**Match.Name\[N\]** or **Match.Name(N)**: Returns the name of the given
subpattern, if it has one.

**Match.Count:** Returns the overall number of subpatterns (capturing
groups), which is also the maximum value for *N*.

**Match.Mark:** Returns the *NAME* of the last encountered
[(\*MARK:NAME)]{.regex}, when applicable.

**Match\[\]** or **Match\[N\]**: Returns the overall match or a captured
subpattern.

All of the above allow *N* to be any of the following:

-   0 for the overall match.
-   The number of a subpattern, even one that also has a name.
-   The name of a subpattern.

**Match.N:** Shorthand for **Match\[\"N\"\]**, where *N* is any unquoted
name or number which does not conflict with a defined property (listed
above). For example, `match.1` or `match.Year`.

The object also supports enumeration; that is, the [for-loop](For.htm)
is supported. Alternatively, use [`Loop`](Loop.htm)` Match.Count`.

## Performance {#Performance}

To search for a simple substring inside a larger string, use
[InStr](InStr.htm) because it is faster than RegExMatch.

To improve performance, the 100 most recently used regular expressions
are kept cached in memory (in compiled form).

The [study option (S)](../misc/RegEx-QuickRef.htm#Study) can sometimes
improve the performance of a regular expression that is used many times
(such as in a loop).

## Remarks {#Remarks}

A subpattern may be given a name such as the word *Year* in the pattern
[(?P\<Year\>\\d{4})]{.regex}. Such names may consist of up to 32
alphanumeric characters and underscores. Note that named subpatterns are
also numbered, so if an [unnamed
subpattern](../misc/RegEx-QuickRef.htm#subpat) occurs after \"Year\", it
would be stored in `OutputVar[2]`, not `OutputVar[1]`.

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

AutoHotkey\'s regular expressions are implemented using Perl-compatible
Regular Expressions (PCRE) from [www.pcre.org](http://www.pcre.org/).

Within an [expression](../Variables.htm#Expressions), `a ~= b` can be
used as shorthand for `RegExMatch(a, b)`.

## Related {#Related}

[RegExReplace](RegExReplace.htm), [RegEx Quick
Reference](../misc/RegEx-QuickRef.htm), [Regular Expression
Callouts](../misc/RegExCallout.htm), [InStr](InStr.htm),
[SubStr](SubStr.htm), [SetTitleMatchMode
RegEx](SetTitleMatchMode.htm#RegEx), [Global matching and Grep (archived
forum link)](https://www.autohotkey.com/board/topic/14817-)

Common sources of text data: [FileRead](FileRead.htm),
[Download](Download.htm), [A_Clipboard](A_Clipboard.htm), [GUI Edit
controls](GuiControls.htm#Edit)

## Examples {#Examples}

For general RegEx examples, see the [RegEx Quick
Reference](../misc/RegEx-QuickRef.htm).

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Reports 4, which is the position where the
match was found.

    MsgBox RegExMatch("xxxabc123xyz", "abc.*xyz")
:::

::: {#ExDollar .ex}
[](#ExDollar){.ex_number} Reports 7 because the \$ requires the match to
be at the end.

    MsgBox RegExMatch("abc123123", "123$")
:::

::: {#ExCaseInsens .ex}
[](#ExCaseInsens){.ex_number} Reports 1 because a match was achieved via
the case-insensitive option.

    MsgBox RegExMatch("abc123", "i)^ABC")
:::

::: {#ExOutputVar .ex}
[](#ExOutputVar){.ex_number} Reports 1 and stores \"XYZ\" in
SubPat\[1\].

    MsgBox RegExMatch("abcXYZ123", "abc(.*)123", &SubPat)
:::

::: {#ExStartingPos .ex}
[](#ExStartingPos){.ex_number} Reports 7 instead of 1 due to the
starting position 2 instead of 1.

    MsgBox RegExMatch("abc123abc456", "abc\d+",, 2)
:::

::: {#ExObject .ex}
[](#ExObject){.ex_number} Demonstrates the usage of the Match object.

    FoundPos := RegExMatch("Michiganroad 72", "(.*) (?<nr>\d+)", &SubPat)
    MsgBox SubPat.Count ": " SubPat[1] " " SubPat.Name[2] "=" SubPat.nr  ; Displays "2: Michiganroad nr=72"
:::

::: {#ExExtension .ex}
[](#ExExtension){.ex_number} Retrieves the extension of a file. Note
that [SplitPath](SplitPath.htm) can also be used for this, which is more
reliable.

    Path := "C:\Foo\Bar\Baz.txt"
    RegExMatch(Path, "\w+$", &Extension)
    MsgBox Extension[]  ; Reports "txt".
:::

::: {#ExDeref .ex}
[](#ExDeref){.ex_number} Similar to AutoHotkey v1\'s Transform Deref,
the following function expands variable references and [escape
sequences](../misc/EscapeChar.htm) contained inside other variables.
Furthermore, this example shows how to find all matches in a string
rather than stopping at the first match (similar to the g flag in
JavaScript\'s RegEx).

    var1 := "abc"
    var2 := 123
    MsgBox Deref("%var1%def%var2%")  ; Reports abcdef123.

    Deref(Str)
    {
        spo := 1
        out := ""
        while (fpo:=RegexMatch(Str, "(%(.*?)%)|``(.)", &m, spo))
        {
            out .= SubStr(Str, spo, fpo-spo)
            spo := fpo + StrLen(m[0])
            if (m[1])
                out .= %m[2]%
            else switch (m[3])
            {
                case "a": out .= "`a"
                case "b": out .= "`b"
                case "f": out .= "`f"
                case "n": out .= "`n"
                case "r": out .= "`r"
                case "t": out .= "`t"
                case "v": out .= "`v"
                default: out .= m[3]
            }
        }
        return out SubStr(Str, spo)
    }
:::
