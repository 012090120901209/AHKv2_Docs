# FileRead

Retrieves the contents of a file.

``` Syntax
Text := FileRead(Filename , Options)
```

## Parameters {#Parameters}

Filename

:   Type: [String](../Concepts.htm#strings)

    The name of the file to read, which is assumed to be in
    [A_WorkingDir](../Variables.htm#WorkingDir) if an absolute path
    isn\'t specified.

Options

:   Type: [String](../Concepts.htm#strings)

    Zero or more of the following strings. Separate each option from the
    next with a single space or tab. For example: `` "`n m5000 UTF-8" ``

    **Encoding:** Specify any of the encoding names accepted by
    [FileEncoding](FileEncoding.htm) (excluding the empty string) to use
    that encoding if the file lacks a UTF-8 or UTF-16 byte order mark.
    If omitted, it defaults to
    [A_FileEncoding](../Variables.htm#FileEncoding).

    **RAW:** Specify the word RAW (case-insensitive) to read the file\'s
    content as [raw binary data](#Binary) and return a
    [Buffer](Buffer.htm) object instead of a string. This option
    overrides any previously specified encoding and vice versa.

    **m1024:** If this option is omitted, the entire file is loaded
    unless there is insufficient memory, in which case an error message
    is shown and the thread exits (but [Try](Try.htm) can be used to
    avoid this). Otherwise, replace 1024 with a decimal or hexadecimal
    number of bytes. If the file is larger than this, only its leading
    part is loaded.

    **Note:** This might result in the last line ending in a naked
    carriage return (\`r) rather than \`r\`n.

    **\`n** (a linefeed character): Replaces any/all occurrences of
    carriage return & linefeed (\`r\`n) with linefeed (\`n). However,
    this translation reduces performance and is usually not necessary.
    For example, text containing \`r\`n is already in the right format
    to be added to a [Gui Edit control](StrReplace.htm). The following
    [parsing loop](LoopParse.htm) will work correctly regardless of
    whether each line ends in \`r\`n or just \`n:
    `` Loop Parse, MyFileContents, "`n", "`r" ``.

## Return Value {#Return_Value}

Type: [String](../Concepts.htm#strings) or
[Object](../Concepts.htm#objects)

This function returns the contents of the specified file. The return
value is a [Buffer object](Buffer.htm) if the RAW option is in effect
and the file can be opened; otherwise, it is a string. If the file does
not exist or cannot be opened for any other reason, an empty string is
returned.

## Error Handling {#Error_Handling}

An [OSError](Error.htm#OSError) is thrown if there was a problem opening
or reading the file.

A file greater than 4 GB in size will cause a
[MemoryError](Error.htm#MemoryError) to be thrown unless the \*m option
is present, in which case the leading part of the file is loaded. A
MemoryError will also be thrown if the program is unable to allocate
enough memory to contain the requested amount of data.

[A_LastError](../Variables.htm#LastError) is set to the result of the
operating system\'s GetLastError() function.

## Reading Binary Data {#Binary}

When the `RAW` option is used, the return value is a
[Buffer](Buffer.htm) object containing the raw, unmodified contents of
the file. The object\'s [Size](Buffer.htm#Size) property returns the
number of bytes read. [NumGet](NumGet.htm) or [StrGet](StrGet.htm) can
be used to retrieve data from the buffer. For example:

    buf := FileRead(A_AhkPath, "RAW")
    if StrGet(buf, 2, "cp0") == "MZ"  ; Looks like an executable file...
    {
        ; Read machine type from COFF file header.
        machine := NumGet(buf, NumGet(buf, 0x3C, "uint") + 4, "ushort")
        machine := machine=0x8664 ? "x64" : machine=0x014C ? "x86" : "unknown"
        ; Display machine type and file size.
        MsgBox "This " machine " executable is " buf.Size " bytes."
    }
    buf := ""

This option is generally required for reading binary data because by
default, any bytes read from file are interpreted as text and may be
converted from the source file\'s encoding (as specified in the options
or by [A_FileEncoding](../Variables.htm#FileEncoding)) to the script\'s
[native encoding](../Compat.htm#Format), UTF-16. If the data is not
UTF-16 text, this conversion generally changes the data in undesired
ways.

For another demonstration of the RAW option, see [ClipboardAll example
#2](ClipboardAll.htm#ExFile).

Finally, [FileOpen](FileOpen.htm) and [File.RawRead](File.htm#RawRead)
or [File.Read*Num*](File.htm#ReadNum) may be used to read binary data
without first reading the entire file into memory.

## Remarks {#Remarks}

When the goal is to load all or a large part of a file into memory,
FileRead performs much better than using a [file-reading
loop](LoopRead.htm).

If there is concern about using too much memory, check the file size
beforehand with [FileGetSize](FileGetSize.htm).

[FileOpen](FileOpen.htm) provides more advanced functionality than
FileRead, such as reading or writing data at a specific location in the
file without reading the entire file into memory. See [File
Object](File.htm) for a list of functions.

## Related {#Related}

[FileEncoding](FileEncoding.htm), [FileOpen](FileOpen.htm)/[File
Object](File.htm), [file-reading loop](LoopRead.htm),
[FileGetSize](FileGetSize.htm), [FileAppend](FileAppend.htm),
[IniRead](IniRead.htm), [Sort](Sort.htm), [Download](Download.htm)

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Reads a text file into *MyText*.

    MyText := FileRead("C:\My Documents\My File.txt")
:::

::: {#ExSort .ex}
[](#ExSort){.ex_number} Quickly sorts the contents of a file.

    Contents := FileRead("C:\Address List.txt")
    Contents := Sort(Contents)
    FileDelete "C:\Address List (alphabetical).txt"
    FileAppend Contents, "C:\Address List (alphabetical).txt"
    Contents := "" ; Free the memory.
:::
