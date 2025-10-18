# OnEvent

Registers a function or method to be called when the given event is
raised by a GUI window or control.

``` Syntax
Gui.OnEvent(EventName, Callback , AddRemove)
GuiCtrl.OnEvent(EventName, Callback , AddRemove)
```

## Parameters {#Parameters}

EventName

:   Type: [String](../Concepts.htm#strings)

    The name of the event. See [Events](#Events) further below.

Callback

:   Type: [String](../Concepts.htm#strings) or [Function
    Object](../misc/Functor.htm)

    The function, method or object to call when the event is raised.

    If the GUI has an event sink (that is, if [Gui()](Gui.htm#Call)\'s
    *EventObj* parameter was specified), this parameter may be the name
    of a method belonging to the event sink. Otherwise, this parameter
    must be a [function object](../misc/Functor.htm).

    For details about the parameters, return value, naming, and more,
    see the following sections.

AddRemove

:   Type: [Integer](../Concepts.htm#numbers)

    If omitted, it defaults to 1. Otherwise, specify one of the
    following numbers:

    -   1 = Call the callback after any previously registered callbacks.
    -   -1 = Call the callback before any previously registered
        callbacks.
    -   0 = Do not call the callback.

## Callback Parameters {#Callback_Parameters}

If the callback is a method registered by name, its hidden [*this*
parameter](../Objects.htm#Custom_Classes_method) seamlessly receives the
event sink object (that is, the object to which the method belongs).
This parameter is not shown in the parameter lists in this
documentation.

Since *Callback* can be an object, it can be a [BoundFunc
object](../misc/Functor.htm#BoundFunc) which inserts additional
parameters at the beginning of the parameter list and then calls another
function. This is a general technique not specific to OnEvent, so is
generally ignored by the rest of this documentation.

The callback\'s first explicit parameter is the [Gui](Gui.htm) or
[GuiControl](GuiControl.htm) object which raised the event. The only
exception is that this parameter is omitted when a Gui [handles its own
events](Gui.htm#EventObj), since `this` already contains a reference to
the Gui.

Many events pass additional parameters about the event, as described for
each event.

As with all methods or functions called dynamically, the callback is not
required to declare parameters which the callback itself does not need,
but in this case an asterisk must be specified as the final parameter,
e.g. `MyCallback(Param1, *)`. If an event has more parameters than are
declared by the callback, they will simply be ignored (unless the
callback is [variadic](../Functions.htm#Variadic)).

The callback can declare more parameters than the event provides if (and
only if) the additional parameters are declared optional. However, the
use of optional parameters is not recommended as future versions of the
program may extend an event with additional parameters, in which case
the optional parameters would stop receiving their default values.

## Callback Return Value {#Callback_Return_Value}

If multiple callbacks have been registered for an event, a callback may
return a non-empty value to prevent any remaining callbacks from being
called.

The return value may have additional meaning for specific events. For
example, a [Close](#Close) callback may return a non-zero number (such
as `true`) to prevent the GUI window from closing.

## Callback Name {#Callback_Name}

By convention, the syntax of each event below is shown with a function
name of the form *`ObjectType`*`_`*`EventName`*, for clarity. Scripts
are not required to follow this convention, and can use any valid
function name.

## Threads {#Threads}

Each event callback is called in a new [thread](../misc/Threads.htm),
and therefore starts off fresh with the default values for settings such
as [SendMode](SendMode.htm). These defaults can be changed during
[script startup](../Scripts.htm#auto).

Whenever a GUI [thread](../misc/Threads.htm) is launched, that thread\'s
[last found window](../misc/WinTitle.htm#LastFoundWindow) starts off as
the GUI window itself. This allows functions for windows and controls
\-- such as [WinGetStyle](WinGetStyle.htm),
[WinSetTransparent](WinSetTransparent.htm), and
[ControlGetFocus](ControlGetFocus.htm) \-- to omit *WinTitle* and
*WinText* when operating upon the GUI window itself (even if it is
hidden).

Except where noted, each event is limited to one thread at a time, per
object. If an event is raised before a previous thread started by that
event finishes, it is usually discarded. To prevent this, use
[Critical](Critical.htm) as the callback\'s first line (however, this
will also buffer/defer other [threads](../misc/Threads.htm) such as the
press of a hotkey).

## Destroying the GUI {#Destroying_the_GUI}

When a GUI is destroyed, all event callbacks are released. Therefore, if
the GUI is destroyed while an event is being dispatched, subsequent
event callbacks are not called. For clarity, callbacks should [return a
non-empty value](#Callback_Return_Value) after destroying the GUI.

## Events {#Events}

The following events are supported by [Gui](Gui.htm) objects:

  Event                         Raised when\...
  ----------------------------- -----------------------------------------------------------------------------------------------
  [Close](#Close)               The window is closed.
  [ContextMenu](#ContextMenu)   The user right-clicks within the window or presses [Menu]{.kbd} or [Shift]{.kbd}+[F10]{.kbd}.
  [DropFiles](#DropFiles)       Files/folders are dragged and dropped onto the window.
  [Escape](#Escape)             The user presses [Esc]{.kbd} while the GUI window is active.
  [Size](#Size)                 The window is resized, minimized, maximized or restored.

The following events are supported by [GuiControl](GuiControl.htm)
objects, depending on the control type:

  Event                              Raised when\...
  ---------------------------------- ----------------------------------------------------------------------------------------------------------------------------------
  [Change](#Change)                  The control\'s value changes.
  [Click](#Click)                    The control is clicked.
  [DoubleClick](#DoubleClick)        The control is double-clicked.
  [ColClick](#ColClick)              One of the ListView\'s column headers is clicked.
  [ContextMenu](#Ctrl-ContextMenu)   The user right-clicks the control or presses [Menu]{.kbd} or [Shift]{.kbd}+[F10]{.kbd} while the control has the keyboard focus.
  [Focus](#Focus)                    The control gains the keyboard focus.
  [LoseFocus](#LoseFocus)            The control loses the keyboard focus.
  [ItemCheck](#ItemCheck)            A ListView or TreeView item is checked or unchecked.
  [ItemEdit](#ItemEdit)              A ListView or TreeView item\'s label is edited by the user.
  [ItemExpand](#ItemExpand)          A TreeView item is expanded or collapsed.
  [ItemFocus](#ItemFocus)            The focused item changes in a ListView.
  [ItemSelect](#ItemSelect)          A ListView or TreeView item is selected, or a ListView item is deselected.

## Window Events {#Window_Events}

### Close {#Close}

Launched when the user or another program attempts to close the window,
such as by pressing the X button in its title bar, selecting \"Close\"
from its system menu, or calling [WinClose](WinClose.htm).

``` Syntax
Gui_Close(GuiObj)
```

By default, the window is automatically hidden after the callback
returns, or if no callbacks were registered. A callback can prevent this
by returning 1 (or `true`), which will also prevent any remaining
callbacks from being called. The callback can hide the window
immediately by calling [GuiObj.Hide](Gui.htm#Hide), or destroy the
window by calling [GuiObj.Destroy](Gui.htm#Destroy).

For example, this GUI shows a confirmation prompt before closing:

    MyGui := Gui()
    MyGui.AddText("", "Press Alt+F4 or the X button in the title bar.")
    MyGui.OnEvent("Close", MyGui_Close)
    MyGui_Close(thisGui) {  ; Declaring this parameter is optional.
        if MsgBox("Are you sure you want to close the GUI?",, "y/n") = "No"
            return true  ; true = 1
    }
    MyGui.Show()

### ContextMenu {#ContextMenu}

Launched whenever the user right-clicks anywhere in the window except
the title bar and menu bar. It is also launched in response to pressing
[Menu]{.kbd} or [Shift]{.kbd}+[F10]{.kbd}.

``` Syntax
Gui_ContextMenu(GuiObj, GuiCtrlObj, Item, IsRightClick, X, Y)
```

GuiCtrlObj

:   Type: [Object](../Concepts.htm#objects) or [String
    (empty)](../Concepts.htm#nothing)

    The [GuiControl object](GuiControl.htm) of the control that received
    the event (blank if none).

Item

:   Type: [Integer](../Concepts.htm#numbers)

    When a ListBox, ListView, or TreeView is the target of the context
    menu (as determined by *GuiCtrlObj*), *Item* specifies which of the
    control\'s items is the target.

    [ListBox](GuiControls.htm#ListBox): The position number of the
    currently focused item. Note that a standard ListBox does not focus
    an item when it is right-clicked, so this might not be the clicked
    item.

    [ListView](ListView.htm) and [TreeView](TreeView.htm): For
    right-clicks, *Item* contains the clicked item\'s row number or ID
    (or 0 if the user clicked somewhere other than an item). For
    [Menu]{.kbd} and [Shift]{.kbd}+[F10]{.kbd}, *Item* contains the
    selected item\'s row number or ID.

IsRightClick

:   Type: [Integer (boolean)](../Concepts.htm#boolean)

    One of the following values:

    -   1 (true) = The user clicked the right mouse button.
    -   0 (false) = The user pressed [Menu]{.kbd} or
        [Shift]{.kbd}+[F10]{.kbd}.

X, Y

:   Type: [Integer](../Concepts.htm#numbers)

    The X and Y coordinates of where the script should display the menu
    (e.g. `MyContextMenu.`[`Show`](Menu.htm#Show)` X, Y`). Coordinates
    are relative to the upper-left corner of the window\'s client area.

Unlike most other GUI events, the ContextMenu event can have more than
one concurrent [thread](../misc/Threads.htm).

Each control can have its own ContextMenu event callback which is called
before any callback registered for the Gui object. Control-specific
callbacks omit the *GuiObj* parameter, but all other parameters are the
same.

Note: Since [Edit](GuiControls.htm#Edit) and
[MonthCal](GuiControls.htm#MonthCal) controls have their own context
menu, a right-click in one of them will not launch the ContextMenu
event.

### DropFiles {#DropFiles}

Launched whenever files/folders are dropped onto the window as part of a
drag-and-drop operation (but if this callback is already running, drop
events are ignored).

``` Syntax
Gui_DropFiles(GuiObj, GuiCtrlObj, FileArray, X, Y)
```

GuiCtrlObj

:   Type: [Object](../Concepts.htm#objects) or [String
    (empty)](../Concepts.htm#nothing)

    The [GuiControl object](GuiControl.htm) of the control upon which
    the files were dropped (blank if none).

FileArray

:   Type: [Array](Array.htm)

    An array of filenames, where `FileArray[1]` is the first file and
    `FileArray.Length` returns the number of files. A
    [for-loop](For.htm) can be used to iterate through the files:

        Gui_DropFiles(GuiObj, GuiCtrlObj, FileArray, X, Y) {
            for i, DroppedFile in FileArray
                MsgBox "File " i " is:`n" DroppedFile
        }

X, Y

:   Type: [Integer](../Concepts.htm#numbers)

    The X and Y coordinates of where the files were dropped, relative to
    the upper-left corner of the window\'s client area.

### Escape {#Escape}

Launched when the user presses [Esc]{.kbd} while the GUI window is
active.

``` Syntax
Gui_Escape(GuiObj)
```

By default, pressing [Esc]{.kbd} has no effect. Known limitation: If the
first control in the window is disabled (possibly depending on control
type), the Escape event will not be launched. There may be other
circumstances that produce this effect.

### Size {#Size}

Launched when the window is resized, minimized, maximized, or restored.

``` Syntax
Gui_Size(GuiObj, MinMax, Width, Height)
```

MinMax

:   Type: [Integer](../Concepts.htm#numbers)

    One of the following values:

    -   0 = The window is neither minimized nor maximized.
    -   1 = The window is maximized.
    -   -1 = The window is minimized.

    Note that a maximized window can be resized without
    restoring/un-maximizing it, so a value of 1 does not necessarily
    mean that this event was raised in response to the user maximizing
    the window.

Width, Height

:   Type: [Integer](../Concepts.htm#numbers)

    The new width and height of the window\'s client area, which is the
    area excluding title bar, menu bar, and borders.

A script may use the Size event to reposition and resize controls in
response to the user\'s resizing of the window.

When the window is resized (even by the script), the Size event might
not be raised immediately. As with other window events, if the current
thread is [uninterruptible](Thread.htm#Interrupt), the Size event won\'t
be raised until the thread becomes interruptible. If the script has just
resized the window, follow this example to ensure the Size event is
raised immediately:

    Critical "Off"  ; Even if Critical "On" was never used.
    Sleep -1

[Gui.Show](Gui.htm#Show) automatically does a `Sleep -1`, so it is
generally not necessary to call Sleep in that case.

## Control Events {#Control_Events}

### Change {#Change}

Raised when the control\'s value changes.

``` Syntax
Ctrl_Change(GuiCtrlObj, Info)
```

Info

:   Type: [Integer](../Concepts.htm#numbers)

    [Slider](GuiControls.htm#Slider): A numeric value indicating how the
    slider moved. For details, see [Detecting
    Changes](GuiControls.htm#slider-change).

    For all other controls, *Info* currently has no meaning.

To retrieve the control\'s new value, use
[GuiCtrlObj.Value](GuiControl.htm#Value).

Applies to: [DDL](GuiControls.htm#DDL),
[ComboBox](GuiControls.htm#ComboBox),
[ListBox](GuiControls.htm#ListBox), [Edit](GuiControls.htm#Edit),
[DateTime](GuiControls.htm#DateTime),
[MonthCal](GuiControls.htm#MonthCal), [Hotkey](GuiControls.htm#Hotkey),
[UpDown](GuiControls.htm#UpDown), [Slider](GuiControls.htm#Slider),
[Tab](GuiControls.htm#Tab).

### Click {#Click}

Raised when the control is clicked.

``` Syntax
Ctrl_Click(GuiCtrlObj, Info)
Link_Click(GuiCtrlObj, Info, Href)
```

Info

:   Type: [Integer](../Concepts.htm#numbers)

    [ListView](GuiControls.htm#ListView): The row number of the clicked
    item, or 0 if the mouse was not over an item.

    [TreeView](GuiControls.htm#TreeView): The ID of the clicked item, or
    0 if the mouse was not over an item.

    [Link](GuiControls.htm#Link): The link\'s ID attribute (a string) if
    it has one, otherwise the link\'s index (an integer).

    [StatusBar](GuiControls.htm#StatusBar): The part number of the
    clicked section (however, the part number might be a very large
    integer if the user clicks near the sizing grip at the right side of
    the bar).

    For all other controls, *Info* currently has no meaning.

Href

:   Type: [String](../Concepts.htm#strings)

    [Link](GuiControls.htm#Link): The link\'s HREF attribute. Note that
    if a Click event callback is registered, the HREF attribute is not
    automatically executed.

Applies to: [Text](GuiControls.htm#Text), [Pic](GuiControls.htm#Pic),
[Button](GuiControls.htm#Button), [CheckBox](GuiControls.htm#CheckBox),
[Radio](GuiControls.htm#Radio), [ListView](ListView.htm),
[TreeView](TreeView.htm), [Link](GuiControls.htm#Link),
[StatusBar](GuiControls.htm#StatusBar).

### DoubleClick {#DoubleClick}

Raised when the control is double-clicked.

``` Syntax
Ctrl_DoubleClick(GuiCtrlObj, Info)
```

Info

:   Type: [Integer](../Concepts.htm#numbers)

    [ListView](GuiControls.htm#ListView),
    [TreeView](GuiControls.htm#TreeView) and
    [StatusBar](GuiControls.htm#StatusBar): Same as for the
    [Click](#Click) event.

    [ListBox](GuiControls.htm#ListBox): The position number of the
    currently focused item. Double-clicking empty space below the last
    item usually focuses the last item and leaves the selection as it
    was.

Applies to: [Text](GuiControls.htm#Text), [Pic](GuiControls.htm#Pic),
[Button](GuiControls.htm#Button), [CheckBox](GuiControls.htm#CheckBox),
[Radio](GuiControls.htm#Radio), [ComboBox](GuiControls.htm#ComboBox),
[ListBox](GuiControls.htm#ListBox), [ListView](ListView.htm),
[TreeView](TreeView.htm), [StatusBar](GuiControls.htm#StatusBar).

### ColClick {#ColClick}

Raised when one of the ListView\'s column headers is clicked.

``` Syntax
Ctrl_ColClick(GuiCtrlObj, Info)
```

Info

:   Type: [Integer](../Concepts.htm#numbers)

    The one-based column number that was clicked. This is the original
    number assigned when the column was created; that is, it does not
    reflect any dragging and dropping of columns done by the user.

Applies to: [ListView](ListView.htm).

### ContextMenu {#Ctrl-ContextMenu}

Raised when the user right-clicks the control or presses [Menu]{.kbd} or
[Shift]{.kbd}+[F10]{.kbd} while the control has the keyboard focus.

``` Syntax
Ctrl_ContextMenu(GuiCtrlObj, Item, IsRightClick, X, Y)
```

For details, see [ContextMenu](#ContextMenu).

Applies to: All controls except [Edit](GuiControls.htm#Edit) and
[MonthCal](GuiControls.htm#MonthCal) (and the Edit control within a
[ComboBox](GuiControls.htm#ComboBox)), which have their own standard
context menu.

[]{#LoseFocus}

### Focus / LoseFocus {#Focus}

Raised when the control gains or loses the keyboard focus.

``` Syntax
Ctrl_Focus(GuiCtrlObj, Info)
Ctrl_LoseFocus(GuiCtrlObj, Info)
```

Info

:   Reserved.

Applies to: [Button](GuiControls.htm#Button),
[CheckBox](GuiControls.htm#CheckBox), [Radio](GuiControls.htm#Radio),
[DDL](GuiControls.htm#DDL), [ComboBox](GuiControls.htm#ComboBox),
[ListBox](GuiControls.htm#ListBox), [ListView](ListView.htm),
[TreeView](TreeView.htm), [Edit](GuiControls.htm#Edit),
[DateTime](GuiControls.htm#DateTime).

Not supported: [Hotkey](GuiControls.htm#Hotkey),
[Slider](GuiControls.htm#Slider), [Tab](GuiControls.htm#Tab) and
[Link](GuiControls.htm#Link). Note that [Text](GuiControls.htm#Text),
[Pic](GuiControls.htm#Pic), [MonthCal](GuiControls.htm#MonthCal),
[UpDown](GuiControls.htm#UpDown) and
[StatusBar](GuiControls.htm#StatusBar) controls do not accept the
keyboard focus.

### ItemCheck {#ItemCheck}

Raised when a ListView or TreeView item is checked or unchecked.

``` Syntax
Ctrl_ItemCheck(GuiCtrlObj, Item, Checked)
```

Applies to: [ListView](ListView.htm), [TreeView](TreeView.htm).

### ItemEdit {#ItemEdit}

Raised when a ListView or TreeView item\'s label is edited by the user.

``` Syntax
Ctrl_ItemEdit(GuiCtrlObj, Item)
```

An item\'s label can only be edited if `-ReadOnly` has been used in the
control\'s options.

Applies to: [ListView](ListView.htm), [TreeView](TreeView.htm).

### ItemExpand {#ItemExpand}

Raised when a TreeView item is expanded or collapsed.

``` Syntax
Ctrl_ItemExpand(GuiCtrlObj, Item, Expanded)
```

Applies to: [TreeView](TreeView.htm).

### ItemFocus {#ItemFocus}

Raised when the focused item changes in a ListView.

``` Syntax
Ctrl_ItemFocus(GuiCtrlObj, Item)
```

Applies to: [ListView](ListView.htm).

### ItemSelect {#ItemSelect}

Raised when a ListView or TreeView item is selected, or a ListView item
is deselected.

``` Syntax
ListView_ItemSelect(GuiCtrlObj, Item, Selected)
TreeView_ItemSelect(GuiCtrlObj, Item)
```

Applies to: [ListView](ListView.htm), [TreeView](TreeView.htm).

ListView: This event is raised once for each item being deselected or
selected, so can be raised multiple times in response to a single action
by the user.

## Other Events {#Other_Events}

Other types of GUI events can be detected and acted upon via
[OnNotify](GuiOnNotify.htm), [OnCommand](GuiOnCommand.htm) or
[OnMessage](OnMessage.htm). For example, a script can display
context-sensitive help via ToolTip whenever the user moves the mouse
over particular controls in the window. This is demonstrated in the [GUI
ToolTip example](Gui.htm#ExToolTip).
