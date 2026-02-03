# ShowIO Digital Combo 8

4-channel digital input + 4-channel digital output module.

## Safety

!!! warning "Electrical Safety Warning"

    **READ AND UNDERSTAND ALL SAFETY INSTRUCTIONS BEFORE INSTALLATION OR USE**

    - This device operates at 12-24 volts DC and outputs up to 2A per channel. Improper installation or use may result in electric shock, fire, equipment damage, or personal injury.
    - Do not use this device in safety-critical applications where failure could result in injury, death, or significant property damage without implementing appropriate redundancy and fail-safe systems.
    - Installation and wiring must be performed by qualified personnel only, in accordance with local electrical codes and regulations.
    - Always disconnect power before making any connections or modifications to the device.
    - Do not exceed the rated voltage or current specifications. Each output channel is rated for 2A continuous current maximum. The power input is rated for 3A continuous current maximum.
    - The 3A fuse provides overcurrent protection for the device but does not replace proper circuit protection at the power source.
    - Ensure proper wire gauge and insulation for all connections. Use only copper conductors rated for the application.
    - This device must be installed in a suitable enclosure to protect against environmental hazards and accidental contact with live circuits.
    - Verify correct polarity before applying power. Reverse polarity may damage the device despite built-in protection.
    - Keep the device away from water, excessive heat, and flammable materials.

    **FAILURE TO FOLLOW THESE WARNINGS MAY RESULT IN SERIOUS INJURY OR DEATH**

## Technical Specifications

### Power Supply
- 12-24 volt DC input
- Resettable fuse sized for 3A continuous draw
- Overcurrent, overvoltage, reverse voltage, and ESD protection

### I/O Channels
- (4) 12-24VDC digital inputs - isolated, 2-wire connection
- (4) 12-24VDC digital outputs - 2A per-channel current limit
- Rugged circuit protection on every channel
- Easily test channels with onboard pushbuttons and indicator lights

### Connectivity
- OSC communication for easy connection to most show control systems
- 10/100 Ethernet port
- DIP switches for quick configuration of LAN settings
- Supports static IP addressing and DHCP
- USB serial port

### Software
- Regular firmware updates with bug fixes and new features
- Implements ShowIO API

## Installation and Usage

### LAN Configuration

The ShowIO Digital Combo 8 uses onboard DIP switches to set its LAN (Local Area Network) configuration. Three configuration modes are available:

| Mode | DIP Switch State | Description |
| --- | --- | --- |
| **Quick-IP** | 1 to 254 | Use the DIP switches to set the last number in a static IP address on a factory-set subnet. |
| **Manual IP** | 0 | Manually set an IP address and subnet in software. |
| **Auto-IP (DHCP)** | 255 | Enable DHCP and receive an automatically assigned IP address from your network infrastructure. |

After making changes to a Node's LAN configuration, power-cycle or restart it for the changes to take effect.

#### Setting the IP Address with Quick-IP

This configuration flow should be familiar to anyone that's set a DMX address on a light. We set the first 8 DIP switches to a binary representation of a number, 1-254.

!!! tip

    If you're not familiar with binary notation, check out this [helpful article from Laserworld](https://www.laserworld.com/en/laserworld-toolbox/dmx-address-setting.html) about setting an address using DIP switches. They even have a handy calculator!

ShowIO products ship with Quick-IP defaults `192.168.10.x` on a `255.255.255.0` subnet, where `x` is the 1-254 number set using the DIP switches. The Quick-IP address prefix, subnet, and gateway are software-configurable via OSC.

##### Quick-IP Example

Alice has (3) ShowIO Nodes that she wants to connect to a network. She sets her laptop to `192.168.10.10` with a subnet mask of `255.255.255.0` and a default gateway of `192.168.10.1`. She sets the DIP switches on her three ShowIO Nodes to `30`, `31`, and `32`. She plugs all her devices into a network switch, and the network looks like:

| Device | IP Address |
| --- | --- |
| Alice's Laptop | 192.168.10.10 |
| Node #1 | 192.168.10.30 |
| Node #2 | 192.168.10.31 |
| Node #3 | 192.168.10.32 |

Now Alice can send messages from her laptop to all three nodes!

#### Setting the IP Address Manually

A Node's static network settings can manually be set using commands from the [OSC API](../../osc_api/overview.md). Note that this requires an existing connection to the Node. To enable manual IP mode, set the DIP switches to `0`. On next boot, the Node will have the manually set IP configuration.

The factory-default manual IP setting is `10.11.12.10` with a subnet mask of `255.0.0.0` and default gateway `10.0.0.1`.

#### Setting the IP Address with Auto-IP

The Node can use DHCP to request an automatically assigned IP address from a DHCP server (generally, a router or managed network switch). To enable DHCP, set the DIP switches to `255`. On next boot, the Node will search for a DHCP server to request an IP address.

### OSC Configuration

After getting a Node connected to a LAN, any Controller on that LAN can send it OSC commands at port `UDP: 8888` (configurable).

When a Controller sends a Node a Request Command, the Node will reply with a message sent to `UDP: 9999` (configurable).

## Channel Wiring

<p align="center"><img src="../../../assets/diagrams/power.svg" height=200></p>