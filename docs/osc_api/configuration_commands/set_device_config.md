# Set Device Config

```
/sio/cfg/set
```

Overwrites the device configuration.

!!! warning

    WILL BE DEPRECATED ONCE DEVICE CONFIG GETS TOO BIG TO FIT IN A UDP PACKET (or I figure out a cleverer way to do this)

### Payload

- Arg 0 (`string` | `blob`): Device configuration JSON object

## Effects
Overwrites device configuration with the JSON object. If the JSON is an invalid device configuration, the existing configuration will not be overwritten.