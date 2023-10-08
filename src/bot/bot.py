"""Subclasses the bot."""
from pathlib import Path
from logging import getLogger
from time import time
from discord.ext import commands


class Bot(commands.Bot):
    """Subclass of commands.Bot with some extra attributes and methods."""

    def __init__(self, command_prefix=..., help_command=..., **options):
        super().__init__(command_prefix, help_command, **options)
        self.logger = getLogger(__package__)
        self.logger.debug("Starting bot.")
        self.load_all_extensions()
        self.start_time = round(time())

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        """Fires when bot is ready."""
        print(f"{self.user} ready!")
        self.logger.info("Bot is ready.")

    def _manage_all_extensions(
        self,
        action: str,
        exclude: list[str] = None,
    ) -> (bool, {}):
        """Manage all extensions from ext folder

        Parameters
        -----------
        `exclude ([str])`:
        The list of extensions that should be excluded from loading.

        Returns
        --------
        `was_success (boolean)`:
        Specifies whether loading was successful or not.
        """

        # Replaces None with an empty list
        # Cant add in default parameter value (W0102)
        if exclude is None:
            exclude = []

        # Dictionary for storing errors
        errors = {}

        # Gets all extensions and also log it
        path = Path("bot/exts/")
        extensions = list(path.glob("**/[!_]*.py"))
        self.logger.debug("%sing %ss", action, extensions)

        # Goes through each extension to perform action
        for extension in extensions:
            # Removes .py and replaces "/" with "."
            extension = str(extension).replace("/", ".")[:-3]

            # Check if extension is in ignore list
            if extension in exclude:
                continue

            # Tries to perform action on the extension
            try:
                match action:
                    case "load":
                        self.load_extension(extension)
                    case "reload":
                        self.reload_extension(extension)
                    case "unload":
                        self.unload_extension(extension)
                    case _:
                        self.logger.critical("Invalid action: {action}")
                self.logger.info("%s %sed.", extension, action)

            # If action fails
            except Exception as err:  # pylint: disable=broad-exception-caught
                self.logger.error("%sing - %s.", action, err)
                errors[extension] = err

        return len(errors) == 0, errors

    def load_all_extensions(self, exclude: list[str] = None) -> (bool, {}):
        """Load all extension from ext folder

        Parameters
        -----------
        `exclude ([str])`:
        The list of extensions that should be excluded from loading.

        Returns
        --------
        `was_success (boolean)`:
        Specifies whether loading was successful or not.
        """
        return self._manage_all_extensions("load", exclude)

    def reload_all_extensions(self, exclude: list[str] = None) -> (bool, {}):
        """Reload all extension from ext folder

        Parameters
        -----------
        `exclude ([str])`:
        The list of extensions that should be excluded from reloading.

        Returns
        --------
        `was_success (boolean)`:
        Specifies whether reloading was successful or not.
        """

        return self._manage_all_extensions("reload", exclude)

    def unload_all_extensions(self, exclude: list[str] = None) -> (bool, {}):
        """Unload all extension from ext folder

        Parameters
        -----------
        `exclude ([str])`:
        The list of extensions that should be excluding from unloading.

        Returns
        --------
        `was_sucess (boolean)`:
        Specifies whether unloading was successful or not.
        """

        return self._manage_all_extensions("unload", exclude)
