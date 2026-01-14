# Get Digital Output

```
/sio/do/{channel}/get
```

...where {channel} is a single character channel number.

Queries the current state of a digital output channel.

### Arguments

none

## Response

```
/sio/do/{channel}
```

### Arguments

- Arg 0 (`int`): Output state (0 for off, 1 for on)