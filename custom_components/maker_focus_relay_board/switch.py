"""Support for switch"""
import logging

import smbus  # pylint: disable=import-error

from pcal9535a import PCAL9535A
import voluptuous as vol

from homeassistant.components.switch import PLATFORM_SCHEMA, SwitchEntity
from homeassistant.const import DEVICE_DEFAULT_NAME
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

CONF_I2C_BUS = "i2c_bus"
CONF_I2C_ADDRESS = "i2c_address"
CONF_PINS = "pins"


CONF_INVERT_LOGIC = "invert_logic"
CONF_STRENGTH = "strength"


DEFAULT_I2C_ADDRESS = 0x10
DEFAULT_I2C_BUS = 1

_SWITCHES_SCHEMA = vol.Schema({cv.positive_int: cv.string})

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_PINS): _SWITCHES_SCHEMA,
        vol.Optional(CONF_I2C_ADDRESS, default=DEFAULT_I2C_ADDRESS): vol.Coerce(int),
        vol.Optional(CONF_I2C_BUS, default=DEFAULT_I2C_BUS): cv.positive_int,
    }
)


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the maker_focus_relay_board devices."""

    bus = config[CONF_I2C_BUS]
    i2c_address = config[CONF_I2C_ADDRESS]

    i2c_bus = smbus.SMBus(bus)

    pcal = PCAL9535A(bus, i2c_address)

    switches = []
    pins = config[CONF_PINS]
    for pin_num, pin_name in pins.items():
        pin = pcal.get_pin(pin_num // 8, pin_num % 8)
        switches.append(I2CRelaySwitch(i2c_bus, i2c_address, pin_name, pin_num))

    add_entities(switches)


class I2CRelaySwitch(SwitchEntity):
    """Representation of a MakerFocus 4 Channel Relay Board Module output pin."""

    def __init__(self, bus, i2c_address, name, pin):
        """Initialize the pin."""
        self._bus = bus
        self._i2c_address = i2c_address
        self._name = name or DEVICE_DEFAULT_NAME
        self._pin = pin
        self._state = False

    @property
    def name(self):
        """Return the name of the switch."""
        return self._name

    @property
    def should_poll(self):
        """No polling needed."""
        return False

    @property
    def is_on(self):
        """Return true if device is on."""
        return self._state

    @property
    def assumed_state(self):
        """Return true if optimistic updates are used."""
        return True

    def turn_on(self, **kwargs):
        """Turn the device on."""
        bus.write_byte_data(self._i2c_address, self._pin_num, 0xFF)
        self._state = True
        self.schedule_update_ha_state()

    def turn_off(self, **kwargs):
        """Turn the device off."""
        bus.write_byte_data(self._i2c_address, self._pin_num, 0x00)
        self._state = False
        self.schedule_update_ha_state()
