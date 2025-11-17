#!/usr/bin/env python3
"""
Generate comprehensive AHK v2 examples for all documented functions.
Creates practical, working examples organized by category.
"""

import re
from pathlib import Path
from collections import defaultdict

# Example templates for different function types
TEMPLATES = {
    'window': '''/*
    Example: {name}
    Category: Window Management
    Description: {description}
*/

; Basic usage
{basic_example}

; With parameters
{param_example}

; Error handling
{error_example}

; Practical example
{practical_example}
''',
    'control': '''/*
    Example: {name}
    Category: Control Functions
    Description: {description}
*/

; Target a control in Notepad
{basic_example}

; With error handling
{error_example}

; Practical usage
{practical_example}
''',
    'file': '''/*
    Example: {name}
    Category: File & Directory
    Description: {description}
*/

; Basic file operation
{basic_example}

; With error handling
{error_example}

; Practical example
{practical_example}
''',
    'string': '''/*
    Example: {name}
    Category: String Functions
    Description: {description}
*/

; Basic usage
{basic_example}

; Multiple examples
{param_example}

; Practical application
{practical_example}
''',
    'math': '''/*
    Example: {name}
    Category: Math Functions
    Description: {description}
*/

; Basic calculation
{basic_example}

; Multiple examples
{param_example}

; Practical usage
{practical_example}
''',
    'gui': '''/*
    Example: {name}
    Category: GUI Functions
    Description: {description}
*/

; Create a simple GUI
{basic_example}

; Event handling
{param_example}

; Complete example
{practical_example}
''',
    'hotkey': '''/*
    Example: {name}
    Category: Keyboard & Hotkeys
    Description: {description}
*/

; Basic hotkey
{basic_example}

; With modifiers
{param_example}

; Practical example
{practical_example}
''',
    'mouse': '''/*
    Example: {name}
    Category: Mouse Functions
    Description: {description}
*/

; Basic mouse operation
{basic_example}

; With coordinates
{param_example}

; Practical usage
{practical_example}
''',
    'flow': '''/*
    Example: {name}
    Category: Flow Control
    Description: {description}
*/

; Basic syntax
{basic_example}

; Multiple variations
{param_example}

; Real-world usage
{practical_example}
''',
    'generic': '''/*
    Example: {name}
    Description: {description}
*/

; Basic usage
{basic_example}

; Advanced usage
{param_example}

; Practical example
{practical_example}
'''
}

