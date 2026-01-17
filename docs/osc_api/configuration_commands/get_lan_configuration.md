# Get LAN Configuration

```
/sio/cfg/lan/get
```

Requests information about the node's LAN configuration

### Arguments

none

## Response

```
/sio/cfg/lan
```

### Arguments

- Arg 0 (`string`): LAN configuration JSON object

 ```json
    {
        "mac_address": [01, 02, 03, 04, 05, 06],
        "ip_mode": "dhcp | manual_ip | quick_ip",
        "quick_ip_prefix": [192, 168, 10],
        "quick_subnet": 24,
        "quick_gateway": [192, 168, 10, 1],
        "manual_ip": [10, 0, 0, 10],
        "manual_subnet": 8,
        "manual_gateway": [10, 0, 0, 1]
    }
```