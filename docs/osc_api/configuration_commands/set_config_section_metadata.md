# Set Config Section - Metadata

```
/sio/cfg/metadata/set
```

Overwrites the metadata configuration section.

### Arguments

- Arg 0 (`string` | `blob`): Metadata JSON object

## Effects
Overwrites metadata configuration section with the JSON object. If the JSON is invalid, the existing configuration will not be overwritten.