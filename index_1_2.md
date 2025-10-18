# AutoHotkey Script Showcase

This showcase lists some scripts created by different authors which show
what AutoHotkey might be capable of. For more ready-to-run scripts and
functions, see [AutoHotkey v2 Scripts and Functions
Forum](https://www.autohotkey.com/boards/viewforum.php?f=83).

## Table of Contents {#toc}

-   [Context Sensitive Help in Any Editor](#ContextSensitiveHelp)
-   [Easy Window Dragging](#EasyWindowDrag)
-   [Easy Window Dragging (KDE style)](#EasyWindowDrag_(KDE))
-   [Easy Access to Favorite Folders](#FavoriteFolders)
-   [Using a Controller as a Mouse](#ControllerMouse)
-   [Controller Test Script](#ControllerTest)
-   [On-Screen Keyboard](#KeyboardOnScreen)
-   [Minimize Window to Tray Menu](#MinimizeToTrayMenu)
-   [Changing MsgBox\'s Button Names](#MsgBoxButtonNames)
-   [Numpad 000 Key](#Numpad000)
-   [Using Keyboard Numpad as a Mouse](#NumpadMouse)
-   [Seek (Search the Start Menu)](#Seek_(SearchTheStartMenu))
-   [ToolTip Mouse Menu](#TooltipMouseMenu)
-   [Volume On-Screen-Display (OSD)](#VolumeOSD)
-   [Window Shading](#WindowShading)
-   [WinLIRC Client](#WinLIRC)
-   [HTML Entities Encoding](#HTML_Entities_Encoding)
-   [Custom Increments for UpDown
    Controls](#Custom_Increments_for_UpDown_Controls)
-   [AutoHotkey v1 Scripts and Functions
    Forum](#Scripts_and_Functions_Forum)

## Context Sensitive Help in Any Editor {#ContextSensitiveHelp}

Based on the v1 script by Rajat

This script makes [Ctrl]{.kbd}+[2]{.kbd} (or another hotkey of your
choice) show the help file page for the selected AutoHotkey function or
keyword. If nothing is selected, the function name will be extracted
from the beginning of the current line.

[Show code](ContextSensitiveHelp.ahk)

## Easy Window Dragging {#EasyWindowDrag}

Normally, a window can only be dragged by clicking on its title bar.
This script extends that so that any point inside a window can be
dragged. To activate this mode, hold down [CapsLock]{.kbd} or the middle
mouse button while clicking, then drag the window to a new position.

[Show code](EasyWindowDrag.ahk)

## Easy Window Dragging (KDE style) {#EasyWindowDrag_(KDE)}

Based on the v1 script by Jonny

This script makes it much easier to move or resize a window: 1) Hold
down [Alt]{.kbd} and LEFT-click anywhere inside a window to drag it to a
new location; 2) Hold down [Alt]{.kbd} and RIGHT-click-drag anywhere
inside a window to easily resize it; 3) Press [Alt]{.kbd} twice, but
before releasing it the second time, left-click to minimize the window
under the mouse cursor, right-click to maximize it, or middle-click to
close it.

[Show code](EasyWindowDrag_(KDE).ahk)

## Easy Access to Favorite Folders {#FavoriteFolders}

Based on the v1 script by Savage

When you click the middle mouse button while certain types of windows
are active, this script displays a menu of your favorite folders. Upon
selecting a favorite, the script will instantly switch to that folder
within the active window. The following window types are supported: 1)
Standard file-open or file-save dialogs; 2) Explorer windows; 3) Console
(command prompt) windows. The menu can also be optionally shown for
unsupported window types, in which case the chosen favorite will be
opened as a new Explorer window.

[Show code](FavoriteFolders.ahk)

## Using a Controller as a Mouse {#ControllerMouse}

This script converts a controller (gamepad, joystick, etc.) into a
three-button mouse. It allows each button to drag just like a mouse
button and it uses virtually no CPU time. Also, it will move the cursor
faster depending on how far you push the stick from center. You can
personalize various settings at the top of the script.

Note: For Xbox controller 2013 and newer (anything newer than the Xbox
360 controller), this script will only work if a window it owns is
active, such as a [message box](../lib/MsgBox.htm),
[GUI](../lib/Gui.htm), or the [script\'s main
window](../Program.htm#main-window).

[Show code](ControllerMouse.ahk)

## Controller Test Script {#ControllerTest}

This script helps determine the button numbers and other attributes of
your controller (gamepad, joystick, etc.). It might also reveal if your
controller is in need of calibration; that is, whether the range of
motion of each of its axes is from 0 to 100 percent as it should be. If
calibration is needed, use the operating system\'s control panel or the
software that came with your controller.

[Show code](ControllerTest.ahk)

## On-Screen Keyboard {#KeyboardOnScreen}

Based on the v1 script by Jon

This script creates a mock keyboard at the bottom of your screen that
shows the keys you are pressing in real time. I made it to help me to
learn to touch-type (to get used to not looking at the keyboard). The
size of the on-screen keyboard can be customized at the top of the
script. Also, you can double-click the [tray
icon](../Program.htm#tray-icon) to show or hide the keyboard.

[Show code](KeyboardOnScreen.ahk)

## Minimize Window to Tray Menu {#MinimizeToTrayMenu}

This script assigns a hotkey of your choice to hide any window so that
it becomes an entry at the bottom of the script\'s tray menu. Hidden
windows can then be unhidden individually or all at once by selecting
the corresponding item on the menu. If the script exits for any reason,
all the windows that it hid will be unhidden automatically.

[Show code](MinimizeToTrayMenu.ahk)

## Changing MsgBox\'s Button Names {#MsgBoxButtonNames}

This is a working example script that uses a timer to change the names
of the buttons in a message box. Although the button names are changed,
the MsgBox\'s return value still requires that the buttons be referred
to by their original names.

[Show code](MsgBoxButtonNames.ahk)

## Numpad 000 Key {#Numpad000}

This example script makes the special [000]{.kbd} that appears on
certain keypads into an equals key. You can change the action by
replacing the `Send "="` line with line(s) of your choice.

[Show code](Numpad000.ahk)

## Using Keyboard Numpad as a Mouse {#NumpadMouse}

Based on the v1 script by deguix

This script makes mousing with your keyboard almost as easy as using a
real mouse (maybe even easier for some tasks). It supports up to five
mouse buttons and the turning of the mouse wheel. It also features
customizable movement speed, acceleration, and \"axis inversion\".

[Show code](NumpadMouse.ahk)

## Seek (Search the Start Menu) {#Seek_(SearchTheStartMenu)}

Based on the v1 script by Phi

Navigating the Start Menu can be a hassle, especially if you have
installed many programs over time. \'Seek\' lets you specify a
case-insensitive key word/phrase that it will use to filter only the
matching programs and directories from the Start Menu, so that you can
easily open your target program from a handful of matched entries. This
eliminates the drudgery of searching and traversing the Start Menu.

[Show code](Seek_(SearchTheStartMenu).ahk)

## ToolTip Mouse Menu {#TooltipMouseMenu}

Based on the v1 script by Rajat

This script displays a popup menu in response to briefly holding down
the middle mouse button. Select a menu item by left-clicking it. Cancel
the menu by left-clicking outside of it. A recent improvement is that
the contents of the menu can change depending on which type of window is
active (Notepad and Word are used as examples here).

[Show code](TooltipMouseMenu.ahk)

## Volume On-Screen-Display (OSD) {#VolumeOSD}

Based on the v1 script by Rajat

This script assigns hotkeys of your choice to raise and lower the master
volume.

[Show code](VolumeOSD.ahk)

## Window Shading {#WindowShading}

Based on the v1 script by Rajat

This script reduces a window to its title bar and then back to its
original size by pressing a single hotkey. Any number of windows can be
reduced in this fashion (the script remembers each). If the script exits
for any reason, all \"rolled up\" windows will be automatically restored
to their original heights.

[Show code](WindowShading.ahk)

## WinLIRC Client {#WinLIRC}

This script receives notifications from
[WinLIRC](https://sourceforge.net/projects/winlirc/) whenever you press
a button on your remote control. It can be used to automate Winamp,
Windows Media Player, etc. It\'s easy to configure. For example, if
WinLIRC recognizes a button named \"VolUp\" on your remote control,
create a label named VolUp and beneath it use the function
`SoundSetVolume "+5"` to increase the soundcard\'s volume by 5 %.

[Show code](WinLIRC.ahk)

## HTML Entities Encoding {#HTML_Entities_Encoding}

Similar to AutoHotkey v1\'s [Transform
HTML](https://www.autohotkey.com/docs/v1/lib/Transform.htm#HTML), this
function converts a string into its HTML equivalent by translating
characters whose ASCII values are above 127 to their HTML names (e.g.
`£` becomes `&pound;`). In addition, the four characters `"&<>` are
translated to `&quot;&amp;&lt;&gt;`. Finally, each linefeed (`` `n ``)
is translated to `` <br>`n `` (i.e. `<br>` followed by a linefeed).

[Show code](EncodeHTML.ahk)

## Custom Increments for UpDown Controls {#Custom_Increments_for_UpDown_Controls}

Based on the v1 script by numEric

This script demonstrates how to change an
[UpDown](../lib/GuiControls.htm#UpDown)\'s increment to a value other
than 1 (such as 5 or 0.1).

[Show code](UpDownCustomIncrements.ahk)

## AutoHotkey v1 Scripts and Functions Forum {#Scripts_and_Functions_Forum}

This forum contains many more scripts, but most scripts will not run
as-is on AutoHotkey v2.0.

[AutoHotkey v1 Scripts and Functions
Forum](https://www.autohotkey.com/boards/viewforum.php?f=6)

Hide code

Loading code\...
