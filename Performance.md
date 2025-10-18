# Script Performance

The following functions may affect performance depending on the nature
of the script: [SendMode](../lib/SendMode.htm),
[SetKeyDelay](../lib/SetKeyDelay.htm),
[SetMouseDelay](../lib/SetMouseDelay.htm),
[SetWinDelay](../lib/SetWinDelay.htm),
[SetControlDelay](../lib/SetControlDelay.htm), and
[SetDefaultMouseSpeed](../lib/SetDefaultMouseSpeed.htm).

## Built-in Performance Features {#Built-in_Performance_Features}

Each script is semi-compiled while it is being loaded and
syntax-checked. In addition to detecting some errors early, this also
greatly improves runtime performance.

Here are some of the technical details of the optimization process
(semi-compiling):

-   [Loops](../lib/Loop.htm), [blocks](../lib/Block.htm),
    [IFs](../lib/If.htm), [ELSEs](../lib/Else.htm) and other [control
    flow statements](../Language.htm#control-flow) are given the memory
    addresses of their related jump-points in the script.
-   Each statement name is replaced by an address in a jump table.
-   Each [expression](../Variables.htm#Expressions) is tokenized and
    converted from infix to postfix.
-   Each reference to a [variable](../Variables.htm) or
    [function](../Functions.htm) is resolved to a memory address, unless
    it is [dynamic](../Variables.htm#deref).
-   Literal integers in expressions are replaced with binary integers.
-   The destination of each [Goto](../lib/Goto.htm) is resolved to a
    memory address unless it is a variable.

In addition, during script execution, binary numbers are cached in
variables to avoid conversions to/from strings.