# Comprehensive function examples database
EXAMPLES = {
    # Built-in Types
    'Map': {
        'basic': 'ages := Map("John", 25, "Jane", 30, "Bob", 35)',
        'param': 'ages["Alice"] := 28\nMsgBox ages["John"]',
        'error': 'if ages.Has("John")\n    MsgBox ages["John"]',
        'practical': 'for name, age in ages\n    MsgBox name ": " age'
    },
    'Object': {
        'basic': 'person := {name: "John", age: 25, city: "NYC"}',
        'param': 'person.email := "john@example.com"\nMsgBox person.name',
        'error': 'if person.HasOwnProp("age")\n    MsgBox person.age',
        'practical': 'for prop, value in person.OwnProps()\n    MsgBox prop ": " value'
    },
    'Buffer': {
        'basic': 'buf := Buffer(1024)  ; Allocate 1KB',
        'param': 'NumPut("UInt", 42, buf, 0)\nvalue := NumGet(buf, 0, "UInt")',
        'error': 'try {\n    buf := Buffer(1024)\n} catch Error as err {\n    MsgBox err.Message\n}',
        'practical': 'data := Buffer(256)\nStrPut("Hello", data)\nresult := StrGet(data)'
    },

    # Window Management
    'WinActivate': {
        'basic': 'WinActivate "Untitled - Notepad"',
        'param': 'WinActivate "ahk_class Notepad"',
        'error': 'if WinExist("Notepad")\n    WinActivate',
        'practical': '; Switch to window by partial title\nif WinExist("Chrome")\n    WinActivate\nelse\n    Run "chrome.exe"'
    },
    'WinClose': {
        'basic': 'WinClose "Untitled - Notepad"',
        'param': 'WinClose "ahk_class Notepad"',
        'error': 'if WinExist("Calculator")\n    WinClose',
        'practical': '; Close all Notepad windows\nwhile WinExist("ahk_class Notepad")\n    WinClose'
    },
    'WinMove': {
        'basic': 'WinMove 0, 0, 800, 600, "Notepad"',
        'param': 'WinMove 100, 100, , , "A"  ; Move active window',
        'error': 'if WinExist("Notepad") {\n    WinMove 0, 0, 800, 600\n}',
        'practical': '; Center window on screen\nWinGetPos &x, &y, &w, &h, "A"\nWinMove (A_ScreenWidth-w)/2, (A_ScreenHeight-h)/2, , , "A"'
    },
    'WinGetTitle': {
        'basic': 'title := WinGetTitle("A")  ; Active window',
        'param': 'title := WinGetTitle("ahk_class Notepad")',
        'error': 'if WinExist("Notepad")\n    title := WinGetTitle()',
        'practical': '; Get all window titles\nids := WinGetList()\nfor id in ids {\n    title := WinGetTitle(id)\n    MsgBox title\n}'
    },
    'WinGetPos': {
        'basic': 'WinGetPos &x, &y, &w, &h, "A"',
        'param': 'WinGetPos , , &width, &height, "Notepad"',
        'error': 'if WinExist("Notepad") {\n    WinGetPos &x, &y, &w, &h\n}',
        'practical': '; Check if window is on screen\nWinGetPos &x, &y, &w, &h, "A"\nif (x < 0 or y < 0)\n    WinMove 100, 100, , , "A"'
    },

    # String Functions
    'StrReplace': {
        'basic': 'text := "Hello World"\nnewText := StrReplace(text, "World", "AHK")',
        'param': 'result := StrReplace("test test", "test", "demo", , &count)\nMsgBox "Replaced " count " times"',
        'error': 'text := "Sample Text"\nif InStr(text, "Sample")\n    text := StrReplace(text, "Sample", "Example")',
        'practical': '; Remove all spaces\ntext := "  Hello   World  "\nclean := StrReplace(Trim(text), "  ", " ")'
    },
    'InStr': {
        'basic': 'pos := InStr("Hello World", "World")',
        'param': 'pos := InStr("test TEST test", "TEST", true)  ; Case-sensitive',
        'error': 'if InStr(text, "error")\n    MsgBox "Error found!"',
        'practical': '; Count occurrences\ntext := "one two one three one"\ncount := 0\npos := 1\nwhile (pos := InStr(text, "one", , pos))\n    count++, pos++'
    },
    'StrSplit': {
        'basic': 'parts := StrSplit("one,two,three", ",")',
        'param': 'words := StrSplit("Hello  World", A_Space)',
        'error': 'try {\n    parts := StrSplit(csvLine, ",")\n}',
        'practical': '; Parse CSV line\nline := "Name,Age,City"\nfields := StrSplit(line, ",")\nfor index, field in fields\n    MsgBox field'
    },
    'SubStr': {
        'basic': 'sub := SubStr("Hello World", 1, 5)  ; "Hello"',
        'param': 'last := SubStr("Hello World", -5)  ; "World"',
        'error': 'if (StrLen(text) > 10)\n    preview := SubStr(text, 1, 10) "..."',
        'practical': '; Get file extension\nfilePath := "document.txt"\next := SubStr(filePath, InStr(filePath, ".", , -1) + 1)'
    },

    # File & Directory
    'FileRead': {
        'basic': 'content := FileRead("test.txt")',
        'param': 'content := FileRead("data.json", "UTF-8")',
        'error': 'try {\n    content := FileRead("config.ini")\n} catch Error as err {\n    MsgBox "Error: " err.Message\n}',
        'practical': '; Read and process lines\ncontent := FileRead("data.txt")\nlines := StrSplit(content, "`n")\nfor line in lines\n    MsgBox line'
    },
    'FileAppend': {
        'basic': 'FileAppend "Log entry`n", "log.txt"',
        'param': 'FileAppend "Data", "output.txt", "UTF-8"',
        'error': 'try {\n    FileAppend A_Now ": Event`n", "log.txt"\n} catch Error as err {\n    MsgBox "Failed to write log"\n}',
        'practical': '; Append timestamp log\ntimestamp := FormatTime(, "yyyy-MM-dd HH:mm:ss")\nFileAppend timestamp ": " message "`n", "app.log"'
    },
    'FileDelete': {
        'basic': 'FileDelete "temp.txt"',
        'param': 'FileDelete "*.tmp"  ; Delete all .tmp files',
        'error': 'if FileExist("old.txt")\n    FileDelete "old.txt"',
        'practical': '; Delete files older than 7 days\nLoop Files, "logs\\*.log" {\n    if (DateDiff(A_Now, FileGetTime(A_LoopFilePath), "days") > 7)\n        FileDelete A_LoopFilePath\n}'
    },
    'DirCreate': {
        'basic': 'DirCreate "NewFolder"',
        'param': 'DirCreate "C:\\Projects\\MyApp\\Data"',
        'error': 'if !DirExist("Output")\n    DirCreate "Output"',
        'practical': '; Create dated backup folder\ndate := FormatTime(, "yyyyMMdd")\nDirCreate "Backups\\" date'
    },

    # GUI Functions
    'Gui': {
        'basic': 'myGui := Gui()\nmyGui.Add("Text", , "Hello")\nmyGui.Show()',
        'param': 'myGui := Gui("+Resize", "My Window")',
        'error': 'try {\n    myGui := Gui()\n    myGui.Show()\n}',
        'practical': '; Simple input form\nmyGui := Gui()\nmyGui.Add("Text", , "Name:")\nedit := myGui.Add("Edit", "w200")\nbtn := myGui.Add("Button", , "Submit")\nbtn.OnEvent("Click", (*) => MsgBox(edit.Value))\nmyGui.Show()'
    },

    # Math Functions
    'Round': {
        'basic': 'result := Round(3.14159, 2)  ; 3.14',
        'param': 'rounded := Round(12.5)  ; 13',
        'error': 'if IsNumber(value)\n    result := Round(value, 2)',
        'practical': '; Calculate percentage\ntotal := 150\npart := 47\npercentage := Round((part / total) * 100, 1) "%"'
    },
    'Abs': {
        'basic': 'positive := Abs(-42)  ; 42',
        'param': 'distance := Abs(x2 - x1)',
        'error': 'result := Abs(Number(userInput))',
        'practical': '; Calculate distance\npoint1 := 10\npoint2 := 25\ndistance := Abs(point2 - point1)'
    },

    # Hotkeys
    'Hotkey': {
        'basic': 'Hotkey "^!t", (*) => MsgBox("Ctrl+Alt+T pressed")',
        'param': 'Hotkey "F1", MyFunction\nHotkey "F1", "Off"  ; Disable',
        'error': 'try {\n    Hotkey "^q", ExitApp\n}',
        'practical': '; Toggle hotkey on/off\ntoggle := true\nHotkey "^!p", (*) => TogglePause()\nTogglePause() {\n    global toggle\n    toggle := !toggle\n    Hotkey "^!p", toggle ? "On" : "Off"\n}'
    },
    'Send': {
        'basic': 'Send "Hello World"',
        'param': 'Send "{Enter}"  ; Press Enter',
        'error': 'if WinActive("Notepad")\n    Send "Test"',
        'practical': '; Type email signature\nSend "Best regards,{Enter}John Doe{Enter}john@example.com"'
    },

    # Mouse Functions
    'Click': {
        'basic': 'Click  ; Click at current position',
        'param': 'Click 100, 200  ; Click at coordinates',
        'error': 'if WinActive("Calculator")\n    Click 50, 100',
        'practical': '; Double-click\nClick 2  ; Double-click at current position'
    },
    'MouseMove': {
        'basic': 'MouseMove 500, 500',
        'param': 'MouseMove 0, 0  ; Move to top-left',
        'error': 'try {\n    MouseMove A_ScreenWidth/2, A_ScreenHeight/2\n}',
        'practical': '; Move in circle\nLoop 360 {\n    x := 500 + Cos(A_Index * 3.14159 / 180) * 100\n    y := 500 + Sin(A_Index * 3.14159 / 180) * 100\n    MouseMove x, y\n    Sleep 10\n}'
    },

    # Control Functions
    'ControlClick': {
        'basic': 'ControlClick "Button1", "Window Title"',
        'param': 'ControlClick "OK", "ahk_class #32770"',
        'error': 'if WinExist("Dialog")\n    ControlClick "Button1"',
        'practical': '; Click Yes in message box\nRun "notepad.exe"\nWinWait "Notepad"\nSend "^s"  ; Ctrl+S to save\nWinWait "Save As"\nControlClick "Cancel", "Save As"'
    },
    'ControlGetText': {
        'basic': 'text := ControlGetText("Edit1", "Notepad")',
        'param': 'text := ControlGetText("Button1", "A")',
        'error': 'if WinExist("Notepad")\n    text := ControlGetText("Edit1")',
        'practical': '; Get all text from Notepad\nif WinExist("ahk_class Notepad") {\n    text := ControlGetText("Edit1")\n    MsgBox text\n}'
    },

    # Flow Control
    'If': {
        'basic': 'if (x > 10)\n    MsgBox "Greater than 10"',
        'param': 'if (name = "John")\n    MsgBox "Hello John!"\nelse\n    MsgBox "Hello stranger!"',
        'error': 'if IsSet(variable)\n    MsgBox variable',
        'practical': '; Check multiple conditions\nif (age >= 18 and hasLicense) {\n    MsgBox "Can drive"\n} else {\n    MsgBox "Cannot drive"\n}'
    },
    'Loop': {
        'basic': 'Loop 5\n    MsgBox A_Index',
        'param': 'Loop {\n    if (A_Index > 10)\n        break\n    MsgBox A_Index\n}',
        'error': 'Loop 100 {\n    if !Continue\n        break\n}',
        'practical': '; Count down timer\nLoop 10 {\n    remaining := 11 - A_Index\n    ToolTip remaining\n    Sleep 1000\n}\nToolTip'
    },
    'For': {
        'basic': 'arr := [1, 2, 3]\nfor index, value in arr\n    MsgBox value',
        'param': 'for key, value in myMap\n    MsgBox key ": " value',
        'error': 'for item in collection {\n    if !item\n        continue\n}',
        'practical': '; Process files\nLoop Files, "*.txt"\n    FileAppend "Processed " A_LoopFileName "`n", "log.txt"'
    },
}

