		# -*- coding: UTF-8 -*-

# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext (please don't change)
_ = lambda x : x

# Add-on information variables
addon_info = {
	# for previously unpublished addons, please follow the community guidelines at:
	# https://bitbucket.org/nvdaaddonteam/todo/raw/master/guideLines.txt
	# add-on Name, internal for nvda
	"addon_name" : "decimal2fraction",
	# Add-on summary, usually the user visible name of the addon.
	# Translators: Summary for this add-on to be shown on installation and add-on information.
	"addon_summary" : _("decimal to fraction convertor"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on add-on information from add-ons manager
	"addon_description" : _("""a simple addon to convert decimal numbers to fraction. e.g., 0.5 will become 1/2.
I've created this addon mainly for myself to easily convert decimal results from the windows calculator to fractions since there is no way to do that on the windows calculater app.
feal free to reach out if you face any problems with this addon, i will try my best to help.
o, and also feal free to copy, modify, and distribute this addon to your hards contempt.
keyboard shortcuts:
* alt+NVDA+s: converts the selected number in to fraction.
* alt+NVDA+a: converts the number on the clipboard to fraction.
* pressing eather shortcuts twice will copy the result to the clipboard.
* all the shortcuts can be customized from the "input gestures" menu.""""""),
	# version
	"addon_version" : "1.0",
	# Author(s)
	"addon_author" : u"tech <admin@techclub.site>",
	# URL for the add-on documentation support
	"addon_url" : "https://github.com/techexplorers123/decimal2fraction",
	# Minimum NVDA version supported (e.g. "2018.3.0", minor version is optional)
	"addon_minimumNVDAVersion" : "2019.3.0",
	# Last NVDA version supported/tested (e.g. "2018.4.0", ideally more recent than minimum version)
	"addon_lastTestedNVDAVersion" : "2024.1.0",
	# Add-on update channel (default is None, denoting stable releases, and for development releases, use "dev"; do not change unless you know what you are doing)
	"addon_updateChannel" : None,
}


import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [os.path.join("addon", "GlobalPlugins", "*.py"), ]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []
