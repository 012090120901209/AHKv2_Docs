# List of Keys [(Keyboard, Mouse and Controller)]{.headnote}

## Table of Contents {#toc}

-   [Mouse](#mouse)
    -   [General Buttons](#mouse-general)
    -   [Advanced Buttons](#mouse-advanced)
    -   [Wheel](#mouse-wheel)
-   [Keyboard](#keyboard)
    -   [General Keys](#general)
    -   [Cursor Control Keys](#cursor)
    -   [Numpad Keys](#numpad)
    -   [Function Keys](#function)
    -   [Modifier Keys](#modifier)
    -   [Multimedia Keys](#multimedia)
    -   [Other Keys](#other)
-   [Game Controller (Gamepad, Joystick, etc.)](#Controller)
-   [Hand-held Remote Controls](#remote)
-   [Special Keys](#SpecialKeys)
-   [CapsLock and IME](#IME)

## Mouse

### General Buttons {#mouse-general}

  Name      Description
  --------- ----------------------------------------------------------------------------------------------------------------------------------
  LButton   Primary mouse button. Which physical button this corresponds to depends on system settings; by default it is the left button.
  RButton   Secondary mouse button. Which physical button this corresponds to depends on system settings; by default it is the right button.
  MButton   Middle or wheel mouse button

### Advanced Buttons {#mouse-advanced}

  Name       Description
  ---------- ----------------------------------------------------------------------------
  XButton1   4th mouse button. Typically performs the same function as Browser_Back.
  XButton2   5th mouse button. Typically performs the same function as Browser_Forward.

### Wheel {#mouse-wheel}

+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+===================================+===================================+
| WheelDown                         | Turn the wheel downward (toward   |
|                                   | you).                             |
+-----------------------------------+-----------------------------------+
| WheelUp                           | Turn the wheel upward (away from  |
|                                   | you).                             |
+-----------------------------------+-----------------------------------+
| WheelLeft\                        | Scroll to the left or right.      |
| WheelRight                        |                                   |
|                                   | These can be [used as             |
|                                   | hotkeys](Hotkeys.htm#HWheel) with |
|                                   | some (but not all) mice which     |
|                                   | have a second wheel or support    |
|                                   | tilting the wheel to either side. |
|                                   | In some cases, software bundled   |
|                                   | with the mouse must instead be    |
|                                   | used to control this feature.     |
|                                   | Regardless of the particular      |
|                                   | mouse, [Send](lib/Send.htm) and   |
|                                   | [Click](lib/Click.htm) can be     |
|                                   | used to scroll horizontally in    |
|                                   | programs which support it.        |
+-----------------------------------+-----------------------------------+

## Keyboard

**Note:** The names of the letter and number keys are the same as that
single letter or digit. For example: b is [B]{.kbd} and 5 is [5]{.kbd}.

Although any single character can be used as a key name, its meaning
(scan code or virtual keycode) depends on the current keyboard layout.
Additionally, some special characters may need to be escaped or enclosed
in braces, depending on the context. The letters a-z or A-Z can be used
to refer to the corresponding virtual keycodes (usually vk41-vk5A) even
if they are not included in the current keyboard layout.

### General Keys {#general}

+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+===================================+===================================+
| CapsLock                          | [CapsLock]{.kbd} (caps lock key)  |
|                                   |                                   |
|                                   | **Note:** Windows IME may         |
|                                   | interfere with the detection and  |
|                                   | functionality of CapsLock; see    |
|                                   | [CapsLock and IME](#IME) for      |
|                                   | details.                          |
+-----------------------------------+-----------------------------------+
| Space                             | [Space]{.kbd} (space bar)         |
+-----------------------------------+-----------------------------------+
| Tab                               | [Tab]{.kbd} (tabulator key)       |
+-----------------------------------+-----------------------------------+
| Enter                             | [Enter]{.kbd}                     |
+-----------------------------------+-----------------------------------+
| Escape (or Esc)                   | [Esc]{.kbd}                       |
+-----------------------------------+-----------------------------------+
| Backspace (or BS)                 | [Backspace]{.kbd}                 |
+-----------------------------------+-----------------------------------+

### Cursor Control Keys {#cursor}

  Name              Description
  ----------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ScrollLock        [ScrollLock]{.kbd} (scroll lock key). While [Ctrl]{.kbd} is held down, [ScrollLock]{.kbd} produces the key code of `CtrlBreak`, but can be differentiated from [Pause]{.kbd} by scan code.
  Delete (or Del)   [Del]{.kbd}
  Insert (or Ins)   [Ins]{.kbd}
  Home              [Home]{.kbd}
  End               [End]{.kbd}
  PgUp              [PgUp]{.kbd} (page up key)
  PgDn              [PgDn]{.kbd} (page down key)
  Up                [↑]{.kbd} (up arrow key)
  Down              [↓]{.kbd} (down arrow key)
  Left              [←]{.kbd} (left arrow key)
  Right             [→]{.kbd} (right arrow key)

### Numpad Keys {#numpad}

Due to system behavior, the following keys separated by a slash are
identified differently depending on whether [NumLock]{.kbd} is ON or
OFF. If [NumLock]{.kbd} is OFF but [Shift]{.kbd} is pressed, the system
temporarily releases [Shift]{.kbd} and acts as though [NumLock]{.kbd} is
ON.

  Name                    Description
  ----------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Numpad0 / NumpadIns     [0]{.kbd} / [Ins]{.kbd}
  Numpad1 / NumpadEnd     [1]{.kbd} / [End]{.kbd}
  Numpad2 / NumpadDown    [2]{.kbd} / [↓]{.kbd}
  Numpad3 / NumpadPgDn    [3]{.kbd} / [PgDn]{.kbd}
  Numpad4 / NumpadLeft    [4]{.kbd} / [←]{.kbd}
  Numpad5 / NumpadClear   [5]{.kbd} / typically does nothing
  Numpad6 / NumpadRight   [6]{.kbd} / [→]{.kbd}
  Numpad7 / NumpadHome    [7]{.kbd} / [Home]{.kbd}
  Numpad8 / NumpadUp      [8]{.kbd} / [↑]{.kbd}
  Numpad9 / NumpadPgUp    [9]{.kbd} / [PgUp]{.kbd}
  NumpadDot / NumpadDel   [.]{.kbd} / [Del]{.kbd}
  NumLock                 [NumLock]{.kbd} (number lock key). While [Ctrl]{.kbd} is held down, [NumLock]{.kbd} produces the key code of `Pause`{.no-highlight}, so use `^Pause`{.no-highlight} in hotkeys instead of `^NumLock`.
  NumpadDiv               [/]{.kbd} (division)
  NumpadMult              [\*]{.kbd} (multiplication)
  NumpadAdd               [+]{.kbd} (addition)
  NumpadSub               [-]{.kbd} (subtraction)
  NumpadEnter             [Enter]{.kbd}

### Function Keys {#function}

  Name       Description
  ---------- ------------------------------------------------------------
  F1 - F24   The 12 or more function keys at the top of most keyboards.

### Modifier Keys {#modifier}

+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+===================================+===================================+
| LWin                              | Left [Win]{.kbd}. Corresponds to  |
|                                   | the `<#` hotkey prefix.           |
+-----------------------------------+-----------------------------------+
| RWin                              | Right [Win]{.kbd}. Corresponds to |
|                                   | the `>#` hotkey prefix.           |
|                                   |                                   |
|                                   | **Note:** Unlike                  |
|                                   | [Ctrl]                            |
|                                   | {.kbd}/[Alt]{.kbd}/[Shift]{.kbd}, |
|                                   | there is no generic/neutral       |
|                                   | \"Win\" key because the OS does   |
|                                   | not support it. However, hotkeys  |
|                                   | with the `#` modifier can be      |
|                                   | triggered by either [Win]{.kbd}.  |
+-----------------------------------+-----------------------------------+
| Control (or Ctrl)                 | [Ctrl]{.kbd}. As a hotkey         |
|                                   | (`Control::`) it fires upon       |
|                                   | release unless it has the tilde   |
|                                   | prefix. Corresponds to the `^`    |
|                                   | hotkey prefix.                    |
+-----------------------------------+-----------------------------------+
| Alt                               | [Alt]{.kbd}. As a hotkey          |
|                                   | (`Alt::`) it fires upon release   |
|                                   | unless it has the tilde prefix.   |
|                                   | Corresponds to the `!` hotkey     |
|                                   | prefix.                           |
+-----------------------------------+-----------------------------------+
| Shift                             | [Shift]{.kbd}. As a hotkey        |
|                                   | (`Shift::`) it fires upon release |
|                                   | unless it has the tilde prefix.   |
|                                   | Corresponds to the `+` hotkey     |
|                                   | prefix.                           |
+-----------------------------------+-----------------------------------+
| LControl (or LCtrl)               | Left [Ctrl]{.kbd}. Corresponds to |
|                                   | the `<^` hotkey prefix.           |
+-----------------------------------+-----------------------------------+
| RControl (or RCtrl)               | Right [Ctrl]{.kbd}. Corresponds   |
|                                   | to the `>^` hotkey prefix.        |
+-----------------------------------+-----------------------------------+
| LShift                            | Left [Shift]{.kbd}. Corresponds   |
|                                   | to the `<+` hotkey prefix.        |
+-----------------------------------+-----------------------------------+
| RShift                            | Right [Shift]{.kbd}. Corresponds  |
|                                   | to the `>+` hotkey prefix.        |
+-----------------------------------+-----------------------------------+
| LAlt                              | Left [Alt]{.kbd}. Corresponds to  |
|                                   | the `<!` hotkey prefix.           |
+-----------------------------------+-----------------------------------+
| RAlt                              | Right [Alt]{.kbd}. Corresponds to |
|                                   | the `>!` hotkey prefix.           |
|                                   |                                   |
|                                   | **Note:** If your keyboard layout |
|                                   | has AltGr instead of RAlt, you    |
|                                   | can probably use it as a hotkey   |
|                                   | prefix via `<^>!` as described    |
|                                   | [here](Hotkeys.htm#AltGr). In     |
|                                   | addition, `LControl & RAlt::`     |
|                                   | would make AltGr itself into a    |
|                                   | hotkey.                           |
+-----------------------------------+-----------------------------------+

### Multimedia Keys {#multimedia}

The function assigned to each of the keys listed below can be overridden
by modifying the Windows registry. This table shows the default function
of each key on most versions of Windows.

  Name                Description
  ------------------- ---------------------------------------------------
  Browser_Back        Back
  Browser_Forward     Forward
  Browser_Refresh     Refresh
  Browser_Stop        Stop
  Browser_Search      Search
  Browser_Favorites   Favorites
  Browser_Home        Homepage
  Volume_Mute         Mute the volume
  Volume_Down         Lower the volume
  Volume_Up           Increase the volume
  Media_Next          Next Track
  Media_Prev          Previous Track
  Media_Stop          Stop
  Media_Play_Pause    Play/Pause
  Launch_Mail         Launch default e-mail program
  Launch_Media        Launch default media player
  Launch_App1         Launch This PC (formerly My Computer or Computer)
  Launch_App2         Launch Calculator

### Other Keys {#other}

+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+===================================+===================================+
| AppsKey                           | [Menu]{.kbd}. This is the key     |
|                                   | that invokes the right-click      |
|                                   | context menu.                     |
+-----------------------------------+-----------------------------------+
| PrintScreen                       | [PrtSc]{.kbd} (print screen key)  |
+-----------------------------------+-----------------------------------+
| CtrlBreak                         | [Ctrl]{.kbd}+[Pause]{.kbd} or     |
|                                   | [Ctrl]{.kbd}+[ScrollLock]{.kbd}   |
+-----------------------------------+-----------------------------------+
| Pause                             | [Pause]{.kbd} or                  |
|                                   | [Ctrl]{.kbd}+[NumLock]{.kbd}.     |
|                                   | While [Ctrl]{.kbd} is held down,  |
|                                   | [Pause]{.kbd} produces the key    |
|                                   | code of `CtrlBreak` and           |
|                                   | [NumLock]{.kbd} produces          |
|                                   | `Pause`{.no-highlight}, so use    |
|                                   | `^CtrlBreak` in hotkeys instead   |
|                                   | of `^Pause`{.no-highlight}.       |
+-----------------------------------+-----------------------------------+
| Help                              | [Help]{.kbd}. This probably       |
|                                   | doesn\'t exist on most keyboards. |
|                                   | It\'s usually not the same as     |
|                                   | [F1]{.kbd}.                       |
+-----------------------------------+-----------------------------------+
| Sleep                             | [Sleep]{.kbd}. Note that the      |
|                                   | sleep key on some keyboards might |
|                                   | not work with this.               |
+-----------------------------------+-----------------------------------+
| SC**nnn**                         | Specify for **nnn** the scan code |
|                                   | of a key. Recognizes unusual keys |
|                                   | not mentioned above. See [Special |
|                                   | Keys](#SpecialKeys) for details.  |
+-----------------------------------+-----------------------------------+
| VK**nn**                          | Specify for **nn** the            |
|                                   | hexadecimal virtual key code of a |
|                                   | key. This rarely-used method also |
|                                   | prevents certain types of         |
|                                   | [hotkeys](Hotkeys.htm) from       |
|                                   | requiring the [keyboard           |
|                                   | hook](lib/InstallKeybdHook.htm).  |
|                                   | For example, the following hotkey |
|                                   | does not use the keyboard hook,   |
|                                   | but as a side-effect it is        |
|                                   | triggered by pressing *either*    |
|                                   | [Home]{.kbd} or NumpadHome:       |
|                                   |                                   |
|                                   |     ^VK24::M                      |
|                                   | sgBox "You pressed Home or Numpad |
|                                   | Home while holding down Control." |
|                                   |                                   |
|                                   | **Known limitation:** VK hotkeys  |
|                                   | that are forced to use the        |
|                                   | [keyboard                         |
|                                   | hook](lib/InstallKeybdHook.htm),  |
|                                   | such as `*VK24` or `~VK24`, will  |
|                                   | fire for only one of the keys,    |
|                                   | not both (e.g. NumpadHome but not |
|                                   | [Home]{.kbd}). For more           |
|                                   | information about the VKnn        |
|                                   | method, see [Special              |
|                                   | Keys](#SpecialKeys).              |
|                                   |                                   |
|                                   | **Warning:** Only                 |
|                                   | [Send](lib/Send.htm),             |
|                                   | [GetKeyName](lib/GetKeyName.htm), |
|                                   | [GetKeyVK](lib/GetKeyVK.htm),     |
|                                   | [GetKeySC](lib/GetKeySC.htm) and  |
|                                   | [A_Me                             |
|                                   | nuMaskKey](lib/A_MenuMaskKey.htm) |
|                                   | support combining VKnn and SCnnn. |
|                                   | If combined in any other case (or |
|                                   | if any other invalid suffix is    |
|                                   | present), the key is not          |
|                                   | recognized. For example,          |
|                                   | `vk1Bsc001::` raises an error.    |
+-----------------------------------+-----------------------------------+

## Game Controller (Gamepad, Joystick, etc.) {#Controller}

**Note:** For historical reasons, the following button and control names
begin with `Joy`, which stands for joystick. However, they usually also
work for other game controllers such as gamepads or steering wheels.

**Joy1 through Joy32:** The buttons of the controller. To help determine
the button numbers for your controller, use this [test
script](scripts/index.htm#ControllerTest). Note that [hotkey prefix
symbols](Hotkeys.htm) such as \^ (control) and + (shift) are not
supported (though [GetKeyState](lib/GetKeyState.htm) can be used as a
substitute). Also note that the pressing of controller buttons always
\"passes through\" to the active window if that window is designed to
detect the pressing of controller buttons.

Although the following control names cannot be used as hotkeys, they can
be used with [GetKeyState](lib/GetKeyState.htm):

-   **JoyX, JoyY, and JoyZ:** The X (horizontal), Y (vertical), and Z
    (altitude/depth) axes of the stick.
-   **JoyR:** The rudder or 4th axis of the stick.
-   **JoyU and JoyV:** The 5th and 6th axes of the stick.
-   **JoyPOV:** The point-of-view (hat) control.
-   **JoyName:** The name of the controller or its driver.
-   **JoyButtons:** The number of buttons supported by the controller
    (not always accurate).
-   **JoyAxes:** The number of axes supported by the controller.
-   **JoyInfo:** Provides a string consisting of zero or more of the
    following letters to indicate the controller\'s capabilities: **Z**
    (has Z axis), **R** (has R axis), **U** (has U axis), **V** (has V
    axis), **P** (has POV control), **D** (the POV control has a limited
    number of discrete/distinct settings), **C** (the POV control is
    continuous/fine). Example string: ZRUVPD

For example, when using Xbox Wireless/360 controllers, JoyX/JoyY is the
left stick, JoyR/JoyU the right stick, JoyZ the left and right triggers,
and JoyPOV the directional pad (D-pad).

**Multiple controllers:** If the computer has more than one controller
and you want to use one beyond the first, include the controller number
(max 16) in front of the control name. For example, 2joy1 is the second
controller\'s first button.

**Note:** If you have trouble getting a script to recognize your
controller, specify a controller number other than 1 even though only a
single controller is present. It is unclear how this situation arises or
whether it is normal, but experimenting with the controller number in
the [controller test script](scripts/index.htm#ControllerTest) can help
determine if this applies to your system.

**See Also:**

-   [Controller remapping](misc/RemapController.htm): Methods of sending
    keystrokes and mouse clicks with a controller.
-   [Controller-To-Mouse script](scripts/index.htm#ControllerMouse):
    Using a controller as a mouse.

## Hand-held Remote Controls {#remote}

Respond to signals from hand-held remote controls via the [WinLIRC
client script](scripts/index.htm#WinLIRC).

## Special Keys {#SpecialKeys}

If your keyboard or mouse has a key not listed above, you might still be
able to make it a hotkey by using the following steps:

1.  Ensure that at least one script is running that is using the
    [keyboard hook](lib/InstallKeybdHook.htm). You can tell if a script
    has the keyboard hook by opening its [main
    window](Program.htm#main-window) and selecting \"View-\>[Key
    history](lib/KeyHistory.htm)\" from the menu bar.

2.  Double-click that script\'s [tray icon](Program.htm#tray-icon) to
    open its [main window](Program.htm#main-window).

3.  Press one of the \"mystery keys\" on your keyboard.

4.  Select the menu item \"View-\>[Key history](lib/KeyHistory.htm)\"

5.  Scroll down to the bottom of the page. Somewhere near the bottom are
    the key-down and key-up events for your key. NOTE: Some keys do not
    generate events and thus will not be visible here. If this is the
    case, you cannot directly make that particular key a hotkey because
    your keyboard driver or hardware handles it at a level too low for
    AutoHotkey to access. For possible solutions, see further below.

6.  If your key is detectable, make a note of the 3-digit hexadecimal
    value in the second column of the list (e.g. **159**).

7.  To define this key as a hotkey, follow this example:

        SC159::MsgBox ThisHotkey " was pressed." ; Replace 159 with your key's value.

    Also see [ThisHotkey](Hotkeys.htm#ThisHotkey).

**Reverse direction:** To remap some other key to *become* a \"mystery
key\", follow this example:

    ; Replace 159 with the value discovered above. Replace FF (if needed) with the
    ; key's virtual key, which can be discovered in the first column of the Key History screen.
    #c::Send "{vkFFsc159}" ; See Send {vkXXscYYY} for more details.

**Alternate solutions:** If your key or mouse button is not detectable
by the [Key History](lib/KeyHistory.htm) screen, one of the following
might help:

1.  Reconfigure the software that came with your mouse or keyboard
    (sometimes accessible in the Control Panel or Start Menu) to have
    the \"mystery key\" send some other keystroke. Such a keystroke can
    then be defined as a hotkey in a script. For example, if you
    configure a mystery key to send [Ctrl]{.kbd}+[F1]{.kbd}, you can
    then indirectly make that key as a hotkey by using `^F1::` in a
    script.

2.  Try
    [AHKHID](https://www.autohotkey.com/board/topic/38015-ahkhid-an-ahk-implementation-of-the-hid-functions/)
    from the archived forum. You can also try searching the
    [forum](https://www.autohotkey.com/boards/) for a keywords like
    `RawInput*`, `USB HID` or `AHKHID`.

3.  The following is a last resort and generally should be attempted
    only in desperation. This is because the chance of success is low
    and it may cause unwanted side-effects that are difficult to undo:\
    Disable or remove any extra software that came with your keyboard or
    mouse or change its driver to a more standard one such as the one
    built into the OS. This assumes there is such a driver for your
    particular keyboard or mouse and that you can live without the
    features provided by its custom driver and software.

## CapsLock and IME {#IME}

Some configurations of Windows IME (such as Japanese input with English
keyboard) use CapsLock to toggle between modes. In such cases, CapsLock
is suppressed by the IME and cannot be detected by AutoHotkey. However,
the [Alt]{.kbd}+[CapsLock]{.kbd}, [Ctrl]{.kbd}+[CapsLock]{.kbd} and
[Shift]{.kbd}+[CapsLock]{.kbd} shortcuts can be disabled with a
workaround. Specifically, send a key-up to modify the state of the IME,
but prevent any other effects by signalling the keyboard hook to
suppress the event. The following function can be used for this purpose:

``` {filename="SendSuppressedKeyUp.ahk"}
; The keyboard hook must be installed.
InstallKeybdHook
SendSuppressedKeyUp(key) {
    DllCall("keybd_event"
        , "char", GetKeyVK(key)
        , "char", GetKeySC(key)
        , "uint", KEYEVENTF_KEYUP := 0x2
        , "uptr", KEY_BLOCK_THIS := 0xFFC3D450)
}
```

After copying the function into a script or saving it as
*SendSuppressedKeyUp.ahk* in a [Lib folder](Scripts.htm#lib) and adding
`#Include <SendSuppressedKeyUp>` to the script, it can be used as
follows:

    ; Disable Alt+key shortcuts for the IME.
    ~LAlt::SendSuppressedKeyUp "LAlt"

    ; Test hotkey:
    !CapsLock::MsgBox A_ThisHotkey

    ; Remap CapsLock to LCtrl in a way compatible with IME.
    *CapsLock::
    {
        Send "{Blind}{LCtrl DownR}"
        SendSuppressedKeyUp "LCtrl"
    }
    *CapsLock up::
    {
        Send "{Blind}{LCtrl Up}"
    }
