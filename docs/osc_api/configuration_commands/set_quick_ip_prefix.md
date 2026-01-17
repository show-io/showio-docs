# Set Quick IP Prefix

```
/sio/cfg/lan/quick/ipPrefix/set
```

Sets the first three octets of the IP address when using Quick IP mode.

### Arguments

- Arg 0 (`int` | `float`): First octet (0-255)
- Arg 1 (`int` | `float`): Second octet (0-255)
- Arg 2 (`int` | `float`): Third octet (0-255)

## Effects
Updates the Quick IP prefix configuration. The fourth octet is determined by the DIP switch setting.