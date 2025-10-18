# Is Functions

Functions for checking the type and other conditions of a given value.

``` Syntax
Result := IsSomething(Value , Mode)
```

There are three categories:

-   [Type](#cat-type): Check the type of a value, or whether a string
    can be interpreted as a value of that type.
-   [Misc](#cat-misc): Check miscellaneous conditions based on a given
    value or variable reference.
-   [String](#cat-string): Check whether a string matches a specific
    pattern.

*Mode* is valid only for IsAlpha, IsAlnum, IsUpper and IsLower. By
default, only ASCII letters are considered. To instead perform the check
according to the rules of the current user\'s locale, specify the string
`"Locale"` for the *Mode* parameter. The default mode can also be used
by specifying 0 or 1.

## Type {#cat-type}

Check the type of a value, or whether a string can be interpreted as a
value of that type.

  Function                   Description
  -------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  IsInteger                  True if *Value* is an integer or a purely numeric string (decimal or hexadecimal) without a decimal point. Leading and trailing spaces and tabs are allowed. The string may start with a plus or minus sign and must not be empty.
  IsFloat                    True if *Value* is a floating point number or a purely numeric string containing a decimal point. Leading and trailing spaces and tabs are allowed. The string may start with a plus sign, minus sign, or decimal point and must not be empty.
  IsNumber                   True if `IsInteger(`*`Value`*`) or IsFloat(`*`Value`*`)` is true.
  [IsObject](IsObject.htm)   True if *Value* is an [object](../Objects.htm). This includes objects derived from [Object](Object.htm), prototype objects such as `0.base`, and COM objects, but not numbers or strings.

## Misc {#cat-misc}

Check miscellaneous conditions based on a given value or variable
reference.

  Function                 Description
  ------------------------ -----------------------------------------------------------------------------------------------------------
  [IsLabel](IsLabel.htm)   True if *Value* is the name of a [label](../misc/Labels.htm) defined within the current scope.
  [IsSet](IsSet.htm)       True if the variable *Value* has been assigned a value.
  [IsSetRef](IsSet.htm)    True if the [VarRef](../Concepts.htm#variable-references) contained by *Value* has been assigned a value.

## String {#cat-string}

Check whether a string matches a specific pattern. *Value* must be a
string, otherwise a [TypeError](Error.htm#TypeError) is thrown.

+-----------------------------------+-----------------------------------+
| Function                          | Description                       |
+===================================+===================================+
| IsDigit                           | True if *Value* is a positive     |
|                                   | integer, an empty string, or a    |
|                                   | string which contains only the    |
|                                   | characters 0 through 9. Other     |
|                                   | characters such as the following  |
|                                   | are not allowed: spaces, tabs,    |
|                                   | plus signs, minus signs, decimal  |
|                                   | points, hexadecimal digits, and   |
|                                   | the 0x prefix.                    |
+-----------------------------------+-----------------------------------+
| IsXDigit                          | Hexadecimal digit: Same as        |
|                                   | [IsDigit](#digit) except the      |
|                                   | characters A through F (uppercase |
|                                   | or lowercase) are also allowed. A |
|                                   | prefix of 0x is tolerated if      |
|                                   | present.                          |
+-----------------------------------+-----------------------------------+
| IsAlpha                           | True if *Value* is a string and   |
|                                   | is empty or contains only         |
|                                   | alphabetic characters. False if   |
|                                   | there are any digits, spaces,     |
|                                   | tabs, punctuation, or other       |
|                                   | non-alphabetic characters         |
|                                   | anywhere in the string. For       |
|                                   | example, if *Value* contains a    |
|                                   | space followed by a letter, it is |
|                                   | *not* considered to be *alpha*.   |
|                                   |                                   |
|                                   | By default, only ASCII letters    |
|                                   | are considered. To instead        |
|                                   | perform the check according to    |
|                                   | the rules of the current user\'s  |
|                                   | locale, use                       |
|                                   | `IsAlpha(Value, "Locale")`.       |
+-----------------------------------+-----------------------------------+
| IsUpper                           | True if *Value* is a string and   |
|                                   | is empty or contains only         |
|                                   | uppercase characters. False if    |
|                                   | there are any digits, spaces,     |
|                                   | tabs, punctuation, or other       |
|                                   | non-uppercase characters anywhere |
|                                   | in the string.                    |
|                                   |                                   |
|                                   | By default, only ASCII letters    |
|                                   | are considered. To instead        |
|                                   | perform the check according to    |
|                                   | the rules of the current user\'s  |
|                                   | locale, use                       |
|                                   | `IsUpper(Value, "Locale")`.       |
+-----------------------------------+-----------------------------------+
| IsLower                           | True if *Value* is a string and   |
|                                   | is empty or contains only         |
|                                   | lowercase characters. False if    |
|                                   | there are any digits, spaces,     |
|                                   | tabs, punctuation, or other       |
|                                   | non-lowercase characters anywhere |
|                                   | in the string.                    |
|                                   |                                   |
|                                   | By default, only ASCII letters    |
|                                   | are considered. To instead        |
|                                   | perform the check according to    |
|                                   | the rules of the current user\'s  |
|                                   | locale, use                       |
|                                   | `IsLower(Value, "Locale")`.       |
+-----------------------------------+-----------------------------------+
| IsAlnum                           | Same as [IsAlpha](#alpha) except  |
|                                   | that integers and characters 0    |
|                                   | through 9 are also allowed.       |
+-----------------------------------+-----------------------------------+
| IsSpace                           | True if *Value* is a string and   |
|                                   | is empty or contains only         |
|                                   | whitespace consisting of the      |
|                                   | following characters: space       |
|                                   | ([A_Space](../Variables.htm) or   |
|                                   | \`s), tab                         |
|                                   | ([A_Tab](../Variables.htm) or     |
|                                   | \`t), linefeed (\`n), return      |
|                                   | (\`r), vertical tab (\`v), and    |
|                                   | formfeed (\`f).                   |
+-----------------------------------+-----------------------------------+
| IsTime                            | True if *Value* is a valid        |
|                                   | date-time stamp, which can be all |
|                                   | or just the leading part of the   |
|                                   | [YYYYMMDDHH                       |
|                                   | 24MISS](FileSetTime.htm#YYYYMMDD) |
|                                   | format. For example, a 4-digit    |
|                                   | string such as 2004 is considered |
|                                   | valid. Use [StrLen](StrLen.htm)   |
|                                   | to determine whether additional   |
|                                   | time components are present.      |
|                                   |                                   |
|                                   | *Value* must have an even number  |
|                                   | of digits between 4 and 14        |
|                                   | (inclusive) to be considered      |
|                                   | valid.                            |
|                                   |                                   |
|                                   | Years less than 1601 are not      |
|                                   | considered valid because the      |
|                                   | operating system generally does   |
|                                   | not support them. The maximum     |
|                                   | year considered valid is 9999.    |
+-----------------------------------+-----------------------------------+

## Remarks {#Remarks}

Since literal numbers such as `128`, `0x7F` and `1.0` are converted to
pure numbers before the script begins executing, the format of the
literal number is lost. To avoid confusion, the string functions listed
above throw an exception if they are given a pure number.

## Related {#Related}

[A_YYYY](../Variables.htm#YYYY), [FileGetTime](FileGetTime.htm),
[If](If.htm), [StrLen](StrLen.htm), [InStr](InStr.htm),
[StrUpper](StrLower.htm), [DateAdd](DateAdd.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Checks whether `var`{.variable} is a floating
point number or an integer and checks whether it is a valid timestamp.

    if isFloat(var)
        MsgBox var " is a floating point number."
    else if isInteger(var)
        MsgBox var " is an integer."
    if isTime(var)
        MsgBox var " is also a valid date-time."
:::
