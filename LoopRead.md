# Loop Read

Retrieves the lines in a text file, one at a time.

``` Syntax
Loop Read InputFile , OutputFile
```

## Parameters {#Parameters}

InputFile

:   Type: [String](../Concepts.htm#strings)

    The name of the text file whose contents will be read by the loop,
    which is assumed to be in
    [A_WorkingDir](../Variables.htm#WorkingDir) if an absolute path
    isn\'t specified. The file\'s lines may end in carriage return and
    linefeed (\`r\`n), just linefeed (\`n), or just carriage return
    (\`r).

OutputFile

:   Type: [String](../Concepts.htm#strings)

    (Optional) The name of the file to be kept open for the duration of
    the loop, which is assumed to be in
    [A_WorkingDir](../Variables.htm#WorkingDir) if an absolute path
    isn\'t specified.

    Within the loop\'s body, use the [FileAppend](FileAppend.htm)
    function without the *Filename* parameter (i.e. omit it) to append
    to this special file. Appending to a file in this manner performs
    better than using [FileAppend](FileAppend.htm) in its 2-parameter
    mode because the file does not need to be closed and re-opened for
    each operation. Remember to include a linefeed (\`n) or carriage
    return and linefeed (\`r\`n) after the text, if desired.

    The file is not opened if nothing is ever written to it. This
    happens if the loop performs zero iterations or if it never calls
    [FileAppend](FileAppend.htm).

    **Options:** The end of line (EOL) translation mode and output file
    encoding depend on which options are passed in the opening call to
    [FileAppend](FileAppend.htm) (i.e. the first call which omits
    *Filename*). Subsequent calls ignore the *Options* parameter. EOL
    translation is not performed by default; that is, linefeed (\`n)
    characters are written as-is unless the `` "`n" `` option is
    present.

    **Standard Output (stdout):** Specifying an asterisk (\*) for
    *OutputFile* sends any text written by [FileAppend](FileAppend.htm)
    to standard output (stdout). Such text can be redirected to a file,
    piped to another EXE, or captured by [fancy text
    editors](_ErrorStdOut.htm). However, text sent to stdout will not
    appear at the command prompt it was launched from. This can be
    worked around by 1) compiling the script with the [Ahk2Exe
    ConsoleApp directive](../misc/Ahk2ExeDirectives.htm#ConsoleApp),
    or 2) piping a script\'s output to another command or program. See
    [FileAppend](FileAppend.htm) for more details.

## Remarks {#Remarks}

A file-reading loop is useful when you want to operate on each line
contained in a text file, one at a time. The file is kept open for the
entire operation to avoid having to re-scan each time to find the next
line.

The built-in variable **A_LoopReadLine** exists within any file-reading
loop. It contains the contents of the current line excluding the
carriage return and linefeed (\`r\`n) that marks the end of the line. If
an inner file-reading loop is enclosed by an outer file-reading loop,
the innermost loop\'s file-line will take precedence.

Lines up to 65,534 characters long can be read. If the length of a line
exceeds this, its remaining characters will be read during the next loop
iteration.

[StrSplit](StrSplit.htm) or a [parsing loop](LoopParse.htm) is often
used inside a file-reading loop to parse the contents of each line
retrieved from *InputFile*. For example, if *InputFile*\'s lines are
each a series of tab-delimited fields, those fields can individually
retrieved as in this example:

    Loop read, "C:\Database Export.txt"
    {
        Loop parse, A_LoopReadLine, A_Tab
        {
            MsgBox "Field number " A_Index " is " A_LoopField "."
        }
    }

To load an entire file into a variable, use [FileRead](FileRead.htm)
because it performs much better than a loop (especially for large
files).

To have multiple files open simultaneously, use
[FileOpen](FileOpen.htm).

The One True Brace (OTB) style may optionally be used, which allows the
open-brace to appear on the same line rather than underneath. For
example: `Loop Read InputFile, OutputFile {`.

See [Loop](Loop.htm) for information about [Blocks](Block.htm),
[Break](Break.htm), [Continue](Continue.htm), and the A_Index variable
(which exists in every type of loop).

To control how the file is decoded when no byte order mark is present,
use [FileEncoding](FileEncoding.htm).

The loop may optionally be followed by an [Else](Else.htm) statement,
which is executed if the input file is empty or could not be found. If
*OutputFile* was specified, the special mode of
[FileAppend](FileAppend.htm) described [above](#OutputFile) may also be
used within the *Else* statement\'s body. If there is no *Else*, an
[OSError](Error.htm#OSError) is thrown if the file could not be found.

## Related {#Related}

[FileEncoding](FileEncoding.htm), [FileOpen](FileOpen.htm)/[File
Object](File.htm), [FileRead](FileRead.htm),
[FileAppend](FileAppend.htm), [Sort](Sort.htm), [Loop](Loop.htm),
[Break](Break.htm), [Continue](Continue.htm), [Blocks](Block.htm),
[FileSetAttrib](FileSetAttrib.htm), [FileSetTime](FileSetTime.htm)

## Examples {#Examples}

::: {#ExFileAppend .ex}
[](#ExFileAppend){.ex_number} Only those lines of the 1st file that
contain the word FAMILY will be written to the 2nd file. Uncomment the
first line to overwrite rather than append to any existing file.

    ;FileDelete "C:\Docs\Family Addresses.txt"

    Loop read, "C:\Docs\Address List.txt", "C:\Docs\Family Addresses.txt"
    {
        if InStr(A_LoopReadLine, "family")
            FileAppend(A_LoopReadLine "`n")
    }
    else
        MsgBox "Address List.txt was completely empty or not found."
:::

::: {#ExLastLine .ex}
[](#ExLastLine){.ex_number} Retrieves the last line from a text file.

    Loop read, "C:\Log File.txt"
        last_line := A_LoopReadLine  ; When loop finishes, this will hold the last line.
:::

::: {#ExURL .ex}
[](#ExURL){.ex_number} Attempts to extract all FTP and HTTP URLs from a
text or HTML file.

    SourceFile := FileSelect(3,, "Pick a text or HTML file to analyze.")
    if SourceFile = ""
        return  ; This will exit in this case.

    SplitPath SourceFile,, &SourceFilePath,, &SourceFileNoExt
    DestFile := SourceFilePath "\" SourceFileNoExt " Extracted Links.txt"

    if FileExist(DestFile)
    {
        Result := MsgBox("Overwrite the existing links file? Press No to append to it.`n`nFILE: " DestFile,, 4)
        if Result = "Yes"
            FileDelete DestFile
    }

    LinkCount := 0
    Loop read, SourceFile, DestFile
    {
        URLSearch(A_LoopReadLine)
    }
    MsgBox LinkCount ' links were found and written to "' DestFile '".'
    return


    URLSearch(URLSearchString)
    {
        ; It's done this particular way because some URLs have other URLs embedded inside them:
        ; Find the left-most starting position:
        URLStart := 0  ; Set starting default.
        for URLPrefix in ["https://", "http://", "ftp://", "www."]
        {
            ThisPos := InStr(URLSearchString, URLPrefix)
            if !ThisPos  ; This prefix is disqualified.
                continue
            if !URLStart
                URLStart := ThisPos
            else ; URLStart has a valid position in it, so compare it with ThisPos.
            {
                if ThisPos && ThisPos < URLStart
                    URLStart := ThisPos
            }
        }

        if !URLStart  ; No URLs exist in URLSearchString.
            return

        ; Otherwise, extract this URL:
        URL := SubStr(URLSearchString, URLStart)  ; Omit the beginning/irrelevant part.
        Loop parse, URL, " `t<>"  ; Find the first space, tab, or angle bracket (if any).
        {
            URL := A_LoopField
            break  ; i.e. perform only one loop iteration to fetch the first "field".
        }
        ; If the above loop had zero iterations because there were no ending characters found,
        ; leave the contents of the URL var untouched.

        ; If the URL ends in a double quote, remove it.  For now, StrReplace is used, but
        ; note that it seems that double quotes can legitimately exist inside URLs, so this
        ; might damage them:
        URLCleansed := StrReplace(URL, '"')
        FileAppend URLCleansed "`n"
        global LinkCount += 1

        ; See if there are any other URLs in this line:
        CharactersToOmit := StrLen(URL)
        CharactersToOmit += URLStart
        URLSearchString := SubStr(URLSearchString, CharactersToOmit)
        
        ; Recursive call to self:
        URLSearch(URLSearchString)
    }
:::
