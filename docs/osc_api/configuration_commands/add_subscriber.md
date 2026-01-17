# Add Subscriber

```
/sio/cfg/osc/subscribers/add
```

Adds a specified endpoint to the list of subscribers that receive report messages from the node.

### Arguments

- Arg 0 (`string`): Transport type: "udp", "tcp", or "usb"
- Arg 1 (`string`): IP address (required for udp/tcp, ignored for usb)
- Arg 2 (`int` | `float`): Port number (required for udp/tcp, ignored for usb)

## Effects
Registers the specified endpoint as a subscriber. The device will send OSC report messages
(e.g., digital input changes) to all registered subscribers. Returns an error if the subscriber is
already registered or the maximum number of subscribers is reached.