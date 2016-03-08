Context manager to mimic *nix tail -f

```
with Tail(sys.argv[1]) as t:
	for l in t:
        	print(l)
                if "quit" in l:
                	t.exit = True
```
