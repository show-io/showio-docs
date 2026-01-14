# Get All Digital Inputs

```
/sio/di/get
```

Queries the current state of all digital input channels.

### Arguments

none

## Response

```
/sio/di
```

### Arguments

- Arg 0 (`int`): Channel 1 state (0 for low, 1 for high)
- Arg 1 (`int`): Channel 2 state (0 for low, 1 for high)
- Arg 2 (`int`): Channel 3 state (0 for low, 1 for high)
- Arg 3 (`int`): Channel 4 state (0 for low, 1 for high)