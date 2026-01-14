# Device Discovery

```
/sio/discover/request
```

Responds to a discovery request with device information including name, serial number, and port.

### Payload

- Arg 0 (`int` | `float`): Response port number

## Response

```
/sio/discovery/response
```

### Payload

- Arg 0 (`string`): Device name
- Arg 1 (`string`): Serial number
- Arg 2 (`int`): UDP receive port