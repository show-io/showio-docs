# Provision Serial Number

```
/sio/cfg/serial/set
```

Sets the device serial number in EEPROM.

### Payload

- Arg 0 (`string`): Serial number to write

## Effects
Writes the provided serial number to the device's EEPROM storage. This is typically used during device provisioning.