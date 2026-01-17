# Get OSC Configuration

```
/sio/cfg/osc/get
```

Queries the OSC configuration section.

### Arguments

none

## Response

```
/sio/cfg/osc
```

### Arguments

- Arg 0 (`string`): OSC configuration JSON object:
 ```json
    {
        "udp_receive_port": 53000,
        "udp_response_port": 53001,
        "subscribers": [
            {"Udp": "192.168.10.10"},
            "Usb"
        ]
    }
```