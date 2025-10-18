# Script Compiler Directives

## Table of Contents {#toc}

-   [Introduction](#Intro1)
-   [Directives that control the script behaviour](#IgnoreKeep):
    -   [IgnoreBegin](#IgnoreKeep)
    -   [IgnoreEnd](#IgnoreKeep)
    -   [IgnoreKeep](#IgnoreKeep)
-   [Directives that control executable metadata](#Directives):
    -   [Introduction](#Intro2)
    -   [AddResource](#AddResource): Adds a resource to the .exe.
    -   [Bin / Base](#Bin): Specifies the base version of AutoHotkey to
        use.
    -   [ConsoleApp](#ConsoleApp): Sets Console mode.
    -   [Cont](#Cont): Specifies a directive continuation line.
    -   [Debug](#Debug): Shows directive debugging text.
    -   [ExeName](#ExeName): Specifies the location and name for the
        .exe.
    -   [Let](#Let): Sets a user variable.
    -   [Nop](#Nop): Does nothing.
    -   [Obey](#Obey): Obeys a command or expression.
    -   [PostExec](#PostExec): Runs a program after compilation.
    -   [ResourceID](#ResourceID): Assigns a non-standard resource ID to
        the main script.
    -   [SetMainIcon](#SetMainIcon): Sets the main icon.
    -   [Set*Prop*](#SetProp): Sets an .exe property.
    -   [Set](#Set): Sets a miscellaneous property.
    -   [UpdateManifest](#UpdateManifest): Changes the .exe\'s manifest.
    -   [UseResourceLang](#UseResourceLang): Changes the resource
        language.

## Introduction {#Intro1}

Script compiler directives allow the user to specify details of how a
script is to be compiled via [Ahk2Exe](../Scripts.htm#ahk2exe). Some of
the features are:

-   Ability to change the version information (such as the name,
    description, version\...).
-   Ability to add resources to the compiled script.
-   Ability to tweak several miscellaneous aspects of compilation.
-   Ability to remove code sections from the compiled script and vice
    versa.

The script compiler looks for special comments in the source script and
recognises these as Compiler Directives. All compiler directives are
introduced by the string `@Ahk2Exe-`, preceded by the comment flag
(usually `;`).

## Directives that control the script behaviour {#IgnoreKeep}

It is possible to remove code sections from the compiled script by
wrapping them in directives:

``` NoIndent
MsgBox "This message appears in both the compiled and uncompiled script"
;@Ahk2Exe-IgnoreBegin
MsgBox "This message does NOT appear in the compiled script"
;@Ahk2Exe-IgnoreEnd
MsgBox "This message appears in both the compiled and uncompiled script"
```

The reverse is also possible, i.e. marking a code section to only be
executed in the compiled script:

``` NoIndent
/*@Ahk2Exe-Keep
MsgBox "This message appears only in the compiled script"
*/
MsgBox "This message appears in both the compiled and uncompiled script"
```

This has advantage over [A_IsCompiled](../Variables.htm#IsCompiled)
because the code is completely removed from the compiled script during
preprocessing, thus making the compiled script smaller. The reverse is
also true: it will not be necessary to check for
[A_IsCompiled](../Variables.htm#IsCompiled) because the code is inside a
comment block in the uncompiled script.

## Directives that control executable metadata {#Directives}

### Introduction {#Intro2}

In the parameters of these directives, the following escape sequences
are supported: ``` `` ```, `` `, ``, `` `n ``, `` `r `` and `` `t ``.
Commas *always* need to be escaped, regardless of the parameter
position. \"Integer\" refers to unsigned 16-bit integers (0..0xFFFF).

If required, directive parameters can reference the following list of
standard built-in variables by enclosing the variable name with `%`
signs:

**Group 1:** [A_AhkPath](../Variables.htm#AhkPath),
[A_AppData](../Variables.htm#AppData),
[A_AppDataCommon](../Variables.htm#AppDataCommon),
[A_ComputerName](../Variables.htm#ComputerName),
[A_ComSpec](../Variables.htm#ComSpec),
[A_Desktop](../Variables.htm#Desktop),
[A_DesktopCommon](../Variables.htm#DesktopCommon),
[A_MyDocuments](../Variables.htm#MyDocuments),
[A_ProgramFiles](../Variables.htm#ProgramFiles),
[A_Programs](../Variables.htm#Programs),
[A_ProgramsCommon](../Variables.htm#ProgramsCommon),
[A_ScriptDir](../Variables.htm#ScriptDir),
[A_ScriptFullPath](../Variables.htm#ScriptFullPath),
[A_ScriptName](../Variables.htm#ScriptName),
[A_Space](../Variables.htm#Space),
[A_StartMenu](../Variables.htm#StartMenu),
[A_StartMenuCommon](../Variables.htm#StartMenuCommon),
[A_Startup](../Variables.htm#Startup),
[A_StartupCommon](../Variables.htm#StartupCommon),
[A_Tab](../Variables.htm#Tab), [A_Temp](../Variables.htm#Temp),
[A_UserName](../Variables.htm#UserName),
[A_WinDir](../Variables.htm#WinDir).

**Group 2:** [A_AhkVersion](../Variables.htm#AhkVersion),
[A_IsCompiled](../Variables.htm#IsCompiled),
[A_PtrSize](../Variables.htm#PtrSize).

In addition to these variable names, the special variable
**A_WorkFileName** holds the temporary name of the processed .exe file.
This can be used to pass the file name as a parameter to any
[PostExec](#PostExec) directives which need to access the generated
.exe.

Furthermore, the special variable **A_BasePath** contains the full path
and name of the selected base file.

Also, the special variable **A_PriorLine** contains the source line
immediately preceding the current compiler directive. Intervening lines
of blanks and comments only are ignored, as are any intervening compiler
directive lines. This variable can be used to \'pluck\' constant
information from the script source, and use it in later compiler
directives. An example would be accessing the version number of the
script, which may be changed often. Accessing the version number in this
way means that it needs to be changed only once in the source code, and
the change will get copied through to the necessary directive. (See the
RegEx example below for more information.)

As well, special user variables can be created with the format
`U_`*`Name`* using the [Let](#Let) and [Obey](#Obey) directives,
described below.

In addition to being available for directive parameters, all variables
can be accessed from any RT_MENU, RT_DIALOG, RT_STRING, RT_ACCELERATORS,
RT_HTML, and RT_MANIFEST file supplied to the
[AddResource](#AddResource) directive, below.

If needed, the value returned from the above variables can be
manipulated by including at the end of the built-in variable name before
the ending `%`, up to 2 parameters (called p2 and p3) all separated by
tilde `~`. The p2 and p3 parameters will be used as literals in the 2nd
and 3rd parameters of a [RegExReplace](../lib/RegExReplace.htm) function
to manipulate the value returned. (See [RegEx Quick
Reference](RegEx-QuickRef.htm).) Note that p3 is optional.

To include a tilde as data in p2 or p3, preceded it with a back-tick,
i.e. `` `~ ``. To include a back-tick character as data in p2 or p3,
double it, i.e. ``` `` ```.

**RegEx examples:**

-   ``` NoIndent
    %A_ScriptName~\.[^\.]+$~.exe%
    ```

    This replaces the extension plus preceding full-stop, with `.exe` in
    the actual script name.\
    (`\.[^\.]+$~.exe` means scan for a `.` followed by 1 or more non-`.`
    characters followed by end-of-string, and replace them with `.exe`)

-   Assume there is a source line followed by two compiler directives as
    follows:

        CodeVersion := "1.2.3.4", company := "My Company"

        ;@Ahk2Exe-Let U_version = %A_PriorLine~U)^(.+"){1}(.+)".*$~$2%

        ;@Ahk2Exe-Let U_company = %A_PriorLine~U)^(.+"){3}(.+)".*$~$2%

    These directives copy the version number `1.2.3.4` into the special
    variable `U_version`, and the company name `My Company` into the
    special variable `U_company` for use in other directives later.\
    (The `{1}` in the first regex was changed to `{3}` in the second
    regex to select after the third `"` to extract the company name.)

**Other examples:** Other working examples which can be downloaded and
examined, are available from
[here](https://github.com/AutoHotkey/Ahk2Exe/releases/tag/DemoCode_1).

### AddResource {#AddResource}

Adds a resource to the compiled executable. (Also see
[UseResourceLang](#UseResourceLang) below)

``` Syntax
;@Ahk2Exe-AddResource FileName , ResourceName
```

FileName
:   The filename of the resource to add. The file is assumed to be in
    (or relative to) the script\'s own directory if an absolute path
    isn\'t specified. The type of the resource (as an integer or string)
    can be explicitly specified by prepending an asterisk to it:
    `*type Filename`{.no-highlight}. If omitted, Ahk2Exe automatically
    detects the type according to the file extension.

ResourceName
:   *(Optional)* The name that the resource will have (can be a string
    or an integer). If omitted, it defaults to the name (with no path)
    of the file, in uppercase.

Here is a list of common standard resource types and the extensions that
trigger them by default.

-   2 (RT_BITMAP): `.bmp`, `.dib`
-   4 (RT_MENU)
-   5 (RT_DIALOG)
-   6 (RT_STRING)
-   9 (RT_ACCELERATORS)
-   10 (RT_RCDATA): Every single other extension.
-   11 (RT_MESSAGETABLE)
-   12 (RT_GROUP_CURSOR): `.cur` (not yet supported)
-   14 (RT_GROUP_ICON): `.ico`
-   23 (RT_HTML): `.htm`, `.html`, `.mht`
-   24 (RT_MANIFEST): `.manifest`. If the name for the resource is not
    specified, it defaults to `1`

**Example 1:** To replace the standard icons (other than the [main
icon](#SetMainIcon)):

    ;@Ahk2Exe-AddResource Icon1.ico, 160  ; Replaces 'H on blue'
    ;@Ahk2Exe-AddResource Icon2.ico, 206  ; Replaces 'S on green'
    ;@Ahk2Exe-AddResource Icon3.ico, 207  ; Replaces 'H on red'
    ;@Ahk2Exe-AddResource Icon4.ico, 208  ; Replaces 'S on red'

**Example 2:** To include another script as a separate RCDATA resource
(see [Embedded Scripts](../Program.htm#embedded-scripts)):

    ;@Ahk2Exe-AddResource MyScript1.ahk, #2
    ;@Ahk2Exe-AddResource MyScript2.ahk, MYRESOURCE

Note that each script added with this directive will be fully and
separately processed by the compiler, and can include further
directives. If there are any competing directives overall, the last
encountered by the compiler will be used.

### Bin / Base {#Bin}

Specifies the base version of AutoHotkey to be used to generate the .exe
file. This directive may be overridden by a base file parameter
specified in the GUI or CLI. This directive can be specified many times
if necessary, but only in the top level script file (i.e. not in an
[#Include](../lib/_Include.htm) file). The compiler will be run at least
once for each Bin/Base directive found. (If an actual comment is
appended to this directive, it must use the ` ;` flag. To truly comment
out this directive, insert a space after the first comment flag.)

``` Syntax
;@Ahk2Exe-Bin  [Path\]Name , [Exe_path\][Name], Codepage ; Deprecated
;@Ahk2Exe-Base [Path\]Name , [Exe_path\][Name], Codepage
```

\[Path\\\]Name
:   The \*.bin or \*.exe file to use. If no extension is supplied,
    `.bin` is assumed. The file is assumed to be in (or relative to) the
    compiler\'s own directory if an absolute path isn\'t specified. A
    DOS mask may be specified for *Name*, e.g. `ANSI*`, `Unicode 32*`,
    `Unicode 64*`, or `*bit` for all three. The compiler will be run for
    each \*.bin or \*.exe file that matches. Any use of built-in
    variable replacements must only be from [group 1](#group1) above.

\[Exe_path\\\]\[Name\]
:   *(Optional)* The file name to be given to the .exe. Any extension
    supplied will be replaced by `.exe`. If no path is specified, the
    .exe will be created in the script folder. If no name is specified,
    the .exe will have the default name. Any use of built-in variable
    replacements must only be from [group 1](#group1) above. (This
    parameter can be overridden by the [ExeName](#ExeName) directive.)

Codepage
:   *(Optional)* Overrides the default
    [codepage](https://learn.microsoft.com/windows/win32/intl/code-page-identifiers)
    used to process script files. (Scripts should begin with a Unicode
    byte-order-mark (BOM), rendering the use of this parameter
    unnecessary.)

### ConsoleApp {#ConsoleApp}

Changes the executable subsystem to Console mode.

``` Syntax
;@Ahk2Exe-ConsoleApp
```

### Cont {#Cont}

Specifies a continuation line for the preceding directive. This allows a
long-lined directive to be formatted so that it is easy to read in the
source code.

``` Syntax
;@Ahk2Exe-Cont Text
```

Text
:   The text to be appended to the previous directive line, before that
    line is processed. The text starts after the single space following
    the `Cont` key-word.

### Debug {#Debug}

Shows a message box with the supplied text, for debugging purposes.

``` Syntax
;@Ahk2Exe-Debug Text
```

Text
:   The text to be shown. Include any special variables between `%`
    signs to see the (manipulated) contents.

### ExeName {#ExeName}

Specifies the location and name given to the generated .exe file. (Also
see the [Base](#Bin) directive.) This directive may be overridden by an
output file specified in the GUI or CLI.

``` Syntax
;@Ahk2Exe-ExeName [Path\][Name]
```

\[Path\\\]\[Name\]
:   The .exe file name. Any extension supplied will be replaced by
    `.exe`. If no path is specified, the .exe will be created in the
    script folder. If no name is specified, the .exe will have the
    default name.

**Example:**

    ;@Ahk2Exe-Obey U_bits, = %A_PtrSize% * 8
    ;@Ahk2Exe-Obey U_type, = "%A_IsUnicode%" ? "Unicode" : "ANSI"
    ;@Ahk2Exe-ExeName %A_ScriptName~\.[^\.]+$%_%U_type%_%U_bits%

### Let {#Let}

Creates (or modifies) one or more user variables which can be accessed
by `%U_`*`Name`*`%`, similar to the built-in variables (see above).

``` Syntax
;@Ahk2Exe-Let Name = Value , Name = Value, ...
```

Name
:   The name of the variable (with or without the leading `U_`).

Value
:   The value to be used.

### Nop {#Nop}

Does nothing.

``` Syntax
;@Ahk2Exe-Nop Text
```

Text
:   *(Optional)* Any text, which is ignored.

**Example:**

    Ver := A_AhkVersion "" ; If quoted literal not empty, do 'SetVersion'
    ;@Ahk2Exe-Obey U_V, = "%A_PriorLine~U)^(.+")(.*)".*$~$2%" ? "SetVersion" : "Nop"
    ;@Ahk2Exe-%U_V%        %A_AhkVersion%%A_PriorLine~U)^(.+")(.*)".*$~$2%

### Obey {#Obey}

Obeys isolated AutoHotkey commands or expressions, with result in
`U_`*`Name`*.

``` Syntax
;@Ahk2Exe-Obey Name, CmdOrExp , Extra
```

Name
:   The name of the variable (with or without the leading `U_`) to
    receive the result.

CmdOrExp

:   The command or expression to obey.

    **Command** format must use *Name* as the output variable (often the
    first parameter), e.g.

        ;@Ahk2Exe-Obey U_date, FormatTime U_date`, R D2 T2

    **Expression** format must start with `=`, e.g.

        ;@Ahk2Exe-Obey U_type, = "%A_IsUnicode%" ? "Unicode" : "ANSI"

    Expressions can be written in command format, e.g.

        ;@Ahk2Exe-Obey U_bits, U_bits := %A_PtrSize% * 8

    If needed, separate multiple commands and expressions with `` `n ``.

Extra
:   *(Optional)* A number (1-9) specifying the number of extra results
    to be returned. e.g. if extra = 2, results will be returned in
    `U_`*`name`*, `U_`*`name`*`1`, and `U_`*`name`*`2`. The values in
    the *`name`*s must first be set by the expression or command.

### PostExec {#PostExec}

Specifies a program to be executed after a successful compilation,
before (or after) any [Compression](../Scripts.htm#mpress) is applied to
the .exe. This directive can be present many times and will be executed
in the order encountered by the compiler, in the appropriate queue as
specified by the *When* parameter.

``` Syntax
;@Ahk2Exe-PostExec Program [parameters] , When, WorkingDir, Hidden, IgnoreErrors
```

Program \[parameters\]
:   The program to execute, plus parameters. To allow access to the
    processed .exe file, specify the special variable
    [A_WorkFileName](#WorkFileName) as a quoted parameter, such as
    `"%A_WorkFileName%"`. If the program changes the .exe, the altered
    .exe must be moved back to the input file specified by
    `%A_WorkFileName%`, by the program. (Note that the .exe will contain
    binary data.)

When

:   *(Optional)* Leave blank to execute before any
    [Compression](../Scripts.htm#mpress) is done. Otherwise set to a
    number to run after compression as follows:

    -   0 - Only run when no compression is specified.
    -   1 - Only run when MPRESS compression is specified.
    -   2 - Only run when UPX compression is specified.

WorkingDir
:   *(Optional)* The working directory for the program. Do not enclose
    the name in double quotes even if it contains spaces. If omitted,
    the directory of the compiler (Ahk2Exe) will be used.

Hidden
:   *(Optional)* If set to 1, the program will be launched hidden.

IgnoreErrors
:   *(Optional)* If set to 1, any errors that occur during the launching
    or running of the program will not be reported to the user.

**Example 1:** (To use the first two examples, first download
[BinMod.ahk](https://github.com/AutoHotkey/Ahk2Exe/blob/master/BinMod.ahk)
and compile it according to the instructions in the downloaded script.)

This example can be used to remove a reference to \"AutoHotkey\" in the
generated .exe to disguise that it is a compiled AutoHotkey script:

    ;@Ahk2Exe-Obey U_au, = "%A_IsUnicode%" ? 2 : 1    ; Script ANSI or Unicode?
    ;@Ahk2Exe-PostExec "BinMod.exe" "%A_WorkFileName%"
    ;@Ahk2Exe-Cont  "%U_au%2.>AUTOHOTKEY SCRIPT<. DATA              "

**Example 2:** This example will alter a UPX compressed .exe so that it
can\'t be de-compressed with `UPX -d`:

    ;@Ahk2Exe-PostExec "BinMod.exe" "%A_WorkFileName%"
    ;@Ahk2Exe-Cont  "11.UPX." "1.UPX!.", 2

(There are other examples mentioned in the
[BinMod.ahk](https://github.com/AutoHotkey/Ahk2Exe/blob/master/BinMod.ahk)
script.)

**Example 3:** This example specifies the
[Compression](../Scripts.htm#mpress) to be used on a compiled script, if
none is specified in the CLI or GUI. The default parameters normally
used by the compiler are shown.

For MPRESS:

    ;@Ahk2Exe-PostExec "MPRESS.exe" "%A_WorkFileName%" -q -x, 0,, 1

For UPX:

    ;@Ahk2Exe-PostExec "UPX.exe" "%A_WorkFileName%"
    ;@Ahk2Exe-Cont  -q --all-methods --compress-icons=0, 0,, 1

### ResourceID {#ResourceID}

Assigns a non-standard resource ID to be used for the main script for
compilations which use an [.exe base file](#Bin) (see [Embedded
Scripts](../Program.htm#embedded-scripts)). This directive may be
overridden by a Resource ID specified in the GUI or CLI. This directive
is ignored if it appears in a script inserted by the
[AddResource](#AddResource) directive.

``` Syntax
;@Ahk2Exe-ResourceID Name
```

Name
:   The resource ID to use. Numeric resource IDs should consist of a
    hash sign (#) followed by a decimal number.

### SetMainIcon {#SetMainIcon}

Overrides the custom EXE icon used for compilation. (To change the other
icons, see the [AddResource](#AddResource) example.) This directive may
be overridden by an icon file specified in the GUI or CLI. The new icon
might not be immediately visible in Windows Explorer if the compiled
file existed before with a different icon, however the new icon can be
shown by selecting `Refresh Windows Icons` from the Ahk2Exe `File` menu.

``` Syntax
;@Ahk2Exe-SetMainIcon IcoFile
```

IcoFile
:   *(Optional)* The icon file to use. If omitted, the default
    AutoHotkey icon is used.

### Set*Prop* {#SetProp}

Changes a property in the compiled executable\'s version information.
Note that all properties are processed in alphabetical order, regardless
of the order they are specified.

``` Syntax
;@Ahk2Exe-SetProp Value
```

*Prop*

:   The name of the property to change. Must be one of those listed
    below.

    +-----------------------------------+-----------------------------------+
    | Property                          | Description                       |
    +===================================+===================================+
    | CompanyName                       | Changes the company name.         |
    +-----------------------------------+-----------------------------------+
    | Copyright                         | Changes the legal copyright       |
    |                                   | information.                      |
    +-----------------------------------+-----------------------------------+
    | Description                       | Changes the file description. On  |
    |                                   | Windows 8 and above, this also    |
    |                                   | changes the script\'s name in     |
    |                                   | Task Manager under \"Processes\". |
    +-----------------------------------+-----------------------------------+
    | FileVersion                       | Changes the file version, in both |
    |                                   | text and raw binary format. (See  |
    |                                   | *Version* below, for more         |
    |                                   | details.)                         |
    +-----------------------------------+-----------------------------------+
    | InternalName                      | Changes the internal name.        |
    +-----------------------------------+-----------------------------------+
    | Language                          | Changes the [language             |
    |                                   | code](Languages.htm). Please note |
    |                                   | that hexadecimal numbers must     |
    |                                   | have an `0x` prefix.              |
    +-----------------------------------+-----------------------------------+
    | LegalTrademarks                   | Changes the legal trademarks      |
    |                                   | information.                      |
    +-----------------------------------+-----------------------------------+
    | Name                              | Changes the product name and the  |
    |                                   | internal name.                    |
    +-----------------------------------+-----------------------------------+
    | OrigFilename                      | Changes the original filename     |
    |                                   | information.                      |
    +-----------------------------------+-----------------------------------+
    | ProductName                       | Changes the product name.         |
    +-----------------------------------+-----------------------------------+
    | ProductVersion                    | Changes the product version, in   |
    |                                   | both text and raw binary format.  |
    |                                   | (See *Version* below, for more    |
    |                                   | details.)                         |
    +-----------------------------------+-----------------------------------+
    | Version                           | Changes the file version and the  |
    |                                   | product version, in both text and |
    |                                   | raw binary format.                |
    |                                   |                                   |
    |                                   | Ahk2Exe fills the binary version  |
    |                                   | fields with the period-delimited  |
    |                                   | numbers (up to four) that may     |
    |                                   | appear at the beginning of the    |
    |                                   | version text. Unfilled fields are |
    |                                   | set to zero. For example,         |
    |                                   | `1.3-alpha` would produce a       |
    |                                   | binary version number of          |
    |                                   | `1.3.0.0`. If this property is    |
    |                                   | not modified, it defaults to the  |
    |                                   | AutoHotkey version used to        |
    |                                   | compile the script.               |
    +-----------------------------------+-----------------------------------+

Value
:   The value to set the property to.

### Set {#Set}

Changes other miscellaneous properties in the compiled executable\'s
version information not covered by the [SetProp](#SetProp) directive.
Note that all properties are processed in alphabetical order, regardless
of the order they are specified. This directive is for specialised use
only.

``` Syntax
;@Ahk2Exe-Set Prop, Value
```

Prop
:   The name of the property to change.

Value
:   The value to set the property to.

### UpdateManifest {#UpdateManifest}

Changes details in the .exe\'s manifest. This directive is for
specialised use only.

``` Syntax
;@Ahk2Exe-UpdateManifest RequireAdmin , Name, Version, UIAccess
```

RequireAdmin
:   Set to 1 to change the executable to require administrative
    privileges when run. Set to 2 to change the executable to request
    highest available privileges when run. Set to 0 to leave unchanged.

Name
:   *(Optional)* The name to be set in the manifest.

Version
:   *(Optional)* The version to be set in the manifest.

UIAccess
:   *(Optional)* Set to 1 to make UIAccess true in the manifest.

### UseResourceLang {#UseResourceLang}

Changes the resource language used by [AddResource](#AddResource). This
directive is positional and affects all [AddResource](#AddResource)
directives that follow it.

``` Syntax
;@Ahk2Exe-UseResourceLang LangCode
```

LangCode
:   The [language code](Languages.htm). Please note that hexadecimal
    numbers must have an `0x` prefix. The default resource language is
    US English (0x0409).
