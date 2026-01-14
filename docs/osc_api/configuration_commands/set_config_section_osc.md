# Set Config Section - OSC

```
/sio/cfg/osc/set
```

Overwrites the OSC configuration section.

### Arguments

- Arg 0 (`string` | `blob`): OSC JSON object

## Effects
Overwrites OSC configuration section with the JSON object. If the JSON is invalid, the existing configuration will not be overwritten.