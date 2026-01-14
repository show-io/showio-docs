# ShowIO API Reference

The ShowIO API is a collection of OSC Methods that can be used with ShowIO nodes. This reference describes every OSC Method in the ShowIO API. 
  
The ShowIO API is designed to flexibly integrate with any other system that can talk over OSC. It implements the [official OSC specification](https://opensoundcontrol.stanford.edu/spec-1_0.html), but defines additional behavior and a shared message set for all ShowIO devices.

## Using This Reference

This reference contains all valid OSC Commands included in the ShowIO API. Each page describes an OSC Command, including any Responses or other effects that the Command triggers.  

Commands are organized by section:

:fontawesome-solid-gears: **[Node Configuration Commands](configuration_commands/overview.md)**  
:fontawesome-solid-magnifying-glass: **[Node Discovery Commands](discovery_commands/overview.md)**  
:fontawesome-solid-arrows-alt-h: **[I/O Control Commands](io_commands/overview.md)**  
:fontawesome-regular-question-circle: **[Utility Commands](utility_commands/overview.md)**  
  
Each Command is identified by a name and an Address. A Command may take a number of Arguments, which are pieces of data attached to an Address. In proper OSC terms, a Command described in this reference is implemented as an OSC Method on a ShowIO Node.
  
## Definitions

### Roles

Communicators using the ShowIO API have one of two roles:  
  
- **Controller:** sends commands and information requests, and listens for event messages in order to coordinate show behavior. Analogous to a DMX Master, RDM Controller, or HTTP Client.  
    - A controller can be any OSC Client.
- **Node:** responds to requests, executes actions, and publishes event messages. Analogous to a DMX Slave, RDM Responder, or HTTP Server.
    - A Node is an entity (usually a ShowIO device) that contains an OSC Server with an address space composed of ShowIO API Methods.

### Message Types

Three types of messages are defined in the ShowIO API:  
  
- **Command:** A directed message instructing a Node to perform an action.
    - Example: Controller A sends a Command `/sio/di/1/get` to Node X telling it to respond with the state of one of its inputs.
- **Response:** A directed message sent in reply to a command.
    - Example: Node X responds to Controller A with a Response `sio/di/1 1` that describes the state of the input.
- **Report:** An unsolicited message emitted by a Node to notify subscribers of an event.
    - Example: an input on Node X is triggered, and it sends a Report `/sio/di/3/ 1` to Controller A to notify it of this state change.