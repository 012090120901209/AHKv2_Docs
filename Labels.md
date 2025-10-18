# Labels

## Table of Contents {#toc}

-   [Syntax and Usage](#syntax-and-usage)
-   [Look-alikes](#look-alikes)
-   [Dynamic Labels](#dynamic-labels)
-   [Named Loops](#named-loops)
-   [Related](#related)

## Syntax and Usage

A label identifies a line of code, and can be used as a
[Goto](../lib/Goto.htm) target or to [specify a loop](#named-loops) to
break out of or continue. A label consist of a
[name](../Concepts.htm#names) followed by a colon:

    this_is_a_label:

Aside from whitespace and comments, no other code can be written on the
same line as a label.

**Names:** Label names are not case-sensitive (for ASCII letters), and
may consist of letters, numbers, underscore and non-ASCII characters.
For example: *MyListView*, *Menu_File_Open*, and *outer_loop*.

**Scope:** Each function has its own list of local labels. Inside a
function, only that function\'s labels are visible/accessible to the
script.

**Target:** The target of a label is the next line of executable code.
Executable code includes functions, assignments,
[expressions](../Variables.htm#Expressions) and
[blocks](../lib/Block.htm), but not directives, labels, hotkeys or
hotstrings. In the following example, `run_notepad_1` and
`run_notepad_2` both point at the `Run` line:

    run_notepad_1:
    run_notepad_2:
        Run "notepad"
        return

**Execution:** Like directives, labels have no effect when reached
during normal execution.

## Look-alikes

Hotkey and hotstring definitions look similar to labels, but are not
labels.

[Hotkeys](../Hotkeys.htm) consist of a hotkey followed by double-colon.

    ^a::

[Hotstrings](../Hotstrings.htm) consist of a colon, zero or more
[options](../Hotstrings.htm#Options), another colon, an abbreviation and
double-colon.

    :*:btw::

## Dynamic Labels

In some cases a [variable](../Variables.htm) can be used in place of a
label name. In such cases, the name stored in the variable is used to
locate the target label. However, performance is slightly reduced
because the target label must be \"looked up\" each time rather than
only once when the script is first loaded.

## Named Loops

A label can also be used to identify a loop for the
[Continue](../lib/Continue.htm) and [Break](../lib/Break.htm)
statements. This allows the script to easily continue or break out of
any number of nested loops.

## Related

[Functions](../Functions.htm), [IsLabel](../lib/IsLabel.htm),
[Goto](../lib/Goto.htm), [Break](../lib/Break.htm),
[Continue](../lib/Continue.htm)
