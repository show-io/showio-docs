# Get Digital Input Report Message

```
/sio/cfg/osc/reportMsg/di/{channel}/{state}/get
```

...where {channel} is a single character channel number and {state} is either "hi" or "lo".

Retrieves the configured custom OSC message for a specific digital input event.

### Arguments

None

## Response

```
/sio/cfg/osc/reportMsg/di
```

### Arguments

- Arg 0 (`string`): JSON object containing the configured DI event message with `address` and `payload` fields
```json
    {
        "address": "/sio/an/address",
        "payload": [
            {"Type": "value"},
            {"Type": "value"},
            {"Type": "value"},
        ]
    }
```