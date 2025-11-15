# Obscure & Unique AutoHotkey v2 Example Scripts

A collection of creative, lesser-known script examples demonstrating advanced AutoHotkey v2 capabilities.

## 📑 Table of Contents

- [Input & Keyboard](#-input--keyboard) - 4 examples
- [System & Windows](#%EF%B8%8F-system--windows) - 4 examples
- [Clipboard & Text](#-clipboard--text) - 3 examples
- [GUI & Visualization](#-gui--visualization) - 3 examples
- [Advanced Techniques](#-advanced-techniques) - 6 examples
- [Game & Input](#-game--input) - 2 examples
- [Sound & Media](#-sound--media) - 2 examples
- [Network & IPC](#-network--ipc) - 2 examples
- [Debug & Development](#-debug--development) - 4 examples
- [Additional Categories](#-additional-categories)
- [Script Combination Ideas](#-script-combination-ideas)
- [Key Techniques Demonstrated](#-key-techniques-demonstrated)

## 🚀 How to Use These Examples

**Difficulty Levels:**
- 🟢 **Beginner** - Easy to understand and modify, minimal AHK knowledge needed
- 🟡 **Intermediate** - Requires understanding of AHK concepts (objects, callbacks, etc.)
- 🔴 **Advanced** - Complex code requiring deep AHK knowledge and Windows API familiarity

**Usage Types:**
- 💾 **Standalone** - Save as `.ahk` file and run directly
- 🧩 **Snippet** - Copy into an existing script
- ⚙️ **Needs Setup** - Requires additional configuration or files

**Tips:**
- Most examples can be modified to suit your needs
- Check the 📚 "See also" references for related documentation
- Start with 🟢 Beginner examples if you're new to these concepts

---

## 🎯 Input & Keyboard

### 1. **Typo Autocorrector with Learning** 🟡 Intermediate
💾 Standalone | 📚 [InputHook](InputHook.md) · [Map](Map.md) · [SendInput](Send.md)
```ahk
; Automatically fixes common typos and learns new corrections
typoMap := Map("teh", "the", "seperate", "separate", "recieve", "receive")

ih := InputHook("V")
ih.OnChar := (ihObj, char) => CheckTypo(char)
ih.Start()

CheckTypo(char) {
    static buffer := ""
    buffer .= char
    if (buffer ~= "\s") {
        for wrong, right in typoMap
            if (InStr(buffer, wrong))
                SendInput("{BS " StrLen(wrong) "}" right)
        buffer := ""
    }
}
```

### 2. **Keystroke Rhythm Analyzer** 🟢 Beginner
💾 Standalone | 📚 [Map](Map.md) · [Hotkeys](Hotkeys.md)
```ahk
; Measures typing speed and rhythm patterns
keyTimes := Map()

~*a:: ~*b:: ~*c:: ~*d:: ~*e:: ~*f:: ~*g::
~*h:: ~*i:: ~*j:: ~*k:: ~*l:: ~*m:: ~*n::
~*o:: ~*p:: ~*q:: ~*r:: ~*s:: ~*t:: ~*u::
~*v:: ~*w:: ~*x:: ~*y:: ~*z:: {
    key := SubStr(A_ThisHotkey, 3)
    keyTimes[key] := keyTimes.Has(key) ? keyTimes[key] + 1 : 1
}

^!r:: {
    fastest := "", max := 0
    for key, count in keyTimes
        if (count > max)
            max := count, fastest := key
    MsgBox("Fastest key: " fastest " (" max " times)")
}
```

### 3. **Context-Aware Hotstring Engine** 🟢 Beginner
💾 Standalone | 📚 [Hotstrings](Hotstrings.md) · [WinActive](WinActive.md)

```ahk
; Hotstrings that change based on active window
::btw::
{
    if WinActive("ahk_exe Discord.exe")
        SendText("by the way")
    else if WinActive("ahk_exe Code.exe")
        SendText("between")
    else
        SendText("btw")
}
```

### 4. **Input Pattern Matcher with Callbacks**
```ahk
; Detects complex keystroke patterns (Konami code style)
ih := InputHook("L4 T2", "{Enter}")
ih.OnEnd := (ihObj) => CheckPattern(ihObj.Input)
ih.Start()

CheckPattern(input) {
    patterns := Map(
        "^^vv", () => MsgBox("Konami code detected!"),
        "1234", () => MsgBox("Sequential numbers!"),
        "wasd", () => MsgBox("Gamer detected!")
    )
    for pattern, callback in patterns
        if (input = pattern)
            callback.Call()
}
```

---

## 🖥️ System & Windows

### 5. **Smart Window Tile Manager**
```ahk
; Monitors window creation and auto-tiles based on rules
OnMessage(0x0006, WindowActivated)  ; WM_ACTIVATE

WindowActivated(wParam, lParam, msg, hwnd) {
    if (wParam = 0)  ; Being deactivated
        return

    title := WinGetTitle("ahk_id " hwnd)

    ; Auto-tile code windows to left
    if InStr(title, "Visual Studio Code")
        WinMove(0, 0, A_ScreenWidth//2, A_ScreenHeight, "ahk_id " hwnd)

    ; Auto-tile browsers to right
    else if InStr(title, "Chrome") or InStr(title, "Firefox")
        WinMove(A_ScreenWidth//2, 0, A_ScreenWidth//2, A_ScreenHeight, "ahk_id " hwnd)
}
```

### 6. **Multi-Monitor Window Bouncer**
```ahk
; Bounce window between monitors with animation
^!b:: {
    WinGetPos(&x, &y, &w, &h, "A")
    targetMonitor := (MonitorGetPrimary() = 1) ? 2 : 1

    MonitorGetWorkArea(targetMonitor, &left, &top, &right, &bottom)

    ; Animate movement
    steps := 20
    Loop steps {
        newX := x + (left - x) * (A_Index / steps)
        WinMove(newX, y,,, "A")
        Sleep(10)
    }
}
```

### 7. **Window Ghosting Detector**
```ahk
; Detects and reports non-responsive windows
SetTimer(CheckGhostWindows, 5000)

CheckGhostWindows() {
    for hwnd in WinGetList() {
        result := SendMessage(0x0000,,,, "ahk_id " hwnd)  ; WM_NULL
        if (result = "FAIL")
            ToolTip("Ghost window detected: " WinGetTitle("ahk_id " hwnd))
    }
}
```

### 8. **Process Tree Visualizer**
```ahk
; Shows parent-child process relationships
^!p:: {
    tree := Map()
    for pid in ProcessList() {
        parent := ProcessGetParent(pid)
        name := ProcessGetName(pid)
        if !tree.Has(parent)
            tree[parent] := []
        tree[parent].Push(pid ": " name)
    }

    output := ""
    for parent, children in tree
        output .= "Parent " parent ":`n  " StrReplace(children.Join("`n"), "`n", "`n  ") "`n"

    MsgBox(output)
}
```

---

## 📋 Clipboard & Text

### 9. **Clipboard History with Format Preservation**
```ahk
; Saves all clipboard states including images
history := []
maxHistory := 20

OnClipboardChange(ClipChanged)

ClipChanged(Type) {
    if (Type = 0)  ; Clipboard emptied
        return

    ; Save full clipboard state (includes images, formatting)
    saved := ClipboardAll()
    history.Push(saved)

    if (history.Length > maxHistory)
        history.RemoveAt(1)
}

^!v:: {
    ; Show history menu
    menu := Menu()
    for index, clip in history {
        preview := Type(clip) = "String" ? SubStr(clip, 1, 50) : "[Binary Data]"
        menu.Add(index ": " preview, RestoreClip)
    }
    menu.Show()
}

RestoreClip(itemName, itemPos, menu) {
    A_Clipboard := history[itemPos]
}
```

### 10. **Smart Paste Formatter**
```ahk
; Automatically formats pasted content based on context
^v:: {
    content := A_Clipboard

    ; In Excel/spreadsheet
    if WinActive("ahk_exe EXCEL.EXE") {
        ; Convert tabs to commas
        content := StrReplace(content, "`t", ",")
    }

    ; In code editor
    else if WinActive("ahk_exe Code.exe") {
        ; Escape special characters
        content := StrReplace(content, '"', '\"')
    }

    ; In email
    else if WinActive("ahk_exe outlook.exe") {
        ; Remove extra line breaks
        content := RegExReplace(content, "\n{3,}", "`n`n")
    }

    SendText(content)
}
```

### 11. **Clipboard Chain Monitor**
```ahk
; Monitors which applications are accessing clipboard
clipboardOwner := 0

OnMessage(0x031D, ClipChainChanged)  ; WM_CHANGECBCHAIN

ClipChainChanged(wParam, lParam, msg, hwnd) {
    newOwner := DllCall("GetClipboardOwner")
    if (newOwner != clipboardOwner) {
        clipboardOwner := newOwner
        owner := WinGetProcessName("ahk_id " newOwner)
        ToolTip("Clipboard now owned by: " owner)
        SetTimer(() => ToolTip(), -3000)
    }
}
```

---

## 🎨 GUI & Visualization

### 12. **Live Window Spy with Pixel Color**
```ahk
; Real-time window and pixel information display
gui := Gui()
gui.Add("Text", "w300", "Window Info:")
infoText := gui.Add("Edit", "w300 h150 ReadOnly")
gui.Show()

SetTimer(UpdateSpy, 100)

UpdateSpy() {
    MouseGetPos(&x, &y, &hwnd)
    color := PixelGetColor(x, y)

    info := ""
    info .= "Window: " WinGetTitle("ahk_id " hwnd) "`n"
    info .= "Class: " WinGetClass("ahk_id " hwnd) "`n"
    info .= "Position: " x "," y "`n"
    info .= "Color: " color "`n"
    info .= "RGB: " Format("({}, {}, {})",
                           (color >> 16) & 0xFF,
                           (color >> 8) & 0xFF,
                           color & 0xFF)

    infoText.Value := info
}
```

### 13. **TreeView File System Browser**
```ahk
; Hierarchical file browser with lazy loading
gui := Gui()
tv := gui.Add("TreeView", "w400 h600")
gui.Show()

; Add root drives
for drive in DriveGetList()
    tv.Add(drive ":\", 0, "Expand")

tv.OnEvent("Expand", ExpandFolder)

ExpandFolder(tv, itemID) {
    path := GetFullPath(tv, itemID)

    ; Clear placeholder children
    child := tv.GetChild(itemID)
    while child
        tv.Delete(child), child := tv.GetChild(itemID)

    ; Add subdirectories
    Loop Files, path "\*.*", "D"
        tv.Add(A_LoopFileName, itemID, "Expand")
}

GetFullPath(tv, itemID) {
    path := tv.GetText(itemID)
    while (parent := tv.GetParent(itemID))
        path := tv.GetText(parent) "\" path, itemID := parent
    return path
}
```

### 14. **ListView with Sortable Columns**
```ahk
; Data table with click-to-sort functionality
gui := Gui()
lv := gui.Add("ListView", "w600 h400", ["Name", "Size", "Date"])
gui.Show()

; Populate with files
Loop Files, A_ScriptDir "\*.*"
    lv.Add(, A_LoopFileName, A_LoopFileSize, A_LoopFileTimeModified)

lv.OnEvent("ColClick", SortColumn)

SortColumn(lv, colNum) {
    static lastCol := 0, ascending := true

    ; Toggle sort direction if same column
    if (colNum = lastCol)
        ascending := !ascending
    else
        ascending := true, lastCol := colNum

    lv.Modify(0, ascending ? "Sort" : "SortDesc", colNum)
}
```

---

## 🔧 Advanced Techniques

### 15. **RegEx with Callout Debugging**
```ahk
; Debug complex regex patterns with callouts
pattern := "(\w+)(?C1)\s+(?C2)(\d+)"
haystack := "Product 123 Item 456"

RegExMatch(haystack, pattern, &match, , , Callout)

Callout(match, calloutNum, pos, haystack, needle) {
    MsgBox(Format("Callout {}: Position {} in '{}'",
                  calloutNum, pos, SubStr(haystack, pos, 10)))
    return 0  ; Continue matching
}
```

### 16. **COM Event Handler (IE Automation)**
```ahk
; Monitor all Internet Explorer events
ie := ComObject("InternetExplorer.Application")
ie.Visible := true
ie.Navigate("https://example.com")

ComObjConnect(ie, "IE_")

IE_NavigateComplete2(ieObj, url) {
    MsgBox("Navigated to: " url)
}

IE_DocumentComplete(ieObj, url) {
    MsgBox("Document loaded: " url)
}
```

### 17. **Buffer-Based Binary File Parser**
```ahk
; Read and parse binary file structures
file := FileOpen("data.bin", "r")
buf := Buffer(1024)
file.RawRead(buf, 1024)
file.Close()

; Parse structure
magic := NumGet(buf, 0, "UInt")
version := NumGet(buf, 4, "UShort")
flags := NumGet(buf, 6, "UShort")
timestamp := NumGet(buf, 8, "Int64")

MsgBox(Format("Magic: 0x{:08X}`nVersion: {}`nFlags: 0x{:04X}",
              magic, version, flags))
```

### 18. **Dynamic DllCall with Callbacks**
```ahk
; Enumerate windows with callback function
callback := CallbackCreate(EnumWindowsProc)
DllCall("EnumWindows", "Ptr", callback, "Ptr", 0)
CallbackFree(callback)

EnumWindowsProc(hwnd, lParam) {
    title := WinGetTitle("ahk_id " hwnd)
    if (title != "")
        OutputDebug(title)
    return 1  ; Continue enumeration
}
```

### 19. **Map-Based Memoization Wrapper**
```ahk
; Cache expensive function results
Memoize(func) {
    cache := Map()
    return (args*) => cache.Has(args.Join("|"))
                      ? cache[args.Join("|")]
                      : cache[args.Join("|")] := func(args*)
}

; Example: expensive Fibonacci
Fibonacci := Memoize((n) => n <= 1 ? n : Fibonacci(n-1) + Fibonacci(n-2))
```

### 20. **SetTimer with Dynamic Adjustment**
```ahk
; Self-adjusting timer based on system load
interval := 1000

SetTimer(AdaptiveTask, interval)

AdaptiveTask() {
    global interval

    start := A_TickCount
    ; Do work here
    Sleep(100)
    elapsed := A_TickCount - start

    ; Adjust interval based on execution time
    if (elapsed > interval * 0.8)
        interval := Min(interval * 1.5, 5000)
    else if (elapsed < interval * 0.2)
        interval := Max(interval * 0.75, 100)

    SetTimer(AdaptiveTask, interval)
}
```

---

## 🎮 Game & Input

### 21. **Joystick to Keyboard Mapper**
```ahk
; Map game controller to keyboard keys
SetTimer(CheckJoystick, 10)

CheckJoystick() {
    static prevButtons := 0

    buttons := GetKeyState("1JoyButtons")

    Loop buttons {
        state := GetKeyState("1Joy" A_Index)
        prevState := (prevButtons >> (A_Index - 1)) & 1

        if (state && !prevState)
            SendInput("{" Chr(64 + A_Index) " down}")
        else if (!state && prevState)
            SendInput("{" Chr(64 + A_Index) " up}")

        if state
            prevButtons |= (1 << (A_Index - 1))
        else
            prevButtons &= ~(1 << (A_Index - 1))
    }
}
```

### 22. **Mouse Gesture Recognizer**
```ahk
; Recognize mouse movement patterns
~RButton::
{
    static path := []

    SetTimer(RecordPath, 50)
    KeyWait("RButton")
    SetTimer(RecordPath, 0)

    RecognizeGesture(path)
}

RecordPath() {
    static lastX := 0, lastY := 0
    MouseGetPos(&x, &y)

    if (Abs(x - lastX) > 20 || Abs(y - lastY) > 20) {
        path.Push({x: x, y: y})
        lastX := x, lastY := y
    }
}

RecognizeGesture(path) {
    if (path.Length < 3)
        return

    ; Simple left/right detection
    deltaX := path[-1].x - path[1].x
    if (deltaX > 100)
        MsgBox("Gesture: Right")
    else if (deltaX < -100)
        MsgBox("Gesture: Left")
}
```

---

## 🎵 Sound & Media

### 23. **Audio Visualizer with Peak Meters**
```ahk
; Real-time audio level display
device := SoundGetInterface("{C02216F6-8C67-4B5B-9D00-D008E73E0064}")
meter := ComCall(3, device, "Ptr*")  ; Activate

gui := Gui()
bar := gui.Add("Progress", "w400 h30 cBlue", 0)
gui.Show()

SetTimer(UpdateMeter, 50)

UpdateMeter() {
    level := ComCall(4, meter, "Float*", &peak := 0.0) ? peak : 0
    bar.Value := level * 100
}
```

### 24. **System Sound Event Logger**
```ahk
; Log all system sound events
sounds := Map()
SetTimer(MonitorSounds, 1000)

MonitorSounds() {
    devices := SoundGetName(,, &count)

    Loop count {
        vol := SoundGetVolume(, A_Index)
        mute := SoundGetMute(, A_Index)

        key := A_Index
        if !sounds.Has(key)
            sounds[key] := {vol: vol, mute: mute}
        else if (sounds[key].vol != vol || sounds[key].mute != mute) {
            OutputDebug(Format("Device {}: Vol {} -> {}, Mute {} -> {}",
                              A_Index, sounds[key].vol, vol,
                              sounds[key].mute, mute))
            sounds[key] := {vol: vol, mute: mute}
        }
    }
}
```

---

## 🌐 Network & IPC

### 25. **Named Pipe Communication**
```ahk
; Send messages between scripts via named pipes
CreateNamedPipe() {
    return DllCall("CreateNamedPipe",
                   "Str", "\\.\pipe\AHKPipe",
                   "UInt", 3,  ; PIPE_ACCESS_DUPLEX
                   "UInt", 0,
                   "UInt", 1,
                   "UInt", 1024,
                   "UInt", 1024,
                   "UInt", 0,
                   "Ptr", 0,
                   "Ptr")
}
```

### 26. **HTTP Client Request Handler**
```ahk
; Simple HTTP client using COM
server := ComObject("WinHttp.WinHttpRequest.5.1")
server.Open("GET", "http://api.example.com/data")
server.Send()

OnMessage(0x8000 + 1, ProcessResponse)

ProcessResponse() {
    if (server.Status = 200)
        MsgBox("Response: " server.ResponseText)
}
```

---

## 🔍 Debug & Development

### 27. **Performance Profiler**
```ahk
; Profile function execution time
Profile(func, name := "") {
    return (args*) => (
        start := A_TickCount,
        result := func(args*),
        elapsed := A_TickCount - start,
        OutputDebug(Format("[{}] took {}ms", name || "Function", elapsed)),
        result
    )
}

; Usage
SlowFunction := Profile((n) => Sleep(n), "SlowFunction")
SlowFunction(100)
```

### 28. **Stack Trace Generator**
```ahk
; Generate call stack for debugging
GetStackTrace() {
    stack := []
    try {
        throw Error("Stack trace")
    } catch as e {
        for line in StrSplit(e.Stack, "`n")
            if (line ~= "^\s*\d+:")
                stack.Push(Trim(line))
    }
    return stack.Join("`n")
}

^!s:: MsgBox(GetStackTrace())
```

### 29. **Variable Inspector GUI**
```ahk
; Inspect all script variables at runtime
^!i:: {
    vars := ""
    for name, value in ObjOwnProps(this)
        vars .= name " = " (IsObject(value) ? Type(value) : value) "`n"
    MsgBox(vars, "Variable Inspector")
}
```

### 30. **Error Handler with Logging**
```ahk
; Comprehensive error logging system
OnError(LogError)

LogError(exception, mode) {
    log := FileOpen("errors.log", "a")
    log.WriteLine(Format("[{}] Error in {}: {} (Line {})",
                         FormatTime(, "yyyy-MM-dd HH:mm:ss"),
                         exception.File,
                         exception.Message,
                         exception.Line))
    log.Close()

    ; Show error dialog
    MsgBox(exception.Message, "Error", "Icon!")

    return 1  ; Suppress error
}
```

---

## 📚 Additional Categories

### Data Structures
- **Circular Buffer** - Ring buffer using Array
- **Priority Queue** - Heap-based with Map
- **LRU Cache** - Least Recently Used with Map
- **Trie** - Prefix tree for autocomplete

### Image Processing
- **Screenshot Diff** - Compare screen regions
- **OCR Integration** - Text extraction from images
- **Color Picker** - Advanced color selection

### Automation
- **Macro Recorder** - Record and playback inputs
- **Task Scheduler** - Cron-like scheduling
- **Auto-Updater** - Self-updating script

### System Integration
- **Registry Monitor** - Track registry changes
- **Service Controller** - Manage Windows services
- **WMI Query Tool** - System information queries

---

## 💡 Script Combination Ideas

1. **Clipboard History** + **TreeView** = Hierarchical clipboard manager
2. **InputHook** + **RegEx Callout** = Advanced text expander with validation
3. **OnMessage** + **Buffer** = Custom window subclassing
4. **COM Events** + **ListView** = Browser automation with event log
5. **SetTimer** + **Sound Interface** = Audio-reactive scripts
6. **DllCall** + **CallbackCreate** = Native API integration
7. **Map** + **Memoization** = High-performance caching
8. **Buffer** + **NumGet/NumPut** = Binary protocol implementation
9. **Monitor Functions** + **Window Management** = Smart multi-monitor layouts
10. **OnClipboardChange** + **ClipboardAll** = Format-preserving clipboard tools

---

## 📖 Key Techniques Demonstrated

- **Event-driven programming** with callbacks and hooks
- **Memory manipulation** with Buffer and NumGet/NumPut
- **COM automation** for system integration
- **GUI development** with reactive controls
- **Binary data processing** for low-level operations
- **Function composition** and higher-order functions
- **Asynchronous execution** with timers and messages
- **Dynamic code generation** with closures
- **System API integration** via DllCall
- **Advanced pattern matching** with RegEx callouts

These examples showcase AutoHotkey v2's power beyond simple hotkeys and demonstrate professional programming techniques.
