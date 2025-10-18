# Window and Control Styles

This page lists some styles and extended styles which can be set or
retrieved with the methods [Gui.Opt](../lib/Gui.htm#Opt) and
[GuiControl.Opt](../lib/GuiControl.htm#Opt), and with the built-in
functions [WinSetStyle](../lib/WinSetStyle.htm),
[WinSetExStyle](../lib/WinSetStyle.htm),
[WinGetStyle](../lib/WinGetStyle.htm),
[WinGetExStyle](../lib/WinGetStyle.htm),
[ControlSetStyle](../lib/ControlSetStyle.htm),
[ControlSetExStyle](../lib/ControlSetStyle.htm),
[ControlGetStyle](../lib/ControlGetStyle.htm) and
[ControlGetExStyle](../lib/ControlGetStyle.htm).

## Table of Contents {#toc}

-   [Styles Common to Gui/Parent Windows and Most Control
    Types](#Common)
-   [Text](#Text) \| [Edit](#Edit) \| [UpDown](#UpDown) \|
    [Picture](#Pic)
-   [Button \| CheckBox \| Radio \| GroupBox](#Button)
-   [DropDownList \| ComboBox](#DDL)
-   [ListBox](#ListBox) \| [ListView](#ListView) \|
    [TreeView](#TreeView)
-   [DateTime](#DateTime) \| [MonthCal](#MonthCal)
-   [Slider](#Slider) \| [Progress](#Progress) \| [Tab](#Tab) \|
    [StatusBar](#StatusBar)

## Common Styles {#Common}

By default, a GUI window uses [WS_POPUP](#WS_POPUP),
[WS_CAPTION](#WS_CAPTION), [WS_SYSMENU](#WS_SYSMENU), and
[WS_MINIMIZEBOX](#WS_MINIMIZEBOX). For a GUI window,
[WS_CLIPSIBLINGS](#WS_CLIPSIBLINGS) is always enabled and cannot be
disabled.

  Style                 Hex          Description
  --------------------- ------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  WS_BORDER             0x800000     +/-Border. Creates a window that has a thin-line border.
  WS_POPUP              0x80000000   Creates a pop-up window. This style cannot be used with the [WS_CHILD](#WS_CHILD) style.
  WS_CAPTION            0xC00000     +/-Caption. Creates a window that has a title bar. This style is a numerical combination of [WS_BORDER](#WS_BORDER) and [WS_DLGFRAME](#WS_DLGFRAME).
  WS_CLIPSIBLINGS       0x4000000    Clips child windows relative to each other; that is, when a particular child window receives a WM_PAINT message, the WS_CLIPSIBLINGS style clips all other overlapping child windows out of the region of the child window to be updated. If WS_CLIPSIBLINGS is not specified and child windows overlap, it is possible, when drawing within the client area of a child window, to draw within the client area of a neighboring child window.
  WS_DISABLED           0x8000000    +/-Disabled. Creates a window that is initially disabled.
  WS_DLGFRAME           0x400000     Creates a window that has a border of a style typically used with dialog boxes.
  WS_GROUP              0x20000      +/-Group. Indicates that this control is the first one in a group of controls. This style is automatically applied to manage the \"only one at a time\" behavior of radio buttons. In the rare case where two groups of radio buttons are added consecutively (with no other control types in between them), this style may be applied manually to the first control of the second radio group, which splits it off from the first.
  WS_HSCROLL            0x100000     Creates a window that has a horizontal scroll bar.
  WS_MAXIMIZE           0x1000000    Creates a window that is initially maximized.
  WS_MAXIMIZEBOX        0x10000      +/-MaximizeBox. Creates a window that has a maximize button. Cannot be combined with the WS_EX_CONTEXTHELP style. The [WS_SYSMENU](#WS_SYSMENU) style must also be specified.
  WS_MINIMIZE           0x20000000   Creates a window that is initially minimized.
  WS_MINIMIZEBOX        0x20000      +/-MinimizeBox. Creates a window that has a minimize button. Cannot be combined with the WS_EX_CONTEXTHELP style. The [WS_SYSMENU](#WS_SYSMENU) style must also be specified.
  WS_OVERLAPPED         0x0          Creates an overlapped window. An overlapped window has a title bar and a border. Same as the WS_TILED style.
  WS_OVERLAPPEDWINDOW   0xCF0000     Creates an overlapped window with the [WS_OVERLAPPED](#WS_OVERLAPPED), [WS_CAPTION](#WS_CAPTION), [WS_SYSMENU](#WS_SYSMENU), [WS_THICKFRAME](#WS_THICKFRAME), [WS_MINIMIZEBOX](#WS_MINIMIZEBOX), and [WS_MAXIMIZEBOX](#WS_MAXIMIZEBOX) styles. Same as the WS_TILEDWINDOW style.
  WS_POPUPWINDOW        0x80880000   Creates a pop-up window with [WS_BORDER](#WS_BORDER), [WS_POPUP](#WS_POPUP), and [WS_SYSMENU](#WS_SYSMENU) styles. The [WS_CAPTION](#WS_CAPTION) and [WS_POPUPWINDOW](#WS_POPUPWINDOW) styles must be combined to make the window menu visible.
  WS_SIZEBOX            0x40000      +/-Resize. Creates a window that has a sizing border. Same as the [WS_THICKFRAME](#WS_THICKFRAME) style.
  WS_SYSMENU            0x80000      +/-SysMenu. Creates a window that has a window menu on its title bar. The [WS_CAPTION](#WS_CAPTION) style must also be specified.
  WS_TABSTOP            0x10000      +/-Tabstop. Specifies a control that can receive the keyboard focus when the user presses [Tab]{.kbd}. Pressing [Tab]{.kbd} changes the keyboard focus to the next control with the WS_TABSTOP style.
  WS_THICKFRAME         0x40000      Creates a window that has a sizing border. Same as the [WS_SIZEBOX](#WS_SIZEBOX) style.
  WS_VSCROLL            0x200000     Creates a window that has a vertical scroll bar.
  WS_VISIBLE            0x10000000   Creates a window that is initially visible.
  WS_CHILD              0x40000000   Creates a child window. A window with this style cannot have a menu bar. This style cannot be used with the [WS_POPUP](#WS_POPUP) style.

## Text Control Styles {#Text}

These styles affect the [Text](../lib/GuiControls.htm#Text) control. It
has neither default styles nor forced styles.

  Style               Hex      Description
  ------------------- -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  SS_BLACKFRAME       0x7      Specifies a box with a frame drawn in the same color as the window frames. This color is black in the default color scheme.
  SS_BLACKRECT        0x4      Specifies a rectangle filled with the current window frame color. This color is black in the default color scheme.
  SS_CENTER           0x1      +/-Center. Specifies a simple rectangle and centers the text in the rectangle. The control automatically wraps words that extend past the end of a line to the beginning of the next centered line.
  SS_CENTERIMAGE      0x200    If the control contains a single line of text, the text is centered vertically within the available height of the control.
  SS_ETCHEDFRAME      0x12     Draws the frame of the static control using the EDGE_ETCHED edge style.
  SS_ETCHEDHORZ       0x10     Draws the top and bottom edges of the static control using the EDGE_ETCHED edge style.
  SS_ETCHEDVERT       0x11     Draws the left and right edges of the static control using the EDGE_ETCHED edge style.
  SS_GRAYFRAME        0x8      Specifies a box with a frame drawn with the same color as the screen background (desktop). This color is gray in the default color scheme.
  SS_GRAYRECT         0x5      Specifies a rectangle filled with the current screen background color. This color is gray in the default color scheme.
  SS_LEFT             0x0      +/-Left. This is the default. It specifies a simple rectangle and left-aligns the text in the rectangle. The text is formatted before it is displayed. Words that extend past the end of a line are automatically wrapped to the beginning of the next left-aligned line. Words that are longer than the width of the control are truncated.
  SS_LEFTNOWORDWRAP   0xC      +/-Wrap. Specifies a rectangle and left-aligns the text in the rectangle. Tabs are expanded, but words are not wrapped. Text that extends past the end of a line is clipped.
  SS_NOPREFIX         0x80     Prevents interpretation of any ampersand (&) characters in the control\'s text as accelerator prefix characters. This can be useful when file names or other strings that might contain an ampersand (&) must be displayed within a text control.
  SS_NOTIFY           0x100    Sends the parent window the STN_CLICKED notification when the user clicks the control.
  SS_RIGHT            0x2      +/-Right. Specifies a rectangle and right-aligns the specified text in the rectangle.
  SS_SUNKEN           0x1000   Draws a half-sunken border around a static control.
  SS_WHITEFRAME       0x9      Specifies a box with a frame drawn with the same color as the window background. This color is white in the default color scheme.
  SS_WHITERECT        0x6      Specifies a rectangle filled with the current window background color. This color is white in the default color scheme.

## Edit Control Styles {#Edit}

These styles affect the [Edit](../lib/GuiControls.htm#Edit) control. By
default, it uses [WS_TABSTOP](#WS_TABSTOP) and WS_EX_CLIENTEDGE
(extended style E0x200). It has no forced styles.

If an Edit control is auto-detected as multi-line due to its starting
contents containing multiple lines, its height being taller than 1 row,
or its row-count having been explicitly specified as greater than 1, the
following styles will be applied by default: [WS_VSCROLL](#WS_VSCROLL),
[ES_WANTRETURN](#ES_WANTRETURN), and [ES_AUTOVSCROLL](#ES_AUTOVSCROLL).

If an Edit control is auto-detected as a single line, it defaults to
having [ES_AUTOHSCROLL](#ES_AUTOHSCROLL).

  Style            Hex      Description
  ---------------- -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ES_AUTOHSCROLL   0x80     +/-Wrap for multi-line edits, and +/-Limit for single-line edits. Automatically scrolls text to the right by 10 characters when the user types a character at the end of the line. When the user presses [Enter]{.kbd}, the control scrolls all text back to the zero position.
  ES_AUTOVSCROLL   0x40     Scrolls text up one page when the user presses [Enter]{.kbd} on the last line.
  ES_CENTER        0x1      +/-Center. Centers text in a multiline edit control.
  ES_LOWERCASE     0x10     +/-Lowercase. Converts all characters to lowercase as they are typed into the edit control.
  ES_NOHIDESEL     0x100    Negates the default behavior for an edit control. The default behavior hides the selection when the control loses the input focus and inverts the selection when the control receives the input focus. If you specify [ES_NOHIDESEL](#ES_NOHIDESEL), the selected text is inverted, even if the control does not have the focus.
  ES_NUMBER        0x2000   +/-Number. Prevents the user from typing anything other than digits in the control.
  ES_OEMCONVERT    0x400    This style is most useful for edit controls that contain file names.
  ES_MULTILINE     0x4      +/-Multi. Designates a multiline edit control. The default is a single-line edit control.
  ES_PASSWORD      0x20     +/-Password. Displays a masking character in place of each character that is typed into the edit control, which conceals the text.
  ES_READONLY      0x800    +/-ReadOnly. Prevents the user from typing or editing text in the edit control.
  ES_RIGHT         0x2      +/-Right. Right-aligns text in a multiline edit control.
  ES_UPPERCASE     0x8      +/-Uppercase. Converts all characters to uppercase as they are typed into the edit control.
  ES_WANTRETURN    0x1000   +/-WantReturn. Specifies that a carriage return be inserted when the user presses [Enter]{.kbd} while typing text into a multiline edit control in a dialog box. If you do not specify this style, pressing [Enter]{.kbd} has the same effect as pressing the dialog box\'s default push button. This style has no effect on a single-line edit control.

## UpDown Control Styles {#UpDown}

These styles affect the [UpDown](../lib/GuiControls.htm#UpDown) control.
By default, it uses [UDS_ARROWKEYS](#UDS_ARROWKEYS),
[UDS_ALIGNRIGHT](#UDS_ALIGNRIGHT), [UDS_SETBUDDYINT](#UDS_SETBUDDYINT),
and [UDS_AUTOBUDDY](#UDS_AUTOBUDDY). It has no forced styles.

  Style             Hex     Description
  ----------------- ------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  UDS_WRAP          0x1     Named option \"Wrap\". Causes the control to wrap around to the other end of its range when the user attempts to go beyond the minimum or maximum. Without *Wrap*, the control stops when the minimum or maximum is reached.
  UDS_SETBUDDYINT   0x2     Causes the UpDown control to set the text of the buddy control (using the WM_SETTEXT message) when the position changes. However, if the buddy is a ListBox, the ListBox\'s current selection is changed instead.
  UDS_ALIGNRIGHT    0x4     Named option \"Right\" (default). Positions UpDown on the right side of its buddy control.
  UDS_ALIGNLEFT     0x8     Named option \"Left\". Positions UpDown on the left side of its buddy control.
  UDS_AUTOBUDDY     0x10    Automatically selects the previous control in the z-order as the UpDown control\'s buddy control.
  UDS_ARROWKEYS     0x20    Allows the user to press [↑]{.kbd} or [↓]{.kbd} on the keyboard to increase or decrease the UpDown control\'s position.
  UDS_HORZ          0x40    Named option \"Horz\". Causes the control\'s arrows to point left and right instead of up and down.
  UDS_NOTHOUSANDS   0x80    Does not insert a thousands separator between every three decimal digits in the buddy control.
  UDS_HOTTRACK      0x100   Causes the control to exhibit \"hot tracking\" behavior. That is, it highlights the control\'s buttons as the mouse passes over them. This flag may be ignored if the desktop theme overrides it.

## Picture Control Styles {#Pic}

These styles affect the [Picture](../lib/GuiControls.htm#Picture)
control. It has no default styles. The style SS_ICON (for icons and
cursors) or SS_BITMAP (for other image types) is always enabled and
cannot be disabled.

  Style                Hex     Description
  -------------------- ------- ------------------------------------------------------------------------------------
  SS_REALSIZECONTROL   0x40    Adjusts the bitmap to fit the size of the control.
  SS_CENTERIMAGE       0x200   Centers the bitmap in the control. If the bitmap is too large, it will be clipped.

## Button, CheckBox, Radio, and GroupBox Control Styles {#Button}

These styles affect the [Button](../lib/GuiControls.htm#Button),
[CheckBox](../lib/GuiControls.htm#CheckBox),
[Radio](../lib/GuiControls.htm#Radio), or
[GroupBox](../lib/GuiControls.htm#GroupBox) controls.

By default, each of these controls except GroupBox uses the styles
[BS_MULTILINE](#BS_MULTILINE) (unless it has no explicitly set width or
height, nor any CR/LF characters in their text) and
[WS_TABSTOP](#WS_TABSTOP) (however, Radio controls other than the first
of each radio group lack WS_TABSTOP).

The following styles are always enabled and cannot be disabled:

-   Button: [BS_PUSHBUTTON](#BS_PUSHBUTTON) or
    [BS_DEFPUSHBUTTON](#BS_DEFPUSHBUTTON)
-   CheckBox: [BS_AUTOCHECKBOX](#BS_AUTOCHECKBOX) or
    [BS_AUTO3STATE](#BS_AUTO3STATE)
-   Radio: [BS_AUTORADIOBUTTON](#BS_AUTORADIOBUTTON)
-   GroupBox: [BS_GROUPBOX](#BS_GROUPBOX)

  Style                Hex      Description
  -------------------- -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  BS_AUTO3STATE        0x6      Creates a button that is the same as a three-state check box, except that the box changes its state when the user selects it. The state cycles through checked, indeterminate, and cleared.
  BS_AUTOCHECKBOX      0x3      Creates a button that is the same as a check box, except that the check state automatically toggles between checked and cleared each time the user selects the check box.
  BS_AUTORADIOBUTTON   0x9      Creates a button that is the same as a radio button, except that when the user selects it, the system automatically sets the button\'s check state to checked and automatically sets the check state for all other buttons in the same group to cleared.
  BS_LEFT              0x100    +/-Left. Left-aligns the text.
  BS_PUSHBUTTON        0x0      Creates a push button that posts a WM_COMMAND message to the owner window when the user selects the button.
  BS_PUSHLIKE          0x1000   Makes a checkbox or radio button look and act like a push button. The button looks raised when it isn\'t pushed or checked, and sunken when it is pushed or checked.
  BS_RIGHT             0x200    +/-Right. Right-aligns the text.
  BS_RIGHTBUTTON       0x20     +Right (i.e. +Right includes both [BS_RIGHT](#BS_RIGHT) and [BS_RIGHTBUTTON](#BS_RIGHTBUTTON), but -Right removes only BS_RIGHT, not BS_RIGHTBUTTON). Positions a checkbox square or radio button circle on the right side of the control\'s available width instead of the left.
  BS_BOTTOM            0x800    Places the text at the bottom of the control\'s available height.
  BS_CENTER            0x300    +/-Center. Centers the text horizontally within the control\'s available width.
  BS_DEFPUSHBUTTON     0x1      +/-Default. Creates a push button with a heavy black border. If the button is in a dialog box, the user can select the button by pressing [Enter]{.kbd}, even when the button does not have the input focus. This style is useful for enabling the user to quickly select the most likely option.
  BS_MULTILINE         0x2000   +/-Wrap. Wraps the text to multiple lines if the text is too long to fit on a single line in the control\'s available width. This also allows linefeed (\`n) to start new lines of text.
  BS_NOTIFY            0x4000   Enables a button to send BN_KILLFOCUS and BN_SETFOCUS notification codes to its parent window. Note that buttons send the BN_CLICKED notification code regardless of whether it has this style. To get BN_DBLCLK notification codes, the button must have the BS_RADIOBUTTON or BS_OWNERDRAW style.
  BS_TOP               0x400    Places text at the top of the control\'s available height.
  BS_VCENTER           0xC00    Vertically centers text in the control\'s available height.
  BS_FLAT              0x8000   Specifies that the button is two-dimensional; it does not use the default shading to create a 3-D effect.
  BS_GROUPBOX          0x7      Creates a rectangle in which other controls can be grouped. Any text associated with this style is displayed in the rectangle\'s upper left corner.

## DropDownList and ComboBox Control Styles {#DDL}

These styles affect the
[DropDownList](../lib/GuiControls.htm#DropDownList) and
[ComboBox](../lib/GuiControls.htm#ComboBox) controls.

By default, each of these controls uses [WS_TABSTOP](#WS_TABSTOP). In
addition, a DropDownList control uses [WS_VSCROLL](#WS_VSCROLL), and a
ComboBox control uses [WS_VSCROLL](#WS_VSCROLL) and
[CBS_AUTOHSCROLL](#CBS_AUTOHSCROLL).

The following styles are always enabled and cannot be disabled:

-   DropDownList: [CBS_DROPDOWNLIST](#CBS_DROPDOWNLIST)
-   ComboBox: Either [CBS_DROPDOWN](#CBS_DROPDOWN) or
    [CBS_SIMPLE](#CBS_SIMPLE)

  Style                  Hex      Description
  ---------------------- -------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  CBS_AUTOHSCROLL        0x40     +/-Limit. Automatically scrolls the text in an edit control to the right when the user types a character at the end of the line. If this style is not set, only text that fits within the rectangular boundary is enabled.
  CBS_DISABLENOSCROLL    0x800    Shows a disabled vertical scroll bar in the drop-down list when it does not contain enough items to scroll. Without this style, the scroll bar is hidden when the drop-down list does not contain enough items.
  CBS_DROPDOWN           0x2      Similar to [CBS_SIMPLE](#CBS_SIMPLE), except that the list box is not displayed unless the user selects an icon next to the edit control.
  CBS_DROPDOWNLIST       0x3      Similar to [CBS_DROPDOWN](#CBS_DROPDOWN), except that the edit control is replaced by a static text item that displays the current selection in the list box.
  CBS_LOWERCASE          0x4000   +/-Lowercase. Converts to lowercase any uppercase characters that are typed into the edit control of a combo box.
  CBS_NOINTEGRALHEIGHT   0x400    Specifies that the combo box will be exactly the size specified by the application when it created the combo box. Usually, Windows CE sizes a combo box so that it does not display partial items.
  CBS_OEMCONVERT         0x80     Converts text typed in the combo box edit control from the Windows CE character set to the OEM character set and then back to the Windows CE set. This style is most useful for combo boxes that contain file names. It applies only to combo boxes created with the [CBS_DROPDOWN](#CBS_DROPDOWN) style.
  CBS_SIMPLE             0x1      +/-Simple (ComboBox only). Displays the drop-down list at all times. The current selection in the list is displayed in the edit control.
  CBS_SORT               0x100    +/-Sort. Sorts the items in the drop-list alphabetically.
  CBS_UPPERCASE          0x2000   +/-Uppercase. Converts to uppercase any lowercase characters that are typed into the edit control of a ComboBox.

## ListBox Control Styles {#ListBox}

These styles affect the [ListBox](../lib/GuiControls.htm#ListBox)
control. By default, it uses [WS_TABSTOP](#WS_TABSTOP),
[LBS_USETABSTOPS](#LBS_USETABSTOPS), [WS_VSCROLL](#WS_VSCROLL), and
WS_EX_CLIENTEDGE (extended style E0x200). The style
[LBS_NOTIFY](#LBS_NOTIFY) (supports detection of double-clicks) is
always enabled and cannot be disabled.

  Style                  Hex      Description
  ---------------------- -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  LBS_DISABLENOSCROLL    0x1000   Shows a disabled vertical scroll bar for the list box when the box does not contain enough items to scroll. If you do not specify this style, the scroll bar is hidden when the list box does not contain enough items.
  LBS_NOINTEGRALHEIGHT   0x100    Specifies that the list box will be exactly the size specified by the application when it created the list box.
  LBS_EXTENDEDSEL        0x800    +/-Multi. Allows multiple selections via control-click and shift-click.
  LBS_MULTIPLESEL        0x8      A simplified version of multi-select in which control-click and shift-click are not necessary because normal left clicks serve to extend the selection or de-select a selected item.
  LBS_NOSEL              0x4000   +/-ReadOnly. Specifies that the user can view list box strings but cannot select them.
  LBS_NOTIFY             0x1      Causes the list box to send a notification code to the parent window whenever the user clicks a list box item (LBN_SELCHANGE), double-clicks an item (LBN_DBLCLK), or cancels the selection (LBN_SELCANCEL).
  LBS_SORT               0x2      +/-Sort. Sorts the items in the list box alphabetically.
  LBS_USETABSTOPS        0x80     Enables a ListBox to recognize and expand tab characters when drawing its strings. The default tab positions are 32 dialog box units apart. A dialog box unit is equal to one-fourth of the current dialog box base-width unit.

## ListView Control Styles {#ListView}

These styles affect the [ListView](../lib/ListView.htm) control. By
default, it uses [WS_TABSTOP](#WS_TABSTOP), [LVS_REPORT](#LVS_REPORT),
[LVS_SHOWSELALWAYS](#LVS_SHOWSELALWAYS),
[LVS_EX_FULLROWSELECT](#LVS_EX_FULLROWSELECT),
[LVS_EX_HEADERDRAGDROP](#LVS_EX_HEADERDRAGDROP), and WS_EX_CLIENTEDGE
(extended style E0x200). It has no forced styles.

  Style                 Hex      Description
  --------------------- -------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  LVS_ALIGNLEFT         0x800    Items are left-aligned in icon and small icon view.
  LVS_ALIGNTOP          0x0      Items are aligned with the top of the list-view control in icon and small icon view. This is the default.
  LVS_AUTOARRANGE       0x100    Icons are automatically kept arranged in icon and small icon view.
  LVS_EDITLABELS        0x200    +/-ReadOnly. Specifying **-**ReadOnly (or +0x200) allows the user to edit the first field of each row in place.
  LVS_ICON              0x0      +Icon. Specifies large-icon view.
  LVS_LIST              0x3      +List. Specifies list view.
  LVS_NOCOLUMNHEADER    0x4000   +/-Hdr. Avoids displaying column headers in report view.
  LVS_NOLABELWRAP       0x80     Item text is displayed on a single line in icon view. By default, item text may wrap in icon view.
  LVS_NOSCROLL          0x2000   Scrolling is disabled. All items must be within the client area. This style is not compatible with the [LVS_LIST](#LVS_LIST) or [LVS_REPORT](#LVS_REPORT) styles.
  LVS_NOSORTHEADER      0x8000   +/-NoSortHdr. Column headers do not work like buttons. This style can be used if clicking a column header in report view does not carry out an action, such as sorting.
  LVS_OWNERDATA         0x1000   This style specifies a virtual list-view control (not directly supported by AutoHotkey).
  LVS_OWNERDRAWFIXED    0x400    The owner window can paint items in report view in response to WM_DRAWITEM messages (not directly supported by AutoHotkey).
  LVS_REPORT            0x1      +Report. Specifies report view.
  LVS_SHAREIMAGELISTS   0x40     The [image list](../lib/ListView.htm#IL) will not be deleted when the control is destroyed. This style enables the use of the same image lists with multiple list-view controls.
  LVS_SHOWSELALWAYS     0x8      The selection, if any, is always shown, even if the control does not have keyboard focus.
  LVS_SINGLESEL         0x4      +/-Multi. Only one item at a time can be selected. By default, multiple items can be selected.
  LVS_SMALLICON         0x2      +IconSmall. Specifies small-icon view.
  LVS_SORTASCENDING     0x10     +/-Sort. Rows are sorted in ascending order based on the contents of the first field.
  LVS_SORTDESCENDING    0x20     +/-SortDesc. Same as above but in descending order.

**Extended ListView styles** require the [LV
prefix](../lib/ListView.htm#LVS_EX) when used with the Gui
methods/properties. Some extended styles introduced in Windows XP or
later versions are not listed here. For a full list, see [Microsoft
Docs: Extended List-View
Styles](https://learn.microsoft.com/windows/win32/controls/extended-list-view-styles).

+-----------------------+-----------------------+-----------------------+
| Extended Style        | Hex                   | Description           |
+=======================+=======================+=======================+
| LVS_EX_BORDERSELECT   | LV0x8000              | When an item is       |
|                       |                       | selected, the border  |
|                       |                       | color of the item     |
|                       |                       | changes rather than   |
|                       |                       | the item being        |
|                       |                       | highlighted (might be |
|                       |                       | non-functional in     |
|                       |                       | recent operating      |
|                       |                       | systems).             |
+-----------------------+-----------------------+-----------------------+
| LVS_EX_CHECKBOXES     | LV0x4                 | +/-Checked. Displays  |
|                       |                       | a checkbox with each  |
|                       |                       | item. When set to     |
|                       |                       | this style, the       |
|                       |                       | control creates and   |
|                       |                       | sets a state image    |
|                       |                       | list with two images  |
|                       |                       | using                 |
|                       |                       | DrawFrameControl.     |
|                       |                       | State image 1 is the  |
|                       |                       | unchecked box, and    |
|                       |                       | state image 2 is the  |
|                       |                       | checked box. Setting  |
|                       |                       | the state image to    |
|                       |                       | zero removes the      |
|                       |                       | check box altogether. |
|                       |                       |                       |
|                       |                       | Checkboxes are        |
|                       |                       | visible and           |
|                       |                       | functional with all   |
|                       |                       | list-view modes       |
|                       |                       | except the tile view  |
|                       |                       | mode. Clicking a      |
|                       |                       | checkbox in tile view |
|                       |                       | mode only selects the |
|                       |                       | item; the state does  |
|                       |                       | not change.           |
+-----------------------+-----------------------+-----------------------+
| LVS_EX_DOUBLEBUFFER   | LV0x10000             | Paints via            |
|                       |                       | double-buffering,     |
|                       |                       | which reduces         |
|                       |                       | flicker. This         |
|                       |                       | extended style also   |
|                       |                       | enables alpha-blended |
|                       |                       | marquee selection on  |
|                       |                       | systems where it is   |
|                       |                       | supported.            |
+-----------------------+-----------------------+-----------------------+
| LVS_EX_FLATSB         | LV0x100               | Enables flat scroll   |
|                       |                       | bars in the list      |
|                       |                       | view.                 |
+-----------------------+-----------------------+-----------------------+
| LVS_EX_FULLROWSELECT  | LV0x20                | When a row is         |
|                       |                       | selected, all its     |
|                       |                       | fields are            |
|                       |                       | highlighted. This     |
|                       |                       | style is available    |
|                       |                       | only in conjunction   |
|                       |                       | with the              |
|                       |                       | [LVS                  |
|                       |                       | _REPORT](#LVS_REPORT) |
|                       |                       | style.                |
+-----------------------+-----------------------+-----------------------+
| LVS_EX_GRIDLINES      | LV0x1                 | +/-Grid. Displays     |
|                       |                       | gridlines around rows |
|                       |                       | and columns. This     |
|                       |                       | style is available    |
|                       |                       | only in conjunction   |
|                       |                       | with the              |
|                       |                       | [LVS                  |
|                       |                       | _REPORT](#LVS_REPORT) |
|                       |                       | style.                |
+-----------------------+-----------------------+-----------------------+
| LVS_EX_HEADERDRAGDROP | LV0x10                | Enables drag-and-drop |
|                       |                       | reordering of columns |
|                       |                       | in a list-view        |
|                       |                       | control. This style   |
|                       |                       | is only available to  |
|                       |                       | list-view controls    |
|                       |                       | that use the          |
|                       |                       | [LVS                  |
|                       |                       | _REPORT](#LVS_REPORT) |
|                       |                       | style.                |
+-----------------------+-----------------------+-----------------------+
| LVS_EX_INFOTIP        | LV0x400               | When a list-view      |
|                       |                       | control uses this     |
|                       |                       | style, the            |
|                       |                       | LVN_GETINFOTIP        |
|                       |                       | notification message  |
|                       |                       | is sent to the parent |
|                       |                       | window before         |
|                       |                       | displaying an item\'s |
|                       |                       | ToolTip.              |
+-----------------------+-----------------------+-----------------------+
| LVS_EX_LABELTIP       | LV0x4000              | If a partially hidden |
|                       |                       | label in any          |
|                       |                       | list-view mode lacks  |
|                       |                       | ToolTip text, the     |
|                       |                       | list-view control     |
|                       |                       | will unfold the       |
|                       |                       | label. If this style  |
|                       |                       | is not set, the       |
|                       |                       | list-view control     |
|                       |                       | will unfold partly    |
|                       |                       | hidden labels only    |
|                       |                       | for the large icon    |
|                       |                       | mode. Note: On some   |
|                       |                       | versions of Windows,  |
|                       |                       | this style might not  |
|                       |                       | work properly if the  |
|                       |                       | GUI window is set to  |
|                       |                       | be always-on-top.     |
+-----------------------+-----------------------+-----------------------+
| LVS_EX_MULTIWORKAREAS | LV0x2000              | If the list-view      |
|                       |                       | control has the       |
|                       |                       | [LVS_AUTOARRAN        |
|                       |                       | GE](#LVS_AUTOARRANGE) |
|                       |                       | style, the control    |
|                       |                       | will not autoarrange  |
|                       |                       | its icons until one   |
|                       |                       | or more work areas    |
|                       |                       | are defined (see      |
|                       |                       | LVM_SETWORKAREAS). To |
|                       |                       | be effective, this    |
|                       |                       | style must be set     |
|                       |                       | before any work areas |
|                       |                       | are defined and any   |
|                       |                       | items have been added |
|                       |                       | to the control.       |
+-----------------------+-----------------------+-----------------------+
| LV                    | LV0x40                | The list-view control |
| S_EX_ONECLICKACTIVATE |                       | sends an              |
|                       |                       | LVN_ITEMACTIVATE      |
|                       |                       | notification message  |
|                       |                       | to the parent window  |
|                       |                       | when the user clicks  |
|                       |                       | an item. This style   |
|                       |                       | also enables hot      |
|                       |                       | tracking in the       |
|                       |                       | list-view control.    |
|                       |                       | Hot tracking means    |
|                       |                       | that when the cursor  |
|                       |                       | moves over an item,   |
|                       |                       | it is highlighted but |
|                       |                       | not selected.         |
+-----------------------+-----------------------+-----------------------+
| LVS_EX_REGIONAL       | LV0x200               | Sets the list-view    |
|                       |                       | window region to      |
|                       |                       | include only the item |
|                       |                       | icons and text using  |
|                       |                       | SetWindowRgn. Any     |
|                       |                       | area that is not part |
|                       |                       | of an item is         |
|                       |                       | excluded from the     |
|                       |                       | window region. This   |
|                       |                       | style is only         |
|                       |                       | available to          |
|                       |                       | list-view controls    |
|                       |                       | that use the          |
|                       |                       | [LVS_ICON](#LVS_ICON) |
|                       |                       | style.                |
+-----------------------+-----------------------+-----------------------+
| LVS_EX_SIMPLESELECT   | LV0x100000            | In icon view, moves   |
|                       |                       | the state image of    |
|                       |                       | the item to the top   |
|                       |                       | right of the large    |
|                       |                       | icon rendering. In    |
|                       |                       | views other than icon |
|                       |                       | view there is no      |
|                       |                       | change. When the user |
|                       |                       | changes the state by  |
|                       |                       | using the space bar,  |
|                       |                       | all selected items    |
|                       |                       | cycle over, not the   |
|                       |                       | item with the focus.  |
+-----------------------+-----------------------+-----------------------+
| LVS_EX_SUBITEMIMAGES  | LV0x2                 | Allows images to be   |
|                       |                       | displayed for fields  |
|                       |                       | beyond the first.     |
|                       |                       | This style is         |
|                       |                       | available only in     |
|                       |                       | conjunction with the  |
|                       |                       | [LVS                  |
|                       |                       | _REPORT](#LVS_REPORT) |
|                       |                       | style.                |
+-----------------------+-----------------------+-----------------------+
| LVS_EX_TRACKSELECT    | LV0x8                 | Enables hot-track     |
|                       |                       | selection in a        |
|                       |                       | list-view control.    |
|                       |                       | Hot track selection   |
|                       |                       | means that an item is |
|                       |                       | automatically         |
|                       |                       | selected when the     |
|                       |                       | cursor remains over   |
|                       |                       | the item for a        |
|                       |                       | certain period of     |
|                       |                       | time. The delay can   |
|                       |                       | be changed from the   |
|                       |                       | default system        |
|                       |                       | setting with a        |
|                       |                       | LVM_SETHOVERTIME      |
|                       |                       | message. This style   |
|                       |                       | applies to all styles |
|                       |                       | of list-view control. |
|                       |                       | You can check whether |
|                       |                       | hot-track selection   |
|                       |                       | is enabled by calling |
|                       |                       | SystemParametersInfo. |
+-----------------------+-----------------------+-----------------------+
| LV                    | LV0x80                | The list-view control |
| S_EX_TWOCLICKACTIVATE |                       | sends an              |
|                       |                       | LVN_ITEMACTIVATE      |
|                       |                       | notification message  |
|                       |                       | to the parent window  |
|                       |                       | when the user         |
|                       |                       | double-clicks an      |
|                       |                       | item. This style also |
|                       |                       | enables hot tracking  |
|                       |                       | in the list-view      |
|                       |                       | control. Hot tracking |
|                       |                       | means that when the   |
|                       |                       | cursor moves over an  |
|                       |                       | item, it is           |
|                       |                       | highlighted but not   |
|                       |                       | selected.             |
+-----------------------+-----------------------+-----------------------+
| LVS_EX_UNDERLINECOLD  | LV0x1000              | Causes those non-hot  |
|                       |                       | items that may be     |
|                       |                       | activated to be       |
|                       |                       | displayed with        |
|                       |                       | underlined text. This |
|                       |                       | style requires that   |
|                       |                       | [LVS_EX_T             |
|                       |                       | WOCLICKACTIVATE](#LVS |
|                       |                       | _EX_TWOCLICKACTIVATE) |
|                       |                       | be set also.          |
+-----------------------+-----------------------+-----------------------+
| LVS_EX_UNDERLINEHOT   | LV0x800               | Causes those hot      |
|                       |                       | items that may be     |
|                       |                       | activated to be       |
|                       |                       | displayed with        |
|                       |                       | underlined text. This |
|                       |                       | style requires that   |
|                       |                       | [LVS_EX_O             |
|                       |                       | NECLICKACTIVATE](#LVS |
|                       |                       | _EX_ONECLICKACTIVATE) |
|                       |                       | or                    |
|                       |                       | [LVS_EX_T             |
|                       |                       | WOCLICKACTIVATE](#LVS |
|                       |                       | _EX_TWOCLICKACTIVATE) |
|                       |                       | also be set.          |
+-----------------------+-----------------------+-----------------------+

## TreeView Control Styles {#TreeView}

These styles affect the [TreeView](../lib/TreeView.htm) control. By
default, it uses [WS_TABSTOP](#WS_TABSTOP),
[TVS_SHOWSELALWAYS](#TVS_SHOWSELALWAYS), [TVS_HASLINES](#TVS_HASLINES),
[TVS_LINESATROOT](#TVS_LINESATROOT), [TVS_HASBUTTONS](#TVS_HASBUTTONS),
and WS_EX_CLIENTEDGE (extended style E0x200). It has no forced styles.

  Style                 Hex      Description
  --------------------- -------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  TVS_CHECKBOXES        0x100    +/-Checked. Displays a checkbox next to each item.
  TVS_DISABLEDRAGDROP   0x10     Prevents the tree-view control from sending TVN_BEGINDRAG notification messages.
  TVS_EDITLABELS        0x8      +/-ReadOnly. Allows the user to edit the names of tree-view items.
  TVS_FULLROWSELECT     0x1000   Enables full-row selection in the tree view. The entire row of the selected item is highlighted, and clicking anywhere on an item\'s row causes it to be selected. This style cannot be used in conjunction with the [TVS_HASLINES](#TVS_HASLINES) style.
  TVS_HASBUTTONS        0x1      +/-Buttons. Displays plus (+) and minus (-) buttons next to parent items. The user clicks the buttons to expand or collapse a parent item\'s list of child items. To include buttons with items at the root of the tree view, [TVS_LINESATROOT](#TVS_LINESATROOT) must also be specified.
  TVS_HASLINES          0x2      +/-Lines. Uses lines to show the hierarchy of items.
  TVS_INFOTIP           0x800    Obtains ToolTip information by sending the TVN_GETINFOTIP notification.
  TVS_LINESATROOT       0x4      +/-Lines. Uses lines to link items at the root of the tree-view control. This value is ignored if [TVS_HASLINES](#TVS_HASLINES) is not also specified.
  TVS_NOHSCROLL         0x8000   +/-HScroll. Disables horizontal scrolling in the control. The control will not display any horizontal scroll bars.
  TVS_NONEVENHEIGHT     0x4000   Sets the height of the items to an odd height with the TVM_SETITEMHEIGHT message. By default, the height of items must be an even value.
  TVS_NOSCROLL          0x2000   Disables both horizontal and vertical scrolling in the control. The control will not display any scroll bars.
  TVS_NOTOOLTIPS        0x80     Disables tooltips.
  TVS_RTLREADING        0x40     Causes text to be displayed from right-to-left (RTL). Usually, windows display text left-to-right (LTR).
  TVS_SHOWSELALWAYS     0x20     Causes a selected item to remain selected when the tree-view control loses focus.
  TVS_SINGLEEXPAND      0x400    Causes the item being selected to expand and the item being unselected to collapse upon selection in the tree-view. If the user holds down [Ctrl]{.kbd} while selecting an item, the item being unselected will not be collapsed.
  TVS_TRACKSELECT       0x200    Enables hot tracking of the mouse in a tree-view control.

## DateTime Control Styles {#DateTime}

These styles affect the [DateTime](../lib/GuiControls.htm#DateTime)
control. By default, it uses
[DTS_SHORTDATECENTURYFORMAT](#DTS_SHORTDATECENTURYFORMAT) and
[WS_TABSTOP](#WS_TABSTOP). It has no forced styles.

  Style                        Hex    Description
  ---------------------------- ------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  DTS_UPDOWN                   0x1    Provides an up-down control to the right of the control to modify date-time values, which replaces the of the drop-down month calendar that would otherwise be available.
  DTS_SHOWNONE                 0x2    Displays a checkbox inside the control that users can uncheck to make the control have no date/time selected. Whenever the control has no date/time, [Gui.Submit](../lib/Gui.htm#Submit) and [GuiControl.Value](../lib/GuiControl.htm#Value) will retrieve a blank value (empty string).
  DTS_SHORTDATEFORMAT          0x0    Displays the date in short format. In some locales, it looks like 6/1/05 or 6/1/2005. On older operating systems, a two-digit year might be displayed. This is why [DTS_SHORTDATECENTURYFORMAT](#DTS_SHORTDATECENTURYFORMAT) is the default and not [DTS_SHORTDATEFORMAT](#DTS_SHORTDATEFORMAT).
  DTS_LONGDATEFORMAT           0x4    [Format option](../lib/GuiControls.htm#DateTimeFormat) \"LongDate\". Displays the date in long format. In some locales, it looks like Wednesday, June 01, 2005.
  DTS_SHORTDATECENTURYFORMAT   0xC    [Format option](../lib/GuiControls.htm#DateTimeFormat) blank/omitted. Displays the date in short format with four-digit year. In some locales, it looks like 6/1/2005. If the system\'s version of Comctl32.dll is older than 5.8, this style is not supported and [DTS_SHORTDATEFORMAT](#DTS_SHORTDATEFORMAT) is automatically substituted.
  DTS_TIMEFORMAT               0x9    [Format option](../lib/GuiControls.htm#DateTimeFormat) \"Time\". Displays only the time, which in some locales looks like 5:31:42 PM.
  DTS_APPCANPARSE              0x10   Not yet supported. Allows the owner to parse user input and take necessary action. It enables users to edit within the client area of the control when they press [F2]{.kbd}. The control sends DTN_USERSTRING notification messages when users are finished.
  DTS_RIGHTALIGN               0x20   +/-Right. The calendar will drop down on the right side of the control instead of the left.

## MonthCal Control Styles {#MonthCal}

These styles affect the [MonthCal](../lib/GuiControls.htm#MonthCal)
control. By default, it uses [WS_TABSTOP](#WS_TABSTOP). It has no forced
styles.

+-----------------------+-----------------------+-----------------------+
| Style                 | Hex                   | Description           |
+=======================+=======================+=======================+
| MCS_DAYSTATE          | 0x1                   | Makes the control     |
|                       |                       | send MCN_GETDAYSTATE  |
|                       |                       | notifications to      |
|                       |                       | request information   |
|                       |                       | about which days      |
|                       |                       | should be displayed   |
|                       |                       | in bold. \[Not yet    |
|                       |                       | supported\]           |
+-----------------------+-----------------------+-----------------------+
| MCS_MULTISELECT       | 0x2                   | Named option          |
|                       |                       | \"Multi\". Allows the |
|                       |                       | user to select a      |
|                       |                       | range of dates rather |
|                       |                       | than being limited to |
|                       |                       | a single date. By     |
|                       |                       | default, the maximum  |
|                       |                       | range is 366 days,    |
|                       |                       | which can be changed  |
|                       |                       | by sending the        |
|                       |                       | MCM_SETMAXSELCOUNT    |
|                       |                       | message to the        |
|                       |                       | control. For example: |
|                       |                       |                       |
|                       |                       |     SendM             |
|                       |                       | essage 0x1004, 7, 0,  |
|                       |                       | "SysMonthCal321", MyG |
|                       |                       | ui ; 7 days. 0x1004 i |
|                       |                       | s MCM_SETMAXSELCOUNT. |
+-----------------------+-----------------------+-----------------------+
| MCS_WEEKNUMBERS       | 0x4                   | Displays week numbers |
|                       |                       | (1-52) to the left of |
|                       |                       | each row of days.     |
|                       |                       | Week 1 is defined as  |
|                       |                       | the first week that   |
|                       |                       | contains at least     |
|                       |                       | four days.            |
+-----------------------+-----------------------+-----------------------+
| MCS_NOTODAYCIRCLE     | 0x8                   | Prevents the circling |
|                       |                       | of today\'s date      |
|                       |                       | within the control.   |
+-----------------------+-----------------------+-----------------------+
| MCS_NOTODAY           | 0x10                  | Prevents the display  |
|                       |                       | of today\'s date at   |
|                       |                       | the bottom of the     |
|                       |                       | control.              |
+-----------------------+-----------------------+-----------------------+

## Slider Control Styles {#Slider}

These styles affect the [Slider](../lib/GuiControls.htm#Slider) control.
By default, it uses [WS_TABSTOP](#WS_TABSTOP). It has no forced styles.

+-----------------------+-----------------------+-----------------------+
| Style                 | Hex                   | Description           |
+=======================+=======================+=======================+
| TBS_VERT              | 0x2                   | +/-Vertical. The      |
|                       |                       | control is oriented   |
|                       |                       | vertically.           |
+-----------------------+-----------------------+-----------------------+
| TBS_LEFT              | 0x4                   | +/-Left. The control  |
|                       |                       | displays tick marks   |
|                       |                       | at the top of the     |
|                       |                       | control (or to its    |
|                       |                       | left if               |
|                       |                       | [TBS_VERT](#TBS_VERT) |
|                       |                       | is present). Same as  |
|                       |                       | [TBS_TOP](#TBS_TOP).  |
+-----------------------+-----------------------+-----------------------+
| TBS_TOP               | 0x4                   | same as               |
|                       |                       | [                     |
|                       |                       | TBS_LEFT](#TBS_LEFT). |
+-----------------------+-----------------------+-----------------------+
| TBS_BOTH              | 0x8                   | +/-Center. The        |
|                       |                       | control displays tick |
|                       |                       | marks on both sides   |
|                       |                       | of the control. This  |
|                       |                       | will be both top and  |
|                       |                       | bottom when used with |
|                       |                       | TBS_HORZ or both left |
|                       |                       | and right if used     |
|                       |                       | with                  |
|                       |                       | [                     |
|                       |                       | TBS_VERT](#TBS_VERT). |
+-----------------------+-----------------------+-----------------------+
| TBS_AUTOTICKS         | 0x1                   | The control has a     |
|                       |                       | tick mark for each    |
|                       |                       | increment in its      |
|                       |                       | range of values. Use  |
|                       |                       | +/-TickInterval to    |
|                       |                       | have more             |
|                       |                       | flexibility.          |
+-----------------------+-----------------------+-----------------------+
| TBS_ENABLESELRANGE    | 0x20                  | The control displays  |
|                       |                       | a selection range     |
|                       |                       | only. The tick marks  |
|                       |                       | at the starting and   |
|                       |                       | ending positions of a |
|                       |                       | selection range are   |
|                       |                       | displayed as          |
|                       |                       | triangles (instead of |
|                       |                       | vertical dashes), and |
|                       |                       | the selection range   |
|                       |                       | is highlighted        |
|                       |                       | (highlighting might   |
|                       |                       | require that the      |
|                       |                       | theme be removed via  |
|                       |                       | `Gu                   |
|                       |                       | iObj.Opt("-Theme")`). |
|                       |                       |                       |
|                       |                       | To set the selection  |
|                       |                       | range, follow this    |
|                       |                       | example, which sets   |
|                       |                       | the starting position |
|                       |                       | to 55 and the ending  |
|                       |                       | position to 66:       |
|                       |                       |                       |
|                       |                       |     SendMessage 0x0   |
|                       |                       | 40B, 1, 55, "msctls_t |
|                       |                       | rackbar321", WinTitle |
|                       |                       |     SendMessage 0x0   |
|                       |                       | 40C, 1, 66, "msctls_t |
|                       |                       | rackbar321", WinTitle |
+-----------------------+-----------------------+-----------------------+
| TBS_FIXEDLENGTH       | 0x40                  | +/-Thick. Allows the  |
|                       |                       | thumb\'s size to be   |
|                       |                       | changed.              |
+-----------------------+-----------------------+-----------------------+
| TBS_NOTHUMB           | 0x80                  | The control does not  |
|                       |                       | display the moveable  |
|                       |                       | bar.                  |
+-----------------------+-----------------------+-----------------------+
| TBS_NOTICKS           | 0x10                  | +/-NoTicks. The       |
|                       |                       | control does not      |
|                       |                       | display any tick      |
|                       |                       | marks.                |
+-----------------------+-----------------------+-----------------------+
| TBS_TOOLTIPS          | 0x100                 | +/-ToolTip. The       |
|                       |                       | control supports      |
|                       |                       | tooltips. When a      |
|                       |                       | control is created    |
|                       |                       | using this style, it  |
|                       |                       | automatically creates |
|                       |                       | a default ToolTip     |
|                       |                       | control that displays |
|                       |                       | the slider\'s current |
|                       |                       | position. You can     |
|                       |                       | change where the      |
|                       |                       | tooltips are          |
|                       |                       | displayed by using    |
|                       |                       | the TBM_SETTIPSIDE    |
|                       |                       | message.              |
+-----------------------+-----------------------+-----------------------+
| TBS_REVERSED          | 0x200                 | Unfortunately, this   |
|                       |                       | style has no effect   |
|                       |                       | on the actual         |
|                       |                       | behavior of the       |
|                       |                       | control, so there is  |
|                       |                       | probably no point in  |
|                       |                       | using it (instead,    |
|                       |                       | use +Invert in the    |
|                       |                       | control\'s options to |
|                       |                       | reverse it).          |
|                       |                       | Depending on OS       |
|                       |                       | version, this style   |
|                       |                       | might require         |
|                       |                       | Internet Explorer 5.0 |
|                       |                       | or greater.           |
+-----------------------+-----------------------+-----------------------+
| TBS_DOWNISLEFT        | 0x400                 | Unfortunately, this   |
|                       |                       | style has no effect   |
|                       |                       | on the actual         |
|                       |                       | behavior of the       |
|                       |                       | control, so there is  |
|                       |                       | probably no point in  |
|                       |                       | using it. Depending   |
|                       |                       | on OS version, this   |
|                       |                       | style might require   |
|                       |                       | Internet Explorer     |
|                       |                       | 5.01 or greater.      |
+-----------------------+-----------------------+-----------------------+

## Progress Control Styles {#Progress}

These styles affect the [Progress](../lib/GuiControls.htm#Progress)
control. It has neither default styles nor forced styles.

+-----------------------+-----------------------+-----------------------+
| Style                 | Hex                   | Description           |
+=======================+=======================+=======================+
| PBS_SMOOTH            | 0x1                   | +/-Smooth. The        |
|                       |                       | progress bar displays |
|                       |                       | progress status in a  |
|                       |                       | smooth scrolling bar  |
|                       |                       | instead of the        |
|                       |                       | default segmented     |
|                       |                       | bar. When this style  |
|                       |                       | is present, the       |
|                       |                       | control automatically |
|                       |                       | reverts to the        |
|                       |                       | Classic Theme         |
|                       |                       | appearance.           |
+-----------------------+-----------------------+-----------------------+
| PBS_VERTICAL          | 0x4                   | +/-Vertical. The      |
|                       |                       | progress bar displays |
|                       |                       | progress status       |
|                       |                       | vertically, from      |
|                       |                       | bottom to top.        |
+-----------------------+-----------------------+-----------------------+
| PBS_MARQUEE           | 0x8                   | The progress bar      |
|                       |                       | moves like a marquee; |
|                       |                       | that is, each change  |
|                       |                       | to its position       |
|                       |                       | causes the bar to     |
|                       |                       | slide further along   |
|                       |                       | its available length  |
|                       |                       | until it wraps around |
|                       |                       | to the other side. A  |
|                       |                       | bar with this style   |
|                       |                       | has no defined        |
|                       |                       | position. Each        |
|                       |                       | attempt to change its |
|                       |                       | position will instead |
|                       |                       | slide the bar by one  |
|                       |                       | increment.            |
|                       |                       |                       |
|                       |                       | This style is         |
|                       |                       | typically used to     |
|                       |                       | indicate an ongoing   |
|                       |                       | operation whose       |
|                       |                       | completion time is    |
|                       |                       | unknown.              |
+-----------------------+-----------------------+-----------------------+

## Tab Control Styles {#Tab}

These styles affect the [Tab](../lib/GuiControls.htm#Tab) control. By
default, it uses [WS_TABSTOP](#WS_TABSTOP) and
[TCS_MULTILINE](#TCS_MULTILINE). The style
[WS_CLIPSIBLINGS](#WS_CLIPSIBLINGS) is always enabled and cannot be
disabled, while [TCS_OWNERDRAWFIXED](#TCS_OWNERDRAWFIXED) is forced on
or off as required by the control\'s background color and/or text color.

+-----------------------+-----------------------+-----------------------+
| Style                 | Hex                   | Description           |
+=======================+=======================+=======================+
| TCS_SCROLLOPPOSITE    | 0x1                   | Unneeded tabs scroll  |
|                       |                       | to the opposite side  |
|                       |                       | of the control when a |
|                       |                       | tab is selected.      |
+-----------------------+-----------------------+-----------------------+
| TCS_BOTTOM            | 0x2                   | +/-Bottom. Tabs       |
|                       |                       | appear at the bottom  |
|                       |                       | of the control        |
|                       |                       | instead of the top.   |
+-----------------------+-----------------------+-----------------------+
| TCS_RIGHT             | 0x2                   | Tabs appear           |
|                       |                       | vertically on the     |
|                       |                       | right side of         |
|                       |                       | controls that use the |
|                       |                       | [TCS_VER              |
|                       |                       | TICAL](#TCS_VERTICAL) |
|                       |                       | style.                |
+-----------------------+-----------------------+-----------------------+
| TCS_MULTISELECT       | 0x4                   | Multiple tabs can be  |
|                       |                       | selected by holding   |
|                       |                       | down [Ctrl]{.kbd}     |
|                       |                       | when clicking. This   |
|                       |                       | style must be used    |
|                       |                       | with the              |
|                       |                       | [TCS_B                |
|                       |                       | UTTONS](#TCS_BUTTONS) |
|                       |                       | style.                |
+-----------------------+-----------------------+-----------------------+
| TCS_FLATBUTTONS       | 0x8                   | Selected tabs appear  |
|                       |                       | as being indented     |
|                       |                       | into the background   |
|                       |                       | while other tabs      |
|                       |                       | appear as being on    |
|                       |                       | the same plane as the |
|                       |                       | background. This      |
|                       |                       | style only affects    |
|                       |                       | tab controls with the |
|                       |                       | [TCS_B                |
|                       |                       | UTTONS](#TCS_BUTTONS) |
|                       |                       | style.                |
+-----------------------+-----------------------+-----------------------+
| TCS_FORCEICONLEFT     | 0x10                  | Icons are aligned     |
|                       |                       | with the left edge of |
|                       |                       | each fixed-width tab. |
|                       |                       | This style can only   |
|                       |                       | be used with the      |
|                       |                       | [TCS_FIXEDWI          |
|                       |                       | DTH](#TCS_FIXEDWIDTH) |
|                       |                       | style.                |
+-----------------------+-----------------------+-----------------------+
| TCS_FORCELABELLEFT    | 0x20                  | Labels are aligned    |
|                       |                       | with the left edge of |
|                       |                       | each fixed-width tab; |
|                       |                       | that is, the label is |
|                       |                       | displayed immediately |
|                       |                       | to the right of the   |
|                       |                       | icon instead of being |
|                       |                       | centered.             |
|                       |                       |                       |
|                       |                       | This style can only   |
|                       |                       | be used with the      |
|                       |                       | [TCS_FIXEDWI          |
|                       |                       | DTH](#TCS_FIXEDWIDTH) |
|                       |                       | style, and it implies |
|                       |                       | the                   |
|                       |                       | [TCS_FORCEICONLEFT    |
|                       |                       | ](#TCS_FORCEICONLEFT) |
|                       |                       | style.                |
+-----------------------+-----------------------+-----------------------+
| TCS_HOTTRACK          | 0x40                  | Items under the       |
|                       |                       | pointer are           |
|                       |                       | automatically         |
|                       |                       | highlighted.          |
+-----------------------+-----------------------+-----------------------+
| TCS_VERTICAL          | 0x80                  | +/-Left or +/-Right.  |
|                       |                       | Tabs appear at the    |
|                       |                       | left side of the      |
|                       |                       | control, with tab     |
|                       |                       | text displayed        |
|                       |                       | vertically. This      |
|                       |                       | style is valid only   |
|                       |                       | when used with the    |
|                       |                       | [TCS_MULTI            |
|                       |                       | LINE](#TCS_MULTILINE) |
|                       |                       | style. To make tabs   |
|                       |                       | appear on the right   |
|                       |                       | side of the control,  |
|                       |                       | also use the          |
|                       |                       | [T                    |
|                       |                       | CS_RIGHT](#TCS_RIGHT) |
|                       |                       | style.                |
|                       |                       |                       |
|                       |                       | This style will not   |
|                       |                       | correctly display the |
|                       |                       | tabs if a custom      |
|                       |                       | background color or   |
|                       |                       | text color is in      |
|                       |                       | effect. To workaround |
|                       |                       | this, specify         |
|                       |                       | -Background and/or    |
|                       |                       | cDefault in the tab   |
|                       |                       | control\'s options.   |
+-----------------------+-----------------------+-----------------------+
| TCS_BUTTONS           | 0x100                 | +/-Buttons. Tabs      |
|                       |                       | appear as buttons,    |
|                       |                       | and no border is      |
|                       |                       | drawn around the      |
|                       |                       | display area.         |
+-----------------------+-----------------------+-----------------------+
| TCS_SINGLELINE        | 0x0                   | +/-Wrap. Only one row |
|                       |                       | of tabs is displayed. |
|                       |                       | The user can scroll   |
|                       |                       | to see more tabs, if  |
|                       |                       | necessary. This style |
|                       |                       | is the default.       |
+-----------------------+-----------------------+-----------------------+
| TCS_MULTILINE         | 0x200                 | +/-Wrap. Multiple     |
|                       |                       | rows of tabs are      |
|                       |                       | displayed, if         |
|                       |                       | necessary, so all     |
|                       |                       | tabs are visible at   |
|                       |                       | once.                 |
+-----------------------+-----------------------+-----------------------+
| TCS_RIGHTJUSTIFY      | 0x0                   | This is the default.  |
|                       |                       | The width of each tab |
|                       |                       | is increased, if      |
|                       |                       | necessary, so that    |
|                       |                       | each row of tabs      |
|                       |                       | fills the entire      |
|                       |                       | width of the tab      |
|                       |                       | control.              |
|                       |                       |                       |
|                       |                       | This window style is  |
|                       |                       | ignored unless the    |
|                       |                       | [TCS_MULTI            |
|                       |                       | LINE](#TCS_MULTILINE) |
|                       |                       | style is also         |
|                       |                       | specified.            |
+-----------------------+-----------------------+-----------------------+
| TCS_FIXEDWIDTH        | 0x400                 | All tabs are the same |
|                       |                       | width. This style     |
|                       |                       | cannot be combined    |
|                       |                       | with the              |
|                       |                       | [TCS_RIGHTJUSTIF      |
|                       |                       | Y](#TCS_RIGHTJUSTIFY) |
|                       |                       | style.                |
+-----------------------+-----------------------+-----------------------+
| TCS_RAGGEDRIGHT       | 0x800                 | Rows of tabs will not |
|                       |                       | be stretched to fill  |
|                       |                       | the entire width of   |
|                       |                       | the control. This     |
|                       |                       | style is the default. |
+-----------------------+-----------------------+-----------------------+
| TCS_FOCUSONBUTTONDOWN | 0x1000                | The tab control       |
|                       |                       | receives the input    |
|                       |                       | focus when clicked.   |
+-----------------------+-----------------------+-----------------------+
| TCS_OWNERDRAWFIXED    | 0x2000                | The parent window is  |
|                       |                       | responsible for       |
|                       |                       | drawing tabs.         |
+-----------------------+-----------------------+-----------------------+
| TCS_TOOLTIPS          | 0x4000                | The tab control has a |
|                       |                       | tooltip control       |
|                       |                       | associated with it.   |
+-----------------------+-----------------------+-----------------------+
| TCS_FOCUSNEVER        | 0x8000                | The tab control does  |
|                       |                       | not receive the input |
|                       |                       | focus when clicked.   |
+-----------------------+-----------------------+-----------------------+

## StatusBar Control Styles {#StatusBar}

These styles affect the [StatusBar](../lib/GuiControls.htm#StatusBar)
control. By default, it uses [SBARS_TOOLTIPS](#SBARS_TOOLTIPS) and
[SBARS_SIZEGRIP](#SBARS_SIZEGRIP) (the latter only if the window is
resizable). It has no forced styles.

+-----------------------+-----------------------+-----------------------+
| Style                 | Hex                   | Description           |
+=======================+=======================+=======================+
| SBARS_TOOLTIPS        | 0x800                 | Displays a tooltip    |
|                       |                       | when the mouse hovers |
|                       |                       | over a part of the    |
|                       |                       | status bar that: 1)   |
|                       |                       | has too much text to  |
|                       |                       | be fully displayed;   |
|                       |                       | or 2) has an icon but |
|                       |                       | no text.              |
|                       |                       |                       |
|                       |                       | The text of the       |
|                       |                       | tooltip can be set    |
|                       |                       | via:                  |
|                       |                       |                       |
|                       |                       |     S                 |
|                       |                       | endMessage 0x0411, 0, |
|                       |                       |  StrPtr("Text to disp |
|                       |                       | lay"), "msctls_status |
|                       |                       | bar321", MyGui ; 0x04 |
|                       |                       | 11 is SB_SETTIPTEXTW. |
|                       |                       |                       |
|                       |                       | The bold **0** above  |
|                       |                       | is the zero-based     |
|                       |                       | part number. To use a |
|                       |                       | part other than the   |
|                       |                       | first, specify 1 for  |
|                       |                       | second, 2 for the     |
|                       |                       | third, etc. NOTE: The |
|                       |                       | tooltip might never   |
|                       |                       | appear on certain OS  |
|                       |                       | versions.             |
+-----------------------+-----------------------+-----------------------+
| SBARS_SIZEGRIP        | 0x100                 | Includes a sizing     |
|                       |                       | grip at the right end |
|                       |                       | of the status bar. A  |
|                       |                       | sizing grip is        |
|                       |                       | similar to a sizing   |
|                       |                       | border; it is a       |
|                       |                       | rectangular area that |
|                       |                       | the user can click    |
|                       |                       | and drag to resize    |
|                       |                       | the parent window.    |
+-----------------------+-----------------------+-----------------------+
