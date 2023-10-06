"""Subclasses the bot."""
from pathlib import Path
from time import time
from discord.ext import commands


class Bot(commands.Bot):
    """Subclass of commands.Bot with some extra attributes and methods."""

    def __init__(self, command_prefix=..., help_command=..., **options):
        super().__init__(command_prefix, help_command, **options)
        self.load_all_extensions()
        self.start_time = round(time())

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        """Fires when bot is ready."""
        print(f"{self.user} ready!")

    def load_all_extensions(self, exclude: [str] = None) -> (bool, {}):
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

        path = Path("bot/exts/")
        errors = {}
        for extension in path.glob("**/*.py"):
            # Removes .py and replaces "/" with "."
            extension = str(extension).replace("/", ".")[:-3]

            # Ignore __init__ file
            if "__init__" in extension:
                continue

            # Check if extension is ignore list
            if exclude and extension in exclude:
                continue

            # Tries to load extension
            try:
                self.load_extension(extension, store=False)
            except Exception as err:  # pylint: disable=broad-exception-caught
                errors[extension] = err
        print(errors)
        return errors

    def reload_all_extensions(self, exclude: [str] = None) -> (bool, {}):
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

        path = Path("bot/exts/")
        errors = {}
        for extension in path.glob("**/*.py"):
            # Removes .py and replaces "/" with "."
            extension = str(extension).replace("/", ".")[:-3]

            # Ignore __init__ file
            if "__init__" in extension:
                continue

            # Check if extension is ignore list
            if exclude and extension not in exclude:
                continue

            # Tries to reload extension
            try:
                self.reload_extension(extension)
            except Exception as err:  # pylint: disable=broad-exception-caught
                errors[extension] = err
        print(errors)
        return errors

    def unload_all_extensions(self, exclude: [str] = None) -> (bool, {}):
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

        path = Path("bot/exts/")
        errors = {}
        for extension in path.glob("**/*.py"):
            # Removes .py and replaces "/" with "."
            extension = str(extension).replace("/", ".")[:-3]

            # Ignore __init__ file
            if "__init__" in extension:
                continue

            # Check if extension is ignore list
            if exclude and extension not in exclude:
                continue

            # Tries to unload extension
            try:
                self.unload_extension(extension)
            except Exception as err:  # pylint: disable=broad-exception-caught
                errors[extension] = err
        print(errors)
        return errors
