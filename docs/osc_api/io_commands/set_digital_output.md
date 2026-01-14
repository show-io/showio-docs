# Set Digital Output

```
/sio/do/{channel}/set
```

...where {channel} is a single character channel number.

Sets the state of a digital output channel.

### Payload

- Arg 0 (`int` | `float` | `True` | `False`): Output state (0/false for off, non-zero/true for on)

## Effects
Changes the state of the specified digital output channel (1-4).