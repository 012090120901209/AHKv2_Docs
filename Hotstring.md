# Hotstring

Creates, modifies, enables, or disables a [hotstring](../Hotstrings.htm)
while the script is running.

``` Syntax
Hotstring String , Replacement, OnOffToggle
Hotstring NewOptions
Hotstring SubFunction , Value1
```

## Parameters {#Parameters}

String

:   Type: [String](../Concepts.htm#strings)

    The hotstring\'s trigger string, preceded by [the usual
    colons](../Hotstrings.htm) and [option
    characters](../Hotstrings.htm#Options). For example, `"::btw"` or
    `":*:]d"`.

    *String* may be matched to an existing hotstring by considering
    [case-sensitivity (C)](../Hotstrings.htm#C), [word-sensitivity
    (?)](../Hotstrings.htm#Question), activation criteria (as set by
    [#HotIf](_HotIf.htm) or [HotIf](HotIf.htm)) and the trigger string.
    For example, `"::btw"` and `"::BTW"` match unless the case-sensitive
    mode was enabled as a default, while `":C:btw"` and `":C:BTW"` never
    match. The `C` and `?` options may be included in *String* or set as
    defaults by the [#Hotstring](_Hotstring.htm) directive or a previous
    use of *NewOptions*.

    If the hotstring already exists, any options specified in *String*
    are put into effect, while all other options are left as is.
    However, since hotstrings with `C` or `?` are considered distinct
    from other hotstrings, it is not possible to add or remove these
    options. Instead, turn off the existing hotstring and create a new
    one.

    When a hotstring is first created \-- either by the Hotstring
    function or the [double-colon syntax](../Hotstrings.htm) in the
    script \-- its trigger string and sequence of option characters
    becomes the permanent name of that hotstring as reflected by
    [ThisHotkey](../Hotstrings.htm#ThisHotkey). This name does not
    change even if the Hotstring function later accesses the hotstring
    with different option characters.

Replacement

:   Type: [String](../Concepts.htm#strings) or [Function
    Object](../misc/Functor.htm)

    If omitted and *String* already exists as a hotstring, its
    replacement will not be changed. This is useful to change only the
    hotstring\'s options, or to turn it on or off. Otherwise, specify
    the replacement string or a callback.

    If *Replacement* is a function, it is called (as a new
    [thread](../misc/Threads.htm)) when the hotstring triggers.

    The callback accepts one parameter and can be
    [defined](../Functions.htm#intro) as follows:

    ``` NoIndent
    MyCallback(HotstringName) { ...
    ```

    Although the name you give the parameter does not matter, it is
    assigned the [hotstring name](../Hotstrings.htm#ThisHotkey).

    You can omit the callback\'s parameter if the corresponding
    information is not needed, but in this case an asterisk must be
    specified, e.g. `MyCallback(*)`.

    Hotstrings defined with the [double-colon syntax](../Hotstrings.htm)
    automatically use the parameter name `ThisHotkey`. Hotstrings can
    also be [assigned a function name](../Hotstrings.htm#Function)
    without the Hotstring function.

    After reassigning the function of a hotstring, its original function
    can only be restored if it was [given a
    name](../Hotstrings.htm#Function).

    **Note:** If this parameter is specified but the hotstring is
    disabled from a previous use of this function, the hotstring will
    remain disabled. To prevent this, specify `"On"` for *OnOffToggle*.

OnOffToggle

:   Type: [String](../Concepts.htm#strings) or
    [Integer](../Concepts.htm#numbers)

    One of the following values:

    **On** or **1** (true): Enables the hotstring.

    **Off** or **0** (false): Disables the hotstring.

    **Toggle** or **-1**: Sets the hotstring to the opposite state
    (enabled or disabled).

NewOptions

:   Type: [String](../Concepts.htm#strings)

    To set new default options for subsequently created hotstrings, pass
    the options to the Hotstring function without any leading or
    trailing colon. For example: `Hotstring "T"`.

    Turning on [case-sensitivity (C)](../Hotstrings.htm#C) or
    [word-sensitivity (?)](../Hotstrings.htm#Question) also affects
    which existing hotstrings will be found by any subsequent calls to
    the Hotstring function. For example, `Hotstring ":T:btw"` will find
    `::BTW` by default, but not if `Hotstring "C"` or
    [`#Hotstring`](_Hotstring.htm)` C` is in effect. This can be undone
    or overridden by passing a mutually-exclusive option; for example,
    `C0` and `C1` override `C`.

SubFunction, Value1

:   Type: [String](../Concepts.htm#strings)

    These parameters are dependent upon each other and their usage is
    described below.

## Sub-functions {#SubFunctions}

For *SubFunction*, specify one of the following:

-   [EndChars](#EndChars): Retrieves or modifies the set of ending
    characters.
-   [MouseReset](#MouseReset): Controls whether mouse clicks reset the
    hotstring recognizer.
-   [Reset](#Reset): Immediately resets the hotstring recognizer.

### EndChars {#EndChars}

Retrieves or modifies the set of characters used as [ending
characters](../Hotstrings.htm#EndChars) by the hotstring recognizer.

``` Syntax
OldValue := Hotstring("EndChars" , NewValue)
```

For example:

    prev_chars := Hotstring("EndChars", "-()[]{}':;`"/\,.?!`n`s`t")
    MsgBox "The previous value was: " prev_chars

[#Hotstring EndChars](#EndChars) also affects this setting.

It is currently not possible to specify a different set of end
characters for each hotstring.

### MouseReset {#MouseReset}

Retrieves or modifies the global setting which controls whether mouse
clicks reset the hotstring recognizer, as described
[here](../Hotstrings.htm#NoMouse).

``` Syntax
OldValue := Hotstring("MouseReset" , NewValue)
```

*NewValue* should be 1 (true) to enable mouse click detection and
resetting of the hotstring recognizer, or 0 (false) to disable it. The
return value is the setting which was in effect before the function was
called.

The [mouse](InstallMouseHook.htm) hook may be installed or removed if
justified by the changes made by this function.

[#Hotstring NoMouse](_Hotstring.htm) also affects this setting, and is
equivalent to specifying `false` for *NewValue*.

### Reset {#Reset}

Immediately resets the hotstring recognizer.

``` Syntax
Hotstring "Reset"
```

In other words, the script will begin waiting for an entirely new
hotstring, eliminating from consideration anything you previously typed.

## Errors {#Errors}

This function throws an exception if the parameters are invalid or a
memory allocation fails.

A [TargetError](Error.htm#TargetError) is thrown if *Replacement* is
omitted and *String* is valid but does not match an existing hotstring.
This can be utilized to test for the existence of a hotstring. For
example:

    try
        Hotstring "::btw"
    catch TargetError
        MsgBox "The hotstring does not exist or it has no variant for the current HotIf criteria."

## Remarks {#Remarks}

The [current HotIf setting](HotIf.htm) determines the
[variant](#variant) of a hotstring upon which the Hotstring function
will operate.

If the script is [suspended](Suspend.htm), newly added/enabled
hotstrings will also be suspended until the suspension is turned off
(unless they are exempt as described in the [Suspend](Suspend.htm)
section).

The [keyboard](InstallKeybdHook.htm) and/or
[mouse](InstallMouseHook.htm) hooks will be installed or removed if
justified by the changes made by this function.

This function cannot directly enable or disable hotstrings in scripts
other than its own.

Once a script has at least one hotstring, it becomes
[persistent](../Scripts.htm#persistent), meaning that
[ExitApp](ExitApp.htm) rather than [Exit](Exit.htm) should be used to
terminate it.

## Variant (Duplicate) Hotstrings {#variant}

A particular hotstring can be created more than once if each definition
has different [HotIf](HotIf.htm) criteria,
[case-sensitivity](../Hotstrings.htm#C) (`C` vs. `C0`/`C1`), or
[word-sensitivity](../Hotstrings.htm#Question) (`?`). These are known as
*hotstring variants*. For example:

    HotIfWinActive "ahk_group CarForums"
    Hotstring "::btw", "behind the wheel"
    HotIfWinActive "Inter-Office Chat"
    Hotstring "::btw", "back to work"
    HotIfWinActive
    Hotstring "::btw", "by the way"

If more than one variant of a hotstring is eligible to fire, only the
one created earliest will fire.

For more information, see [HotIf](HotIf.htm).

## Related {#Related}

[Hotstrings](../Hotstrings.htm), [HotIf](HotIf.htm),
[A_ThisHotkey](../Variables.htm#ThisHotkey),
[#MaxThreadsPerHotkey](_MaxThreadsPerHotkey.htm),
[Suspend](Suspend.htm), [Threads](../misc/Threads.htm),
[Thread](Thread.htm), [Critical](Critical.htm), [Hotkey
function](Hotkey.htm)

## Examples {#Examples}

::: {#ExHelper .ex}
[](#ExHelper){.ex_number} Hotstring Helper. The following script might
be useful if you are a heavy user of hotstrings. It\'s based on the v1
script created by Andreas Borutta. By pressing [Win]{.kbd}+[H]{.kbd} (or
another hotkey of your choice), the currently selected text can be
turned into a hotstring. For example, if you have \"by the way\"
selected in a word processor, pressing [Win]{.kbd}+[H]{.kbd} will prompt
you for its abbreviation (e.g. btw), add the new hotstring to the script
and activate it.

    #h::  ; Win+H hotkey
    {
        ; Get the text currently selected. The clipboard is used instead of
        ; EditGetSelectedText because it works in a greater variety of editors
        ; (namely word processors). Save the current clipboard contents to be
        ; restored later. Although this handles only plain text, it seems better
        ; than nothing:
        ClipboardOld := A_Clipboard
        A_Clipboard := "" ; Must start off blank for detection to work.
        Send "^c"
        if !ClipWait(1)  ; ClipWait timed out.
        {
            A_Clipboard := ClipboardOld ; Restore previous contents of clipboard before returning.
            return
        }
        ; Replace CRLF and/or LF with `n for use in a "send-raw" hotstring:
        ; The same is done for any other characters that might otherwise
        ; be a problem in raw mode:
        ClipContent := StrReplace(A_Clipboard, "``", "````")  ; Do this replacement first to avoid interfering with the others below.
        ClipContent := StrReplace(ClipContent, "`r`n", "``n")
        ClipContent := StrReplace(ClipContent, "`n", "``n")
        ClipContent := StrReplace(ClipContent, "`t", "``t")
        ClipContent := StrReplace(ClipContent, "`;", "```;")
        A_Clipboard := ClipboardOld  ; Restore previous contents of clipboard.
        ShowInputBox(":T:::" ClipContent)
    }

    ShowInputBox(DefaultValue)
    {
        ; This will move the input box's caret to a more friendly position:
        SetTimer MoveCaret, 10
        ; Show the input box, providing the default hotstring:
        IB := InputBox("
        (
        Type your abbreviation at the indicated insertion point. You can also edit the replacement text if you wish.

        Example entry: :T:btw::by the way
        )", "New Hotstring",, DefaultValue)
        if IB.Result = "Cancel"  ; The user pressed Cancel.
            return

        if RegExMatch(IB.Value, "(?P<Label>:.*?:(?P<Abbreviation>.*?))::(?P<Replacement>.*)", &Entered)
        {
            if !Entered.Abbreviation
                MsgText := "You didn't provide an abbreviation"
            else if !Entered.Replacement
                MsgText := "You didn't provide a replacement"
            else
            {
                Hotstring Entered.Label, Entered.Replacement  ; Enable the hotstring now.
                FileAppend "`n" IB.Value, A_ScriptFullPath  ; Save the hotstring for later use.
            }
        }
        else
            MsgText := "The hotstring appears to be improperly formatted"

        if IsSet(MsgText)
        {
            Result := MsgBox(MsgText ". Would you like to try again?",, 4)
            if Result = "Yes"
                ShowInputBox(DefaultValue)
        }
        
        MoveCaret()
        {
            WinWait "New Hotstring"
            ; Otherwise, move the input box's insertion point to where the user will type the abbreviation.
            Send "{Home}{Right 3}"
            SetTimer , 0
        }
    }
:::
