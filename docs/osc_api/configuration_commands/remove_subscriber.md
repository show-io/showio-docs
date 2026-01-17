# Remove Subscriber

```
/sio/cfg/osc/subscribers/remove
```

Removes a specified endpoint from the list of subscribers.

### Arguments

- Arg 0 (`string`): Transport type: "udp", "tcp", or "usb"
- Arg 1 (`string`): IP address (required for udp/tcp, ignored for usb)
- Arg 2 (`int` | `float`): Port number (required for udp/tcp, ignored for usb)

## Effects
Removes the specified endpoint from the subscriber list. Returns an error if the endpoint is not in the subscriber list.