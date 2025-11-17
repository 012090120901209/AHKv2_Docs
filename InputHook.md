# InputHook

Creates an object which can be used to collect or intercept keyboard
input.

``` Syntax
InputHookObj := InputHook(Options, EndKeys, MatchList)
```

## Parameters {#Parameters}

Options

:   Type: [String](../Concepts.htm#strings)

    A string of zero or more of the following options (in any order,
    with optional spaces in between):

    **B:** Sets [BackspaceIsUndo](#BackspaceIsUndo) to 0 (false), which
    causes [Backspace]{.kbd} to be ignored.

    **C:** Sets [CaseSensitive](#CaseSensitive) to 1 (true), making
    *MatchList* case-sensitive.

    **I:** Sets [MinSendLevel](#MinSendLevel) to 1 or a given value,
    causing any input with [send level](SendLevel.htm) below this value
    to be ignored. For example, `I2` would ignore any input with a level
    of 0 (the default) or 1, but would capture input at level 2.

    **L:** Length limit (e.g. `L5`). The maximum allowed length of the
    input. When the text reaches this length, the Input is terminated
    and [EndReason](#EndReason) is set to the word Max (unless the text
    matches one of the *MatchList* phrases, in which case
    [EndReason](#EndReason) is set to the word Match). If unspecified,
    the length limit is 1023.

    Specifying `L0` disables collection of text and the length limit,
    but does not affect which keys are counted as producing text (see
    [VisibleText](#VisibleText)). This can be useful in combination with
    [OnChar](#OnChar), [OnKeyDown](#OnKeyDown), [KeyOpt](#KeyOpt) or the
    *EndKeys* parameter.

    **M:** Allows a greater range of modified keypresses to produce
    text. Normally, a key is treated as non-text if it is modified by
    any combination *other than* [Shift]{.kbd}, [Ctrl]{.kbd}+[Alt]{.kbd}
    (i.e. [AltGr]{.kbd}) or [Ctrl]{.kbd}+[Alt]{.kbd}+[Shift]{.kbd} (i.e.
    [AltGr]{.kbd}+[Shift]{.kbd}). This option causes translation to be
    attempted for other combinations of modifiers. Consider this
    example, which typically recognizes [Ctrl]{.kbd}+[C]{.kbd}:

        CtrlC := Chr(3) ; Store the character for Ctrl-C in the CtrlC var.
        ih := InputHook("L1 M")
        ih.Start()
        ih.Wait()
        if (ih.Input = CtrlC)
            MsgBox "You pressed Control-C."

    By default, the system maps [Ctrl]{.kbd}+[A]{.kbd} through
    [Ctrl]{.kbd}+[Z]{.kbd} to ASCII control characters [Chr(1)](Chr.htm)
    through [Chr(26)](Chr.htm). Other translations may be defined by the
    system or the active window\'s keyboard layout. Translation may
    ignore any modifier key for which the keyboard layout does not
    define a modifier bitmask. For example, [Win]{.kbd}+[E]{.kbd}
    typically transcribes to \"e\" if the M option is used.

    The M option might cause some keyboard shortcuts such as
    [Ctrl]{.kbd}+[←]{.kbd} to misbehave while an Input is in progress.

    **T:** Sets [Timeout](#Timeout) (e.g. `T3` or
    `T2.5`{.no-highlight}).

    **V:** Sets [VisibleText](#VisibleText) and
    [VisibleNonText](#VisibleNonText) to 1 (true). Normally, the user\'s
    input is blocked (hidden from the system). Use this option to have
    the user\'s keystrokes sent to the active window.

    **\*:** Wildcard. Sets [FindAnywhere](#FindAnywhere) to 1 (true),
    allowing matches to be found anywhere within what the user types.

    **E:** Handle single-character end keys by character code instead of
    by keycode. This provides more consistent results if the active
    window\'s keyboard layout is different to the script\'s keyboard
    layout. It also prevents key combinations which don\'t actually
    produce the given end characters from ending input; for example, if
    @ is an end key, on the US layout [Shift]{.kbd}+[2]{.kbd} will
    trigger it but [Ctrl]{.kbd}+[Shift]{.kbd}+[2]{.kbd} will not (if the
    [E option](#E) is used). If the [C option](#option-c) is also used,
    the end character is case-sensitive.

EndKeys

:   Type: [String](../Concepts.htm#strings)

    A list of zero or more keys, any one of which terminates the Input
    when pressed (the end key itself is not written to the Input
    buffer). When an Input is terminated this way,
    [EndReason](#EndReason) is set to the word EndKey and
    [EndKey](#EndKey) is set to the name of the key.

    *EndKeys* uses a format similar to the [Send](Send.htm) function.
    For example, specifying `{Enter}.{Esc}` would cause either
    [Enter]{.kbd}, [.]{.kbd}, or [Esc]{.kbd} to terminate the Input. To
    use the braces themselves as end keys, specify `{ {` and/or `} }`.

    To use [Ctrl]{.kbd}, [Alt]{.kbd}, or [Shift]{.kbd} as end keys,
    specify the left and/or right version of the key, not the neutral
    version. For example, specify `{LControl}{RControl}` rather than
    `{Control}`.

    Although modified keys such as [Alt]{.kbd}+[C]{.kbd} (!c) are not
    supported, non-alphanumeric characters such as `?!:@&{}` by default
    require [Shift]{.kbd} or [AltGr]{.kbd} to be pressed or not pressed
    depending on how the character is normally typed. If the [E
    option](#E) is present, single character key names are interpreted
    as characters instead, and in those cases the modifier keys must be
    in the correct state to produce that character. When both the [E
    option](#E) and [M option](#option-m) are used,
    [Ctrl]{.kbd}+[A]{.kbd} through [Ctrl]{.kbd}+[Z]{.kbd} are supported
    by including the corresponding ASCII control characters in
    *EndKeys*.

    An explicit key code such as `{vkFF}` or `{sc001}` may also be
    specified. This is useful in the rare case where a key has no name
    and produces no visible character when pressed. Its key code can be
    determined by following the steps at the bottom of the [key list
    page](../KeyList.htm#SpecialKeys).

MatchList

:   Type: [String](../Concepts.htm#strings)

    A comma-separated list of key phrases, any of which will cause the
    Input to be terminated (in which case [EndReason](#EndReason) will
    be set to the word Match). The entirety of what the user types must
    exactly match one of the phrases for a match to occur (unless the
    [\* option](#asterisk) is present). In addition, **any spaces or
    tabs around the delimiting commas are significant**, meaning that
    they are part of the match string. For example, if *MatchList* is
    `ABC , XYZ`, the user must type a space after ABC or before XYZ to
    cause a match.

    Two consecutive commas results in a single literal comma. For
    example, the following would produce a single literal comma at the
    end of string1: `string1,,,string2`. Similarly, the following list
    contains only a single item with a literal comma inside it:
    `single,,item`.

    Because the items in *MatchList* are not treated as individual
    parameters, the list can be contained entirely within a variable.
    For example, *MatchList* might consist of
    `List1 "," List2 "," List3` \-- where each of the variables contains
    a large sub-list of match phrases.

## Input Stack {#stack}

Any number of InputHook objects can be created and in progress at any
time, but the order in which they are started affects how input is
collected.

When each Input is started (by the [Start](#Start) method), it is pushed
onto the top of a stack, and is removed from this stack only when the
Input is terminated. Keyboard events are passed to each Input in order
of most recently started to least. If an Input suppresses a given
keyboard event, it is passed no further down the stack.

[Sent](Send.htm) keystrokes are ignored if the [send
level](SendLevel.htm) of the keystroke is below the InputHook\'s
[MinSendLevel](#MinSendLevel). In such cases, the keystroke may still be
processed by an Input lower on the stack.

Multiple InputHooks can be used in combination with
[MinSendLevel](#MinSendLevel) to separately collect both sent keystrokes
and real ones.

## InputHook Object {#object}

The InputHook function returns an InputHook object, which has the
following methods and properties.

\"InputHookObj\" is used below as a placeholder for any InputHook
object, as \"InputHook\" is the class itself.

-   [Methods](#Methods):
    -   [KeyOpt](#KeyOpt): Sets options for a key or list of keys.
    -   [Start](#Start): Starts collecting input.
    -   [Stop](#Stop): Terminates the Input and sets EndReason to the
        word Stopped.
    -   [Wait](#Wait): Waits until the Input is terminated (InProgress
        is false).
-   [General Properties](#General_Properties):
    -   [EndKey](#EndKey): Returns the name of the end key which was
        pressed to terminate the Input.
    -   [EndMods](#EndMods): Returns a string of the modifiers which
        were logically down when Input was terminated.
    -   [EndReason](#EndReason): Returns an EndReason string indicating
        how Input was terminated.
    -   [InProgress](#InProgress): Returns 1 (true) if the Input is in
        progress, otherwise 0 (false).
    -   [Input](#Input): Returns any text collected since the last time
        Input was started.
    -   [Match](#Match): Returns the *MatchList* item which caused the
        Input to terminate.
    -   [OnEnd](#OnEnd): Retrieves or sets the function object which is
        called when Input is terminated.
    -   [OnChar](#OnChar): Retrieves or sets the function object which
        is called after a character is added to the input buffer.
    -   [OnKeyDown](#OnKeyDown): Retrieves or sets the function object
        which is called when a notification-enabled key is pressed.
    -   [OnKeyUp](#OnKeyUp): Retrieves or sets the function object which
        is called when a notification-enabled key is released.
-   [Option Properties](#Option_Properties):
    -   [BackspaceIsUndo](#BackspaceIsUndo): Controls whether the
        Backspace key removes the most recently pressed character from
        the end of the Input buffer.
    -   [CaseSensitive](#CaseSensitive): Controls whether *MatchList* is
        case-sensitive.
    -   [FindAnywhere](#FindAnywhere): Controls whether each match can
        be a substring of the input text.
    -   [MinSendLevel](#MinSendLevel): Retrieves or sets the minimum
        send level of input to collect.
    -   [NotifyNonText](#NotifyNonText): Controls whether the OnKeyDown
        and OnKeyUp callbacks are called whenever a non-text key is
        pressed.
    -   [Timeout](#Timeout): Retrieves or sets the timeout value in
        seconds.
    -   [VisibleNonText](#VisibleNonText): Controls whether keys or key
        combinations which do not produce text are visible (not
        blocked).
    -   [VisibleText](#VisibleText): Controls whether keys or key
        combinations which produce text are visible (not blocked).

### Methods {#Methods}

::: {#KeyOpt .methodShort}
### KeyOpt

Sets options for a key or list of keys.

``` Syntax
InputHookObj.KeyOpt(Keys, KeyOptions)
```

#### Parameters {#KeyOpt_Parameters}

Keys

:   Type: [String](../Concepts.htm#strings)

    A list of keys. Braces are used to enclose key names, virtual key
    codes or scan codes, similar to the [Send](Send.htm) function. For
    example, `{Enter}.{ {` would apply to [Enter]{.kbd}, [.]{.kbd} and
    [{]{.kbd}. Specifying a key by name, by `{vkNN}` or by `{scNNN}` may
    produce three different results; see below for details.

    Specify the string `{All}` (case-insensitive) on its own to apply
    *KeyOptions* to all VK and all SC, including `{vkE7}` and `{sc000}`
    as described below. KeyOpt may then be called a second time to
    remove options from specific keys.

    Specify `{sc000}` to apply *KeyOptions* to all events which lack a
    scan code.

    Specify `{vkE7}` to apply *KeyOptions* to Unicode events, such as
    those sent by `SendEvent "{U+221e}"` or `SendEvent "{Text}∞"`.

KeyOptions

:   Type: [String](../Concepts.htm#strings)

    One or more of the following single-character options (spaces and
    tabs are ignored).

    **-** (minus): Removes any of the options following the `-`, up to
    the next `+`.

    **+** (plus): Cancels any previous `-`, otherwise has no effect.

    **E:** End key. If enabled, pressing the key terminates Input, sets
    [EndReason](#EndReason) to the word EndKey and [EndKey](#EndKey) to
    the key\'s normalized name. Unlike the *EndKeys* parameter, the
    state of [Shift]{.kbd} or [AltGr]{.kbd} is ignored. For example, `@`
    and `2`{.no-highlight} are both equivalent to `{vk32}` on the US
    keyboard layout.

    **I:** Ignore text. Any text normally produced by this key is
    ignored, and the key is treated as a non-text key (see
    [VisibleNonText](#VisibleNonText)). Has no effect if the key
    normally does not produce text.

    **N:** Notify. Causes the [OnKeyDown](#OnKeyDown) and
    [OnKeyUp](#OnKeyUp) callbacks to be called each time the key is
    pressed.

    **S:** Suppresses (blocks) the key after processing it. This
    overrides [VisibleText](#VisibleText) or
    [VisibleNonText](#VisibleNonText) until `-S` is used. `+S` implies
    `-V`.

    **V:** Visible. Prevents the key from being suppressed (blocked).
    This overrides [VisibleText](#VisibleText) or
    [VisibleNonText](#VisibleNonText) until `-V` is used. `+V` implies
    `-S`.

#### Remarks {#KeyOpt_Remarks}

Options can be set by both virtual key code (VK) and scan code (SC), and
are accumulative.

When a key is specified by name, options are added either by VK or by
SC. Where two physical keys share the same VK but differ by SC (such as
[Up]{.kbd} and [NumpadUp]{.kbd}), they are handled by SC. By contrast,
if a VK number is used, it will apply to any physical key which produces
that VK (and this may vary over time as it depends on the active
keyboard layout).

Removing an option by VK number does not affect any options that were
set by SC, or vice versa. However, when an option is removed by key name
and that name is handled by VK, the option is also removed for the
corresponding SC (according to the script\'s keyboard layout). This
allows keys to be excluded by name after applying an option to [all
keys](#all-keys).

To prevent an option from affecting a key, the option must be removed
from both the VK and the SC of that key, or sc000 if the key has no SC.

Unicode events, such as those sent by `SendEvent "{U+221e}"` or
`SendEvent "{Text}∞"`, are affected by options which have been set for
either [vkE7](#vke7) or [sc000](#sc000). Any option applied to
[{All}](#all-keys) is applied to both vkE7 and sc000, so to exclude
Unicode events, remove the option from both. For example:

    InputHookObj.KeyOpt("{All}", "+I")  ; Ignore text produced by any event
    InputHookObj.KeyOpt("{vkE7}{sc000}", "-I")  ; except Unicode events.
:::

::: {#Start .methodShort}
### Start

Starts collecting input.

``` Syntax
InputHookObj.Start()
```

Has no effect if the Input is already in progress.

The newly started Input is placed on the top of the [InputHook
stack](#stack), which allows it to override any previously started
Input.

This method installs the [keyboard hook](InstallKeybdHook.htm) (if it
was not already).
:::

::: {#Stop .methodShort}
### Stop

Terminates the Input and sets [EndReason](#EndReason) to the word
Stopped.

``` Syntax
InputHookObj.Stop()
```

Has no effect if the Input is not in progress.
:::

::: {#Wait .methodShort}
### Wait

Waits until the Input is terminated ([InProgress](#InProgress) is
false).

``` Syntax
EndReason := InputHookObj.Wait(MaxTime)
```

#### Parameters {#Wait_Parameters}

MaxTime

:   Type: [Float](../Concepts.htm#numbers)

    If omitted, the wait is indefinitely. Otherwise, specify the maximum
    number of seconds to wait. If Input is still in progress after
    *MaxTime* seconds, the method returns and does not terminate Input.

#### Return Value {#Wait_Return_Value}

Type: [String](../Concepts.htm#strings)

This method returns [EndReason](#EndReason).
:::

### General Properties {#General_Properties}

::: {#EndKey .methodShort}
### EndKey

Returns the name of the [end key](#EndKeys) which was pressed to
terminate the Input.

``` Syntax
KeyName := InputHookObj.EndKey
```

Note that EndKey returns the \"normalized\" name of the key regardless
of how it was written in the *EndKeys* parameter. For example, `{Esc}`
and `{vk1B}` both produce `Escape`. [GetKeyName](GetKeyName.htm) can be
used to retrieve the normalized name.

If the [E option](#E) was used, EndKey returns the actual character
which was typed (if applicable). Otherwise, the key name is determined
according to the script\'s active keyboard layout.

EndKey returns an empty string if [EndReason](#EndReason) is not
\"EndKey\".
:::

::: {#EndMods .methodShort}
### EndMods

Returns a string of the modifiers which were logically down when Input
was terminated.

``` Syntax
Mods := InputHookObj.EndMods
```

If all modifiers were logically down (pressed), the full string is:

    <^>^<!>!<+>+<#>#

These modifiers have the same meaning as with [hotkeys](../Hotkeys.htm).
Each modifier is always qualified with \< (left) or \> (right). The
corresponding key names are: LCtrl, RCtrl, LAlt, RAlt, LShift, RShift,
LWin, RWin.

[InStr](InStr.htm) can be used to check whether a given modifier (such
as `>!` or `^`) is present. The following line can be used to convert
*Mods* to a string of neutral modifiers, such as `^!+#`:

    Mods := RegExReplace(Mods, "[<>](.)(?:>\1)?", "$1")

Due to split-second timing, this property may be more reliable than
[GetKeyState](GetKeyState.htm) even if it is used immediately after
Input terminates, or in the [OnEnd](#OnEnd) callback.
:::

::: {#EndReason .methodShort}
### EndReason

Returns an [EndReason string](#EndReasons) indicating how Input was
terminated.

``` Syntax
Reason := InputHookObj.EndReason
```

If the Input is still in progress, an empty string is returned.
:::

::: {#InProgress .methodShort}
### InProgress

Returns 1 (true) if the Input is in progress, otherwise 0 (false).

``` Syntax
Boolean := InputHookObj.InProgress
```
:::

::: {#Input .methodShort}
### Input

Returns any text collected since the last time Input was started.

``` Syntax
String := InputHookObj.Input
```

This property can be used while the Input is in progress, or after it
has ended.
:::

::: {#Match .methodShort}
### Match

Returns the *[MatchList](#MatchList)* item which caused the Input to
terminate.

``` Syntax
String := InputHookObj.Match
```

This property returns the matched item with its original case, which may
differ from what the user typed if the [C option](#option-c) was
omitted, or an empty string if [EndReason](#EndReason) is not \"Match\".
:::

::: {#OnEnd .methodShort}
### OnEnd

Retrieves or sets the [function object](../misc/Functor.htm) which is
called when Input is terminated.

``` Syntax
MyCallback := InputHookObj.OnEnd
```

``` Syntax
InputHookObj.OnEnd := MyCallback
```

*MyCallback* is the [function object](../misc/Functor.htm) to call. An
empty string means no function object.

The callback accepts one parameter and can be
[defined](../Functions.htm#intro) as follows:

``` NoIndent
MyCallback(InputHookObj) { ...
```

Although the name you give the parameter does not matter, it is assigned
a reference to the InputHook object.

You can omit the callback\'s parameter if the corresponding information
is not needed, but in this case an asterisk must be specified, e.g.
`MyCallback(*)`.

The function is called as a new [thread](../misc/Threads.htm), so starts
off fresh with the default values for settings such as
[SendMode](SendMode.htm) and
[DetectHiddenWindows](DetectHiddenWindows.htm).
:::

::: {#OnChar .methodShort}
### OnChar

Retrieves or sets the [function object](../misc/Functor.htm) which is
called after a character is added to the input buffer.

``` Syntax
MyCallback := InputHookObj.OnChar
```

``` Syntax
InputHookObj.OnChar := MyCallback
```

*MyCallback* is the [function object](../misc/Functor.htm) to call. An
empty string means no function object.

The callback accepts two parameters and can be
[defined](../Functions.htm#intro) as follows:

``` NoIndent
MyCallback(InputHookObj, Char) { ...
```

Although the names you give the parameters do not matter, the following
values are sequentially assigned to them:

1.  A reference to the InputHook object.
2.  A string containing the character (or multiple characters, see below
    for details).

You can omit one or more parameters from the end of the callback\'s
parameter list if the corresponding information is not needed, but in
this case an asterisk must be specified as the final parameter, e.g.
`MyCallback(Param1, *)`.

The presence of multiple characters indicates that a dead key was used
prior to the last keypress, but the two keys could not be transliterated
to a single character. For example, on some keyboard layouts
[\`]{.kbd}[e]{.kbd} produces `è` while [\`]{.kbd}[z]{.kbd} produces
`` `z ``.

The function is never called when an end key is pressed.
:::

::: {#OnKeyDown .methodShort}
### OnKeyDown

Retrieves or sets the [function object](../misc/Functor.htm) which is
called when a notification-enabled key is pressed.

``` Syntax
MyCallback := InputHookObj.OnKeyDown
```

``` Syntax
InputHookObj.OnKeyDown := MyCallback
```

Key-down notifications must first be enabled by [KeyOpt](#KeyOpt) or
[NotifyNonText](#NotifyNonText).

*MyCallback* is the [function object](../misc/Functor.htm) to call. An
empty string means no function object.

The callback accepts three parameters and can be
[defined](../Functions.htm#intro) as follows:

``` NoIndent
MyCallback(InputHookObj, VK, SC) { ...
```

Although the names you give the parameters do not matter, the following
values are sequentially assigned to them:

1.  A reference to the InputHook object.
2.  An integer representing the virtual key code of the key.
3.  An integer representing the scan code of the key.

You can omit one or more parameters from the end of the callback\'s
parameter list if the corresponding information is not needed, but in
this case an asterisk must be specified as the final parameter, e.g.
`MyCallback(Param1, *)`.

To retrieve the key name (if any), use
`GetKeyName(Format("vk{:x}sc{:x}", VK, SC))`.

The function is called as a new [thread](../misc/Threads.htm), so starts
off fresh with the default values for settings such as
[SendMode](SendMode.htm) and
[DetectHiddenWindows](DetectHiddenWindows.htm).

The function is never called when an end key is pressed.
:::

::: {#OnKeyUp .methodShort}
### OnKeyUp

Retrieves or sets the [function object](../misc/Functor.htm) which is
called when a notification-enabled key is released.

``` Syntax
MyCallback := InputHookObj.OnKeyUp
```

``` Syntax
InputHookObj.OnKeyUp := MyCallback
```

Key-up notifications must first be enabled by [KeyOpt](#KeyOpt) or
[NotifyNonText](#NotifyNonText). Whether a key is considered text or
non-text is determined when the key is pressed. If an InputHook detects
a key-up without having detected key-down, it is considered non-text.

*MyCallback* is the [function object](../misc/Functor.htm) to call. An
empty string means no function object.

The callback accepts three parameters and can be
[defined](../Functions.htm#intro) as follows:

``` NoIndent
MyCallback(InputHookObj, VK, SC) { ...
```

Although the names you give the parameters do not matter, the following
values are sequentially assigned to them:

1.  A reference to the InputHook object.
2.  An integer representing the virtual key code of the key.
3.  An integer representing the scan code of the key.

You can omit one or more parameters from the end of the callback\'s
parameter list if the corresponding information is not needed, but in
this case an asterisk must be specified as the final parameter, e.g.
`MyCallback(Param1, *)`.

To retrieve the key name (if any), use
`GetKeyName(Format("vk{:x}sc{:x}", VK, SC))`.

The function is called as a new [thread](../misc/Threads.htm), so starts
off fresh with the default values for settings such as
[SendMode](SendMode.htm) and
[DetectHiddenWindows](DetectHiddenWindows.htm).
:::

### Option Properties {#Option_Properties}

::: {#BackspaceIsUndo .methodShort}
### BackspaceIsUndo

Controls whether [Backspace]{.kbd} removes the most recently pressed
character from the end of the Input buffer.

``` Syntax
CurrentSetting := InputHookObj.BackspaceIsUndo
```

``` Syntax
InputHookObj.BackspaceIsUndo := NewSetting
```

*CurrentSetting* is *NewSetting* if assigned, otherwise 1 (true) by
default unless overwritten by the [B option](#option-b).

*NewSetting* is a [boolean value](../Concepts.htm#boolean) that enables
or disables this setting.

When [Backspace]{.kbd} acts as undo, it is treated as a text entry key.
Specifically, whether the key is suppressed depends on
[VisibleText](#VisibleText) rather than
[VisibleNonText](#VisibleNonText).

[Backspace]{.kbd} is always ignored if pressed in combination with a
modifier key such as [Ctrl]{.kbd} (the logical modifier state is checked
rather than the physical state).

**Note:** If the input text is visible (such as in an editor) and the
arrow keys or other means are used to navigate within it,
[Backspace]{.kbd} will still remove the last character rather than the
one behind the caret (insertion point).
:::

::: {#CaseSensitive .methodShort}
### CaseSensitive

Controls whether [*MatchList*](#MatchList) is case-sensitive.

``` Syntax
CurrentSetting := InputHookObj.CaseSensitive
```

``` Syntax
InputHookObj.CaseSensitive := NewSetting
```

*CurrentSetting* is *NewSetting* if assigned, otherwise 0 (false) by
default unless overwritten by the [C option](#option-c).

*NewSetting* is a [boolean value](../Concepts.htm#boolean) that enables
or disables this setting.
:::

::: {#FindAnywhere .methodShort}
### FindAnywhere

Controls whether each match can be a substring of the input text.

``` Syntax
CurrentSetting := InputHookObj.FindAnywhere
```

``` Syntax
InputHookObj.FindAnywhere := NewSetting
```

*CurrentSetting* is *NewSetting* if assigned, otherwise 0 (false) by
default unless overwritten by the [\* option](#asterisk).

*NewSetting* is a [boolean value](../Concepts.htm#boolean) that enables
or disables this setting. If true, a match can be found anywhere within
what the user types (the match can be a substring of the input text). If
false, the entirety of what the user types must match one of the
*MatchList* phrases. In both cases, one of the *MatchList* phrases must
be typed in full.
:::

::: {#MinSendLevel .methodShort}
### MinSendLevel

Retrieves or sets the minimum [send level](SendLevel.htm) of input to
collect.

``` Syntax
CurrentLevel := InputHookObj.MinSendLevel
```

``` Syntax
InputHookObj.MinSendLevel := NewLevel
```

*CurrentLevel* is *NewLevel* if assigned, otherwise 0 by default unless
overwritten by the [I option](#option-i).

*NewLevel* should be an [integer](../Concepts.htm#numbers) between 0 and
101. Events which have a send level [lower]{.underline} than this value
are ignored. For example, a value of 101 causes all input generated by
[SendEvent](Send.htm) to be ignored, while a value of 1 only ignores
input at the default send level (zero).

The [SendInput](Send.htm#SendInput) and [SendPlay](Send.htm#SendPlay)
methods are always ignored, regardless of this setting. Input generated
by any source other than AutoHotkey is never ignored as a result of this
setting.
:::

::: {#NotifyNonText .methodShort}
### NotifyNonText

Controls whether the [OnKeyDown](#OnKeyDown) and [OnKeyUp](#OnKeyUp)
callbacks are called whenever a non-text key is pressed.

``` Syntax
CurrentSetting := InputHookObj.NotifyNonText
```

``` Syntax
InputHookObj.NotifyNonText := NewSetting
```

*CurrentSetting* is *NewSetting* if assigned, otherwise 0 (false) by
default.

*NewSetting* is a [boolean value](../Concepts.htm#boolean) that enables
or disables this setting. If true, notifications are enabled for all
keypresses which do not produce text, such as when pressing [←]{.kbd} or
[Alt]{.kbd}+[F]{.kbd}. Setting this property does not affect a key\'s
[options](#KeyOpt), since the production of text depends on the active
window\'s keyboard layout at the time the key is pressed.

NotifyNonText is applied to key-up events by considering whether a
previous key-down with a matching VK code was classified as text or
non-text. For example, if NotifyNonText is true, pressing
[Ctrl]{.kbd}+[A]{.kbd} will produce [OnKeyDown](#OnKeyDown) and
[OnKeyUp](#OnKeyUp) calls for both [Ctrl]{.kbd} and [A]{.kbd}, while
pressing [A]{.kbd} on its own will not call OnKeyDown or OnKeyUp unless
[KeyOpt](#KeyOpt) has been used to enable notifications for that key.

See [VisibleText](#VisibleText) for details about which keys are counted
as producing text.
:::

::: {#Timeout .methodShort}
### Timeout

Retrieves or sets the timeout value in seconds.

``` Syntax
CurrentSeconds := InputHookObj.Timeout
```

``` Syntax
InputHookObj.Timeout := NewSeconds
```

*CurrentSeconds* is *NewSeconds* if assigned, otherwise 0 by default
unless overwritten by the [T option](#option-t).

*NewSeconds* is a [floating-point number](../Concepts.htm#numbers)
representing the timeout. 0 means no timeout.

The timeout period ordinarily starts when [Start](#Start) is called, but
will restart if this property is assigned a value while Input is in
progress. If Input is still in progress when the timeout period elapses,
it is terminated and [EndReason](#EndReason) is set to the word Timeout.
:::

::: {#VisibleNonText .methodShort}
### VisibleNonText

Controls whether keys or key combinations which do not produce text are
visible (not blocked).

``` Syntax
CurrentSetting := InputHookObj.VisibleNonText
```

``` Syntax
InputHookObj.VisibleNonText := NewSetting
```

*CurrentSetting* is *NewSetting* if assigned, otherwise 1 (true) by
default. The [V option](#vis) sets this to 1 (true).

*NewSetting* is a [boolean value](../Concepts.htm#boolean) that enables
or disables this setting. If true, keys and key combinations which do
not produce text may trigger hotkeys or be passed on to the active
window. If false, they are blocked.

See [VisibleText](#VisibleText) for details about which keys are counted
as producing text.
:::

::: {#VisibleText .methodShort}
### VisibleText

Controls whether keys or key combinations which produce text are visible
(not blocked).

``` Syntax
CurrentSetting := InputHookObj.VisibleText
```

``` Syntax
InputHookObj.VisibleText := NewSetting
```

*CurrentSetting* is *NewSetting* if assigned, otherwise 0 (false) by
default unless overwritten by the [V option](#vis).

*NewSetting* is a [boolean value](../Concepts.htm#boolean) that enables
or disables this setting. If true, keys and key combinations which
produce text may trigger hotkeys or be passed on to the active window.
If false, they are blocked.

Any keystrokes which cause text to be appended to the Input buffer are
counted as producing text, even if they do not normally do so in other
applications. For instance, [Ctrl]{.kbd}+[A]{.kbd} produces text if the
[M option](#option-m) is used, and [Esc]{.kbd} produces the control
character `Chr(27)`.

Dead keys are counted as producing text, although they do not typically
produce an immediate effect. Pressing a dead key might also cause the
following key to produce text (if only the dead key\'s character).

[Backspace]{.kbd} is counted as producing text only when it [acts as
undo](#BackspaceIsUndo).

The [standard modifier keys](../KeyList.htm#modifier) and
[CapsLock]{.kbd}, [NumLock]{.kbd} and [ScrollLock]{.kbd} are always
visible (not blocked).
:::

## EndReason {#EndReasons}

The [EndReason](#EndReason) property returns one of the following
strings:

  String    Description
  --------- --------------------------------------------------------------------------------------------------------------------------------------------------------
  Stopped   The [Stop](#Stop) method was called or the [Start](#Start) method has not yet been called for the first time.
  Max       The Input reached the maximum allowed length and it does not match any of the items in [*MatchList*](#MatchList).
  Timeout   The Input timed out.
  Match     The Input matches one of the items in [*MatchList*](#MatchList). The [Match](#Match) property contains the matched item.
  EndKey    One of the *EndKeys* was pressed to terminate the Input. The [EndKey](#EndKey) property contains the terminating key name or character without braces.
            If the Input is in progress, EndReason is blank.

## Remarks {#Remarks}

The [Start](#Start) method must be called before input will be
collected.

InputHook is designed to allow different parts of the script to monitor
input, with minimal conflicts. It can operate continuously, such as to
watch for [arbitrary words](#ExSac) or other patterns. It can also
operate temporarily, such as to collect user input or temporarily
override specific (or [non-specific](#ExKeyWaitAny)) keys without
interfering with hotkeys.

Keyboard [hotkeys](../Hotkeys.htm) are still in effect while an Input is
in progress, but cannot activate if any of the required modifier keys
are suppressed, or if the hotkey uses the *reg* method and its suffix
key is suppressed. For example, the hotkey `^+a::` *might* be overridden
by InputHook, whereas the hotkey `$^+a::` would take priority unless the
InputHook suppressed [Ctrl]{.kbd} or [Shift]{.kbd}.

Keys are either suppressed (blocked) or not depending on the following
factors (in order):

-   If the [V option](#KeyOpt-v) is in effect for this VK or SC, it is
    not suppressed.
-   If the [S option](#KeyOpt-s) is in effect for this VK or SC, it is
    suppressed.
-   If the key is a [standard modifier key](../KeyList.htm#modifier) or
    [CapsLock]{.kbd}, [NumLock]{.kbd} or [ScrollLock]{.kbd}, it is not
    suppressed.
-   [VisibleText](#VisibleText) or [VisibleNonText](#VisibleNonText) is
    consulted, depending on whether the key produces text. If the
    property is 0 (false), the key is suppressed. See
    [VisibleText](#VisibleText) for details about which keys are counted
    as producing text.

The [keyboard hook](InstallKeybdHook.htm) is required while an Input is
in progress, but will be uninstalled automatically if it is no longer
needed when the Input is terminated.

The script is [automatically persistent](../Scripts.htm#persistent)
while an Input is in progress, so it will continue monitoring input even
if there are no running [threads](../misc/Threads.htm). The script may
exit automatically when input ends (if there are no running threads and
the script is not persistent for some other reason).

AutoHotkey does not support Input Method Editors (IME). The keyboard
hook intercepts keyboard events and translates them to text by using
[ToUnicodeEx](https://learn.microsoft.com/windows/win32/api/winuser/nf-winuser-tounicodeex)
or ToAsciiEx (except in the case of
[VK_PACKET](https://learn.microsoft.com/windows/win32/inputdev/virtual-key-codes#vk_packet)
events, which encapsulate a single character).

If you use multiple languages or keyboard layouts, InputHook uses the
keyboard layout of the active window rather than the script\'s
(regardless of whether the Input is [visible](#vis)).

Although not as flexible, [hotstrings](../Hotstrings.htm) are generally
easier to use.

## InputHook vs. Input (v1) {#comparison}

In AutoHotkey v1.1, InputHook is a replacement for the Input command,
offering greater flexbility. The Input command was removed for v2.0, but
the code below is mostly equivalent:

    ; Input OutputVar, % Options, % EndKeys, % MatchList  ; v1
    ih := InputHook(Options, EndKeys, MatchList)
    ih.Start()
    ErrorLevel := ih.Wait()
    if (ErrorLevel = "EndKey")
        ErrorLevel .= ":" ih.EndKey
    OutputVar := ih.Input

The Input command terminates any previous Input which it started,
whereas InputHook allows [more than one Input](#stack) at a time.

*Options* is interpreted the same, but the default settings differ:

-   The Input command limits the length of the input to 16383, while
    InputHook limits it to 1023. This can be overridden with the [L
    option](#option-l), and there is no absolute maximum.
-   The Input command blocks both text and non-text keystrokes by
    default, and blocks neither if the [V option](#vis) is present. By
    contrast, InputHook blocks only text keystrokes by default
    ([VisibleNonText](#VisibleNonText) defaults to true), so most
    hotkeys can be used while an Input is in progress.

The Input command blocks the [thread](../misc/Threads.htm) while it is
in progress, whereas InputHook allows the thread to continue, or even
exit (which allows any thread that it interrupted to resume). Instead of
waiting, the script can register an [OnEnd](#OnEnd) function to be
called when the Input is terminated.

The Input command returns the user\'s input only after the Input is
terminated, whereas InputHook\'s [Input](#Input) property allows it to
be retrieved at any time. The script can register an [OnChar](#OnChar)
function to be called whenever a character is added, instead of
continuously checking the Input property.

InputHook gives much more control over individual keys via the
[KeyOpt](#KeyOpt) method. This includes adding or removing end keys,
suppressing or not suppressing specific keys, or ignoring the text
produced by specific keys.

Unlike the Input command, InputHook can be used to detect keys which do
not produce text, *without* terminating the Input. This is done by
registering an [OnKeyDown](#OnKeyDown) function and using
[KeyOpt](#KeyOpt) or [NotifyNonText](#NotifyNonText) to specify which
keys are of interest.

If a *MatchList* item caused the Input to terminate, the [Match](#Match)
property can be consulted to determine exactly which match (this is more
useful when the [\* option](#asterisk) is present).

Although the script can consult [GetKeyState](GetKeyState.htm) after the
Input command returns, sometimes it does not accurately reflect which
keys were pressed when the Input was terminated. InputHook\'s
[EndMods](#EndMods) property reflects the logical state of the modifier
keys at the time Input was terminated.

There are some differences relating to backward-compatibility:

-   The Input command stores end keys [A]{.kbd}-[Z]{.kbd} in uppercase
    even though other letters on some keyboard layouts are lowercase.
    Passing the value to [Send](Send.htm) would produce a shifted
    keystroke instead of a plain one. By contrast, InputHook\'s
    [EndKeys](#EndKeys) property always returns the normalized name;
    i.e. whichever character is produced by pressing the key without
    holding [Shift]{.kbd} or other modifiers.

-   If a key name used in *EndKeys* corresponds to a VK which is shared
    between two physical keys (such as [NumpadUp]{.kbd} and [Up]{.kbd}),
    the Input command handles the primary key by VK and the secondary
    key by SC, whereas InputHook handles both by SC. `{vkNN}` notation
    can be used to handle the key by VK.

    When the end key is handled by VK, both physical keys can terminate
    the Input. For example, `{NumpadUp}` would cause the Input command
    to be terminated by pressing [Up]{.kbd}, but ErrorLevel would
    contain `EndKey:NumpadUp` since only the VK is considered.

    When an end key is handled by SC, the Input command always produces
    names for the known secondary SC of any given VK, and always
    produces `sc`*`NNN`* for any other key (even if it has a name). By
    contrast, InputHook produces a name if the key has one.

## Related {#Related}

[KeyWait](KeyWait.htm), [Hotstrings](../Hotstrings.htm),
[InputBox](InputBox.htm), [InstallKeybdHook](InstallKeybdHook.htm),
[Threads](../misc/Threads.htm)

## Examples {#Examples}

::: {#ExKeyWaitAny .ex}
[](#ExKeyWaitAny){.ex_number} Waits for the user to press any single
key.

    MsgBox KeyWaitAny()

    ; Same again, but don't block the key.
    MsgBox KeyWaitAny("V")

    KeyWaitAny(Options:="")
    {
        ih := InputHook(Options)
        if !InStr(Options, "V")
            ih.VisibleNonText := false
        ih.KeyOpt("{All}", "E")  ; End
        ih.Start()
        ih.Wait()
        return ih.EndKey  ; Return the key name
    }
:::

::: {#ExKeyWaitCombo .ex}
[](#ExKeyWaitCombo){.ex_number} Waits for any key in combination with
Ctrl/Alt/Shift/Win.

    MsgBox KeyWaitCombo()

    KeyWaitCombo(Options:="")
    {
        ih := InputHook(Options)
        if !InStr(Options, "V")
            ih.VisibleNonText := false
        ih.KeyOpt("{All}", "E")  ; End
        ; Exclude the modifiers
        ih.KeyOpt("{LCtrl}{RCtrl}{LAlt}{RAlt}{LShift}{RShift}{LWin}{RWin}", "-E")
        ih.Start()
        ih.Wait()
        return ih.EndMods . ih.EndKey  ; Return a string like <^<+Esc
    }
:::

::: {#ExSac .ex}
[](#ExSac){.ex_number} Simple auto-complete: any day of the week. Pun
aside, this is a mostly functional example. Simply run the script and
start typing today, press [Tab]{.kbd} to complete or press [Esc]{.kbd}
to exit.

    WordList := "Monday`nTuesday`nWednesday`nThursday`nFriday`nSaturday`nSunday"

    Suffix := ""

    SacHook := InputHook("V", "{Esc}")
    SacHook.OnChar := SacChar
    SacHook.OnKeyDown := SacKeyDown
    SacHook.KeyOpt("{Backspace}", "N")
    SacHook.Start()

    SacChar(ih, char)  ; Called when a character is added to SacHook.Input.
    {
        global Suffix := ""
        if RegExMatch(ih.Input, "`nm)\w+$", &prefix)
            && RegExMatch(WordList, "`nmi)^" prefix[0] "\K.*", &Suffix)
            Suffix := Suffix[0]
        
        if CaretGetPos(&cx, &cy)
            ToolTip Suffix, cx + 15, cy
        else
            ToolTip Suffix

        ; Intercept Tab only while we're showing a tooltip.
        ih.KeyOpt("{Tab}", Suffix = "" ? "-NS" : "+NS")
    }

    SacKeyDown(ih, vk, sc)
    {
        if (vk = 8) ; Backspace
            SacChar(ih, "")
        else if (vk = 9) ; Tab
            Send "{Text}" Suffix
    }
:::

::: {#ExAnyKey .ex}
[](#ExAnyKey){.ex_number} Waits for the user to press any key. Keys that
produce no visible character \-- such as the modifier keys, function
keys, and arrow keys \-- are listed as end keys so that they will be
detected too.

    ih := InputHook("L1", "{LControl}{RControl}{LAlt}{RAlt}{LShift}{RShift}{LWin}{RWin}{AppsKey}{F1}{F2}{F3}{F4}{F5}{F6}{F7}{F8}{F9}{F10}{F11}{F12}{Left}{Right}{Up}{Down}{Home}{End}{PgUp}{PgDn}{Del}{Ins}{BS}{CapsLock}{NumLock}{PrintScreen}{Pause}")
    ih.Start()
    ih.Wait()
:::

::: {#ExHotkey .ex}
[](#ExHotkey){.ex_number} This is a working hotkey example. Since the
hotkey has the tilde (\~) prefix, its own keystroke will pass through to
the active window. Thus, if you type `[btw` (or one of the other match
phrases) in any editor, the script will automatically perform an action
of your choice (such as replacing the typed text). For an alternative
version of this example, see [Switch](Switch.htm#ExInput).

    ~[::
    {
        msg := ""
        ih := InputHook("V T5 L4 C", "{enter}.{esc}{tab}", "btw,otoh,fl,ahk,ca")
        ih.Start()
        ih.Wait()
        if (ih.EndReason = "Max")
            msg := 'You entered "{1}", which is the maximum length of text.'
        else if (ih.EndReason = "Timeout")
            msg := 'You entered "{1}" at which time the input timed out.'
        else if (ih.EndReason = "EndKey")
            msg := 'You entered "{1}" and terminated the input with {2}.'

        if msg  ; If an EndReason was found, skip the rest below.
        {
            MsgBox Format(msg, ih.Input, ih.EndKey)
            return
        }

        ; Otherwise, a match was found.
        if (ih.Input = "btw")
            Send("{backspace 4}by the way")
        else if (ih.Input = "otoh")
            Send("{backspace 5}on the other hand")
        else if (ih.Input = "fl")
            Send("{backspace 3}Florida")
        else if (ih.Input = "ca")
            Send("{backspace 3}California")
        else if (ih.Input = "ahk")
            Run("https://www.autohotkey.com")
    }
:::
