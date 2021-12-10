"""TuneBladeEntity class"""
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, NAME, VERSION


class TuneBladeEntity(CoordinatorEntity):
    def __init__(self, coordinator, config_entry):
        super().__init__(coordinator)
        self.config_entry = config_entry

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return self.config_entry.entry_id

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.unique_id)},
            "name": NAME,
            "model": VERSION,
            "manufacturer": NAME,
        }

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        return {
            "device_friendly_name": str(self.coordinator.data.get("Name")),
            "status": str(self.coordinator.data.get("Status")),
            "substate": str(self.coordinator.data.get("Substate")),
            "buffering": str(self.coordinator.data.get("Buffering")),
            "buffering_percent": str(self.coordinator.data.get("BufferingPercent")),
        }