"""Subclasses bot to add extra functionalities."""

# Standard Libraries.
from enum import Enum
import pathlib
import time

# Third Party Libraries.
from discord.ext import commands

# Project Modules.
from bot.constants import InternalConstants
from bot.log import get_logger

log = get_logger(__name__)


class ExtensionActions(Enum):
    """Actions possible for extensions.

    Attributes:
    LOAD
        Load extension to the bot.
    RELOAD
        Reload extension in the bot.
        UNLOAD
        Unload extension from the bot.
    """

    LOAD = "load"
    RELOAD = "reload"
    UNLOAD = "unload"


class ExtensionError(Exception):
    """Exception when an extension errors.

    Attributes:
    name
        The name of extension.
    """

    name: str

    def __init__(self, name: str, *args) -> None:
        super().__init__(args)
        self.name = name


ExtensionsList = list[str]
"""Represent a list of extensions names."""
ExtensionUpdateResponse = tuple[bool, list[ExtensionError]]
"""Represent reponse after performing action on extenions.

    success
        Specifies whether loading was successful or not.
    errors
        Dictionary contains extension name as key and value as error occured.
"""


class Bot(commands.Bot):
    """Subclasses bot to add extra attributes and methods.

    Attributes:
    start_time
        The time bot started in seconds since the Epoch.

    Methods:
    on_ready
        Runs when bot is ready.
    _manage_all_extensions
        Manage all extensions.
    """

    start_time: int

    def __init__(self, command_prefix=None, **kwargs) -> None:
        super().__init__(command_prefix, **kwargs)

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        """Runs when bot is ready. It saves the time and logs the message to console"""
        self.start_time = round(time.time())
        log.info(" %s is ready!", self.user)
        await self.load_all_extensions()

    async def _manage_all_extensions(
        self,
        action: ExtensionActions,
        exclude: ExtensionsList | None = None,
        include_only: ExtensionsList | None = None,
    ) -> ExtensionUpdateResponse:
        """Can perform load, unload, reload action on extensions.
        Its assummed that exts folder is categorized.\n
        exts/
            category1/
                commandName1.py
                commandName2.py
            category2/
                commandName3.py
                commandName4.py

        Args:
        action
            Action to perform on extensions.
        exclude
            The list of extensions name that should be excluded from loading.
        """

        # Dictionary for storing errors
        errors = []

        # Gets all extensions and also log it
        path = pathlib.Path(InternalConstants.EXTENSIONS_PATH)
        extension_paths = list(path.glob("**/[!_]*.py"))

        # Goes through each extension to perform action
        for extension_path in extension_paths:
            # Removes .py and replaces "/" with "."
            extension = str(extension_path).replace("/", ".")[:-3]

            # Check if extension is in ignore list
            if exclude and extension in exclude:
                continue

            # Check if extension is in include list
            if include_only and extension not in include_only:
                continue

            # Tries to perform action on the extension
            try:
                match action:
                    case ExtensionActions.LOAD:
                        await self.load_extension(extension)
                        log.info("%s succesfully loaded!", extension)
                    case ExtensionActions.RELOAD:
                        await self.reload_extension(extension)
                        log.info("%s succesfully reloaded!", extension)
                    case ExtensionActions.UNLOAD:
                        await self.unload_extension(extension)
                        log.info("%s succesfully unloaded!", extension)
                    case _:
                        log.error(
                            "Invalid action to perform over extension: %s", action
                        )

            # If action fails
            except Exception as err:  # pylint: disable=broad-exception-caught
                log.critical("Error while %sing - %s.", action, err)
                errors.append(ExtensionError(extension, err.args))

        return len(errors) == 0, errors

    async def load_all_extensions(
        self, exclude: ExtensionsList | None = None
    ) -> ExtensionUpdateResponse:
        """Abstracted method to load all extensions.

        Args:
        exclude
            The list of extensions that needs to be excluded from loading.
        """
        return await self._manage_all_extensions(ExtensionActions.LOAD, exclude)

    async def reload_all_extensions(
        self, exclude: ExtensionsList | None = None
    ) -> ExtensionUpdateResponse:
        """Abstracted method to reload all extensions.

        Args:
        exclude
            The list of extensions that needs to be excluded from reloading.
        """
        return await self._manage_all_extensions(ExtensionActions.RELOAD, exclude)

    async def unload_all_extensions(
        self, exclude: ExtensionsList | None = None
    ) -> ExtensionUpdateResponse:
        """Abstracted method to unload all extensions.

        Args:
        exclude
            The list of extensions that needs to be excluded from unloading.
        """
        return await self._manage_all_extensions(ExtensionActions.UNLOAD, exclude)

    async def load_extensions(
        self, extensions: ExtensionsList
    ) -> ExtensionUpdateResponse:
        """Abstracted method to load one or more extensions.

        Args:
        extensions
            The list of extensions that needs to be loaded.
        """
        return await self._manage_all_extensions(
            ExtensionActions.LOAD,
            include_only=extensions,
        )

    async def reload_extensions(
        self, extensions: ExtensionsList
    ) -> ExtensionUpdateResponse:
        """Abstracted method to reload one or more extensions.

        Args:
        extensions
            The list of extensions that needs to be reloaded.
        """
        return await self._manage_all_extensions(
            ExtensionActions.RELOAD,
            include_only=extensions,
        )

    async def unload_extensions(
        self, extensions: ExtensionsList
    ) -> ExtensionUpdateResponse:
        """Abstracted method to unload one or more extensions.

        Args:
        extensions
            The list of extensions that needs to be unloaded.
        """
        return await self._manage_all_extensions(
            ExtensionActions.UNLOAD,
            include_only=extensions,
        )