def get_category_folder(filename):
    """Map filename to category folder."""
    name_lower = filename.lower()

    if 'win' in name_lower and filename not in ['Winamp.md']:
        return 'window-management'
    elif 'control' in name_lower:
        return 'control-functions'
    elif 'gui' in name_lower:
        return 'gui-functions'
    elif 'file' in name_lower or 'dir' in name_lower:
        return 'file-directory'
    elif 'key' in name_lower or 'send' in name_lower or 'hotkey' in name_lower:
        return 'keyboard-hotkeys'
    elif 'mouse' in name_lower or 'click' in name_lower:
        return 'mouse-functions'
    elif 'str' in name_lower:
        return 'string-functions'
    elif 'math' in name_lower or 'random' in name_lower:
        return 'math-functions'
    elif 'loop' in name_lower or 'for' in name_lower or 'if' in name_lower or 'while' in name_lower:
        return 'flow-control'
    elif filename in ['Array.md', 'Map.md', 'Object.md', 'Buffer.md', 'Func.md']:
        return 'built-in-types'
    elif 'sound' in name_lower:
        return 'sound-functions'
    elif 'drive' in name_lower:
        return 'drive-functions'
    elif 'reg' in name_lower:
        return 'registry-functions'
    elif 'process' in name_lower:
        return 'process-management'
    elif 'error' in name_lower or 'try' in name_lower or 'catch' in name_lower:
        return 'error-handling'
    elif filename.startswith('_') or filename.startswith('#'):
        return 'directives-special'
    elif filename in ['Functions.md', 'Objects.md', 'Variables.md', 'Language.md', 'Concepts.md']:
        return 'core-concepts'
    else:
        return 'other-functions'

