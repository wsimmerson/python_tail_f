Context manager to mimic *nix tail -f

```
with Tail("mylogfile") as t:
	for line in t:
		print(line)
		if "quit" in line:
			t.exit = True
```
