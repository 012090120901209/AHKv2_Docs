# #Warn

Enables or disables warnings for specific conditions which may indicate
an error, such as a typo or missing \"global\" declaration.

``` Syntax
#Warn WarningType, WarningMode
```

## Parameters {#Parameters}

WarningType

:   Type: [String](../Concepts.htm#strings)

    If omitted, it defaults to *All*. Otherwise, specify the type of
    warning to enable or disable.

    **VarUnset:** Before the script starts to run, display a warning for
    the first reference to each variable which is never used in any of
    the following ways:

    -   As the target of a direct, non-dynamic assignment such as
        `MyVar := ""`.
    -   Used with the [reference operator](../Variables.htm#ref) (e.g.
        `&MyVar`).
    -   Passed directly to [IsSet](IsSet.htm) (e.g. `IsSet(MyVar)`).

    **LocalSameAsGlobal:** Before the script starts to run, display a
    warning for each *undeclared* local variable which has the same name
    as a global variable. This is intended to prevent errors caused by
    forgetting to declare a global variable inside a function before
    attempting to assign to it. If the variable really was intended to
    be local, a declaration such as `local x` or `static y` can be used
    to suppress the warning.

    This warning is disabled by default.

        #Warn
        g := 1
        ShowG() {       ; The warning is displayed even if the function is never called.
            ;global g   ; <-- This is required to assign to the global variable.
            g := 2
        }
        ShowG
        MsgBox g        ; Without the declaration, the above assigned to a local "g".

    **Unreachable:** Before the script starts to run, show a warning for
    each line that immediately follows a `Return`, `Break`, `Continue`,
    `Throw` or `Goto` at the same nesting level, unless that line is the
    target of a label. Any such line would never be executed.

    If the code is intended to be unreachable - such as if a `return`
    has been used to temporarily disable a block of code, or a hotkey or
    hotstring has been temporarily disabled by commenting it out -
    consider commenting out the unreachable code as well. Alternatively,
    the warning can be suppressed by defining a
    [label](../misc/Labels.htm) above the first unreachable line.

    **All:** Apply the given *WarningMode* to all supported warning
    types.

WarningMode

:   Type: [String](../Concepts.htm#strings)

    If omitted, it defaults to *MsgBox*. Otherwise, specify a value
    indicating how warnings should be delivered.

    **MsgBox:** Show a message box describing the warning. Note that
    once the message box is dismissed, the script will continue as
    usual.

    **StdOut:** Send a description of the warning to *stdout* (the
    program\'s standard output stream), along with the filename and line
    number. This allows fancy editors such as SciTE to capture warnings
    without disrupting the script - the user can later jump to each
    offending line via the editor\'s output pane.

    **OutputDebug:** Send a description of the warning to the debugger
    for display. If a debugger is not active, this will have no effect.
    For more details, see [OutputDebug](OutputDebug.htm).

    **Off:** Disable warnings of the given *WarningType*.

## Remarks {#Remarks}

If this directive is unspecified in the script, all warnings are enabled
and use the MsgBox mode, except for LocalSameAsGlobal, which is
disabled.

The checks which produce VarUnset, LocalSameAsGlobal and Unreachable
warnings are performed after all directives have been parsed, but before
the script executes. Therefore, the location in the script is not
significant (and, like other directives, #Warn cannot be executed
conditionally).

However, the ordering of multiple #Warn directives is significant: the
last occurrence that sets a given warning determines the mode for that
warning. So, for example, the two statements below have the combined
effect of enabling all warnings except LocalSameAsGlobal:

    #Warn All
    #Warn LocalSameAsGlobal, Off

## Related {#Related}

[Local and Global Variables](../Functions.htm#Local)

## Examples {#Examples}

::: {#ExAllOff .ex}
[](#ExAllOff){.ex_number} Disables all warnings. Not recommended.

    #Warn All, Off
:::

::: {#ExOmitted .ex}
[](#ExOmitted){.ex_number} Enables every type of warning and shows each
warning in a message box.

    #Warn
:::

::: {#ExLSAGOutputDebug .ex}
[](#ExLSAGOutputDebug){.ex_number} Sends a warning to OutputDebug for
each undeclared local variable which has the same name as a global
variable.

    #Warn LocalSameAsGlobal, OutputDebug
:::
