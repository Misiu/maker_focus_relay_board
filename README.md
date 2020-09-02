# MakerFocus 4 Channel Relay Board Module Integration for Home Assistant

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

![Project Maintenance][maintenance-shield]
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]


_Component to integrate with [MakerFocus 4 Channel Relay Board Module][makerfocus]._

**This component will set up the following platforms.**

Platform | Description
-- | --
`switch` | Switch something `True` or `False`.

## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `maker_focus_relay_board`.
4. Download _all_ the files from the `custom_components/maker_focus_relay_board/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant
7. Add sample config to `configuration.yaml`:

```
switch:
  - platform: maker_focus_relay_board
    i2c_address: 0x10
    pins:
      1: First
      2: Second
      3: Third
      4: Fourth
```


## Configuration will be done in the UI in the future

<!---->

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

***

[releases-shield]: https://img.shields.io/github/release/Misiu/maker_focus_relay_board.svg?style=for-the-badge
[releases]: https://github.com/Misiu/maker_focus_relay_board/releases

[commits-shield]: https://img.shields.io/github/commit-activity/y/Misiu/maker_focus_relay_board.svg?style=for-the-badge
[commits]: https://github.com/Misiu/maker_focus_relay_board/commits/master

[license-shield]: https://img.shields.io/github/license/Misiu/maker_focus_relay_board.svg?style=for-the-badge

[makerfocus]: https://www.makerfocus.com/products/raspberry-pi-expansion-board-4-channel-relay-board-module-for-raspberry-pi-4b-3-model-b-raspberry-pi-3-2-model-b
[buymecoffee]: https://www.buymeacoffee.com/Misiu
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge

[maintenance-shield]: https://img.shields.io/badge/maintainer-%40Misiu-blue.svg?style=for-the-badge
