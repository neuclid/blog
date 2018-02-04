Title: How to get multiple tabs on git bash [Windows]
Date: 2018-01-19
Category: Programming
Tags: gitbash, windows, workflow

I’m on Windows (please no bully). So while `cmd.exe` is terrible to get comfortable with, I’ve gotten along alright with git bash. However, whenever I use the Linux terminal, I find myself using **tmux** and/or tabs in general. So naturally, I wanted to figure out similar functionality on Windows.

Let’s get to it.

1. Get [ConEmu](https://sourceforge.net/projects/conemu/files/latest/download). If you’re curious about what it does, more details [here](https://conemu.github.io/).
2. Unzip it into a folder.
3. If you’re on an x64 machine, run `ConEmu64.exe`. If you’re not sure or if you’re on x86, run `ConEmu.exe`
4. If you’re prompted by any UAC warnings, allow them.
5. You’ll be asked for some settings. Make the changes as shown with the arrows. The first change is to choose Git bash as the program that you want to run in tabbed mode. The second change is to assign a shortcut for running bash inside ConEmu.
6. Profit!

Here are the settings just in case:
![conEmu settings](/images/conemu_1.png)

### Usage:
* Use the shortcut you assigned (default is ``` Ctrl + ` ```) to run your git bash
* Use `Win + W` to create a new tab
* Use `Ctrl + Tab` to move across tabs
* Use `Win + Alt + Del` to delete tab

### Bonus:

* Use `Ctrl + Shift + e` to split your terminal vertically (to the right)
* Use `Ctrl + Shift + o` to split your terminal horizontally (to the bottom)
* You can even use your mouse to move across these splits if you prefer that
