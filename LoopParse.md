# Loop Parse

Retrieves substrings (fields) from a string, one at a time.

``` Syntax
Loop Parse String , DelimiterChars, OmitChars
```

## Parameters {#Parameters}

String

:   Type: [String](../Concepts.htm#strings)

    The string to analyze.

DelimiterChars

:   Type: [String](../Concepts.htm#strings)

    If blank or omitted, each character of the input string will be
    treated as a separate substring.

    If this parameter is `"CSV"`, the string will be parsed in standard
    comma separated value format. Here is an example of a CSV line
    produced by MS Excel:

    ``` no-highlight
    "first field",SecondField,"the word ""special"" is quoted literally",,"last field, has literal comma"
    ```

    Otherwise, specify one or more characters (case-sensitive), each of
    which is used to determine where the boundaries between substrings
    occur.

    Delimiter characters are not considered to be part of the substrings
    themselves. In addition, if there is nothing between a pair of
    delimiter characters within the input string, the corresponding
    substring will be empty.

    For example: `','` (a comma) would divide the string based on every
    occurrence of a comma. Similarly, `A_Space A_Tab` would start a new
    substring every time a space or tab is encountered in the input
    string.

    To use a string as a delimiter rather than a character, first use
    [StrReplace](StrReplace.htm) to replace all occurrences of the
    string with a single character that is never used literally in the
    text, e.g. one of these special characters: `¢¤¥¦§©ª«®µ¶`. Consider
    this example, which uses the string \<br\> as a delimiter:

        NewHTML := StrReplace(HTMLString, "<br>", "¢")
        Loop Parse, NewHTML, "¢" ; Parse the string based on the cent symbol.
        {
            ; ...
        }

OmitChars

:   Type: [String](../Concepts.htm#strings)

    If blank or omitted, no characters will be excluded. Otherwise,
    specify a list of characters (case-sensitive) to exclude from the
    beginning and end of each substring. For example, if *OmitChars* is
    `A_Space A_Tab`, spaces and tabs will be removed from the beginning
    and end (but not the middle) of every retrieved substring.

    If *DelimiterChars* is blank, *OmitChars* indicates which characters
    should be excluded from consideration (the loop will not see them).

## Remarks {#Remarks}

A string parsing loop is useful when you want to operate on each field
contained in a string, one at a time. Parsing loops use less memory than
[StrSplit](StrSplit.htm) (though either way the memory use is temporary)
and in most cases they are easier to use.

The built-in variable **A_LoopField** exists within any parsing loop. It
contains the contents of the current substring (field). If an inner
parsing loop is enclosed by an outer parsing loop, the innermost loop\'s
field will take precedence.

Although there is no built-in variable \"A_LoopDelimiter\", the example
at the very bottom of this page demonstrates how to detect which
delimiter character was encountered for each field.

There is no restriction on the size of the input string or its fields.

To arrange the fields in a different order prior to parsing, use the
[Sort](Sort.htm) function.

See [Loop](Loop.htm) for information about [Blocks](Block.htm),
[Break](Break.htm), [Continue](Continue.htm), and the A_Index variable
(which exists in every type of loop).

The loop may optionally be followed by an [Else](Else.htm) statement,
which is executed if the loop had zero iterations. Note that the loop
always has at least one iteration unless *String* is empty or
*DelimiterChars* is omitted and all characters in *String* are included
in *OmitChars*.

## Related {#Related}

[StrSplit](StrSplit.htm), [file-reading loop](LoopRead.htm),
[Loop](Loop.htm), [Break](Break.htm), [Continue](Continue.htm),
[Blocks](Block.htm), [Sort](Sort.htm),
[FileSetAttrib](FileSetAttrib.htm), [FileSetTime](FileSetTime.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Parses a comma-separated string.

    Colors := "red,green,blue"
    Loop parse, Colors, ","
    {
        MsgBox "Color number " A_Index " is " A_LoopField
    }
:::

::: {#ExFileRead .ex}
[](#ExFileRead){.ex_number} Reads the lines inside a variable, one by
one (similar to a [file-reading loop](LoopRead.htm)). A file can be
loaded into a variable via [FileRead](FileRead.htm).

    Loop parse, FileContents, "`n", "`r"  ; Specifying `n prior to `r allows both Windows and Unix files to be parsed.
    {
        Result := MsgBox("Line number " A_Index " is " A_LoopField ".`n`nContinue?",, "y/n")
    }
    until Result = "No"
:::

::: {#ExClipboard .ex}
[](#ExClipboard){.ex_number} This is the same as the example above
except that it\'s for the [clipboard](A_Clipboard.htm). It\'s useful
whenever the clipboard contains files, such as those copied from an open
Explorer window (the program automatically converts such files to their
file names).

    Loop parse, A_Clipboard, "`n", "`r"
    {
        Result := MsgBox("File number " A_Index " is " A_LoopField ".`n`nContinue?",, "y/n")
    }
    until Result = "No"
:::

::: {#ExCSV .ex}
[](#ExCSV){.ex_number} Parses a comma separated value (CSV) file.

    Loop read, "C:\Database Export.csv"
    {
        LineNumber := A_Index
        Loop parse, A_LoopReadLine, "CSV"
        {
            Result := MsgBox("Field " LineNumber "-" A_Index " is:`n" A_LoopField "`n`nContinue?",, "y/n")
            if Result = "No"
                return
        }
    }
:::

::: {#ExDelimiter .ex}
[](#ExDelimiter){.ex_number} Determines which delimiter character was
encountered.

    ; Initialize string to search.
    Colors := "red,green|blue;yellow|cyan,magenta"
    ; Initialize counter to keep track of our position in the string.
    Position := 0

    Loop Parse, Colors, ",|;"
    {
        ; Calculate the position of the delimiter character at the end of this field.
        Position += StrLen(A_LoopField) + 1
        ; Retrieve the delimiter character found by the parsing loop.
        DelimiterChar := SubStr(Colors, Position, 1)

        MsgBox "Field: " A_LoopField "`nDelimiter character: " DelimiterChar
    }
:::
