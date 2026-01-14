# Set Config Section - Device ID

```
/sio/cfg/deviceid/set
```

Overwrites the device ID configuration section.

### Payload

- Arg 0 (`string` | `blob`): Device ID JSON object

## Effects
Overwrites device ID configuration section with the JSON object. If the JSON is invalid, the existing configuration will not be overwritten.