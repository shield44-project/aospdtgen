#
# Copyright (C) 2022 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

from aospdtgen.proprietary_files.section import Section, register_section

class HealthSection(Section):
	name = "Health"
	interfaces = [
		"android.hardware.health",
	]

register_section(HealthSection)
