# Set Digital Input Event Message

```
/sio/cfg/osc/reportMsg/di/{channel}/{state}/set
```

...where {channel} is a single character channel number and {state} is either "hi" or "lo".

Configures a custom OSC message to be sent to subscribers when a digital input state changes.

!!! warning

    Event messages have an encoded size limitation of 128 bytes.

### Arguments

- Arg 0 (`string` | `blob`): Address of new event message. Example: "/cue/20/go"
- Arg 1+ (OPTIONAL - `any`): After the required arguments, up to 10 optional arguments provided in this
configuration message will be packed into the new event message.

## Effects
Stores a custom OSC message in the device configuration. When the specified digital input channel changes to the specified state, the custom message will be sent to all registered subscribers.

## Example
Message:
```
/sio/cfg/osc/reportMsg/di/3/hi/set "/fader1/set", 255
```

- Address ("/sio/cfg/osc/reportMsg/di/3/hi/set"): set the event message for Digital Input Channel 3 high state
- Arg 0 (string, "/fader1/set"): the event message will have an address of "/fader1/set"
- Arg 1 (int, 255): the event message will include an integer argument of 255