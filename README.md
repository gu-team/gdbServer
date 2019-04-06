# gdbServer

a server work in gdb

## how to install

```bash
pip install -r requirements.txt
```

## how to run

### either

```bash
gdb
```

come in the gdb, than:

```gdb
(gdb) source entry.py
```

### or

```bash
echo "source xxx/gdbServer/entry.py" >> ~/.gdbinit
gdb
```

`xxx` is where gdbServer project locate in
