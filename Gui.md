# Gui Object

``` NoIndent
class Gui extends Object
```

Provides an interface to create a window, add controls, modify the
window, and retrieve information about the window. Such windows can be
used as data entry forms or custom user interfaces.

Gui objects can be created with [Gui()](#Call) and retrieved with
[GuiFromHwnd](GuiFromHwnd.htm).

\"MyGui\" is used below as a placeholder for any Gui object (and a
variable name in examples), as \"Gui\" is the class itself.

In addition to the methods and property inherited from
[Object](Object.htm), Gui objects have the following predefined methods
and properties.

## Table of Contents {#toc}

-   [Static Methods](#Static_Methods):
    -   [Call](#Call): Creates a new window.
-   [Methods](#Methods):
    -   [Add](#Add): Creates a new control and adds it to the window.
    -   [Destroy](#Destroy): Deletes the window.
    -   [Flash](#Flash): Blinks the window and its taskbar button.
    -   [GetClientPos](#GetClientPos): Retrieves the position and size
        of the window\'s client area.
    -   [GetPos](#GetPos): Retrieves the position and size of the
        window.
    -   [Hide](#Hide): Hides the window.
    -   [Maximize](#Maximize): Unhides and maximizes the window.
    -   [Minimize](#Minimize): Unhides and minimizes the window.
    -   [Move](#Move): Moves and/or resizes the window.
    -   [OnEvent](#OnEvent): Registers a function or method to be called
        when the given event is raised.
    -   [Opt](#Opt): Sets various options and styles for the appearance
        and behavior of the window.
    -   [Restore](#Restore): Unhides and unminimizes or unmaximizes the
        window.
    -   [SetFont](#SetFont): Sets the typeface, size, style, and text
        color for subsequently created controls.
    -   [Show](#Show): Displays the window. It can also minimize,
        maximize, or move the window.
    -   [Submit](#Submit): Collects the values from named controls and
        composes them into an [Object](Object.htm). Optionally hides the
        window.
    -   [\_\_Enum](#__Enum): Enumerates the window\'s controls.
    -   [\_\_New](#__New): Constructs a new Gui instance.
-   [Properties](#Properties):
    -   [BackColor](#BackColor): Retrieves or sets the background color
        of the window.
    -   [FocusedCtrl](#FocusedCtrl): Retrieves the [GuiControl
        object](GuiControl.htm) of the window\'s focused control.
    -   [Hwnd](#Hwnd): Retrieves the window handle (HWND) of the window.
    -   [MarginX](#MarginX): Retrieves or sets the size of horizontal
        margins between sides and subsequently created controls.
    -   [MarginY](#MarginY): Retrieves or sets the size of vertical
        margins between sides and subsequently created controls.
    -   [MenuBar](#MenuBar): Retrieves or sets the window\'s menu bar.
    -   [Name](#Name): Retrieves or sets a custom name for the window.
    -   [Title](#Title): Retrieves or sets the window\'s title.
    -   [\_\_Item](#__Item): Retrieves the [GuiControl
        object](GuiControl.htm) associated with the specified name,
        text, ClassNN or HWND.
-   General:
    -   [Keyboard Navigation](#Navigate)
    -   [Window Appearance](#Appear)
    -   [General Remarks](#GenRemarks)
    -   [Related](#Related)
    -   [Examples](#Examples)

## Static Methods {#Static_Methods}

::: {#Call .methodShort}
### Call

Creates a new window.

``` Syntax
MyGui := Gui(Options, Title, EventObj)
MyGui := Gui.Call(Options, Title, EventObj)
```

#### Parameters {#Call_Parameters}

Options

:   Type: [String](../Concepts.htm#strings)

    Any of the options supported by [Gui.Opt](#Opt).

Title

:   Type: [String](../Concepts.htm#strings)

    If omitted, it defaults to
    [A_ScriptName](../Variables.htm#ScriptName). Otherwise, specify the
    window title.

EventObj

:   Type: [Object](../Concepts.htm#objects)

    An \"event sink\", or object to bind events to. If *EventObj* is
    specified, [OnEvent](GuiOnEvent.htm), [OnNotify](GuiOnNotify.htm)
    and [OnCommand](GuiOnCommand.htm) can be used to register methods of
    *EventObj* to be called when an event is raised.

#### Return Value {#Call_Return_Value}

Type: [Object](../Concepts.htm#objects)

This method or function returns a Gui object.
:::

## Methods {#Methods}

::: {#Add .methodShort}
### Add

Creates a new control and adds it to the window.

``` Syntax
GuiCtrl := MyGui.Add(ControlType , Options, Text)
GuiCtrl := MyGui.AddControlType(Options, Text)
```

#### Parameters {#Add_Parameters}

ControlType

:   Type: [String](../Concepts.htm#strings)

    This is one of the following: [ActiveX](GuiControls.htm#ActiveX),
    [Button](GuiControls.htm#Button),
    [CheckBox](GuiControls.htm#CheckBox),
    [ComboBox](GuiControls.htm#ComboBox),
    [Custom](GuiControls.htm#Custom),
    [DateTime](GuiControls.htm#DateTime), [DropDownList (or
    DDL)](GuiControls.htm#DropDownList), [Edit](GuiControls.htm#Edit),
    [GroupBox](GuiControls.htm#GroupBox),
    [Hotkey](GuiControls.htm#Hotkey), [Link](GuiControls.htm#Link),
    [ListBox](GuiControls.htm#ListBox),
    [ListView](GuiControls.htm#ListView),
    [MonthCal](GuiControls.htm#MonthCal), [Picture (or
    Pic)](GuiControls.htm#Picture),
    [Progress](GuiControls.htm#Progress),
    [Radio](GuiControls.htm#Radio), [Slider](GuiControls.htm#Slider),
    [StatusBar](GuiControls.htm#StatusBar), [Tab](GuiControls.htm#Tab),
    [Tab2](GuiControls.htm#Tab), [Tab3](GuiControls.htm#Tab),
    [Text](GuiControls.htm#Text), [TreeView](GuiControls.htm#TreeView),
    [UpDown](GuiControls.htm#UpDown)

    For example:

        MyGui := Gui()
        MyGui.Add("Text",, "Please enter your name:")
        MyGui.AddEdit("vName")
        MyGui.Show()

Options

:   Type: [String](../Concepts.htm#strings)

    If blank or omitted, the control starts off at its defaults.
    Otherwise, specify one or more of the following options and styles,
    each separated from the next with one or more spaces or tabs.

    **Positioning and Sizing of Controls**

    If some dimensions and/or coordinates are omitted from *Options*,
    the control will be positioned relative to the previous control
    and/or sized automatically according to its nature and contents.

    The following options are supported:

    **R***n*: Rows of text (where *n* is any number, even a floating
    point number such as `r2.5`{.no-highlight}). R is often preferable
    to specifying H (Height). If both the R and H options are present, R
    will take precedence. For a GroupBox, this setting is the number of
    controls for which to reserve space inside the box. For
    [DropDownLists](GuiControls.htm#DropDownList),
    [ComboBoxes](GuiControls.htm#ComboBox), and
    [ListBoxes](GuiControls.htm#ListBox), it is the number of items
    visible at one time inside the list portion of the control (but it
    is often desirable to omit both the R and H options for DropDownList
    and ComboBox, as the popup list will automatically take advantage of
    the available height of the user\'s desktop). For other control
    types, R is the number of rows of text that can visibly fit inside
    the control.

    **W***n*: Width (where *n* is any number in pixels). If omitted, the
    width is calculated automatically for some control types based on
    their contents; tab controls default to 30 times the current font
    size, plus 3 times the [X-margin](#MarginX); vertical Progress Bars
    default to two times the current font size; and horizontal Progress
    Bars, horizontal Sliders, DropDownLists, ComboBoxes, ListBoxes,
    GroupBoxes, Edits, and Hotkeys default to 15 times the current font
    size (except GroupBoxes, which multiply by 18 to provide room inside
    for margins).

    **H***n*: Height (where *n* is any number in pixels). If both the H
    and R options are absent, DropDownLists, ComboBoxes, ListBoxes, and
    empty multi-line Edit controls default to 3 rows; GroupBoxes default
    to 2 rows; vertical Sliders and Progress Bars default to 5 rows;
    horizontal Sliders default to 30 pixels (except if a thickness has
    been specified); horizontal Progress Bars default to 2 times the
    current font size; Hotkey controls default to 1 row; and Tab
    controls default to 10 rows. For the other control types, the height
    is calculated automatically based on their contents. Note that for
    DropDownLists and ComboBoxes, H is the combined height of the
    control\'s always-visible portion and its list portion (but even if
    the height is set too low, at least one item will always be visible
    in the list). Also, for all types of controls, specifying the number
    of rows via the R option is usually preferable to using H because it
    prevents a control from showing partial/incomplete rows of text.

    **WP***±n*, **HP***±n* (where *n* is any number in pixels) can be
    used to set the width and/or height of a control equal to the
    previously added control\'s width or height, with an optional plus
    or minus adjustment. For example, `wp` would set a control\'s width
    to that of the previous control, and `wp-50`{.no-highlight} would
    set it equal to 50 less than that of the previous control.

    **X***n*, **Y***n*: X-position, Y-position (where *n* is any number
    in pixels). For example, specifying `x0 y0` would position the
    control in the upper left corner of the window\'s client area, which
    is the area beneath the title bar and menu bar (if any).

    **X+***n*, **Y+***n* (where *n* is any number in pixels): An
    optional plus sign can be included to position a control relative to
    the right or bottom edge (respectively) of the control that was
    previously added. For example, specifying `y+10`{.no-highlight}
    would position the control 10 pixels beneath the bottom of the
    previous control rather than using the standard padding distance.
    Similarly, specifying `x+10`{.no-highlight} would position the
    control 10 pixels to the right of the previous control\'s right
    edge. Since negative numbers such as `x-10`{.no-highlight} are
    reserved for absolute positioning, to use a negative offset, include
    a plus sign in front of it. For example: `x+-10`{.no-highlight}.

    For X+ and Y+, the letter **M** can be used as a substitute for the
    window\'s current [margin](#MarginX). For example, `x+m` uses the
    right edge of the previous control plus the standard padding
    distance. `xp y+m` positions a control below the previous control,
    whereas specifying a relative X coordinate on its own (with XP or
    X+) would normally imply `yp` by default.

    **XP***±n*, **YP***±n* (where *n* is any number in pixels) can be
    used to position controls relative to the previous control\'s upper
    left corner, which is often useful for enclosing controls in a
    [GroupBox](GuiControls.htm#GroupBox).

    **XM***±n* and **YM***±n* (where *n* is any number in pixels) can be
    used to position a control at the leftmost and topmost
    [margins](#MarginX) of the window, respectively, with an optional
    plus or minus adjustment.

    **XS***±n* and **YS***±n* (where *n* is any number in pixels): These
    are similar to XM and YM except that they refer to coordinates that
    were saved by having previously added a control with the word
    [Section](#Section) in its options (the first control of the window
    always starts a new section, even if that word isn\'t specified in
    its options). For example:

        MyGui := Gui()
        MyGui.Add("Edit", "w600")  ; Add a fairly wide edit control at the top of the window.
        MyGui.Add("Text", "Section", "First Name:")  ; Save this control's position and start a new section.
        MyGui.Add("Text",, "Last Name:")
        MyGui.Add("Edit", "ys")  ; Start a new column within this section.
        MyGui.Add("Edit")
        MyGui.Show()

    XS and YS may optionally be followed by a plus/minus sign and a
    number. Also, it is possible to specify both the word
    [Section](#Section) and XS/YS in a control\'s options; this uses the
    previous section for itself but establishes a new section for
    subsequent controls.

    Omitting either X, Y or both is useful to make a GUI layout
    automatically adjust to any future changes you might make to the
    size of controls or font. By contrast, specifying an absolute
    position for every control might require you to manually shift the
    position of all controls that lie beneath and/or to the right of a
    control that is being enlarged or reduced.

    If both X and Y are omitted, the control will be positioned beneath
    the previous control using a standard padding distance (the current
    [margin](#MarginX)). Consecutive Text or Link controls are given
    additional vertical padding, so that they typically align better in
    cases where a column of Edit, DDL or similar-sized controls are
    later added to their right. To use only the standard vertical
    margin, specify `y+m` or any value for X.

    If only one component is omitted, its default value depends on which
    option was used to specify the other component:

      Specified X             Default for Y
      ----------------------- ----------------------------------------------------------------------------------------------------
      X*n* or XM              Beneath all previous controls (maximum Y extent plus margin).
      XS                      Beneath all previous controls since the most recent use of the [Section](#Section) option.
      X+*n* or XP+*nonzero*   Same as the previous control\'s top edge ([YP](#xp)).
      XP or XP+0              Below the previous control (bottom edge plus margin).
      Specified Y             Default for X
      Y*n* or YM              To the right of all previous controls (maximum X extent plus margin).
      YS                      To the right of all previous controls since the most recent use of the [Section](#Section) option.
      Y+*n* or YP+*nonzero*   Same as the previous control\'s left edge ([XP](#xp)).
      YP or YP+0              To the right of the previous control (right edge plus margin).

    **Storing and Responding to User Input**

    **V:** Sets the control\'s [Name](GuiControl.htm#Name). Specify the
    name immediately after the letter V, which is not included in the
    name. For example, specifying **`v`**`MyEdit` would name the control
    \"MyEdit\".

    **Events:** Event handlers (such as a function which is called
    automatically when the user clicks or changes a control) cannot be
    set within the control\'s *Options*. Instead, [OnEvent](#OnEvent)
    can be used to register a callback function or method for each event
    of interest.

    **Common Options and Styles for Controls**

    Note: In the absence of a preceding sign, a plus sign is assumed;
    for example, `Wrap` is the same as `+Wrap`. By contrast, `-Wrap`
    would remove the word-wrapping property.

    **AltSubmit:** Uses alternate submit method. For DropDownList,
    ComboBox, ListBox and Tab, this causes [Gui.Submit](#Submit) to
    store the position of the selected item rather than its text. If no
    item is selected, a ComboBox will still store the text of its edit
    field.

    **C:** Color of text (has no effect on
    [buttons](GuiControls.htm#Button) and [status
    bars](GuiControls.htm#StatusBar)). Specify the letter C followed
    immediately by a color name (see [color chart](../misc/Colors.htm))
    or RGB value (the 0x prefix is optional). Examples: `cRed`,
    `cFF2211`, `c0xFF2211`, `cDefault`.

    **Disabled:** Makes an input-capable control appear in a disabled
    state, which prevents the user from focusing or modifying its
    contents. Use [GuiControl.Enabled](GuiControl.htm#Enabled) to enable
    it later. Note: To make an Edit control read-only, specify the
    string `ReadOnly` instead. Also, the word Disabled may optionally be
    followed immediately by a 0 or 1 to indicate the starting state (0
    for enabled and 1 for disabled). In other words, `Disabled` and
    `"Disabled" VarContainingOne` are the same.

    **Hidden:** The control is initially invisible. Use
    [GuiControl.Visible](GuiControl.htm#Visible) to show it later. The
    word Hidden may optionally be followed immediately by a 0 or 1 to
    indicate the starting state (0 for visible and 1 for hidden). In
    other words, `Hidden` and `"Hidden" VarContainingOne` are the same.

    **Left:** Left-justifies the control\'s text within its available
    width. This option affects the following controls: Text, Edit,
    Button, CheckBox, Radio, UpDown, Slider, Tab, Tab2, GroupBox,
    DateTime.

    **Right:** Right-justifies the control\'s text within its available
    width. For checkboxes and radio buttons, this also puts the box
    itself on the right side of the control rather than the left. This
    option affects the following controls: Text, Edit, Button, CheckBox,
    Radio, UpDown, Slider, Tab, Tab2, GroupBox, DateTime, Link.

    **Center:** Centers the control\'s text within its available width.
    This option affects the following controls: Text, Edit, Button,
    CheckBox, Radio, Slider, GroupBox.

    **Section:** Starts a new section and saves this control\'s position
    for later use with the XS and YS positioning options described
    [above](#xs).

    **Tabstop:** Use `-Tabstop` (minus Tabstop) to have an input-capable
    control skipped over when the user presses [Tab]{.kbd} to navigate.

    **Wrap:** Enables word-wrapping of the control\'s contents within
    its available width. Since nearly all control types start off with
    word-wrapping enabled, use `-Wrap` to disable word-wrapping.

    **VScroll:** Provides a vertical scroll bar if appropriate for this
    type of control.

    **HScroll:** Provides a horizontal scroll bar if appropriate for
    this type of control. The rest of this paragraph applies to
    [ListBox](GuiControls.htm#ListBox) only. The horizontal scrolling
    width defaults to 3 times the width of the ListBox. To specify a
    different scrolling width, include a number immediately after the
    word HScroll. For example, `HScroll500` would allow 500 pixels of
    scrolling inside the ListBox. However, if the specified scrolling
    width is smaller than the width of the ListBox, no scroll bar will
    be shown (though the mere presence of `HScroll` makes it possible
    for the horizontal scroll bar to be added later via
    `MyScrollBar.`[`Opt`](GuiControl.htm#Opt)`("+HScroll500")`, which is
    otherwise impossible).

    **Uncommon Options and Styles for Controls**

    **BackgroundTrans:** Uses a transparent background, which allows any
    control that lies behind a Text, Picture, or GroupBox control to
    show through. For example, a transparent Text control displayed on
    top of a Picture control would make the text appear to be part of
    the picture. Use
    `GuiCtrl.`[`Opt`](GuiControl.htm#Opt)`("+Background")` to remove
    this option later. See [Picture control\'s AltSubmit
    section](GuiControls.htm#PicAltSubmit) for more information about
    transparent images. Known limitation: BackgroundTrans might not work
    properly for controls inside a [Tab control](GuiControls.htm#Tab)
    that contains a [ListView](ListView.htm). If a control type does not
    support this option, an error is thrown.

    **Background***Color*: Changes the background color of the control.
    Replace *Color* with a color name (see [color
    chart](../misc/Colors.htm)) or RGB value (the 0x prefix is
    optional). Examples: `BackgroundSilver`, `BackgroundFFDD99`. If this
    option is not used, or if `+Background` is used with no suffix, a
    [Text](GuiControls.htm#Text), [Picture](GuiControls.htm#Picture),
    [GroupBox](GuiControls.htm#GroupBox),
    [CheckBox](GuiControls.htm#CheckBox),
    [Radio](GuiControls.htm#Radio), [Slider](GuiControls.htm#Slider),
    [Tab](GuiControls.htm#Tab) or [Link](GuiControls.htm#Link) control
    uses the background color set by [Gui.BackColor](#BackColor) (or if
    none or other control type, the system\'s default background color).
    Specifying `BackgroundDefault` or `-Background` applies the
    system\'s default background color. For example, a control can be
    restored to the system\'s default color via
    `LV.Opt("+BackgroundDefault")`. If a control type does not support
    this option, an error is thrown.

    **Border:** Provides a thin-line border around the control. Most
    controls do not need this because they already have a type-specific
    border. When adding a border to an *existing* control, it might be
    necessary to increase the control\'s width and height by 1 pixel.

    **Redraw:** When used with [GuiControl.Opt](GuiControl.htm#Opt),
    this option enables or disables redraw (visual updates) for a
    control by sending it a [WM_SETREDRAW
    message](https://learn.microsoft.com/windows/win32/gdi/wm-setredraw).
    See [Redraw](GuiControl.htm#redraw-remarks) for more details.

    **Theme:** This option can be used to override the window\'s current
    theme setting for the newly created control. It has no effect when
    used on an existing control; however, this may change in a future
    version. See GUI\'s [+/-Theme](#Theme) option for details.

    **(Unnamed Style):** Specify a plus or minus sign followed
    immediately by a decimal or hexadecimal [style
    number](../misc/Styles.htm). If the sign is omitted, a plus sign is
    assumed.

    **(Unnamed ExStyle):** Specify a plus or minus sign followed
    immediately by the letter E and a decimal or hexadecimal extended
    style number. If the sign is omitted, a plus sign is assumed. For
    example, `E0x200` would add the WS_EX_CLIENTEDGE style, which
    provides a border with a sunken edge that might be appropriate for
    pictures and other controls. For other extended styles not
    documented here (since they are rarely used), see [Extended Window
    Styles \| Microsoft
    Docs](https://learn.microsoft.com/windows/win32/winmsg/extended-window-styles)
    for a complete list.

Text
:   Depending on the specified control type, a string, number or an
    array.

#### Return Value {#Add_Return_Value}

Type: [Object](../Concepts.htm#objects)

This method returns a [GuiControl object](GuiControl.htm).
:::

::: {#Destroy .methodShort}
### Destroy

Removes the window and all its controls, freeing the corresponding
memory and system resources.

``` Syntax
MyGui.Destroy()
```

If `MyGui.Destroy()` is not used, the window is automatically destroyed
when the Gui object is deleted (see [General Remarks](#deleted) for
details). All GUI windows are automatically destroyed when the script
exits.
:::

::: {#Flash .methodShort}
### Flash

Blinks the window\'s button in the taskbar.

``` Syntax
MyGui.Flash(Blink)
```

#### Parameters {#Flash_Parameters}

Blink

:   Type: [Boolean](../Concepts.htm#boolean)

    If omitted, it defaults to true.

    If **true**, the window\'s button in the taskbar will blink. This is
    done by inverting the color of the window\'s title bar and/or
    taskbar button (if it has one).

    If **false**, the original colors of the title bar and taskbar
    button will be restored (but the actual behavior might vary
    depending on OS version).

#### Remarks {#Flash_Remarks}

In the below example, the window will blink three times because each
pair of flashes inverts then restores its appearance:

    Loop 6
    {
        MyGui.Flash()
        Sleep 500  ; It's quite sensitive to this value; altering it may change the behavior in unexpected ways.
    }
:::

::: {#GetClientPos .methodShort}
### GetClientPos

Retrieves the position and size of the window\'s client area.

``` Syntax
MyGui.GetClientPos(&X, &Y, &Width, &Height)
```

#### Parameters {#GetClientPos_Parameters}

&X, &Y

:   Type: [VarRef](../Concepts.htm#variable-references)

    If omitted, the corresponding values will not be stored. Otherwise,
    specify references to the output variables in which to store the X
    and Y coordinates of the client area\'s upper left corner.

&Width, &Height

:   Type: [VarRef](../Concepts.htm#variable-references)

    If omitted, the corresponding values will not be stored. Otherwise,
    specify references to the output variables in which to store the
    width and height of the client area.

    Width is the horizontal distance between the left and right side of
    the client area, and height the vertical distance between the top
    and bottom side (in pixels).

#### Remarks {#GetClientPos_Remarks}

The client area is the part of the window which can contain controls. It
excludes the window\'s title bar, menu (if it has a standard one) and
borders. The position and size of the client area are less dependent on
OS version and theme than the values returned by [Gui.GetPos](#GetPos).

Unlike [WinGetClientPos](WinGetClientPos.htm), this method applies [DPI
scaling](#DPIScale) to *Width* and *Height* (unless the `-DPIScale`
option was used).
:::

::: {#GetPos .methodShort}
### GetPos

Retrieves the position and size of the window.

``` Syntax
MyGui.GetPos(&X, &Y, &Width, &Height)
```

#### Parameters {#GetPos_Parameters}

&X, &Y

:   Type: [VarRef](../Concepts.htm#variable-references)

    If omitted, the corresponding values will not be stored. Otherwise,
    specify references to the output variables in which to store the X
    and Y coordinates of the window\'s upper left corner, in screen
    coordinates.

&Width, &Height

:   Type: [VarRef](../Concepts.htm#variable-references)

    If omitted, the corresponding values will not be stored. Otherwise,
    specify references to the output variables in which to store the
    width and height of the window.

    Width is the horizontal distance between the left and right side of
    the window, and height the vertical distance between the top and
    bottom side (in pixels).

#### Remarks {#GetPos_Remarks}

As the coordinates returned by this method include the window\'s title
bar, menu and borders, they may be dependent on OS version and theme. To
get more consistent values across different systems, consider using
[Gui.GetClientPos](#GetClientPos) instead.

Unlike [WinGetPos](WinGetPos.htm), this method applies [DPI
scaling](#DPIScale) to *Width* and *Height* (unless the `-DPIScale`
option was used).
:::

::: {#Hide .methodShort}
### Hide

Hides the window.

``` Syntax
MyGui.Hide()
```
:::

::: {#Maximize .methodShort}
### Maximize

Unhides the window (if necessary) and maximizes it.

``` Syntax
MyGui.Maximize()
```
:::

::: {#Minimize .methodShort}
### Minimize

Unhides the window (if necessary) and minimizes it.

``` Syntax
MyGui.Minimize()
```
:::

::: {#Move .methodShort}
### Move

Moves and/or resizes the window.

``` Syntax
MyGui.Move(X, Y, Width, Height)
```

#### Parameters {#Move_Parameters}

X, Y

:   Type: [Integer](../Concepts.htm#numbers)

    If either is omitted, the position in that dimension will not be
    changed. Otherwise, specify the X and Y coordinates of the upper
    left corner of the window\'s new location, in screen coordinates.

Width, Height

:   Type: [Integer](../Concepts.htm#numbers)

    If either is omitted, the size in that dimension will not be
    changed. Otherwise, specify the new width and height of the window
    (in pixels).

#### Remarks {#Move_Remarks}

Unlike [WinMove](WinMove.htm), this method applies [DPI
scaling](#DPIScale) to *Width* and *Height* (unless the `-DPIScale`
option was used).

#### Examples {#Move_Examples}

    MyGui.Move(10, 20, 200, 100)
    MyGui.Move(VarX+10, VarY+5, VarW*2, VarH*1.5)

    ; Expand the left and right side by 10 pixels.
    MyGui.GetPos(&x,, &w)
    MyGui.Move(x-10,, w+20)
:::

::: {#OnEvent .methodShort}
### OnEvent

Registers a function or method to be called when the given event is
raised.

``` Syntax
MyGui.OnEvent(EventName, Callback , AddRemove)
```

See [OnEvent](GuiOnEvent.htm) for details.
:::

::: {#Opt .methodShort}
### Opt

Sets various options and styles for the appearance and behavior of the
window.

``` Syntax
MyGui.Opt(Options)
```

#### Parameters {#Opt_Parameters}

Options

:   Type: [String](../Concepts.htm#strings)

    Zero or more of the following options and styles, each separated
    from the next with one or more spaces or tabs.

    For performance reasons, it is better to set all options in a single
    line, and to do so before creating the window (that is, before any
    use of other methods such as [Gui.Add](#Add)).

    The effect of this parameter is cumulative; that is, it alters only
    those settings that are explicitly specified, leaving all the others
    unchanged.

    Specify a plus sign to add the option and a minus sign to remove it.
    For example: `MyGui.Opt("+Resize -MaximizeBox")`.

    **AlwaysOnTop:** Makes the window stay on top of all other windows,
    which is the same effect as
    [WinSetAlwaysOnTop](WinSetAlwaysOnTop.htm).

    **Border:** Provides a thin-line border around the window. This is
    not common.

    **Caption** (present by default): Provides a title bar and a thick
    window border/edge. When removing the caption from a window that
    will use [WinSetTransColor](WinSetTransColor.htm), remove it only
    after setting the TransColor.

    **Disabled:** Disables the window, which prevents the user from
    interacting with its controls. This is often used on a window that
    owns other windows (see [Owner](#Owner)).

    **DPIScale:** Use `MyGui.Opt("-DPIScale")` to disable [DPI
    scaling](../misc/DPIScaling.htm), which is enabled by default. If
    DPI scaling is enabled, coordinates and sizes passed to or retrieved
    from the Gui and [GuiControl](GuiControl.htm) methods/properties are
    automatically scaled based on [screen
    DPI](../Variables.htm#ScreenDPI). For example, with a DPI of 144
    (150 %), `MyGui.Show("w100")` would make the Gui 150 (100 \* 1.5)
    pixels wide, and resizing the window to 200 pixels wide via the
    mouse or [WinMove](WinMove.htm) would cause
    `MyGui.GetClientPos(,,&W)` to set *W* to 133 (200 // 1.5).
    [A_ScreenDPI](../Variables.htm#ScreenDPI) contains the system\'s
    current DPI.

    DPI scaling only applies to the Gui and [GuiControl](GuiControl.htm)
    methods/properties, so coordinates coming directly from other
    sources such as ControlGetPos or WinGetPos will not work. There are
    a number of ways to deal with this:

    -   Avoid using hard-coded coordinates wherever possible. For
        example, use the [XP](#xp), [XS](#xs), [XM](#xm) and
        [X+M](#PosPlusMargin) options for positioning controls and
        specify height in [rows of text](#R) instead of pixels.
    -   Enable (`MyGui.Opt("+DPIScale")`) and disable
        (`MyGui.Opt("-DPIScale")`) scaling on the fly, as needed.
        Changing the setting does not affect positions or sizes which
        have already been set.
    -   Manually scale the coordinates. For example,
        `x*(A_ScreenDPI/96)` converts x from logical/GUI coordinates to
        physical/non-GUI coordinates.

    **LastFound:** Sets the window to be the [last found
    window](../misc/WinTitle.htm#LastFoundWindow) (though this is
    unnecessary in a [GUI thread](GuiOnEvent.htm#Threads) because it is
    done automatically), which allows functions such as
    [WinGetStyle](WinGetStyle.htm) and
    [WinSetTransparent](WinSetTransparent.htm) to operate on it even if
    it is hidden (that is,
    [DetectHiddenWindows](DetectHiddenWindows.htm) is not necessary).
    This is especially useful for changing the properties of the window
    before showing it. For example:

        MyGui.Opt("+LastFound")
        WinSetTransColor(CustomColor " 150")
        MyGui.Show()

    **MaximizeBox:** Enables the maximize button in the title bar. This
    is also included as part of *Resize* below.

    **MinimizeBox** (present by default): Enables the minimize button in
    the title bar.

    **MinSize** and **MaxSize**: Determines the minimum and/or maximum
    size of the window, such as when the user drags its edges to resize
    it. Specify `+MinSize` and/or `+MaxSize` (i.e. without suffix) to
    use the window\'s current size as the limit (if the window has no
    current size, it will use the size from the first use of
    [Gui.Show](#Show)). Alternatively, append the width, followed by an
    X, followed by the height; for example:
    `MyGui.Opt("+Resize +MinSize640x480")`. The dimensions are in
    pixels, and they specify the size of the window\'s client area
    (which excludes borders, title bar, and [menu bar](#MenuBar)).
    Specify each number as decimal, not hexadecimal.

    Either the width or the height may be omitted to leave it unchanged
    (e.g. `+MinSize640x` or `+MinSizex480`). Furthermore, Min/MaxSize
    can be specified more than once to use the window\'s current size
    for one dimension and an explicit size for the other. For example,
    `+MinSize +MinSize640x` would use the window\'s current size for the
    height and 640 for the width.

    If MinSize and MaxSize are never used, the operating system\'s
    defaults are used (similarly, `MyGui.Opt("-MinSize -MaxSize")` can
    be used to return to the defaults). Note: the window must have
    [+Resize](#Resize) to allow resizing by the user.

    **OwnDialogs:** `MyGui.Opt("+OwnDialogs")` should be specified in
    each [thread](../misc/Threads.htm) (such as a event handling
    function of a Button control) for which subsequently displayed
    [MsgBox](MsgBox.htm), [InputBox](InputBox.htm),
    [FileSelect](FileSelect.htm), and [DirSelect](DirSelect.htm) dialogs
    should be owned by the window. Such dialogs are modal, meaning that
    the user cannot interact with the GUI window until dismissing the
    dialog. By contrast, [ToolTip](ToolTip.htm) windows do not become
    modal even though they become owned; they will merely stay always on
    top of their owner. In either case, any owned dialog or window is
    automatically destroyed when its GUI window is
    [destroyed](#Destroy).

    There is typically no need to turn this setting back off because it
    does not affect other [threads](../misc/Threads.htm). However, if a
    thread needs to display both owned and unowned dialogs, it may turn
    off this setting via `MyGui.Opt("-OwnDialogs")`.

    **Owner:** Use `+Owner` to make the window owned by another. An
    owned window has no taskbar button by default, and when visible it
    is always on top of its owner. It is also automatically destroyed
    when its owner is destroyed, as long as the owner was created by the
    same script (i.e. has the same [process
    ID](../misc/WinTitle.htm#ahk_pid)). `+Owner` can be used before or
    after the owned window is created. There are two ways to use
    `+Owner`, as shown below:

        MyGui.Opt("+Owner" OtherGui.Hwnd)  ; Make the GUI owned by OtherGui.
        MyGui.Opt("+Owner")  ; Make the GUI owned by the script's main window to prevent display of a taskbar button.

    `+Owner` can be immediately followed by the [HWND](#Hwnd) of any
    top-level window.

    To prevent the user from interacting with the owner while one of its
    owned window is visible, disable the owner via
    `MyGui.Opt("+Disabled")`. Later (when the time comes to cancel or
    destroy the owned window), re-enable the owner via
    `MyGui.Opt("-Disabled")`. Do this prior to cancel/destroy so that
    the owner will be reactivated automatically.

    **Parent:** Use `+Parent` immediately followed by the [HWND](#Hwnd)
    of any window or control to use it as the parent of this window. To
    convert the GUI back into a top-level window, use `-Parent`. This
    option works even after the window is created. Known limitations:

    -   [Running with UI access](../Program.htm#Installer_uiAccess)
        prevents the `+Parent` option from working on an existing window
        if the new parent is always-on-top and the child window is not.
    -   The `+Parent` option may fail during GUI creation if the parent
        window is external, but may work after the GUI is created. This
        is due to differences in how styles are applied.

    **Resize:** Makes the window resizable and enables its maximize
    button in the title bar. To avoid enabling the maximize button,
    specify `+Resize -MaximizeBox`.

    **SysMenu** (present by default): Specify `-SysMenu` (minus SysMenu)
    to omit the system menu and icon in the window\'s upper left corner.
    This will also omit the minimize, maximize, and close buttons in the
    title bar.

    **Theme:** By specifying `-Theme`, all subsequently created controls
    in the window will have the Classic Theme appearance. To later
    create additional controls that obey the current theme, turn it back
    on via `+Theme`. Note: This option has no effect if the Classic
    Theme is in effect. Finally, this setting may be changed for an
    individual control by specifying `+Theme` or `-Theme` in its options
    when it is created.

    **ToolWindow:** Provides a narrower title bar but the window will
    have no taskbar button. This always hides the maximize and minimize
    buttons, regardless of whether the
    [WS_MAXIMIZEBOX](../misc/Styles.htm#WS_MAXIMIZEBOX) and
    [WS_MINIMIZEBOX](../misc/Styles.htm#WS_MINIMIZEBOX) styles are
    present.

    **(Unnamed Style):** Specify a plus or minus sign followed
    immediately by a decimal or hexadecimal [style
    number](../misc/Styles.htm).

    **(Unnamed ExStyle):** Specify a plus or minus sign followed
    immediately by the letter E and a decimal or hexadecimal extended
    style number. For example, `+E0x40000` would add the WS_EX_APPWINDOW
    style, which provides a taskbar button for a window that would
    otherwise lack one. For other extended styles not documented here
    (since they are rarely used), see [Extended Window Styles \|
    Microsoft
    Docs](https://learn.microsoft.com/windows/win32/winmsg/extended-window-styles)
    for a complete list.
:::

::: {#Restore .methodShort}
### Restore

Unhides the window (if necessary) and unminimizes or unmaximizes it.

``` Syntax
MyGui.Restore()
```
:::

::: {#SetFont .methodShort}
### SetFont

Sets the font typeface, size, style, and/or color for controls added to
the window from this point onward.

``` Syntax
MyGui.SetFont(Options, FontName)
```

#### Parameters {#SetFont_Parameters}

Options

:   Type: [String](../Concepts.htm#strings)

    Zero or more options. Each option is either a single letter
    immediately followed by a value, or a single word. To specify more
    than one option, include a space between each. For example:
    `cBlue s12 bold`.

    The following words are supported: **bold**, *italic*, ~~strike~~,
    [underline]{.underline}, and norm. *Norm* returns the font to normal
    weight/boldness and turns off italic, strike, and underline (but it
    retains the existing color and size). It is possible to use norm to
    turn off all attributes and then selectively turn on others. For
    example, specifying `norm italic` would set the font to normal then
    to italic.

    **C:** Color name (see [color chart](../misc/Colors.htm)) or RGB
    value \-- or specify the word Default to return to the system\'s
    default color (black on most systems). Example values: `cRed`,
    `cFFFFAA`, `cDefault`. Note: [Buttons](GuiControls.htm#Button) and
    [status bars](GuiControls.htm#StatusBar) do not obey custom colors.
    Also, an individual control can be created with a font color other
    than the current one by including the C option. For example:
    `MyGui.Add("Text", "cRed", "My Text")`.

    **S:** Size (in points). For example: `s12` (specify decimal, not
    hexadecimal)

    **W:** Weight (boldness), which is a number between 1 and 1000 (400
    is normal and 700 is bold). For example: `w600` (specify decimal,
    not hexadecimal)

    **Q:** Text rendering quality. For example: `q3`. Q should be
    followed by a number from the following table:

      Number   Windows Constant         Description
      -------- ------------------------ -------------------------------------------------------------------------------------------------------------------
      0        DEFAULT_QUALITY          Appearance of the font does not matter.
      1        DRAFT_QUALITY            Appearance of the font is less important than when the PROOF_QUALITY value is used.
      2        PROOF_QUALITY            Character quality of the font is more important than exact matching of the logical-font attributes.
      3        NONANTIALIASED_QUALITY   Font is never antialiased, that is, font smoothing is not done.
      4        ANTIALIASED_QUALITY      Font is antialiased, or smoothed, if the font supports it and the size of the font is not too small or too large.
      5        CLEARTYPE_QUALITY        If set, text is rendered (when possible) using ClearType antialiasing method.

    For more details of what these values mean, see [Microsoft Docs:
    CreateFont](https://learn.microsoft.com/windows/win32/api/wingdi/nf-wingdi-createfonta).

    Since the highest quality setting is usually the default, this
    feature is more typically used to disable anti-aliasing in specific
    cases where doing so makes the text clearer.

FontName

:   Type: [String](../Concepts.htm#strings)

    *FontName* may be the name of any font, such as one from the [font
    table](../misc/FontsStandard.htm). If *FontName* is omitted or does
    not exist on the system, the previous font\'s typeface will be used
    (or if none, the system\'s default GUI typeface). This behavior is
    useful to make a GUI window have a similar font on multiple systems,
    even if some of those systems lack the preferred font. For example,
    by using the following methods in order, Verdana will be given
    preference over Arial, which in turn is given preference over MS
    Sans Serif:

        MyGui.SetFont(, "MS Sans Serif")
        MyGui.SetFont(, "Arial")
        MyGui.SetFont(, "Verdana")  ; Preferred font.

#### Remarks {#SetFont_Remarks}

Omit both parameters to restore the font to the system\'s default GUI
typeface, size, and color. Otherwise, any font attributes which are not
specified will be copied from the previous font.

On a related note, the operating system offers standard dialog boxes
that prompt the user to pick a font, color, or icon. These dialogs can
be displayed via [DllCall](DllCall.htm) in combination with
[comdlg32\\ChooseFont](https://learn.microsoft.com/previous-versions/windows/desktop/legacy/ms646914(v=vs.85)),
[comdlg32\\ChooseColor](https://learn.microsoft.com/previous-versions/windows/desktop/legacy/ms646912(v=vs.85)),
or
[shell32\\PickIconDlg](https://learn.microsoft.com/windows/win32/api/shlobj_core/nf-shlobj_core-pickicondlg).
Search the forums for examples.
:::

::: {#Show .methodShort}
### Show

By default, this makes the window visible, unminimizes it (if necessary)
and [activates](WinActivate.htm) it.

``` Syntax
MyGui.Show(Options)
```

#### Parameters {#Show_Parameters}

Options

:   Type: [String](../Concepts.htm#strings)

    Omit the X, Y, W, and H options below to have the window retain its
    previous size and position. If there is no previous position, the
    window will be auto-centered in one or both dimensions if the X
    and/or Y options mentioned below are absent. If there is no previous
    size, the window will be auto-sized according to the size and
    positions of the controls it contains.

    Zero or more of the following strings may be present in *Options*
    (specify each number as decimal, not hexadecimal):

    **W***n*: Specify for *n* the width (in pixels) of the window\'s
    client area (the client area excludes the window\'s borders, title
    bar, and [menu bar](#MenuBar)).

    **H***n*: Specify for *n* the height of the window\'s client area,
    in pixels.

    **X***n*: Specify for *n* the window\'s X-position on the screen, in
    pixels. Position 0 is the leftmost column of pixels visible on the
    screen.

    **Y***n*: Specify for *n* the window\'s Y-position on the screen, in
    pixels. Position 0 is the topmost row of pixels visible on the
    screen.

    **Center:** Centers the window horizontally and vertically on the
    screen.

    **xCenter:** Centers the window horizontally on the screen. For
    example: `MyGui.Show("xCenter y0")`.

    **yCenter:** Centers the window vertically on the screen.

    **AutoSize:** Resizes the window to accommodate only its currently
    visible controls. This is useful to resize the window after new
    controls are added, or existing controls are resized, hidden, or
    unhidden. For example: `MyGui.Show("AutoSize Center")`.

    ***One of the following may also be present:***

    **Minimize:** Minimizes the window and activates the one beneath it.

    **Maximize:** Maximizes and activates the window.

    **Restore:** Unminimizes or unmaximizes the window, if necessary.
    The window is also shown and activated, if necessary.

    **NoActivate:** Unminimizes or unmaximizes the window, if necessary.
    The window is also shown without activating it.

    **NA:** Shows the window without activating it. If the window is
    minimized, it will stay that way but will probably rise higher in
    the z-order (which is the order seen in the alt-tab selector). If
    the window was previously hidden, this will probably cause it to
    appear on top of the active window even though the active window is
    not deactivated.

    **Hide:** Hides the window and activates the one beneath it. This is
    identical in function to [Gui.Hide](#Hide) except that it allows a
    hidden window to be moved or resized without showing it. For
    example: `MyGui.Show("Hide x55 y66 w300 h200")`.
:::

::: {#Submit .methodShort}
### Submit

Collects the values from named controls and composes them into an
[Object](Object.htm). Optionally hides the window.

``` Syntax
NamedCtrlValues := MyGui.Submit(Hide)
```

#### Parameters {#Submit_Parameters}

Hide

:   Type: [Boolean](../Concepts.htm#boolean)

    If omitted, it defaults to true.

    If **true**, the window will be hidden.

    If **false**, the window will not be hidden.

#### Return Value {#Submit_Return_Value}

Type: [Object](../Concepts.htm#objects)

This method returns an object that contains one own property per named
control, like
`NamedCtrlValues.%GuiCtrl.`[`Name`](GuiControl.htm#Name)`% := GuiCtrl.`[`Value`](GuiControl.htm#Value),
with the exceptions noted below. Only input-capable controls which
support [GuiControl.Value](GuiControl.htm#Value) and have been given a
name are included. Use `NamedCtrlValues.NameOfControl` to retrieve an
individual value or [OwnProps](Object.htm#OwnProps) to enumerate them
all.

For [DropDownList](GuiControls.htm#DropDownList),
[ComboBox](GuiControls.htm#ComboBox), [ListBox](GuiControls.htm#ListBox)
and [Tab](GuiControls.htm#Tab), the text of the selected item/tab is
stored instead of its position number if the control [lacks]{.underline}
the [AltSubmit](#AltSubmit) option, or if the ComboBox\'s text does not
match a list item. Otherwise, [Value](GuiControl.htm#Value) (the item\'s
position number) is stored.

If only one [Radio](GuiControls.htm#Radio) button in a radio group has a
name, Submit stores the number of the currently selected button instead
of the control\'s [Value](GuiControl.htm#Value). 1 is the first radio
button (according to original creation order), 2 is the second, and so
on. If there is no button selected, 0 is stored.

Excluded because they are not input-capable:
[Text](GuiControls.htm#Text), [Pic](GuiControls.htm#Pic),
[GroupBox](GuiControls.htm#GroupBox), [Button](GuiControls.htm#Button),
[Progress](GuiControls.htm#Progress), [Link](GuiControls.htm#Link),
[StatusBar](GuiControls.htm#StatusBar).

Also excluded: [ListView](ListView.htm), [TreeView](TreeView.htm),
[ActiveX](GuiControls.htm#ActiveX), [Custom](GuiControls.htm#Custom).
:::

::: {#__Enum .methodShort}
### \_\_Enum

Enumerates the window\'s controls.

``` Syntax
For Ctrl in MyGui
```

``` Syntax
For Hwnd, Ctrl in MyGui
```

Returns a new [enumerator](Enumerator.htm). This method is typically not
called directly. Instead, the Gui object is passed directly to a
[for-loop](For.htm), which calls \_\_Enum once and then calls the
enumerator once for each iteration of the loop. Each call to the
enumerator returns the next control. The for-loop\'s variables
correspond to the enumerator\'s parameters, which are:

Hwnd

:   Type: [Integer](../Concepts.htm#numbers)

    The control\'s HWND. This is present only in the two-parameter mode.

Ctrl

:   Type: [Object](../Concepts.htm#objects)

    The control\'s [GuiControl object](GuiControl.htm).

For example:

    For Hwnd, GuiCtrlObj in MyGui
        MsgBox "Control #" A_Index " is " GuiCtrlObj.ClassNN
:::

::: {#__New .methodShort}
### \_\_New

Constructs a new Gui instance.

``` Syntax
MyGui.__New(Options, Title, EventObj)
```

A Gui subclass may override \_\_New and call
`super.__New(Options, Title, this)` to handle its own events. In such
cases, events for the main window (such as Close) do not pass an
explicit Gui parameter, as `this` already contains a reference to the
Gui.

The Gui retains a reference to *EventObj* for the purpose of calling
event handlers, and releases it when the window is destroyed. If
*EventObj* itself contains a reference to the Gui, this would typically
create a circular reference which prevents the Gui from being
[automatically destroyed](#Destroy). However, an exception is made for
when *EventObj* is the Gui itself, to avoid a circular reference in that
case.

An exception is thrown if the window has already been constructed or
destroyed.
:::

## Properties {#Properties}

::: {#BackColor .methodShort}
### BackColor

Retrieves or sets the background color of the window.

``` Syntax
CurrentColor := MyGui.BackColor
```

``` Syntax
MyGui.BackColor := NewColor
```

*CurrentColor* is a 6-digit RGB value of the current color previously
set by this property, or an empty string if the default color is being
used.

*NewColor* is one of the 16 primary [HTML color
names](../misc/Colors.htm), a hexadecimal RGB color value (the 0x prefix
is optional), a pure numeric RGB color value, or the word Default (or an
empty string) for its default color. Example values: `"Silver"`,
`"FFFFAA"`, `0xFFFFAA`, `"Default"`, `""`.

By default, the window\'s background color is the system\'s color for
the face of buttons.

The color of the [menu bar](#MenuBar) and its submenus can be changed as
in this example: `MyMenuBar.`[`SetColor`](Menu.htm#SetColor)` "White"`.

To make the background transparent, use
[WinSetTransColor](WinSetTransColor.htm). However, if you do this
without first having assigned a custom window via
[Gui.BackColor](#BackColor), buttons will also become transparent. To
prevent this, first assign a custom color and then make that color
transparent. For example:

    MyGui.BackColor := "EEAA99"
    WinSetTransColor("EEAA99", MyGui)

To additionally remove the border and title bar from a window with a
transparent background, use the following: `MyGui.Opt("-Caption")`

To illustrate the above, there is an example of an on-screen display
(OSD) near the bottom of this page.
:::

::: {#FocusedCtrl .methodShort}
### FocusedCtrl

Retrieves the [GuiControl object](GuiControl.htm) of the window\'s
focused control.

``` Syntax
GuiCtrlObj := MyGui.FocusedCtrl
```

Note: To be effective, the window generally must not be minimized or
hidden.
:::

::: {#Hwnd .methodShort}
### Hwnd

Retrieves the window handle (HWND) of the window.

``` Syntax
CurrentHwnd := MyGui.Hwnd
```

A GUI\'s HWND is often used with [PostMessage](PostMessage.htm),
[SendMessage](SendMessage.htm), and [DllCall](DllCall.htm). It can also
be used directly in a [WinTitle parameter](../misc/WinTitle.htm#ahk_id).
:::

::: {#MarginX .methodShort}
### MarginX

Retrieves or sets the size of horizontal margins between sides and
subsequently created controls.

``` Syntax
CurrentValue := MyGui.MarginX
```

``` Syntax
MyGui.MarginX := NewValue
```

*CurrentValue* is the number of pixels of the current horizontal margin.

*NewValue* is the number of pixels of space to leave at the left and
right side of the window when auto-positioning any control that lacks an
explicit [X coordinate](#XY). Also, the margin is used to determine the
horizontal distance that separates auto-positioned controls from each
other. Finally, the margin is taken into account by the first use of
[Gui.Show](#Show) to calculate the window\'s size (when no explicit size
is specified).

By default, this margin is proportional to the size of the currently
selected [font](#SetFont) (1.25 times font-height for left & right).
:::

::: {#MarginY .methodShort}
### MarginY

Retrieves or sets the size of vertical margins between sides and
subsequently created controls.

``` Syntax
CurrentValue := MyGui.MarginY
```

``` Syntax
MyGui.MarginY := NewValue
```

*CurrentValue* is the number of pixels of the current vertical margin.

*NewValue* is the number of pixels of space to leave at the top and
bottom side of the window when auto-positioning any control that lacks
an explicit [Y coordinate](#XY). Also, the margin is used to determine
the vertical distance that separates auto-positioned controls from each
other. Finally, the margin is taken into account by the first use of
[Gui.Show](#Show) to calculate the window\'s size (when no explicit size
is specified).

By default, this margin is proportional to the size of the currently
selected [font](#SetFont) (0.75 times font-height for top & bottom).
:::

::: {#MenuBar .methodShort}
### MenuBar

Retrieves or sets the window\'s menu bar.

``` Syntax
CurrentBar := MyGui.MenuBar
```

``` Syntax
MyGui.MenuBar := NewBar
```

*CurrentBar* and *NewBar* are a [MenuBar object](Menu.htm) created by
[MenuBar()](Menu.htm#Call). For example:

    FileMenu := Menu()
    FileMenu.Add("&Open`tCtrl+O", (*) => FileSelect())  ; See remarks below about Ctrl+O.
    FileMenu.Add("E&xit", (*) => ExitApp())
    HelpMenu := Menu()
    HelpMenu.Add("&About", (*) => MsgBox("Not implemented"))
    Menus := MenuBar()
    Menus.Add("&File", FileMenu)  ; Attach the two submenus that were created above.
    Menus.Add("&Help", HelpMenu)
    MyGui := Gui()
    MyGui.MenuBar := Menus
    MyGui.Show("w300 h200")

In the first line above, notice that `&Open` is followed by `Ctrl+O`
(with a tab character in between). This indicates a keyboard shortcut
that the user may press instead of selecting the menu item. If the
shortcut uses only the standard modifier key names Ctrl, Alt and Shift,
it is automatically registered as a *keyboard accelerator* for the GUI.
Single-character accelerators with no modifiers are case-sensitive and
can be triggered by unusual means such as IME or [Alt]{.kbd}+NNNN.

If a particular key combination does not work automatically, the use of
a [context-sensitive hotkey](_HotIf.htm) may be required. However, such
hotkeys typically cannot be triggered by [Send](Send.htm) and are more
likely to interfere with other scripts than a standard keyboard
accelerator.

To remove a window\'s current menu bar, use `MyGui.MenuBar := ""` (that
is, assign an empty string).
:::

::: {#Name .methodShort}
### Name

Retrieves or sets a custom name for the window.

``` Syntax
CurrentName := MyGui.Name
```

``` Syntax
MyGui.Name := NewName
```
:::

::: {#Title .methodShort}
### Title

Retrieves or sets the window\'s title.

``` Syntax
CurrentTitle := MyGui.Title
```

``` Syntax
MyGui.Title := NewTitle
```
:::

::: {#__Item .methodShort}
### \_\_Item

Retrieves the [GuiControl object](GuiControl.htm) associated with the
specified name, text, ClassNN or HWND.

``` Syntax
GuiCtrlObj := MyGui[Name]
GuiCtrlObj := MyGui.__Item[Name]
```
:::

## Keyboard Navigation {#Navigate}

A GUI window may be navigated via [Tab]{.kbd}, which moves keyboard
focus to the next input-capable control (controls from which the
[Tabstop](#Tabstop) style has been removed are skipped). The order of
navigation is determined by the order in which the controls were
originally added. When the window is shown for the first time, the first
input-capable control that has the Tabstop style (which most control
types have by default) will have keyboard focus, unless that control is
a Button and there is a Default button, in which case the latter is
focused instead.

Certain controls may contain an ampersand (&) to create a keyboard
shortcut, which might be displayed in the control\'s text as an
underlined character (depending on system settings). A user activates
the shortcut by holding down [Alt]{.kbd} then typing the corresponding
character. For buttons, checkboxes, and radio buttons, pressing the
shortcut is the same as clicking the control. For GroupBoxes and Text
controls, pressing the shortcut causes keyboard focus to jump to the
first input-capable [tabstop](#Tabstop) control that was created after
it. However, if more than one control has the same shortcut key,
pressing the shortcut will alternate keyboard focus among all controls
with the same shortcut.

To display a literal ampersand inside the control types mentioned above,
specify two consecutive ampersands as in this example:
`MyGui.Add("Button",, "Save && Exit")`.

## Window Appearance {#Appear}

For its icon, a GUI window uses the [tray
icon](../Program.htm#tray-icon) that was in effect at the time the
window was created. Thus, to have a different icon, change the tray icon
before creating the window. For example:
[`TraySetIcon`](TraySetIcon.htm)`("MyIcon.ico")`. It is also possible to
have a different large icon for a window than its small icon (the large
icon is displayed in the alt-tab task switcher). This can be done via
[LoadPicture](LoadPicture.htm) and [SendMessage](SendMessage.htm); for
example:

    iconsize := 32  ; Ideal size for alt-tab varies between systems and OS versions.
    hIcon := LoadPicture("My Icon.ico", "Icon1 w" iconsize " h" iconsize, &imgtype)
    MyGui := Gui()
    SendMessage(0x0080, 1, hIcon, MyGui)  ; 0x0080 is WM_SETICON; and 1 means ICON_BIG (vs. 0 for ICON_SMALL).
    MyGui.Show()

Due to OS limitations, Checkboxes, Radio buttons, and GroupBoxes for
which a non-default text color was specified will take on the Classic
Theme appearance.

Related topic: [window\'s margin](#MarginX).

## General Remarks {#GenRemarks}

Use the [GuiControl object](GuiControl.htm) to operate upon individual
controls in a GUI window.

Each GUI window may have up to 11,000 controls. However, use caution
when creating more than 5000 controls because system instability may
occur for certain control types.

The GUI window is automatically [destroyed](#Destroy) when the Gui
object is deleted, which occurs when its [reference
count](../Objects.htm#Reference_Counting) reaches zero. However, this
does not typically occur while the window is visible, as [Show](#Show)
automatically increments the reference count. While the window is
visible, the user can interact with it and raise events which are
handled by the script. When the user closes the window or it is hidden
by [Hide](#Hide), [Show](#Show) or [Submit](#Submit), this extra
reference is released.

To keep a GUI window \"alive\" without calling [Show](#Show) or
retaining a reference to its Gui object, the script can increment the
object\'s reference count with [ObjAddRef](ObjAddRef.htm) (in which case
[ObjRelease](ObjAddRef.htm) must be called when the window is no longer
needed). For example, this might be done when using a hidden GUI window
to [receive messages](OnMessage.htm), or if the window is shown by
\"external\" means such as [WinShow](WinShow.htm) (by this script or any
other).

If the script is not [persistent](../Scripts.htm#persistent) for any
other reason, it will exit after the last visible GUI is closed; either
when the last thread completes or immediately if no threads are running.

## Related {#Related}

[GuiControl object](GuiControl.htm), [GuiFromHwnd](GuiFromHwnd.htm),
[GuiCtrlFromHwnd](GuiCtrlFromHwnd.htm), [Control
Types](GuiControls.htm), [ListView](ListView.htm),
[TreeView](TreeView.htm), [Menu object](Menu.htm), [Control
functions](Control.htm), [MsgBox](MsgBox.htm),
[FileSelect](FileSelect.htm), [DirSelect](DirSelect.htm)

## Examples {#Examples}

::: {#ExPopup .ex}
[](#ExPopup){.ex_number} Creates a popup window.

    MyGui := Gui(, "Title of Window")
    MyGui.Opt("+AlwaysOnTop +Disabled -SysMenu +Owner")  ; +Owner avoids a taskbar button.
    MyGui.Add("Text",, "Some text to display.")
    MyGui.Show("NoActivate")  ; NoActivate avoids deactivating the currently active window.
:::

::: {#ExInputBox .ex}
[](#ExInputBox){.ex_number} Creates a simple input-box that asks for the
first and last name.

    MyGui := Gui(, "Simple Input Example")
    MyGui.Add("Text",, "First name:")
    MyGui.Add("Text",, "Last name:")
    MyGui.Add("Edit", "vFirstName ym")  ; The ym option starts a new column of controls.
    MyGui.Add("Edit", "vLastName")
    MyGui.Add("Button", "default", "OK").OnEvent("Click", ProcessUserInput)
    MyGui.OnEvent("Close", ProcessUserInput)
    MyGui.Show()

    ProcessUserInput(*)
    {
        Saved := MyGui.Submit()  ; Save the contents of named controls into an object.
        MsgBox("You entered '" Saved.FirstName " " Saved.LastName "'.")
    }
:::

::: {#ExTab .ex}
[](#ExTab){.ex_number} Creates a tab control with multiple tabs, each
containing different controls to interact with.

    MyGui := Gui()
    Tab := MyGui.Add("Tab3",, ["First Tab", "Second Tab", "Third Tab"])
    MyGui.Add("CheckBox", "vMyCheckBox", "Sample checkbox") 
    Tab.UseTab(2)
    MyGui.Add("Radio", "vMyRadio", "Sample radio1")
    MyGui.Add("Radio",, "Sample radio2")
    Tab.UseTab(3)
    MyGui.Add("Edit", "vMyEdit r5")  ; r5 means 5 rows tall.
    Tab.UseTab()  ; i.e. subsequently-added controls will not belong to the tab control.
    Btn := MyGui.Add("Button", "default xm", "OK")  ; xm puts it at the bottom left corner.
    Btn.OnEvent("Click", ProcessUserInput)
    MyGui.OnEvent("Close", ProcessUserInput)
    MyGui.OnEvent("Escape", ProcessUserInput)
    MyGui.Show()

    ProcessUserInput(*)
    {
        Saved := MyGui.Submit()  ; Save the contents of named controls into an object.
        MsgBox("You entered:`n" Saved.MyCheckBox "`n" Saved.MyRadio "`n" Saved.MyEdit)
    }
:::

::: {#ExListBox .ex}
[](#ExListBox){.ex_number} Creates a ListBox control containing files in
a directory.

    MyGui := Gui()
    MyGui.Add("Text",, "Pick a file to launch from the list below.")
    LB := MyGui.Add("ListBox", "w640 r10")
    LB.OnEvent("DoubleClick", LaunchFile)
    Loop Files, "C:\*.*"  ; Change this folder and wildcard pattern to suit your preferences.
        LB.Add([A_LoopFilePath])
    MyGui.Add("Button", "Default", "OK").OnEvent("Click", LaunchFile)
    MyGui.Show()

    LaunchFile(*)
    {
        if MsgBox("Would you like to launch the file or document below?`n`n" LB.Text,, 4) = "No"
            return
        ; Otherwise, try to launch it:
        try Run(LB.Text)
        if A_LastError
            MsgBox("Could not launch the specified file. Perhaps it is not associated with anything.")
    }
:::

::: {#ExToolTip .ex}
[](#ExToolTip){.ex_number} Displays a context-sensitive help (via
ToolTip) whenever the user moves the mouse over a particular control.

    MyGui := Gui()
    MyEdit := MyGui.Add("Edit")
    ; Store the tooltip text in a custom property:
    MyEdit.ToolTip := "This is a tooltip for the control whose name is MyEdit."
    MyDDL := MyGui.Add("DropDownList",, ["Red", "Green", "Blue"])
    MyDDL.ToolTip := "Choose a color from the drop-down list."
    MyGui.Add("CheckBox",, "This control has no tooltip.")
    MyGui.Show()
    OnMessage(0x0200, On_WM_MOUSEMOVE)

    On_WM_MOUSEMOVE(wParam, lParam, msg, Hwnd)
    {
        static PrevHwnd := 0
        if (Hwnd != PrevHwnd)
        {
            Text := "", ToolTip() ; Turn off any previous tooltip.
            CurrControl := GuiCtrlFromHwnd(Hwnd)
            if CurrControl
            {
                if !CurrControl.HasProp("ToolTip")
                    return ; No tooltip for this control.
                Text := CurrControl.ToolTip
                SetTimer () => ToolTip(Text), -1000
                SetTimer () => ToolTip(), -4000 ; Remove the tooltip.
            }
            PrevHwnd := Hwnd
        }
    }
:::

::: {#ExOSD .ex}
[](#ExOSD){.ex_number} Creates an On-screen display (OSD) via
transparent window.

    MyGui := Gui()
    MyGui.Opt("+AlwaysOnTop -Caption +ToolWindow")  ; +ToolWindow avoids a taskbar button and an alt-tab menu item.
    MyGui.BackColor := "EEAA99"  ; Can be any RGB color (it will be made transparent below).
    MyGui.SetFont("s32")  ; Set a large font size (32-point).
    CoordText := MyGui.Add("Text", "cLime", "XXXXX YYYYY")  ; XX & YY serve to auto-size the window.
    ; Make all pixels of this color transparent and make the text itself translucent (150):
    WinSetTransColor(MyGui.BackColor " 150", MyGui)
    SetTimer(UpdateOSD, 200)
    UpdateOSD()  ; Make the first update immediate rather than waiting for the timer.
    MyGui.Show("x0 y400 NoActivate")  ; NoActivate avoids deactivating the currently active window.

    UpdateOSD(*)
    {
        MouseGetPos &MouseX, &MouseY
        CoordText.Value := "X" MouseX ", Y" MouseY
    }
:::

::: {#ExProgressBar .ex}
[](#ExProgressBar){.ex_number} Creates a moving progress bar overlayed
on a background image.

    MyGui := Gui()
    MyGui.BackColor := "White"
    MyGui.Add("Picture", "x0 y0 h350 w450", A_WinDir "\Web\Wallpaper\Windows\img0.jpg")
    MyBtn := MyGui.Add("Button", "Default xp+20 yp+250", "Start the Bar Moving")
    MyBtn.OnEvent("Click", MoveBar)
    MyProgress := MyGui.Add("Progress", "w416")
    MyText := MyGui.Add("Text", "wp")  ; wp means "use width of previous".
    MyGui.Show()

    MoveBar(*)
    {
        Loop Files, A_WinDir "\*.*", "R"
        {
            if (A_Index > 100)
                break
            MyProgress.Value := A_Index
            MyText.Value := A_LoopFileName
            Sleep 50
        }
        MyText.Value := "Bar finished."
    }
:::

::: {#ExImageViewer .ex}
[](#ExImageViewer){.ex_number} Creates a simple image viewer.

    MyGui := Gui("+Resize")
    MyBtn := MyGui.Add("Button", "default", "&Load New Image")
    MyBtn.OnEvent("Click", LoadNewImage)
    MyRadio := MyGui.Add("Radio", "ym+5 x+10 checked", "Load &actual size")
    MyGui.Add("Radio", "ym+5 x+10", "Load to &fit screen")
    MyPic := MyGui.Add("Pic", "xm")
    MyGui.Show()

    LoadNewImage(*)
    {
        Image := FileSelect(,, "Select an image:", "Images (*.gif; *.jpg; *.bmp; *.png; *.tif; *.ico; *.cur; *.ani; *.exe; *.dll)")
        if Image = ""
            return
        if (MyRadio.Value)  ; Display image at its actual size.
        {
            Width := 0
            Height := 0
        }
        else ; Second radio is selected: Resize the image to fit the screen.
        {
            Width := A_ScreenWidth - 28  ; Minus 28 to allow room for borders and margins inside.
            Height := -1  ; "Keep aspect ratio" seems best.
        }
        MyPic.Value := Format("*w{1} *h{2} {3}", Width, Height, Image)  ; Load the image.
        MyGui.Title := Image
        MyGui.Show("xCenter y0 AutoSize")  ; Resize the window to match the picture size.
    }
:::

::: {#ExEditor .ex}
[](#ExEditor){.ex_number} Creates a simple text editor with menu bar.

    ; Create the MyGui window:
    MyGui := Gui("+Resize", "Untitled")  ; Make the window resizable.

    ; Create the submenus for the menu bar:
    FileMenu := Menu()
    FileMenu.Add("&New", MenuFileNew)
    FileMenu.Add("&Open", MenuFileOpen)
    FileMenu.Add("&Save", MenuFileSave)
    FileMenu.Add("Save &As", MenuFileSaveAs)
    FileMenu.Add() ; Separator line.
    FileMenu.Add("E&xit", MenuFileExit)
    HelpMenu := Menu()
    HelpMenu.Add("&About", MenuHelpAbout)

    ; Create the menu bar by attaching the submenus to it:
    MyMenuBar := MenuBar()
    MyMenuBar.Add("&File", FileMenu)
    MyMenuBar.Add("&Help", HelpMenu)

    ; Attach the menu bar to the window:
    MyGui.MenuBar := MyMenuBar

    ; Create the main Edit control:
    MainEdit := MyGui.Add("Edit", "WantTab W600 R20")

    ; Apply events:
    MyGui.OnEvent("DropFiles", Gui_DropFiles)
    MyGui.OnEvent("Size", Gui_Size)

    MenuFileNew()  ; Apply default settings.
    MyGui.Show()  ; Display the window.

    MenuFileNew(*)
    {
        MainEdit.Value := ""  ; Clear the Edit control.
        FileMenu.Disable("3&")  ; Gray out &Save.
        MyGui.Title := "Untitled"
    }

    MenuFileOpen(*)
    {
        MyGui.Opt("+OwnDialogs")  ; Force the user to dismiss the FileSelect dialog before returning to the main window.
        SelectedFileName := FileSelect(3,, "Open File", "Text Documents (*.txt)")
        if SelectedFileName = "" ; No file selected.
            return
        global CurrentFileName := readContent(SelectedFileName)
    }

    MenuFileSave(*)
    {
        saveContent(CurrentFileName)
    }

    MenuFileSaveAs(*)
    {
        MyGui.Opt("+OwnDialogs")  ; Force the user to dismiss the FileSelect dialog before returning to the main window.
        SelectedFileName := FileSelect("S16",, "Save File", "Text Documents (*.txt)")
        if SelectedFileName = "" ; No file selected.
            return
        global CurrentFileName := saveContent(SelectedFileName)
    }

    MenuFileExit(*)  ; User chose "Exit" from the File menu.
    {
        WinClose()
    }

    MenuHelpAbout(*)
    {
        About := Gui("+owner" MyGui.Hwnd)  ; Make the main window the owner of the "about box".
        MyGui.Opt("+Disabled")  ; Disable main window.
        About.Add("Text",, "Text for about box.")
        About.Add("Button", "Default", "OK").OnEvent("Click", About_Close)
        About.OnEvent("Close", About_Close)
        About.OnEvent("Escape", About_Close)
        About.Show()

        About_Close(*)
        {
            MyGui.Opt("-Disabled")  ; Re-enable the main window (must be done prior to the next step).
            About.Destroy()  ; Destroy the about box.
        }
    }

    readContent(FileName)
    {
        try
            FileContent := FileRead(FileName)  ; Read the file's contents into the variable.
        catch
        {
            MsgBox("Could not open '" FileName "'.")
            return
        }
        MainEdit.Value := FileContent  ; Put the text into the control.
        FileMenu.Enable("3&")  ; Re-enable &Save.
        MyGui.Title := FileName  ; Show file name in title bar.
        return FileName
    }

    saveContent(FileName)
    {
        try
        {
            if FileExist(FileName)
                FileDelete(FileName)
            FileAppend(MainEdit.Value, FileName)  ; Save the contents to the file.
        }
        catch
        {
            MsgBox("The attempt to overwrite '" FileName "' failed.")
            return
        }
        ; Upon success, Show file name in title bar (in case we were called by MenuFileSaveAs):
        MyGui.Title := FileName
        return FileName
    }

    Gui_DropFiles(thisGui, Ctrl, FileArray, *)  ; Support drag & drop.
    {
        CurrentFileName := readContent(FileArray[1])  ; Read the first file only (in case there's more than one).
    }

    Gui_Size(thisGui, MinMax, Width, Height)
    {
        if MinMax = -1  ; The window has been minimized. No action needed.
            return
        ; Otherwise, the window has been resized or maximized. Resize the Edit control to match.
        MainEdit.Move(,, Width-20, Height-20)
    }
:::

::: {#ExRefCycle .ex}
[](#ExRefCycle){.ex_number} Demonstrates [problems caused by reference
cycles](../Objects.htm#refs-problems).

    ; Click Open or double-click tray icon to show another GUI.
    ; Use the menu items, Escape or Close button to see how it responds.
    A_TrayMenu.Add("&Open", ShowRefCycleGui)
    Persistent

    ShowRefCycleGui(*) {
        static n := 0
        g := Gui(, "GUI #" (++n)), g.n := n
        g.MenuBar := mb := MenuBar()   ; g -> mb
        mb.Add("Gui", m := Menu())     ; mb -> m
        m.Add("Hide", (*) => g.Hide()) ; (*) -> g
        m.Add("Destroy", (*) => g.Destroy())
        ; For a GUI event, the callback parameter can be used to avoid a
        ; reference cycle (using the same name prevents accidental capture).
        ; However, Hide() doesn't break the *other* reference cycles.
        g.OnEvent("Escape", (g, *) => g.Hide())
        ; Capturing the variable can work out in our favour.
        g.OnEvent("Close", (*) => g := unset)
        g.Show("w300 h200")
        ; __Delete is not called due to the reference cycle:
        ;   g -> mb -> m -> (*) -> g
        ; unless g is unset by triggering the Close event,
        ; or MenuBar and event handlers are released by Destroy.
        g.__Delete := this => MsgBox("GUI #" this.n " deleted")
    }
:::
