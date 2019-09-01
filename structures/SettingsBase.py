from typing import NamedTuple


class OvertoolsSettingsBase(NamedTuple):
    filename: str

    def replicate_with_filename(self, filename): OvertoolsSettingsBase(filename=filename, **self._asdict())
