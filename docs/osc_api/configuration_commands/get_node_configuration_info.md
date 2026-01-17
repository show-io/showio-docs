# Get Node Configuration Info

```
/sio/cfg/info/get
```

Requests basic information about the node's configuration.

### Arguments

none

## Response

```
/sio/cfg/info
```

### Arguments

- Arg 0 (`string`): Info JSON object

```json
    {
        "serial_num": "XXXXXXXXXXXX",
        "device_id": "Device-Id",
        "bootloader_version": "vX.Y.Z",
        "firmware_version": "vX.Y.Z"
    }
```