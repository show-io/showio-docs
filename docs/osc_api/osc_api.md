# OSC API Reference

Auto-generated documentation for OSC functions.

## I/O Commands

These OSC commands control and query the digital I/O channels.

---
# Set Digital Output

```
/sio/do/{channel}/set
```

...where {channel} is a single character channel number.

Sets the state of a digital output channel.

### Payload

- Arg 0 (`int` | `float` | `True` | `False`): Output state (0/false for off, non-zero/true for on)

### Effects
> **Function:** `set_digital_output`  
> **Source:** `io.rs`
Changes the state of the specified digital output channel (1-4).

---
# Get Digital Output

```
/sio/do/{channel}/get
```

...where {channel} is a single character channel number.

Queries the current state of a digital output channel.

### Payload

none

### Response
> **Function:** `get_digital_output`  
> **Source:** `io.rs`

```
/sio/do/{channel}
```

### Payload

- Arg 0 (`int`): Output state (0 for off, 1 for on)

---
# Get Digital Input

```
/sio/di/{channel}/get
```

...where {channel} is a single character channel number.

Queries the current state of a digital input channel.

### Payload

none

### Response
> **Function:** `get_digital_input`  
> **Source:** `io.rs`

```
/sio/di/{channel}
```

### Payload

- Arg 0 (`int`): Input state (0 for low, 1 for high)

---
# Get All Digital Inputs

```
/sio/di/get
```

Queries the current state of all digital input channels.

### Payload

none

### Response
> **Function:** `get_all_di_state`  
> **Source:** `io.rs`

```
/sio/di
```

### Payload

- Arg 0 (`int`): Channel 1 state (0 for low, 1 for high)
- Arg 1 (`int`): Channel 2 state (0 for low, 1 for high)
- Arg 2 (`int`): Channel 3 state (0 for low, 1 for high)
- Arg 3 (`int`): Channel 4 state (0 for low, 1 for high)

---
## Discovery Commands

These OSC commands allow clients to discover ShowIO devices on the network.

---
# Device Discovery

```
/sio/discover/request
```

Responds to a discovery request with device information including name, serial number, and port.

### Payload

- Arg 0 (`int` | `float`): Response port number

### Response
> **Function:** `handle_discovery_request`  
> **Source:** `discovery.rs`

```
/sio/discovery/response
```

### Payload

- Arg 0 (`string`): Device name
- Arg 1 (`string`): Serial number
- Arg 2 (`int`): UDP receive port

---
## Configuration Commands

These OSC commands allow the user to reconfigure the ShowIO device.

---
# Get Device Config

```
/sio/cfg/get
```

Queries the device configuration.

!!! warning

    WILL BE DEPRECATED ONCE DEVICE CONFIG GETS TOO BIG TO FIT IN A UDP PACKET (or I figure out a cleverer way to do this)

### Payload

none

### Response
> **Function:** `get_cnfg`  
> **Source:** `cfg.rs`

```
/sio/cfg
```

### Payload

- Arg 0 (`string`): Device configuration JSON object

---
# Set Device Config

```
/sio/cfg/set
```

Overwrites the device configuration.

!!! warning

    WILL BE DEPRECATED ONCE DEVICE CONFIG GETS TOO BIG TO FIT IN A UDP PACKET (or I figure out a cleverer way to do this)

### Payload

- Arg 0 (`string` | `blob`): Device configuration JSON object

### Effects
> **Function:** `set_cfg_from_json`  
> **Source:** `cfg.rs`
Overwrites device configuration with the JSON object. If the JSON is an invalid device configuration, the existing configuration will not be overwritten.

---
# Wipe Device Config

```
/sio/cfg/wipe
```

Resets the device configuration to factory defaults.

### Payload

none

### Effects
> **Function:** `wipe_config`  
> **Source:** `cfg.rs`
Overwrites the entire device configuration with the default initialization values.

---
# Get Config Section - Device ID

```
/sio/cfg/deviceid/get
```

Queries the device ID configuration section.

### Payload

none

### Response
> **Function:** `get_device_id`  
> **Source:** `cfg.rs`

```
/sio/cfg/deviceid
```

### Payload

- Arg 0 (`string`): Device ID JSON object

---
# Set Config Section - Device ID

```
/sio/cfg/deviceid/set
```

Overwrites the device ID configuration section.

### Payload

- Arg 0 (`string` | `blob`): Device ID JSON object

### Effects
> **Function:** `set_device_id`  
> **Source:** `cfg.rs`
Overwrites device ID configuration section with the JSON object. If the JSON is invalid, the existing configuration will not be overwritten.

---
# Get Config Section - Metadata

```
/sio/cfg/metadata/get
```

Queries the metadata configuration section.

### Payload

none

### Response
> **Function:** `get_metadata`  
> **Source:** `cfg.rs`

```
/sio/cfg/metadata
```

### Payload

- Arg 0 (`string`): Metadata JSON object

---
# Set Config Section - Metadata

```
/sio/cfg/metadata/set
```

Overwrites the metadata configuration section.

### Payload

- Arg 0 (`string` | `blob`): Metadata JSON object

### Effects
> **Function:** `set_metadata`  
> **Source:** `cfg.rs`
Overwrites metadata configuration section with the JSON object. If the JSON is invalid, the existing configuration will not be overwritten.

---
# Get Config Section - Local IP

```
/sio/cfg/localip/get
```

Queries the local IP configuration section.

