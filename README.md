# Learn programming with music course plan

### A WIP plan to teach simple programming ideas using Python & Music
### Target audience: New programmers, no musical knowledge assumed

1. Make a beep. 
	* Goal: 
		1. Code: Make a beep with code. Progress to making a sequence of beeps.
		2. Understand note names  
    [Your First Beeps](https://sonic-pi.net/tutorial.html#section-2-1)
2. Make a sequence of beeps
3. Refactor beeps sequence with a loop
4. Refactor beeps sequence with `sleep`, `amp` and `pan`
5. Randomisation & sleep
```
	3.times do
  	play 60 + rand(10)
  	sleep 0.5
	end
```
6. If else with rand(). 
 `Toss a virtual musical coin`
```
if rand(1) < 0.5
 # if heads, play two ascending notes
  play 60
  sleep 0.5
  play 62
else
  # if tails, play three descending notes
  play 72
  sleep 0.25
  play 71
  sleep 0.25
  play 70
end
```

7. What are comments in code?
8. Errors and debugging
	1. Try removing spaces / indents
	2. Remove `end` from a loop
	3. Remove `end` from an if-else block
9. Discovering new sounds
	1. Synths: [Switching Synths](https://sonic-pi.net/tutorial.html#section-2-3)
	2. Drums
	3. Bass
10. Make a simple melody with all these ideas
