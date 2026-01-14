# Subscribe Me

```
/sio/sub/me
```

Adds an endpoint to the list of subscribers that receive event notifications.

### Payload

- Arg 0 (OPTIONAL - `int` | `float`): Port number of the subscriber, if necessary

## Effects
Registers the source endpoint as a subscriber. If sent over network, the subscriber will be added as either TCP or UDP, depending on the source protocol, and the
subscriber's socket address will be the source IP and the supplied port. If a port is not supplied, it will default to the configured response port. If a subscription
request is sent over USB, the port is not necessary.
The device will send OSC event messages (e.g., digital input changes) to all registered subscribers. Returns an error if the subscriber is already registered or
the maximum number of subscribers is reached.