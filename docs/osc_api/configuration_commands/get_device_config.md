# Get Device Config

```
/sio/cfg/get
```

Queries the device configuration.

!!! warning

    WILL BE DEPRECATED ONCE DEVICE CONFIG GETS TOO BIG TO FIT IN A UDP PACKET (or I figure out a cleverer way to do this)

### Payload

none

## Response

```
/sio/cfg
```

### Payload

- Arg 0 (`string`): Device configuration JSON object