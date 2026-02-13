# Changelog

## Firmware Release - v0.2.7
Released January 30, 2026

### Features:

- Enabled Watchdog timer in firmware; if program crashes, watchdog will auto-reset

### Fixes:

- Stopped firmware + bootloader version from getting overwritten on factory reset

## Firmware Release - v0.2.6
Released January 26, 2026

### Features:

- Added ability to factory reset nodes using 10th dip switch
- Added channel configuration settings
    - Software-set debouncing filter

### Fixes:

- Eliminated crash points when pinging a node with /ping
- Fixed /sio/cfg/lan/get response address

### Changes:

- Changed serial number format to new 18-char format