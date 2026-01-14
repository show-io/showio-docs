# Get Digital Input

```
/sio/di/{channel}/get
```

...where {channel} is a single character channel number.

Queries the current state of a digital input channel.

### Payload

none

## Response

```
/sio/di/{channel}
```

### Payload

- Arg 0 (`int`): Input state (0 for low, 1 for high)