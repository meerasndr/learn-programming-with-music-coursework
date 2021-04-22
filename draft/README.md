# The Draft of the Course

This directory contains the tool chain to convert the markdown files into a html with livecode integrated.

## How to use

Step 1. Run `make serve` to build and serve the course

```
$ make serve
...
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

Step 2: Visit http://0.0.0.0:8000/

Alternatively, you can run `make` or `make build` and open the `build/index.html` file in the browser.

## How to add new course content

The course content is added as markdown files. Each markdown file will get exported as a HTML file.

In each markdown files, any code specified as code, will be turned into livecode editor. All you need to do is, add the code with tripple backticks.

    ```
    play("C3")
    ```

After making any changes, you need to run `make` to rebuild the contents.

## How does this work?

The livecode execution is done using the [livecode][] project.

Whenever run button is pressed, the code is sent to the livecode server along with couple of python scripts defined in the `src/` folder. When they are executed, they will send command to play music to the frontend. Those commands are executed in the frontend using [Tone.js][] library to create music. See `src/music.js` for the code that is responsible for playing the music.

[livecode]: https://github.com/fossunited/livecode
[Tone.js]: https://tonejs.github.io/

## How to add new functions to livecode

If you want to add a new function, let's say `chord` to play a list of notes together. For this you need to make the following code changes.

Add a `chord` function to `music.py`:

```
def chord(notes):
  sendmsg("music", function="chord", notes=note2)
```

Add a `chord` function to `music.js`:

```
function chord(notes) {
    synth.triggerAttackRelease(notes, "8n")
}
```

And add the following code to the `runCommand` function in `music.js` to call this function when the function name specified in the `cmd` is `chord`:

```
    else if (cmd.function == "chord") {
        chord(cmd.notes);
    }
```

Now you have added a new function `chord` to the available functions in the livecode editor.

Happy coding!