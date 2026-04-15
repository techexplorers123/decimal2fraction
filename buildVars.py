# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

from site_scons.site_tools.NVDATool.typings import (
    AddonInfo,
    BrailleTables,
    SymbolDictionaries,
    SpeechDictionaries,
)

# Since some strings in `addon_info` are translatable,
# we need to include them in the .po files.
# Gettext recognizes only strings given as parameters to the `_` function.
# To avoid initializing translations in this module we simply import a "fake" `_` function
# which returns whatever is given to it as an argument.
from site_scons.site_tools.NVDATool.utils import _


# Add-on information variables
addon_info = AddonInfo(
    # add-on Name/identifier, internal for NVDA
    addon_name="decimal2fraction",
    # Add-on summary/title, usually the user visible name of the add-on
    # Translators: Summary/title for this add-on
    # to be shown on installation and add-on information found in add-on store
    addon_summary=_("decimal to fraction convertor"),
    # Add-on description
    # Translators: Long description to be shown for this add-on on add-on information from add-on store
    addon_description=_(
        """a simple addon to convert decimal numbers to fraction. e.g., 0.5 will become 1/2.
I've created this addon mainly for myself to easily convert decimal results from the windows calculator to fractions since there is no way to do that on the windows calculater app.
feal free to reach out if you face any problems with this addon, i will try my best to help.
o, and also feal free to copy, modify, and distribute this addon to your hards contempt.
keyboard shortcuts:
* alt+NVDA+s: converts the selected number in to fraction.
* alt+NVDA+a: converts the number on the clipboard to fraction.
* pressing eather shortcuts twice will copy the result to the clipboard.
* all the shortcuts can be customized from the "input gestures" menu."""
    ),
    # version
    addon_version="1.4",
    # Brief changelog for this version
    # Translators: what's new content for the add-on version to be shown in the add-on store
    addon_changelog=_("""updated to support nvda 2026"""),
    # Author(s)
    addon_author="tech <admin@techclub.co.in>",
    # URL for the add-on documentation support
    addon_url="https://github.com/techexplorers123/decimal2fraction",
    # URL for the add-on repository where the source code can be found
    addon_sourceURL="https://github.com/techexplorers123/decimal2fraction",
    # Documentation file name
    addon_docFileName="readme.md",
    # Minimum NVDA version supported (e.g. "2019.3.0", minor version is optional)
    addon_minimumNVDAVersion="2019.3.0",
    # Last NVDA version supported/tested (e.g. "2024.4.0", ideally more recent than minimum version)
    addon_lastTestedNVDAVersion="2026.1.11",
    # Add-on update channel (default is None, denoting stable releases,
    # and for development releases, use "dev".)
    # Do not change unless you know what you are doing!
    addon_updateChannel=None,
    # Add-on license such as GPL 2
    addon_license="GPLv2",
    # URL for the license document the ad-on is licensed under
    addon_licenseURL="https://github.com/techexplorers123/decimal2fraction/LICENSE",
)

# Define the python files that are the sources of your add-on.
# You can either list every file (using ""/") as a path separator,
# or use glob expressions.
# For example to include all files with a ".py" extension from the "globalPlugins" dir of your add-on
# the list can be written as follows:
# pythonSources = ["addon/globalPlugins/*.py"]
# For more information on SCons Glob expressions please take a look at:
# https://scons.org/doc/production/HTML/scons-user/apd.html
import os

pythonSources = [
    os.path.join("addon", "GlobalPlugins", "*.py"),
]


# Files that contain strings for translation. Usually your python sources
i18nSources: list[str] = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
# You can either list every file (using ""/") as a path separator,
# or use glob expressions.
excludedFiles: list[str] = []

# Base language for the NVDA add-on
# If your add-on is written in a language other than english, modify this variable.
# For example, set baseLanguage to "es" if your add-on is primarily written in spanish.
# You must also edit .gitignore file to specify base language files to be ignored.
baseLanguage: str = "en"

# Markdown extensions for add-on documentation
# Most add-ons do not require additional Markdown extensions.
# If you need to add support for markup such as tables, fill out the below list.
# Extensions string must be of the form "markdown.extensions.extensionName"
# e.g. "markdown.extensions.tables" to add tables.
markdownExtensions: list[str] = []

# Custom braille translation tables
# If your add-on includes custom braille tables (most will not), fill out this dictionary.
# Each key is a dictionary named according to braille table file name,
# with keys inside recording the following attributes:
# displayName (name of the table shown to users and translatable),
# contracted (contracted (True) or uncontracted (False) braille code),
# output (shown in output table list),
# input (shown in input table list).
brailleTables: BrailleTables = {}

# Custom speech symbol dictionaries
# Symbol dictionary files reside in the locale folder, e.g. `locale\en`, and are named `symbols-<name>.dic`.
# If your add-on includes custom speech symbol dictionaries (most will not), fill out this dictionary.
# Each key is the name of the dictionary,
# with keys inside recording the following attributes:
# displayName (name of the speech dictionary shown to users and translatable),
# mandatory (True when always enabled, False when not).
symbolDictionaries: SymbolDictionaries = {}

# Custom speech dictionaries (distinct from symbol dictionaries above)
# Speech dictionary files reside in the speechDicts folder and are named `name.dic`.
# If your add-on includes custom speech (pronunciation) dictionaries (most will not), fill out this dictionary.
# Each key is the name of the dictionary,
# with keys inside recording the following attributes:
# displayName (name of the speech dictionary shown to users and translatable),
# mandatory (True when always enabled, False when not).
speechDictionaries: SpeechDictionaries = {}
