# Switch

Compares a value with multiple cases and executes the
[statements](../Concepts.htm#statement) of the first match.

``` Syntax
Switch SwitchValue, CaseSense
{
Case CaseValue1:
    Statements1
Case CaseValue2a, CaseValue2b:
    Statements2
Default:
    Statements3
}
```

## Parameters {#Parameters}

SwitchValue

:   If this and *CaseSense* are omitted, the first case which evaluates
    to [true](../Concepts.htm#boolean) (non-zero and non-empty) is
    executed. Otherwise, *SwitchValue* is evaluated once and compared to
    each case value until a match is found, and then that case is
    executed.

    If there is no matching case and *Default* is present, it is
    executed.

CaseSense

:   Type: [String](../Concepts.htm#strings) or [Integer
    (boolean)](../Concepts.htm#boolean)

    If omitted, it defaults to *On*. Otherwise, specify one of the
    following values, which forces all values to be compared as strings:

    **On** or **1** (true): Each comparison is case-sensitive.

    **Off** or **0** (false): Each comparison is not case-sensitive,
    i.e. the letters A-Z are considered identical to their lowercase
    counterparts.

    **Locale:** Each comparison is not case-sensitive according to the
    rules of the current user\'s locale. For example, most English and
    Western European locales treat not only the letters A-Z as identical
    to their lowercase counterparts, but also non-ASCII letters like Ä
    and Ü as identical to theirs. *Locale* is 1 to 8 times slower than
    *Off* depending on the nature of the strings being compared.

CaseValueN

:   The value to check or compare depending on whether *SwitchValue* is
    present.

## Remarks {#Remarks}

As with the `=` and `==` operators, when *CaseSense* is omitted, numeric
comparison is performed if *SwitchValue* and the case value are both
pure numbers, or if one is a pure number and the other is a numeric
string. Each case value is considered separately and does not affect the
type of comparison used for other case values.

If the *CaseSense* parameter is present, all values are compared as
strings, not as numbers, and a [TypeError](Error.htm#TypeError) is
thrown if *SwitchValue* or a *CaseValue* evaluates to an object.

If the *CaseSense* parameter is omitted, string comparisons are
case-sensitive by default.

Each case may list up to 20 values. Each value must be an
[expression](../Language.htm#expressions), but can be a simple one such
as a literal number, quoted string or variable. *Case* and *Default*
must be terminated with a colon.

The first statement of each case may be below *Case* or on the same
line, following the colon. Each case implicitly ends at the next
*Case*/*Default* or the closing brace. Unlike the switch statement found
in some other languages, there is no implicit fall-through and
[Break](Break.htm) is not used (except to break out of an enclosing
loop).

As all cases are enclosed in the same block, a label defined in one case
can be the target of [Goto](Goto.htm) from another case. However, if a
label is placed immediately above *Case* or *Default*, it targets the
end of the previous case, not the beginning of the next one.

*Default* is not required to be listed last.

## Related {#Related}

[If](If.htm), [Else](Else.htm), [Blocks](Block.htm)

## Examples

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Compares a number with multiple cases and shows
the message box of the first match.

    switch 2
    {
    case 1: MsgBox "no match"
    case 2: MsgBox "match"
    case 3: MsgBox "no match"
    }
:::

::: {#ExBasicOmitted .ex}
[](#ExBasicOmitted){.ex_number} The *SwitchValue* parameter can be
omitted to execute the first case which evaluates to true.

    str := "The quick brown fox jumps over the lazy dog"
    switch
    {
    case InStr(str, "blue"): MsgBox "false"
    case InStr(str, "brown"): MsgBox "true"
    case InStr(str, "green"): MsgBox "false"
    }
:::

::: {#ExInput .ex}
[](#ExInput){.ex_number} To test this example, type [\[]{.kbd} followed
by one of the abbreviations listed below, any other 5 characters, or
Enter/Esc/Tab/[.]{.kbd}; or wait for 4 seconds.

    ~[::
    {
        ih := InputHook("V T5 L4 C", "{enter}.{esc}{tab}", "btw,otoh,fl,ahk,ca")
        ih.Start()
        ih.Wait()
        switch ih.EndReason
        {
        case "Max":
            MsgBox 'You entered "' ih.Input '", which is the maximum length of text'
        case "Timeout":
            MsgBox 'You entered "' ih.Input '" at which time the input timed out'
        case "EndKey":
            MsgBox 'You entered "' ih.Input '" and terminated it with ' ih.EndKey
        default:  ; Match
            switch ih.Input
            {
            case "btw":   Send "{backspace 3}by the way"
            case "otoh":  Send "{backspace 4}on the other hand"
            case "fl":    Send "{backspace 2}Florida"
            case "ca":    Send "{backspace 2}California"
            case "ahk":
                Send "{backspace 3}"
                Run "https://www.autohotkey.com"
            }
        }
    }
:::
