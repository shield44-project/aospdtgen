#
# Copyright (C) 2022 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

from aospdtgen.proprietary_files.section import Section, register_section

class DolbySection(Section):
	name = "Dolby"
	interfaces = [
		"vendor.dolby.hardware.dms",
	]
	libraries = [
		"libdapparamstorage",
		"libdeccfg",
	]
	folders = [
		"etc/dolby",
	]

register_section(DolbySection)
