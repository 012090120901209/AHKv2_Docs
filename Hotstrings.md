# Hotstrings

## Table of Contents {#toc}

-   [Introduction and Simple Examples](#intro)
-   [Ending Characters](#EndChars)
-   [Options](#Options)
-   [Long Replacements](#continuation)
-   [Context-sensitive Hotstrings](#variant)
-   [AutoCorrect](#AutoCorrect)
-   [Remarks](#remarks)
-   [Named Function Hotstrings](#Function)
-   [Hotstring Helper](#Helper)

## Introduction and Simple Examples {#intro}

Although hotstrings are mainly used to expand abbreviations as you type
them (auto-replace), they can also be used to launch any scripted
action. In this respect, they are similar to [hotkeys](Hotkeys.htm)
except that they are typically composed of more than one character (that
is, a string).

To define a hotstring, enclose the triggering abbreviation between pairs
of colons as in this example:

    ::btw::by the way

In the above example, the abbreviation btw will be automatically
replaced with \"by the way\" whenever you type it (however, by default
you must type an [ending character](#EndChars) after typing btw, such as
[Space]{.kbd}, [.]{.kbd}, or [Enter]{.kbd}).

The \"by the way\" example above is known as an auto-replace hotstring
because the typed text is automatically erased and replaced by the
string specified after the second pair of colons. By contrast, a
hotstring may also be defined to perform any custom action as in the
following examples. Note that the [statements](Concepts.htm#statement)
must appear [beneath]{.underline} the abbreviation within the
hotstring\'s [function body](Functions.htm):

    ::btw::
    {
        MsgBox 'You typed "btw".'
    }

    :*:]d::  ; This hotstring replaces "]d" with the current date and time via the statement below.
    {
        Send FormatTime(, "M/d/yyyy h:mm tt")  ; It will look like 9/1/2005 3:53 PM
    }

In the above, the braces serve to define a function body for each
hotstring. The opening brace may also be specified on the same line as
the double-colon to support the [OTB (One True Brace)
style](lib/Block.htm#otb).

Even though the two examples above are not auto-replace hotstrings, the
abbreviation you type is erased by default. This is done via automatic
backspacing, which can be disabled via the [b0 option](#b0).

When a hotstring is triggered, the name of the hotstring is passed as
its first parameter named `ThisHotkey` (which excludes the trailing
colons). For example:

    :X:btw::MsgBox ThisHotkey  ; Reports :X:btw

With few exceptions, this is similar to the built-in variable
[A_ThisHotkey](Variables.htm#ThisHotkey). The parameter name can be
changed by using a [named function](#Function).

## Ending Characters {#EndChars}

Unless the [asterisk option](#Asterisk) is in effect, you must type an
*ending character* after a hotstring\'s abbreviation to trigger it.
Ending characters initially consist of the following:
**-()\[\]{}\':;\"/\\,.?!\`n\`s\`t** (note that \`n is [Enter]{.kbd}, \`s
is [Space]{.kbd}, and \`t is [Tab]{.kbd}). This set of characters can be
changed by editing the following example, which sets the new ending
characters for [all]{.underline} hotstrings, not just the ones beneath
it:

    #Hotstring EndChars -()[]{}:;'"/\,.?!`n`s`t

The ending characters can be changed while the script is running by
calling the [Hotstring](lib/Hotstring.htm) function as demonstrated
below:

    Hotstring("EndChars", "-()[]{}:;")

## Options {#Options}

A hotstring\'s default behavior can be changed in two possible ways:

1.  The [#Hotstring](lib/_Hotstring.htm) directive, which affects all
    hotstrings physically beneath that point in the script. The
    following example puts the C and R options into effect:
    `#Hotstring `**`c r`**.
2.  Putting options inside a hotstring\'s first pair of colons. The
    following example puts the C and \* options (case-sensitive and
    \"ending character not required\") into effect for a single
    hotstring: `:`**`c*`**`:j@::john@somedomain.com`.

The list below describes each option. When specifying more than one
option using the methods above, spaces optionally may be included
between them.

**\*** (asterisk): An ending character (e.g. [Space]{.kbd}, [.]{.kbd},
or [Enter]{.kbd}) is not required to trigger the hotstring. For example:

    :*:j@::jsmith@somedomain.com

The example above would send its replacement the moment you type the @
character. When using the [#Hotstring directive](lib/_Hotstring.htm),
use **\*0** to turn this option back off.

**?** (question mark): The hotstring will be triggered even when it is
inside another word; that is, when the character typed immediately
before it is alphanumeric. For example, if `:?:al::airline` is a
hotstring, typing \"practical \" would produce \"practicairline \". Use
**?0** to turn this option back off.

**B0** (B followed by a zero): Automatic backspacing is
[not]{.underline} done to erase the abbreviation you type. Use a plain
**B** to turn backspacing back on after it was previously turned off. A
script may also do its own backspacing via {bs 5}, which sends
[Backspace]{.kbd} five times. Similarly, it may send [←]{.kbd} five
times via {left 5}. For example, the following hotstring produces
\"\<em\>\</em\>\" and moves the caret 5 places to the left (so that
it\'s between the tags):

    :*b0:<em>::</em>{left 5}

**C:** Case-sensitive: When you type an abbreviation, it must exactly
match the case defined in the script. Use **C0** to turn case
sensitivity back off.

**C1:** Do not conform to typed case. Use this option to make
[auto-replace hotstrings](#auto) case-insensitive and prevent them from
conforming to the case of the characters you actually type.
Case-conforming hotstrings (which are the default) produce their
replacement text in all caps if you type the abbreviation in all caps.
If you type the first letter in caps, the first letter of the
replacement will also be capitalized (if it is a letter). If you type
the case in any other way, the replacement is sent exactly as defined.
When using the [#Hotstring directive](lib/_Hotstring.htm), **C0** can be
used to turn this option back off, which makes hotstrings conform again.

**Kn:** Key-delay: This rarely-used option sets the delay between
keystrokes produced by auto-backspacing or [auto-replacement](#auto).
Specify the new delay for **n**; for example, specify k10 to have a
10 ms delay and k-1 to have no delay. The exact behavior of this option
depends on which [sending mode](#SendMode) is in effect:

-   SI (SendInput): Key-delay is ignored because a delay is not possible
    in this mode. The exception to this is when SendInput is
    [unavailable](lib/Send.htm#SendInputUnavail), in which case
    hotstrings revert to SendPlay mode below (which does obey
    key-delay).
-   SP (SendPlay): A delay of length zero is the default, which for
    SendPlay is the same as -1 (no delay). In this mode, the delay is
    actually a [PressDuration](lib/SetKeyDelay.htm#dur) rather than a
    delay between keystrokes.
-   SE (SendEvent): A delay of length zero is the default. Zero is
    recommended for most purposes since it is fast but still cooperates
    well with other processes (due to internally doing a [Sleep
    0](lib/Sleep.htm)). Specify k-1 to have no delay at all, which is
    useful to make auto-replacements faster if your CPU is frequently
    under heavy load. When set to -1, a script\'s process-priority
    becomes an important factor in how fast it can send keystrokes. To
    raise a script\'s priority, use
    [`ProcessSetPriority`](lib/ProcessSetPriority.htm)` "High"`.

**O:** Omit the ending character of [auto-replace hotstrings](#auto)
when the replacement is produced. This is useful when you want a
hotstring to be kept unambiguous by still requiring an ending character,
but don\'t actually want the ending character to be shown on the screen.
For example, if `:o:ar::aristocrat` is a hotstring, typing \"ar\"
followed by the spacebar will produce \"aristocrat\" with no trailing
space, which allows you to make the word plural or possessive without
having to press [Backspace]{.kbd}. Use **O0** (the letter O followed by
a zero) to turn this option back off.

**Pn:** The [priority](misc/Threads.htm) of the hotstring (e.g. P1).
This rarely-used option has no effect on [auto-replace
hotstrings](#auto).

**R:** Send the replacement text [raw](lib/Send.htm#SendRaw); that is,
without translating {Enter} to [Enter]{.kbd}, \^c to
[Ctrl]{.kbd}+[C]{.kbd}, etc. Use **R0** to turn this option back off, or
override it with **T**.

**Note:** [Text mode](#T) may be more reliable. The R and T options are
mutually exclusive.

**S** or **S0**: Specify the letter S to make the hotstring
[exempt](lib/_SuspendExempt.htm) from [Suspend](lib/Suspend.htm).
Specify S0 (S with the number 0) to remove the exemption, allowing the
hotstring to be suspended. When applied as a default option, either `S`
or `#SuspendExempt` will make the hotstring exempt; that is, to override
the directive, `S0` must be used explicitly in the hotstring.

**SI** or **SP** or **SE**: Sets the method by which [auto-replace
hotstrings](#auto) send their keystrokes. These options are mutually
exclusive: only one can be in effect at a time. The following describes
each option:

-   [SI stands for [SendInput](lib/Send.htm#SendInputDetail), which
    typically has superior speed and reliability than the other modes.
    Another benefit is that like SendPlay below, SendInput postpones
    anything you type during a hotstring\'s [auto-replacement
    text](#auto). This prevents your keystrokes from being interspersed
    with those of the replacement. When SendInput is
    [unavailable](lib/Send.htm#SendInputUnavail), hotstrings
    automatically use SendPlay instead.]{#SI}
-   [SP stands for [SendPlay](lib/Send.htm#SendPlayDetail), which may
    allow hotstrings to work in a broader variety of games.]{#SP}
-   [SE stands for [SendEvent](lib/Send.htm#SendEvent).]{#SE}

If none of the above options are used, the default mode is SendInput.
However, unlike the SI option, SendEvent is used instead of SendPlay
when SendInput is unavailable.

**T:** Send the replacement text using [Text
mode](lib/Send.htm#SendText). That is, send each character by character
code, without translating {Enter} to [Enter]{.kbd}, \^c to
[Ctrl]{.kbd}+[C]{.kbd}, etc. and without translating each character to a
keystroke. This option is put into effect automatically for hotstrings
that have a [continuation section](#continuation). Use **T0** or **R0**
to turn this option back off, or override it with **R**.

**X:** Execute. Instead of replacement text, the hotstring accepts a
function call or expression to execute. For example, `:X:~mb::MsgBox`
would cause a message box to be displayed when the user types \"\~mb\"
instead of auto-replacing it with the word \"MsgBox\". This is most
useful when defining a large number of hotstrings which call functions,
as it would otherwise require three lines per hotstring.

This option should not be used with the [Hotstring](lib/Hotstring.htm)
function. To make a hotstring call a function when triggered, pass the
function by reference.

**Z:** This rarely-used option resets the hotstring recognizer after
each triggering of the hotstring. In other words, the script will begin
waiting for an entirely new hotstring, eliminating from consideration
anything you previously typed. This can prevent unwanted triggerings of
hotstrings. To illustrate, consider the following hotstring:

    :b0*?:11::
    {
        Send "xx"
    }

Since the above lacks the Z option, typing 111 (three consecutive 1\'s)
would trigger the hotstring twice because the middle 1 is the *last*
character of the first triggering but also the *first* character of the
second triggering. By adding the letter Z in front of b0, you would have
to type four 1\'s instead of three to trigger the hotstring twice. Use
**Z0** to turn this option back off.

## Long Replacements {#continuation}

Hotstrings that produce a large amount of replacement text can be made
more readable and maintainable by using a [continuation
section](Scripts.htm#continuation). For example:

    ::text1::
    (
    Any text between the top and bottom parentheses is treated literally.
    By default, the hard carriage return (Enter) between the previous line and this one is also preserved.
        By default, the indentation (tab) to the left of this line is preserved.
    )

See [continuation section](Scripts.htm#continuation) for how to change
these default behaviors. The presence of a continuation section also
causes the hotstring to default to [Text mode](#T). The only way to
override this special default is to specify an opposing option in each
hotstring that has a continuation section (e.g. `:t0:text1::` or
`:r:text2::`).

## Context-sensitive Hotstrings {#variant}

The [#HotIf](lib/_HotIf.htm) directive can be used to make selected
hotstrings context sensitive. Such hotstrings send a different
replacement, perform a different action, or do nothing at all depending
on any condition, such as the type of window that is active. For
example:

    #HotIf WinActive("ahk_class Notepad")
    ::btw::This replacement text will appear only in Notepad.
    #HotIf
    ::btw::This replacement text appears in windows other than Notepad.

## AutoCorrect {#AutoCorrect}

The following script uses hotstrings to correct about 4700 common
English misspellings on-the-fly. It also includes a
[Win]{.kbd}+[H]{.kbd} hotkey to make it easy to add more misspellings:

Download:
[AutoCorrect.ahk](https://www.autohotkey.com/download/AutoCorrect.ahk)
(127 KB)

Author: [Jim Biancolo](http://www.biancolo.com/blog/autocorrect/) and
[Wikipedia\'s Lists of Common
Misspellings](https://en.wikipedia.org/wiki/Wikipedia:Lists_of_common_misspellings)

## Remarks

[Expressions](Variables.htm#Expressions) are not currently supported
within the replacement text. To work around this, don\'t make such
hotstrings [auto-replace](#auto). Instead, use the [Send](lib/Send.htm)
function in the body of the hotstring or in combination with the [X
(execute) option](#X).

To send an extra space or tab after a replacement, include the [escape
sequence](misc/EscapeChar.htm) `` `s `` or `` `t `` at the end of the
replacement, e.g. `` :*:btw::by the way`s ``.

For an auto-replace hotstring which doesn\'t use the [Text](#T) or
[Raw](#raw) mode, sending a `{` alone, or one preceded only by
white-space, requires it being enclosed in a pair of brackets, for
example `:*:brace::{{}` and `:*:space_brace:: {{}`. Otherwise it is
interpreted as the opening brace for the hotstring\'s function to
support the [OTB (One True Brace) style](lib/Block.htm#otb).

By default, any click of the left or right mouse button will reset the
hotstring recognizer. In other words, the script will begin waiting for
an entirely new hotstring, eliminating from consideration anything you
previously typed (if this is undesirable, specify the line
[`#Hotstring`](lib/_Hotstring.htm)` NoMouse` anywhere in the script).
This \"reset upon mouse click\" behavior is the default because each
click typically moves the text insertion point (caret) or sets keyboard
focus to a new control/field. In such cases, it is usually desirable
to: 1) fire a hotstring even if it lacks the [question mark
option](#Question); 2) prevent a firing when something you type after
clicking the mouse accidentally forms a valid abbreviation with what you
typed before.

The hotstring recognizer checks the active window each time a character
is typed, and resets if a different window is active than before. If the
active window changes but reverts before any characters are typed, the
change is not detected (but the hotstring recognizer may be reset for
some other reason). The hotstring recognizer can also be reset by
calling [`Hotstring "Reset"`](lib/Hotstring.htm#Reset).

The built-in variable **A_EndChar** contains the ending character that
you typed to trigger the most recent non-auto-replace hotstring. If no
ending character was required (due to the [\* option](#Asterisk)), this
variable will be blank. A_EndChar is useful when making hotstrings that
use the Send function or whose behavior should vary depending on which
ending character you typed. To send the ending character itself, use
`SendText A_EndChar` ([SendText](lib/Send.htm) is used because
characters such as !{} would not be sent correctly by the normal Send
function).

Although single-colons within hotstring definitions do not need to be
[escaped](misc/EscapeChar.htm) unless they precede the double-colon
delimiter, backticks and those semicolons having a space or tab to their
left must always be escaped. See [Escape Sequences](misc/EscapeChar.htm)
for a complete list.

Although the [Send function](lib/Send.htm)\'s special characters such as
{Enter} are supported in [auto-replacement text](#auto) (unless the [raw
option](#raw) is used), the hotstring abbreviations themselves do not
use this. Instead, specify \`n for [Enter]{.kbd} and \`t (or a literal
tab) for [Tab]{.kbd} (see [Escape Sequences](misc/EscapeChar.htm) for a
complete list). For example, the hotstring `` :*:ab`t:: `` would be
triggered when you type \"ab\" followed by a tab.

Spaces and tabs are treated literally within hotstring definitions. For
example, the following would produce two different results:
`::btw::by the way` and `::btw:: by the way`.

Each hotstring abbreviation can be no more than 40 characters long. The
program will warn you if this length is exceeded. By contrast, the
length of hotstring\'s replacement text is limited to about 5000
characters when the [sending mode](#SendMode) is at its default of
SendInput. That limit can be removed by switching to one of the other
[sending modes](#SendMode), or by using
[SendPlay](lib/Send.htm#SendPlayDetail) or
[SendEvent](lib/Send.htm#SendEvent) in the body of the hotstring or in
combination with the [X (execute) option](#X).

The order in which hotstrings are defined determines their precedence
with respect to each other. In other words, if more than one hotstring
matches something you type, only the one listed first in the script will
take effect. Related topic: [context-sensitive hotstrings](#variant).

Any backspacing you do is taken into account for the purpose of
detecting hotstrings. However, the use of [↑]{.kbd}, [→]{.kbd},
[↓]{.kbd}, [←]{.kbd}, [PgUp]{.kbd}, [PgDn]{.kbd}, [Home]{.kbd}, and
[End]{.kbd} to navigate within an editor will cause the hotstring
recognition process to reset. In other words, it will begin waiting for
an entirely new hotstring.

A hotstring may be typed even when the active window is ignoring your
keystrokes. In other words, the hotstring will still fire even though
the triggering abbreviation is never visible. In addition, you may still
press [Backspace]{.kbd} to undo the most recently typed keystroke (even
though you can\'t see the effect).

A hotstring\'s function can be called explicitly by the script only if
the function has been named. See [Named Function Hotstrings](#Function).

Hotstrings are not monitored and will not be triggered while input is
blocked by an invisible [Input hook](lib/InputHook.htm).

By default, hotstrings are never triggered by keystrokes produced by any
AutoHotkey script. This avoids the possibility of an infinite loop where
hotstrings trigger each other over and over. This behaviour can be
controlled with [#InputLevel](lib/_InputLevel.htm) and
[SendLevel](lib/SendLevel.htm). However, auto-replace hotstrings always
use send level 0 and therefore never trigger [hook
hotkeys](lib/_UseHook.htm) or hotstrings.

The [Suspend](lib/Suspend.htm) function can temporarily disable all
hotstrings except for ones you make exempt. For greater selectivity, use
[#HotIf](lib/_HotIf.htm).

Hotstrings can be created dynamically by means of the
[Hotstring](lib/Hotstring.htm) function, which can also modify, disable,
or enable the script\'s existing hotstrings individually.

The [InputHook](lib/InputHook.htm) function is more flexible than
hotstrings for certain purposes. For example, it allows your keystrokes
to be invisible in the active window (such as a game). It also supports
non-character ending keys such as [Esc]{.kbd}.

The [keyboard hook](lib/InstallKeybdHook.htm) is automatically used by
any script that contains hotstrings.

Hotstrings behave identically to hotkeys in the following ways:

-   They are affected by the [Suspend](lib/Suspend.htm) function.
-   They obey [#MaxThreads](lib/_MaxThreads.htm) and
    [#MaxThreadsPerHotkey](lib/_MaxThreadsPerHotkey.htm) (but not
    [#MaxThreadsBuffer](lib/_MaxThreadsBuffer.htm)).
-   Scripts containing hotstrings are automatically
    [persistent](Scripts.htm#persistent).
-   Non-auto-replace hotstrings will create a new
    [thread](misc/Threads.htm) when launched. In addition, they will
    update the built-in hotkey variables such as
    [A_ThisHotkey](Variables.htm#ThisHotkey).

Known limitation: On some systems in Java applications, hotstrings might
interfere with the user\'s ability to type diacritical letters (via dead
keys). To work around this, [Suspend](lib/Suspend.htm) can be turned on
temporarily (which disables all hotstrings).

## Named Function Hotstrings {#Function}

If the function of a hotstring is ever needed to be called without
triggering the hotstring itself, one or more hotstrings can be assigned
a named [function](Functions.htm) by simply defining it immediately
after the hotstring\'s double-colon, as in this example:

    ; This example also demonstrates one way to implement case conformity in a script.
    :C:BTW::  ; Typed in all-caps.
    :C:Btw::  ; Typed with only the first letter upper-case.
    : :btw::  ; Typed in any other combination.
        case_conform_btw(hs) ; hs will hold the name of the hotstring which triggered the function.
        {
            if (hs == ":C:BTW")
                Send "BY THE WAY"
            else if (hs == ":C:Btw")
                Send "By the way"
            else
                Send "by the way"
        }

If the function *case_conform_btw* is ever called explicitly by the
script, the first parameter (hs) must be passed a value.

[Hotkeys](Hotkeys.htm) can also be defined this way. Multiple hotkeys or
hotstrings can be stacked together to call the same function.

There must only be whitespace or comments between the hotstring and the
function name.

Naming the function also encourages self-documenting hotstrings, like in
the code above where the function name describes the hotstring.

The [Hotstring](lib/Hotstring.htm) function can also be used to assign a
function or function object to a hotstring.

## Hotstring Helper {#Helper}

Take a look at the [first example](lib/Hotstring.htm#ExHelper) in the
example section of the [Hotstring](lib/Hotstring.htm) function\'s page,
which might be useful if you are a heavy user of hotstrings. By pressing
[Win]{.kbd}+[H]{.kbd} (or another hotkey of your choice), the currently
selected text can be turned into a hotstring. For example, if you have
\"by the way\" selected in a word processor, pressing
[Win]{.kbd}+[H]{.kbd} will prompt you for its abbreviation (e.g. btw),
add the new hotstring to the script and activate it.
