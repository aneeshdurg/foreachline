# foreachline

Utility to run a python snippet against every line in a stream

Example - get a per line character count:

```console
$ head -n 5 file.txt
a
bb
ccc
dddd
eeeee
$ cat file.txt | foreachline run "len(l)"
1
2
3
4
5
...
```

`foreachline` can also filter text based on a predicate

```console
$ head file.txt
a
bb
ccc
dddd
eeeee
ffffff
ggggggg
hhhhhhhh
iiiiiiiii
jjjjjjjjjj
$ cat file.txt | foreachline filter "len(l) > 3"
dddd
eeeee
ffffff
ggggggg
hhhhhhhh
iiiiiiiii
jjjjjjjjjj
...
```
