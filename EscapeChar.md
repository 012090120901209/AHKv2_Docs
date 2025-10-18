# Escape Sequences

The escape character `` ` `` (back-tick or grave accent) is used to
indicate that the character immediately following it should be
interpreted differently than it normally would. This character is at the
upper left corner of most English keyboards.

In AutoHotkey the following escape sequences can be used:

+-----------------------------------+-----------------------------------+
| Sequence                          | Result                            |
+===================================+===================================+
| ``` `` ```                        | `` ` `` (literal accent; i.e. two |
|                                   | consecutive escape characters     |
|                                   | result in a single literal        |
|                                   | character)                        |
+-----------------------------------+-----------------------------------+
| `` `; ``                          | `;`{.no-highlight} (literal       |
|                                   | semicolon)                        |
|                                   |                                   |
|                                   | **Note:** It is not necessary to  |
|                                   | escape a semicolon which has any  |
|                                   | character [other                  |
|                                   | than]{.underline} space or tab to |
|                                   | its immediate left, since it      |
|                                   | would not be interpreted as a     |
|                                   | comment anyway.                   |
+-----------------------------------+-----------------------------------+
| `` `: ``                          | `:` (literal colon). This is      |
|                                   | necessary only in a hotstring\'s  |
|                                   | triggering abbreviation.          |
+-----------------------------------+-----------------------------------+
| `` `{ ``                          | [{]{.kbd} (keyboard key). This is |
|                                   | only valid, and is required, when |
|                                   | [                                 |
|                                   | remapping](Remap.htm#EscapeBrace) |
|                                   | a key to [{]{.kbd}.               |
+-----------------------------------+-----------------------------------+
| `` `n ``                          | newline (linefeed/LF)             |
+-----------------------------------+-----------------------------------+
| `` `r ``                          | carriage return (CR)              |
+-----------------------------------+-----------------------------------+
| `` `b ``                          | backspace                         |
+-----------------------------------+-----------------------------------+
| `` `t ``                          | tab (the more typical horizontal  |
|                                   | variety)                          |
+-----------------------------------+-----------------------------------+
| `` `s ``                          | space                             |
+-----------------------------------+-----------------------------------+
| `` `v ``                          | vertical tab \-- corresponds to   |
|                                   | Ascii value 11. It can also be    |
|                                   | manifest in some applications by  |
|                                   | typing [Ctrl]{.kbd}+[K]{.kbd}.    |
+-----------------------------------+-----------------------------------+
| `` `a ``                          | alert (bell) \-- corresponds to   |
|                                   | Ascii value 7. It can also be     |
|                                   | manifest in some applications by  |
|                                   | typing [Ctrl]{.kbd}+[G]{.kbd}.    |
+-----------------------------------+-----------------------------------+
| `` `f ``                          | formfeed \-- corresponds to Ascii |
|                                   | value 12. It can also be manifest |
|                                   | in some applications by typing    |
|                                   | [Ctrl]{.kbd}+[L]{.kbd}.           |
+-----------------------------------+-----------------------------------+
| `` `" `` or `` `' ``              | Single-quote marks (\') and       |
|                                   | double-quote marks (\") function  |
|                                   | identically, except that a string |
|                                   | enclosed in single-quote marks    |
|                                   | can contain literal double-quote  |
|                                   | marks and vice versa. Therefore,  |
|                                   | to include an actual quote mark   |
|                                   | inside a literal string, escape   |
|                                   | the quote mark or enclose the     |
|                                   | string in the opposite type of    |
|                                   | quote mark. For example:          |
|                                   | `` Var :=                         |
|                                   | "The color `"red`" was found." `` |
|                                   | or                                |
|                                   | `Var                              |
|                                   | := 'The color "red" was found.'`. |
+-----------------------------------+-----------------------------------+

## Examples {#Examples}

::: {#ExBasic .ex}
[](#ExBasic){.ex_number} Reports a multi-line string. The lines are
separated by a linefeed character.

    MsgBox "Line 1`nLine 2"
:::
