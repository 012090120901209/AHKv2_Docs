# GuiControl Object

``` NoIndent
class Gui.Control extends Object
```

Provides an interface for modifying GUI controls and retrieving
information about them. [Gui.Add](Gui.htm#Add),
[Gui.\_\_Item](Gui.htm#__Item) and
[GuiCtrlFromHwnd](GuiCtrlFromHwnd.htm) return an object of this type.

\"GuiCtrl\" is used below as a placeholder for instances of the
`Gui.Control` class.

`Gui.Control` serves as the base class for all GUI controls, but each
type of control has its own class. Some of the following methods are
defined by the prototype of the appropriate class, or the `Gui.List`
base class. See [Built-in Classes](../ObjList.htm) for a full list.

In addition to the methods and property inherited from
[Object](Object.htm), GuiControl objects may have the following
predefined methods and properties.

## Table of Contents {#toc}

-   [Methods](#Methods):
    -   [Add](#Add): Appends items to a multi-item control.
    -   [Choose](#Choose): Selects an item in a multi-item control.
    -   [Delete](#Delete): Deletes one or all items from a multi-item
        control.
    -   [Focus](#Focus): Sets keyboard focus to the control.
    -   [GetPos](#GetPos): Retrieves the position and size of the
        control.
    -   [Move](#Move): Moves and/or resizes the control.
    -   [OnCommand](#OnCommand): Registers a function or method to be
        called on WM_COMMAND.
    -   [OnEvent](#OnEvent): Registers a function or method to be called
        when the given event is raised.
    -   [OnNotify](#OnNotify): Registers a function or method to be
        called on WM_NOTIFY.
    -   [Opt](#Opt): Sets various options and styles for the appearance
        and behavior of the control.
    -   [Redraw](#Redraw): Redraws the region of the GUI window occupied
        by the control.
    -   [SetFont](#SetFont): Sets the font typeface, size, style, and/or
        color for the control.
-   [Properties](#Properties):
    -   [ClassNN](#ClassNN): Retrieves the class name and sequence
        number (ClassNN) of the control.
    -   [Enabled](#Enabled): Retrieves or sets the interaction state of
        the control.
    -   [Focused](#Focused): Retrieves the focus state of the control.
    -   [Gui](#Gui): Retrieves the [Gui object](Gui.htm) of the
        control\'s parent window.
    -   [Hwnd](#Hwnd): Retrieves the window handle (HWND) of the
        control.
    -   [Name](#Name): Retrieves or sets the explicit name of the
        control.
    -   [Text](#Text): Retrieves or sets the text/caption of the
        control.
    -   [Type](#Type): Retrieves the type of the control.
    -   [Value](#Value): Retrieves or sets the contents of a
        value-capable control.
    -   [Visible](#Visible): Retrieves or sets the visibility state of
        the control.
-   [General Remarks](#GenRemarks):
    -   [Redraw](#redraw-remarks): Performance-related remarks about
        redraw behaviour of controls.

## Methods {#Methods}

::: {#Add .methodShort}
### Add

Appends items to a multi-item control (ListBox, DropDownList, ComboBox,
or Tab).

``` Syntax
GuiCtrl.Add(Items)
```

#### Parameters {#Add_Parameters}

Items

:   Type: [Array](Array.htm)

    An array of strings to be inserted as items at the end of the
    control\'s list, e.g. `["Red", "Green", "Blue"]`.

#### Remarks {#Add_Remarks}

To replace (overwrite) the list instead, use the [Delete
method](#Delete) beforehand. To select an item, use the [Choose
method](#Choose).

#### Related {#Add_Related}

[ListView.Add](ListView.htm#Add), [TreeView.Add](TreeView.htm#Add)
:::

::: {#Choose .methodShort}
### Choose

Selects an item in a multi-item control (ListBox, DropDownList,
ComboBox, or Tab).

``` Syntax
GuiCtrl.Choose(Value)
```

#### Parameters {#Choose_Parameters}

Value

:   Type: [Integer](../Concepts.htm#numbers) or
    [String](../Concepts.htm#strings)

    Specify 1 for the first item, 2 for the second, etc.

    If *Value* is a string (even a numeric string), the item whose
    leading name part matches *Value* will be selected. The search is
    not case-sensitive. For example, if the control contains the item
    \"UNIX Text\", specifying the word unix (lowercase) would be enough
    to select it. For a [multi-select
    ListBox](GuiControls.htm#ListBoxMulti), all matching items are
    selected.

    If *Value* is zero or empty, the current selection is removed.

#### Remarks {#Choose_Remarks}

To select or deselect [all]{.underline} items in a [multi-select
ListBox](GuiControls.htm#ListBoxMulti), follow this example:

    PostMessage 0x0185, 1, -1, ListBox  ; Select all items. 0x0185 is LB_SETSEL.
    PostMessage 0x0185, 0, -1, ListBox  ; Deselect all items.
    ListBox.Choose(0)  ; Deselect all items.

Unlike [ControlChooseIndex](ControlChooseIndex.htm), this method does
not raise a [Change](GuiOnEvent.htm#Change) or
[DoubleClick](GuiOnEvent.htm#DoubleClick) event.
:::

::: {#Delete .methodShort}
### Delete

Deletes one or all items from a multi-item control (ListBox,
DropDownList, ComboBox, or Tab).

``` Syntax
GuiCtrl.Delete(Value)
```

#### Parameters {#Delete_Parameters}

Value

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted, all items will be deleted. Otherwise, specify 1 for the
    first item, 2 for the second, etc.

#### Remarks {#Delete_Remarks}

For Tab controls, a tab\'s sub-controls stay associated with their
original tab number; that is, they are never associated with their
tab\'s actual display-name. For this reason, renaming or removing a tab
will not change the tab number to which the sub-controls belong. For
example, if there are three tabs `["Red", "Green", "Blue"]` and the
second tab is removed by means of `MyTab.Delete(2)`, the sub-controls
originally associated with Green will now be associated with Blue.
Because of this behavior, only tabs at the end should generally be
removed. Tabs that are removed in this way can be added back later, at
which time they will reclaim their original set of controls.

#### Related {#Delete_Related}

[ListView.Delete](ListView.htm#Delete),
[TreeView.Delete](TreeView.htm#Delete)
:::

::: {#Focus .methodShort}
### Focus

Sets keyboard focus to the control.

``` Syntax
GuiCtrl.Focus()
```

To be effective, the window generally must not be minimized or hidden.

To retrieve the focus state of the control, use the [Focused
property](#Focused).
:::

::: {#GetPos .methodShort}
### GetPos

Retrieves the position and size of the control.

``` Syntax
GuiCtrl.GetPos(&X, &Y, &Width, &Height)
```

#### Parameters {#GetPos_Parameters}

&X, &Y

:   Type: [VarRef](../Concepts.htm#variable-references)

    If omitted, the corresponding value will not be stored. Otherwise,
    specify references to the output variables in which to store the X
    and Y coordinates (in pixels) of the control\'s upper left corner.
    These coordinates are relative to the upper-left corner of the
    window\'s client area, which is the area not including title bar,
    menu bar, and borders.

&Width, &Height

:   Type: [VarRef](../Concepts.htm#variable-references)

    If omitted, the corresponding value will not be stored. Otherwise,
    specify references to the output variables in which to store the
    control\'s width and height (in pixels).

#### Remarks {#GetPos_Remarks}

Unlike [ControlGetPos](ControlGetPos.htm), this method applies [DPI
scaling](Gui.htm#DPIScale) to the returned coordinates (unless the
`-DPIScale` option was used).

#### Examples {#GetPos_Examples}

    MyEdit.GetPos(&x, &y, &w, &h)
    MsgBox "The X coordinate is " x ". The Y coordinate is " y ". The width is " w ". The height is " h "."
:::

::: {#Move .methodShort}
### Move

Moves and/or resizes the control.

``` Syntax
GuiCtrl.Move(X, Y, Width, Height)
```

#### Parameters {#Move_Parameters}

X, Y

:   Type: [Integer](../Concepts.htm#numbers)

    If either is omitted, the control\'s position in that dimension will
    not be changed. Otherwise, specify the X and Y coordinates (in
    pixels) of the upper left corner of the control\'s new location. The
    coordinates are relative to the upper-left corner of the window\'s
    client area, which is the area not including title bar, menu bar,
    and borders.

Width, Height

:   Type: [Integer](../Concepts.htm#numbers)

    If either is omitted, the control\'s size in that dimension will not
    be changed. Otherwise, specify the new width and height of the
    control (in pixels).

#### Remarks {#Move_Remarks}

Unlike [ControlMove](ControlMove.htm), this method applies [DPI
scaling](Gui.htm#DPIScale) to the coordinates (unless the `-DPIScale`
option was used).

#### Examples {#Move_Examples}

    MyEdit.Move(10, 20, 200, 100)
    MyEdit.Move(VarX+10, VarY+5, VarW*2, VarH*1.5)
:::

::: {#OnCommand .methodShort}
### OnCommand

Registers a function or method to be called when a control notification
is received via the [WM_COMMAND](GuiOnCommand.htm#WM_COMMAND) message.

``` Syntax
GuiCtrl.OnCommand(NotifyCode, Callback , AddRemove)
```

See [OnCommand](GuiOnCommand.htm) for details.
:::

::: {#OnEvent .methodShort}
### OnEvent

Registers a function or method to be called when the given
[event](GuiOnEvent.htm#Control_Events) is raised.

``` Syntax
GuiCtrl.OnEvent(EventName, Callback , AddRemove)
```

See [OnEvent](GuiOnEvent.htm) for details.
:::

::: {#OnNotify .methodShort}
### OnNotify

Registers a function or method to be called when a control notification
is received via the [WM_NOTIFY](GuiOnNotify.htm#WM_NOTIFY) message.

``` Syntax
GuiCtrl.OnNotify(NotifyCode, Callback , AddRemove)
```

See [OnNotify](GuiOnNotify.htm) for details.
:::

::: {#Opt .methodShort}
### Opt

Sets various options and styles for the appearance and behavior of the
control.

``` Syntax
GuiCtrl.Opt(Options)
```

#### Parameters {#Opt_Parameters}

Options

:   Type: [String](../Concepts.htm#strings)

    Specify one or more [control-specific](GuiControls.htm) or
    [general](Gui.htm#OtherOptions) options and styles, each separated
    from the next with one or more spaces or tabs.

#### Remarks {#Opt_Remarks}

In the following example, the control is [disabled](Gui.htm#Disabled)
and its [background](Gui.htm#Background) is restored to the system
default:

    MyEdit.Opt("+Disabled -Background")

In the next example, the OK button is made the new default button:

    OKButton.Opt("+Default")

Although [styles](../misc/Styles.htm) and extended styles are also
recognized, some of them cannot be applied or removed after a control
has been created. Even if a change is successfully applied, the control
might choose to ignore it.
:::

::: {#Redraw .methodShort}
### Redraw

Redraws the region of the GUI window occupied by the control.

``` Syntax
GuiCtrl.Redraw()
```

Although this may cause an unwanted flickering effect when called
repeatedly and rapidly, it solves display artifacts for certain control
types such as [GroupBoxes](GuiControls.htm#GroupBox).
:::

::: {#SetFont .methodShort}
### SetFont

Sets the font typeface, size, style, and/or color for the control.

``` Syntax
GuiCtrl.SetFont(Options, FontName)
```

Omit both parameters to set the font to the GUI\'s current font, as set
by [Gui.SetFont](Gui.htm#SetFont). Otherwise, any font attributes which
are not specified will be copied from the control\'s previous font. Text
color is changed only if specified in *Options*.

For details about both parameters, see [Gui.SetFont](Gui.htm#SetFont).
:::

## Properties {#Properties}

::: {#ClassNN .methodShort}
### ClassNN

Retrieves the class name and sequence number (ClassNN) of the control.

``` Syntax
ClassNN := GuiCtrl.ClassNN
```

A control\'s ClassNN is the name of its window class followed by its
sequence number within the top-level window which contains it. For
example, \"Edit1\" is the first Edit control on a window and
\"Button12\" is the twelth button.

Related: [ControlGetClassNN](ControlGetClassNN.htm)
:::

::: {#Enabled .methodShort}
### Enabled

Retrieves or sets the interaction state of the control.

``` Syntax
CurrentSetting := GuiCtrl.Enabled
```

``` Syntax
GuiCtrl.Enabled := NewSetting
```

*CurrentSetting* is *NewSetting* if assigned, otherwise 1 (true) by
default unless overwritten by the [Disabled option](Gui.htm#Disabled).

*NewSetting* is a [boolean value](../Concepts.htm#boolean) that enables
or disables this setting. If true, the control is enabled. If false, the
control is disabled.

For Tab controls, this will also enable or disable all of the tab\'s
sub-controls. However, any sub-control explicitly disabled via
`GuiCtrl.Enabled := false` will remember that setting and thus remain
disabled even after its Tab control is re-enabled.
:::

::: {#Focused .methodShort}
### Focused

Retrieves the focus state of the control.

``` Syntax
IsFocused := GuiCtrl.Focused
```

*IsFocused* is 1 (true) if the control has the keyboard focus, otherwise
0 (false).

To be effective, the window generally must not be minimized or hidden.

To focus the control, use the [Focus method](#Focus).
:::

::: {#Gui .methodShort}
### Gui

Retrieves the [Gui object](Gui.htm) of the control\'s parent window.

``` Syntax
GuiObj := GuiCtrl.Gui
```
:::

::: {#Hwnd .methodShort}
### Hwnd

Retrieves the window handle (HWND) of the control.

``` Syntax
Hwnd := GuiCtrl.Hwnd
```

A control\'s HWND is often used with [PostMessage](PostMessage.htm),
[SendMessage](SendMessage.htm), and [DllCall](DllCall.htm). It can also
be used directly in a [Control parameter](Control.htm#Parameter).
:::

::: {#Name .methodShort}
### Name

Retrieves or sets the explicit name of the control.

``` Syntax
CurrentName := GuiCtrl.Name
```

``` Syntax
GuiCtrl.Name := NewName
```

*CurrentName* is *NewName* if assigned, otherwise an empty string by
default unless overwritten by the [V option](Gui.htm#var).

*NewName* is the control\'s new name, which can be used with
[Gui.\_\_Item](Gui.htm#__Item) to retrieve the GuiControl object. For
most input-capable controls, the name is also used by
[Gui.Submit](Gui.htm#Submit).
:::

::: {#Text .methodShort}
### Text

Retrieves or sets the text/caption of the control.

``` Syntax
CurrentText := GuiCtrl.Text
```

``` Syntax
GuiCtrl.Text := NewText
```

Note: If the control has no visible caption text and no (single) text
value, this property corresponds to the control\'s hidden caption text
(like
[ControlGetText](ControlGetText.htm)/[ControlSetText](ControlSetText.htm)).

*CurrentText* and *NewText* depend on the [control
type](GuiControls.htm):

**Button / CheckBox / Edit / GroupBox / Link / Radio / Text**

*CurrentText* and *NewText* are the caption/display text of the
[Button](GuiControls.htm#Button), [CheckBox](GuiControls.htm#CheckBox),
[Edit](GuiControls.htm#Edit), [GroupBox](GuiControls.htm#GroupBox),
[Link](GuiControls.htm#Link), [Radio](GuiControls.htm#Radio) or
[Text](GuiControls.htm#Text) control. Since the control will not expand
automatically, use `GuiCtrl.`[`Move`](#Move)`(,, 300)` or similar if the
control needs to be widened.

**DateTime**

*CurrentText* and *NewText* are the formatted text displayed by the
[DateTime](GuiControls.htm#DateTime) control. Assigning a formatted
date/time string to the control is not supported. To change the
date/time being displayed, assign the [Value property](#Value) a
date-time stamp in [YYYYMMDDHH24MISS](FileSetTime.htm#YYYYMMDD) format.

**DropDownList / ComboBox / ListBox / Tab**

*CurrentText* and *NewText* are the text of the currently selected
item/tab of the [DropDownList](GuiControls.htm#DropDownList),
[ComboBox](GuiControls.htm#ComboBox), [ListBox](GuiControls.htm#ListBox)
or [Tab](GuiControls.htm#Tab) control.

*NewText* should be the full text (case-insensitive) of the item/tab to
select.

For a ComboBox, if there is no selected item, the text in the control\'s
edit field is retrieved instead. For other controls, *CurrentText* is
empty/blank. Similarly, if *NewText* is empty/blank, the current
item/tab will be deselected.

For a [multi-select ListBox](GuiControls.htm#ListBoxMulti),
*CurrentText* is an array. *NewText* cannot be an array, but if multiple
items match, they are all selected. To select multiple items with
different text, call the [Choose method](#Choose) repeatedly.

To select an item by its position number instead of its text, use the
[Value property](#Value).

**Edit**

*CurrentText* and *NewText* are the text of the
[Edit](GuiControls.htm#Edit) control. As with other controls, the text
is retrieved or set as-is; no end-of-line translation is performed. To
retrieve or set the text of a multi-line Edit control while also
translating between `` `r`n `` and `` `n ``, use the [Value
property](#Value).

**StatusBar**

*CurrentText* and *NewText* are the text of the
[StatusBar](GuiControls.htm#StatusBar) control\'s first part only (use
[SB.SetText](GuiControls.htm#SB_SetText) for greater flexibility).
:::

::: {#Type .methodShort}
### Type

Retrieves the type of the control.

``` Syntax
CurrentType := GuiCtrl.Type
```

Depending on the [control type](GuiControls.htm),
`CurrentType`{.variable} is one of the following strings: ActiveX,
Button, CheckBox, ComboBox, Custom, DateTime, DDL, Edit, GroupBox,
Hotkey, Link, ListBox, ListView, MonthCal, Pic, Progress, Radio, Slider,
StatusBar, Tab, Tab2, Tab3, Text, TreeView, UpDown.
:::

::: {#Value .methodShort}
### Value

Retrieves or sets the contents of a value-capable control.

``` Syntax
CurrentValue := GuiCtrl.Value
```

``` Syntax
GuiCtrl.Value := NewValue
```

Note: If the control is not value-capable, *CurrentValue* will be blank
and assigning *NewValue* will raise an error. Invalid values throw an
exception.

*CurrentValue* and *NewValue* depend on the [control
type](GuiControls.htm):

**ActiveX**

*CurrentValue* is the ActiveX object of the
[ActiveX](GuiControls.htm#ActiveX) control. For example, if the control
was created with the text *Shell.Explorer*, this is a
[WebBrowser](https://learn.microsoft.com/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa752043(v=vs.85))
object. The same [wrapper object](ComValue.htm) is returned each time.

*NewValue* is invalid and throws an exception.

**CheckBox / Radio**

*CurrentValue* is 1 if the [CheckBox](GuiControls.htm#CheckBox) or
[Radio](GuiControls.htm#Radio) control is checked, 0 if it is unchecked,
or -1 if it has a gray checkmark.

*NewValue* can be 0 to uncheck the button, 1 to check it, or -1 to give
it a gray checkmark. For Radio buttons, if one is being checked (turned
on) and it is a member of a multi-radio group, the other radio buttons
in its group will be automatically unchecked.

To get or set control\'s text/caption instead, use the [Text
property](#Text).

**ComboBox / DropDownList / ListBox / Tab**

*CurrentValue* is the position number of the currently selected item/tab
in the [ComboBox](GuiControls.htm#ComboBox),
[DropDownList](GuiControls.htm#DropDownList),
[ListBox](GuiControls.htm#ListBox) or [Tab](GuiControls.htm#Tab)
control. If none is selected, zero is returned. If text is entered into
a ComboBox, the first item with matching text is used. If there is no
matching item, the result is zero even if there is text in the control.
For a [multi-select ListBox](GuiControls.htm#ListBoxMulti), the result
is an array of numbers (which is empty if no items are selected).

*NewValue* is the position number of a single item/tab to select, or
zero to clear the current selection (this is valid even for Tab
controls). To select multiple items, call the [Choose method](#Choose)
repeatedly.

To get or set the selected item given its text instead of its position,
use the [Text property](#Text).

**DateTime / MonthCal**

*CurrentValue* is a date-time stamp in
[YYYYMMDDHH24MISS](FileSetTime.htm#YYYYMMDD) format currently selected
in the [DateTime](GuiControls.htm#DateTime) or
[MonthCal](GuiControls.htm#MonthCal) control.

*NewValue* is a date-time stamp in
[YYYYMMDDHH24MISS](FileSetTime.htm#YYYYMMDD) format. Specify `A_Now` to
use the current date and time (today). For DateTime controls, *NewValue*
may be an empty string to cause the control to have no date/time
selected (if it was created with [that
ability](GuiControls.htm#ChooseNone)). For MonthCal controls, a range
may be specified if the control is
[multi-select](GuiControls.htm#MonthCalMulti).

**Edit**

*CurrentValue* is the current content of the
[Edit](GuiControls.htm#Edit) control. For multi-line controls, any line
breaks in the text will be represented as plain linefeeds (\`n) rather
than the traditional CR+LF (\`r\`n) used by non-GUI functions such as
[ControlGetText](ControlGetText.htm) and
[ControlSetText](ControlSetText.htm).

*NewValue* is the new content. For multi-line controls, Any linefeeds
(\`n) in *NewValue* that lack a preceding carriage return (\`r) are
automatically translated to CR+LF (\`r\`n) to make them display
properly. However, this is usually not a concern because when using
[Gui.Submit](Gui.htm#Submit) or when retrieving this value this
translation will be reversed automatically by replacing CR+LF with LF
(\`n).

To retrieve or set the text without translating \`n to or from \`r\`n,
use the [Text property](#Text).

**Hotkey**

*CurrentValue* is the modifiers and key name if there is a hotkey in the
[Hotkey](GuiControls.htm#Hotkey) control; otherwise blank. Examples:
`^!C`, `^Home`, `+^NumpadHome`.

*NewValue* can be a set of modifiers with a key name, or blank to clear
the control. Examples: `^!c`, `^Numpad1`, `+Home`. The only modifiers
supported are \^ (Control), ! (Alt), and + (Shift). See the [key
list](../KeyList.htm) for available key names.

**Picture**

*CurrentValue* is the picture\'s file name as it was originally
specified when the [Picture](GuiControls.htm#Picture) control was
created. This name does not change even if a new picture file name is
specified.

*NewValue* is the filename (or [handle](../misc/ImageHandles.htm)) of
the new image to load (see [Picture](GuiControls.htm#Picture) for
supported file types). Zero or more of the following options may be
specified immediately in front of the filename: `*wN` (width N), `*hN`
(height N), and `*IconN` (icon group number N in a DLL or EXE file). In
the following example, the default icon from the second icon group is
loaded with a width of 100 and an automatic height via \"keep aspect
ratio\": `MyPic.Value := "*icon2 *w100 *h-1 C:\My Application.exe"`.
Specify `*w0 *h0` to use the image\'s actual width and height. If `*w`
and `*h` are omitted, the image will be scaled to fit the current size
of the control. When loading from a multi-icon .ICO file, specifying a
width and height also determines which icon to load. Note: Use only one
space or tab between the final option and the filename itself; any other
spaces and tabs are treated as part of the filename.

**Progress / Slider / UpDown**

*CurrentValue* is the current position of the
[Progress](GuiControls.htm#Progress), [Slider](GuiControls.htm#Slider)
or [UpDown](GuiControls.htm#UpDown) control.

*NewValue* is the new position of the control, for example
`MySlider.Value := 10`. To adjust the value by a relative amount, use
the operators `+=`, `-=`, `++` or `--` instead of `:=`. If the new
position would be outside the range of the control, the control is
generally set to the nearest valid value.

**Text**

*CurrentValue* is the text/caption of the [Text](GuiControls.htm#Text)
control.

*NewValue* is the control\'s new text. Since the control will not expand
automatically, use `GuiCtrl.`[`Move`](#Move)`(,, 300)` if the control
needs to be widened.
:::

::: {#Visible .methodShort}
### Visible

Retrieves or sets the visibility state of the control.

``` Syntax
CurrentSetting := GuiCtrl.Visible
```

``` Syntax
GuiCtrl.Visible := NewSetting
```

*CurrentSetting* is *NewSetting* if assigned, otherwise 1 (true) by
default unless overwritten by the [Hidden option](Gui.htm#Hidden).

*NewSetting* is a [boolean value](../Concepts.htm#boolean) that enables
or disables this setting. If true, the control is visible. If false, the
control is hidden.

For Tab controls, this will also show or hide all of the tab\'s
sub-controls. If you additionally want to prevent a control\'s shortcut
key (underlined letter) from working, disable the control via
`GuiCtrl.Enabled := false`.
:::

## General Remarks {#GenRemarks}

### Redraw {#redraw-remarks}

When adding a large number of items to a control (such as a
[ListView](ListView.htm), [TreeView](TreeView.htm) or
[ListBox](GuiControls.htm#ListBox)), performance can be improved by
preventing the control from being redrawn while the changes are being
made. This is done by using `GuiCtrl.Opt("-Redraw")` before adding the
items and `GuiCtrl.Opt("+Redraw")` afterward. Changes to the control
which have not yet become visible prior to disabling redraw will
generally not become visible until after redraw is re-enabled.

For performance reasons, changes to a control\'s content generally do
not cause the control to be immediately redrawn even if redraw is
enabled. Instead, a portion of the control is \"invalidated\" and is
usually repainted after a brief delay, when the program checks its
internal message queue. The script can force this to take place
immediately by calling `Sleep -1`.
