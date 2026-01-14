# Set Config Section - Local IP

```
/sio/cfg/localip/set
```

Overwrites the local IP configuration section.

### Arguments

- Arg 0 (`string` | `blob`): Local IP JSON object

## Effects
Overwrites local IP configuration section with the JSON object. If the JSON is invalid, the existing configuration will not be overwritten.