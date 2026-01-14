# Unsubscribe

```
/sio/unsub/me
```

Removes an endpoint from the list of event notification subscribers.

### Payload

- Arg 0 (OPTIONAL - `int` | `float`): Port number of the subscriber to remove

## Effects
Removes the source from the subscriber list, with the specified port number (if necessary). If a request is received from a UDP source with no specified port, it will default to trying the configured response port. Returns an error if the endpoint is not in the subscriber list.