def generate_example_file(func_name, category, examples):
    """Generate an example file for a function."""
    template = TEMPLATES.get(category, TEMPLATES['generic'])

    cat_title = category.replace('-', ' ').title()
    basic_default = f'; {func_name} basic example\n; See documentation for details'
    param_default = f'; {func_name} with parameters\n; See documentation for details'
    error_default = f'; {func_name} with error handling\ntry {{\n    ; Your code here\n}} catch Error as err {{\n    MsgBox "Error: " err.Message\n}}'
    practical_default = f'; Practical example of {func_name}\n; See documentation for real-world usage'

    basic_ex = examples.get('basic', basic_default)
    param_ex = examples.get('param', param_default)
    error_ex = examples.get('error', error_default)
    practical_ex = examples.get('practical', practical_default)

    content = f'''/*
    AutoHotkey v2 Example: {func_name}
    Category: {cat_title}

    This example demonstrates the usage of {func_name} with practical code.
*/

; ===== Basic Usage =====
{basic_ex}

; ===== Advanced Usage =====
{param_ex}

; ===== Error Handling =====
{error_ex}

; ===== Practical Example =====
{practical_ex}

/*
    For more information, see the official documentation:
    https://www.autohotkey.com/docs/v2/
*/
'''
    return content

def main():
    """Generate all example files."""
    examples_created = 0

    # Generate from EXAMPLES database
    for func_name, examples in EXAMPLES.items():
        # Determine category
        category = 'other-functions'
        if any(x in func_name.lower() for x in ['win', 'window']):
            category = 'window-management'
        elif 'control' in func_name.lower():
            category = 'control-functions'
        elif 'file' in func_name.lower() or 'dir' in func_name.lower():
            category = 'file-directory'
        elif 'str' in func_name.lower() or func_name in ['InStr', 'SubStr']:
            category = 'string-functions'
        elif func_name in ['Map', 'Object', 'Buffer', 'Array']:
            category = 'built-in-types'
        elif func_name in ['Round', 'Abs']:
            category = 'math-functions'
        elif 'gui' in func_name.lower():
            category = 'gui-functions'
        elif 'hotkey' in func_name.lower() or func_name == 'Send':
            category = 'keyboard-hotkeys'
        elif 'click' in func_name.lower() or 'mouse' in func_name.lower():
            category = 'mouse-functions'
        elif func_name in ['If', 'Loop', 'For']:
            category = 'flow-control'

        # Generate file
        content = generate_example_file(func_name, category, examples)

        # Write file
        folder = Path('examples') / category
        folder.mkdir(parents=True, exist_ok=True)

        file_path = folder / f'{func_name}_Example.ahk'
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        examples_created += 1
        print(f'Created: {file_path}')

    print(f'\nTotal examples created: {examples_created}')

if __name__ == '__main__':
    main()
