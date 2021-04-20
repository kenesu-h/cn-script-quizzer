# cn-script-quizzer
Long project name aside, this was made to help myself and others memorize their
scripts for a Chinese skit. This is a command line program that will take in a
text file and parse it 3 lines at a time. These three line chunks will be
parsed as Dialogues, which represent each individual script line, their speaker,
plus the English and Chinese variations of the line.

## Command Line Arguments
```
./script-quizzer [-h] [-a ATTEMPTS] [-l LANGUAGE] [-n] [-s [SPEAKERS [SPEAKERS ...]]] path
```
`script-quizzer` may change depending on your operating system and the name of
the compiled program, but for the sake of simplicity, we will be using `script-quizzer`.
  - [-a ATTEMPTS] (optional)
    - Default: 2
    - Decides how many attempts you're given for each line.
  - [-l LANGUAGE] (optional)
    - Default: "chinese"
    - Decides which language you will be asked to input. If "chinese" is given,
      you will be shown the English versions of lines and asked to give the
      Chinese versions.
  - [-n] (optional)
    - Default: False
    - Decides whether you will be shown the lines. If this is enabled, you won't
      be shown the English versions of lines at all and will have to give the
      Chinese versions despite that. This is useful for memorizing the lines by
      heart as opposed to just translating them.
  - [-s [SPEAKERS [SPEAKERS ...]]] (optional)
    - Default: ""
    - Decides what lines you will be shown. For example, if you pass "-s student
      teacher", you will only be asked for the lines whose speaker is either
      "Student" or "Teacher". If you don't pass anything, you will be shown
      everyone's lines.
  - path (required)
    - The path to the script file you want to be quizzed on. For example, to run
      the program on the provided script file inside the `scripts` folder, run
      this in the command line:
      ```
      ./script-quizzer scripts/script.txt
      ```

## Script Formatting
In order to ensure file parsing consistency, you will have to structure your
script a certain way. Each line/piece of dialogue should be structured like
this:

```
Speaker Name:
My surname is Hou.
我姓侯。
```
  - The first line should contain the speaker's name or title. It's okay to
    include spaces or colons.
  - The second line should contain the English version of the line. As long as
    it's a single line, you should be fine.
  - The third line should contain the Chinese version of the line. Like the
    second line, it just has to all be on a single line.

With these rules, you can structure a file like this, for example:
```
Kenneth H:
My surname is Hou.
我姓侯。

John Smith:
Hello.
你好。
```
I don't think you need the empty line between the two pieces of dialogue.
Hopefully you shouldn't encounter any oddities, but try to avoid having your
scripts end with an empty line.

## Quizzing
You will be shown the line you have to translate/give the equivalent of (unless
you gave the `-n` flag), then you will be given a number of attempts to type the
answer. You will only get the answer right if you give EXACTLY what's given in
the script, so your answer may be wrong if you don't use the same punctuation,
or forget a space or two that's in the script. I don't have the time right now
to make this program smarter.

If you run out of attempts, you will be shown the exact answer. You will also be
shown all the lines you got wrong at the end so you can study them for later.

## Source Code and Compilation
If you're a developer, you can try your hand at editing the source code and
compiling the program on your own. You don't need any dependencies, but I use
PyInstaller to compile my Python projects into a binary executable. A version
of PyInstaller for Windows is given with the source code - which is allowed
under the GPL license - and a `Makefile` is provided for you, so you can call
`make` to compile the program provided that you have GNU Make installed on
your Windows 10 (unsure if this works on 7 or 8) computer. If you're using
other operating systems, you may have to acquire your own version of
PyInstaller and modify the `Makefile` accordingly, as executables compiled
using the Windows version of PyInstaller will not work on other OS's.

## Release
If you have Windows 10 and you don't have GNU Make - or if you don't want to
install it - I have a compiled version available right in the root directory
(base folder) that you can download and use. Just note that Windows Defender
might see it as a virus of some kind, which apparently happens a ton with
programs compiled using PyInstaller. Add it as an exception if this happens.

## Running It Directly
If you can't use the compiled Windows binary or still don't want to compile
it, you can run `main.py` if you've got a command line and Python 3 (it must
be 3) installed on your computer - preferably added to PATH variables too.
You can just run it with the same command line syntax as follows, assuming
your current directory is the root (cn-script-quizzer):
```
python src/main.py [-h] [-a ATTEMPTS] [-l LANGUAGE] [-n] [-s [SPEAKERS [SPEAKERS ...]]] path
```
Or if you have Python added to your PATH variables as `python3`:
```
python3 src/main.py [-h] [-a ATTEMPTS] [-l LANGUAGE] [-n] [-s [SPEAKERS [SPEAKERS ...]]] path
```

## The Future
I only started this project for a Chinese class, and I can't foresee myself
continuing to work on this until I take another foreign language. As a result,
this might not be as cleanly structured as my other projects. However, I may
revisit this at a later point to repurpose this into something more
general-purpose, or to clean up the code and make it more readable and/or
applicable to future projects.
