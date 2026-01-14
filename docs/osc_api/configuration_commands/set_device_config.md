# Set Device Config

```
/sio/cfg/set
```

Overwrites the device configuration.

!!! warning

    Due to message size constraints, this Command will be deprecated in the near future.

### Arguments

- Arg 0 (`string` | `blob`): Device configuration JSON object

## Effects
Overwrites device configuration with the JSON object. If the JSON is an invalid device configuration, the existing configuration will not be overwritten.