### Payload

none

### Response
> **Function:** `get_local_ip`  
> **Source:** `cfg.rs`

```
/sio/cfg/localip
```

### Payload

- Arg 0 (`string`): Local IP JSON object

---
# Set Config Section - Local IP

```
/sio/cfg/localip/set
```

Overwrites the local IP configuration section.

### Payload

- Arg 0 (`string` | `blob`): Local IP JSON object

### Effects
> **Function:** `set_local_ip`  
> **Source:** `cfg.rs`
Overwrites local IP configuration section with the JSON object. If the JSON is invalid, the existing configuration will not be overwritten.

---
# Get Config Section - OSC

```
/sio/cfg/osc/get
```

Queries the OSC configuration section.

### Payload

none

### Response
> **Function:** `get_osc`  
> **Source:** `cfg.rs`

```
/sio/cfg/osc
```

### Payload

- Arg 0 (`string`): OSC JSON object

---
# Set Config Section - OSC

```
/sio/cfg/osc/set
```

Overwrites the OSC configuration section.

### Payload

- Arg 0 (`string` | `blob`): OSC JSON object

### Effects
> **Function:** `set_osc`  
> **Source:** `cfg.rs`
Overwrites OSC configuration section with the JSON object. If the JSON is invalid, the existing configuration will not be overwritten.

---
# Set Response Port

```
/sio/cfg/responseport/set
```

Sets the UDP port number used for OSC response messages.

### Payload

- Arg 0 (`int` | `float`): UDP port number for responses

### Effects
> **Function:** `set_response_port`  
> **Source:** `cfg.rs`
Updates the device configuration to send all OSC response messages to the specified port.

---
# Subscribe Me

```
/sio/sub/me
```

Adds an endpoint to the list of subscribers that receive event notifications.

### Payload

- Arg 0 (OPTIONAL - `int` | `float`): Port number of the subscriber, if necessary

### Effects
> **Function:** `subscribe_me`  
> **Source:** `cfg.rs`
Registers the source endpoint as a subscriber. If sent over network, the subscriber will be added as either TCP or UDP, depending on the source protocol, and the
subscriber's socket address will be the source IP and the supplied port. If a port is not supplied, it will default to the configured response port. If a subscription
request is sent over USB, the port is not necessary.
The device will send OSC event messages (e.g., digital input changes) to all registered subscribers. Returns an error if the subscriber is already registered or
the maximum number of subscribers is reached.

---
# Unsubscribe

```
/sio/unsub/me
```

Removes an endpoint from the list of event notification subscribers.

### Payload

- Arg 0 (OPTIONAL - `int` | `float`): Port number of the subscriber to remove

### Effects
> **Function:** `unsubscribe_me`  
> **Source:** `cfg.rs`
Removes the source from the subscriber list, with the specified port number (if necessary). If a request is received from a UDP source with no specified port, it will default to trying the configured response port. Returns an error if the endpoint is not in the subscriber list.

---
# Provision Serial Number

```
/sio/cfg/serial/set
```

Sets the device serial number in EEPROM.

### Payload

- Arg 0 (`string`): Serial number to write

### Effects
> **Function:** `provision_serial_number`  
> **Source:** `cfg.rs`
Writes the provided serial number to the device's EEPROM storage. This is typically used during device provisioning.

---
# Set Digital Input Event Message

```
/sio/cfg/eventmsg/di/{channel}/set
```

...where {channel} is a single character channel number.

Configures a custom OSC message to be sent to subscribers when a digital input state changes.

!!! warning

    Event messages have an encoded size limitation of 128 bytes.

### Payload

- Arg 0 (`int` | `float` | `True` | `False`): Input state trigger (0/false for off, 1/true for on)
- Arg 1 (`string` | `blob`): Address of new event message. Example: "/cue/20/go"
- Arg 2+ (OPTIONAL - `any`): After the required arguments, up to 10 optional arguments provided in this
configuration message will be packed into the new event message.

### Effects
> **Function:** `set_di_event_message`  
> **Source:** `cfg.rs`
Stores a custom OSC message in the device configuration. When the specified digital input channel changes to the specified state, the custom message will be sent to all registered subscribers.

## Example
Message:
```
/sio/cfg/eventmsg/di/3/set T, /fader1/set, 255
```

- Address ("/sio/cfg/eventmsg/di/3/set"): set the event message for Digital Input Channel 3
- Arg 0 (True): this event message will trigger when the digital input changes state to True
- Arg 1 (string, "/fader1/set"): the event message will have an address of "/fader1/set"
- Arg 2 (int, 255): the event message will include an integer argument of 255

---
## Utility Commands

These OSC commands provide utility functions for debugging and testing.

---
# Ping

```
/ping
```

Responds to a ping request with a pong message, echoing back the provided arguments.

### Payload

- Arg 0 (any): Message ID to echo back
- Arg 1 (any): Additional data to echo back

### Response
> **Function:** `ping_handler`  
> **Source:** `misc.rs`

```
/pong
```

### Payload

- Arg 0 (any): Echoed message ID from request
- Arg 1 (any): Echoed additional data from request

---
# Default Handler

```
(any unmatched address)
```

Fallback handler for OSC messages that don't match any registered route. Logs the message address and arguments for debugging.

### Payload

(any)

### Effects
> **Function:** `default_handler`  
> **Source:** `misc.rs`
Logs the received message address and argument count to the debug output.

---