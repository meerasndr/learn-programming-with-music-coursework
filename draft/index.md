# The Joy of Music

Lets play some music.

```
play("c3")
```

How about trying it in a loop?

```
notes = ["c3", "d3", "e3", "f3", "g3", "a3", "b3"]

for note in notes:
    play(note)
    sleep(0.5)
```

Now, can we play the notes in reverse?

```
reversenotes = ["b3", "a3", "g3", "f3", "e3", "d3", "c3"]

for note in reversenotes:
  play(note)
  sleep(0.5)
```

How do we play each note 2 times?
```
notes = ["c3", "d3", "e3", "f3", "g3", "a3", "b3"]

for note in notes:
    play(note)
    sleep(0.5)
    play(note)
    sleep(0.5)
```

Try changing the sleep duration from 0.5 to 1. What happens? <br><br>

Shall we try playing the same *set of notes* 3 times? But, with different sleep duration!

```
notes = ["c3", "d3", "e3", "f3", "g3", "a3", "b3"]

for note in notes:
    play(note)
    sleep(1.5)
for note in notes:
    play(note)
    sleep(1)
for note in notes:
    play(note)
    sleep(0.5)
```
