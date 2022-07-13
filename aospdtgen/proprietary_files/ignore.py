#
# Copyright (C) 2022 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

from pathlib import Path
import re
from sebaubuntu_libs.libstring import removeprefix

IGNORE_BINARIES = [
	"acpi",
	"awk",
	"base64",
	"basename",
	"blockdev",
	"btconfig",
	"cal",
	"cat",
	"chcon",
	"chgrp",
	"chmod",
	"chown",
	"chroot",
	"chrt",
	"cksum",
	"clear",
	"cmp",
	"comm",
	"cp",
	"cpio",
	"cut",
	"date",
	"dd",
	"df",
	"diff",
	"dirname",
	"dmesg",
	"dos2unix",
	"du",
	"echo",
	"egrep",
	"env",
	"expand",
	"expr",
	"fallocate",
	"false",
	"fgrep",
	"file",
	"find",
	"flock",
	"fmt",
	"free",
	"getenforce",
	"getevent",
	"getprop",
	"grep",
	"groups",
	"gunzip",
	"gzip",
	"head",
	"hostapd_cli",
	"hostname",
	"hwclock",
	"id",
	"ifconfig",
	"inotifyd",
	"insmod",
	"ionice",
	"iorenice",
	"ipacm",
	"kill",
	"killall",
	"ln",
	"load_policy",
	"log",
	"logname",
	"logwrapper",
	"losetup",
	"ls",
	"lsmod",
	"lsof",
	"lspci",
	"lsusb",
	"md5sum",
	"microcom",
	"mkdir",
	"mkfifo",
	"mknod",
	"mkswap",
	"mktemp",
	"modinfo",
	"modprobe",
	"more",
	"mount",
	"mountpoint",
	"mv",
	"netstat",
	"newfs_msdos",
	"nice",
	"nl",
	"nohup",
	"od",
	"paste",
	"patch",
	"pgrep",
	"pidof",
	"pkill",
	"pmap",
	"printenv",
	"printf",
	"ps",
	"pwd",
	"readlink",
	"realpath",
	"renice",
	"restorecon",
	"rm",
	"rmdir",
	"rmmod",
	"runcon",
	"sed",
	"sendevent",
	"seq",
	"setenforce",
	"setprop",
	"setsid",
	"sh",
	"sha1sum",
	"sha224sum",
	"sha256sum",
	"sha384sum",
	"sha512sum",
	"sleep",
	"sort",
	"split",
	"start",
	"stat",
	"stop",
	"strings",
	"stty",
	"swapoff",
	"swapon",
	"sync",
	"sysctl",
	"tac",
	"tail",
	"tar",
	"taskset",
	"tee",
	"time",
	"timeout",
	"toolbox",
	"top",
	"touch",
	"toybox_vendor",
	"tr",
	"true",
	"truncate",
	"tty",
	"ulimit",
	"umount",
	"uname",
	"uniq",
	"unix2dos",
	"uptime",
	"usleep",
	"uudecode",
	"uuencode",
	"vmstat",
	"vndservice",
	"vndservicemanager",
	"wc",
	"which",
	"whoami",
	"wpa_cli",
	"xargs",
	"xxd",
	"yes",
	"zcat"
]

"""
These shared libs are provided by AOSP
Source: https://cs.android.com/android/platform/superproject
"""
IGNORE_SHARED_LIBS = [
	"audio.a2dp.default.so",
	"hidl.tests.vendor@1.0.so",
	"hidl.tests.vendor@1.1.so",
	"ld-android.so",
	"libaacextractor.so",
	"libaaudioservice.so",
	"libaaudio.so",
	"libadbconnectiond.so",
	"libadbconnection.so",
	"libadf.so",
	"libamrextractor.so",
	"libandroidfw.so",
	"libandroid_net.so",
	"libandroid_runtime.so",
	"libandroid_servers.so",
	"libandroid.so",
	"libappfuse.so",
	"libart-compiler.so",
	"libartd-compiler.so",
	"libartd-dexlayout.so",
	"libart-dexlayout.so",
	"libart-disassembler.so",
	"libartd.so",
	"libart.so",
	"libasyncio.so",
	"libaudioclient.so",
	"libaudioeffect_jni.so",
	"libaudioflinger.so",
	"libaudiohal@2.0.so",
	"libaudiohal_deathhandler.so",
	"libaudiohal.so",
	"libaudiomanager.so",
	"libaudiopolicyenginedefault.so",
	"libaudiopolicymanagerdefault.so",
	"libaudiopolicymanager.so",
	"libaudiopolicyservice.so",
	"libaudiopreprocessing.so",
	"libaudioprocessing.so",
	"libaudioroute.so",
	"libaudiospdif.so",
	"libaudioutils.so",
	"libavservices_minijail.so",
	"libavservices_minijail_vendor.so",
	"libbacktrace.so",
	"libbase.so",
	"libbcc.so",
	"libbcinfo.so",
	"libbinder_ndk.so",
	"libbinder.so",
	"libbinderthreadstate.so",
	"libbinderwrapper.so",
	"libblas.so",
	"libbluetooth-binder.so",
	"libbluetooth_jni.so",
	"libbluetooth.so",
	"libbootanimation.so",
	"libbrillo-binder.so",
	"libbrillo.so",
	"libbrillo-stream.so",
	"libbrotli.so",
	"libbufferhubqueue.so",
	"libbufferhub.so",
	"libbundlewrapper.so",
	"libbz.so",
	"libcamera2ndk.so",
	"libcamera_client.so",
	"libcamera_metadata.so",
	"libcameraservice.so",
	"libcap.so",
	"libcgrouprc.so",
	"libchrome.so",
	"libclang_rt.asan-aarch64-android.so",
	"libclang_rt.asan-arm-android.so",
	"libclang_rt.asan-i686-android.so",
	"libclang_rt.asan-mips64-android.so",
	"libclang_rt.asan-mips-android.so",
	"libclang_rt.asan-x86_64-android.so",
	"libclang_rt.hwasan-aarch64-android.so",
	"libclang_rt.scudo-aarch64-android.so",
	"libclang_rt.scudo-arm-android.so",
	"libclang_rt.scudo-i686-android.so",
	"libclang_rt.scudo_minimal-aarch64-android.so",
	"libclang_rt.scudo_minimal-arm-android.so",
	"libclang_rt.scudo_minimal-i686-android.so",
	"libclang_rt.scudo_minimal-x86_64-android.so",
	"libclang_rt.scudo-x86_64-android.so",
	"libclang_rt.ubsan_standalone-aarch64-android.so",
	"libclang_rt.ubsan_standalone-arm-android.so",
	"libclang_rt.ubsan_standalone-i686-android.so",
	"libclang_rt.ubsan_standalone-x86_64-android.so",
	"libcld80211.so",
	"libc_malloc_debug.so",
	"libcn-cbor.so",
	"libcodec2_hidl@1.0.so",
	"libcodec2.so",
	"libcodec2_vndk.so",
	"libcompiler_rt.so",
	"libcrypto.so",
	"libcrypto_utils.so",
	"libc++_shared.so",
	"libc++.so",
	"libc.so",
	"libcups.so",
	"libcurl.so",
	"libcutils.so",
	"libdebuggerd_client.so",
	"libdefcontainer_jni.so",
	"libdexfile.so",
	"libdiskconfig.so",
	"libdisplayservicehidl.so",
	"libdl_android.so",
	"libdl.so",
	"libdng_sdk.so",
	"libdownmix.so",
	"libdrmframework_jni.so",
	"libdrmframework.so",
	"libdrm.so",
	"libdt_fd_forward.so",
	"libdt_socket.so",
	"libdumpstateaidl.so",
	"libdumpstateutil.so",
	"libeffectproxy.so",
	"libeffectsconfig.so",
	"libeffects.so",
	"libEGL.so",
	"libETC1.so",
	"libevent.so",
	"libexif.so",
	"libexpat.so",
	"libext2_blkid.so",
	"libext2_com_err.so",
	"libext2_e2p.so",
	"libext2fs.so",
	"libext2_misc.so",
	"libext2_quota.so",
	"libext2_uuid.so",
	"libext4_utils.so",
	"libf2fs_sparseblock.so",
	"libFFTEm.so",
	"libfilterfw.so",
	"libfilterpack_imageproc.so",
	"libflacextractor.so",
	"libfmq.so",
	"libframesequence.so",
	"libft2.so",
	"libfwdlockengine.so",
	"libgatekeeper.so",
	"libgiftranscode.so",
	"libGLESv1_CM.so",
	"libGLESv2.so",
	"libGLESv3.so",
	"libgraphicsenv.so",
	"libgtest_prod.so",
	"libgui_vendor.so",
	"libgui.so",
	"libhardware_legacy.so",
	"libhardware.so",
	"libharfbuzz_ng.so",
	"libheif.so",
	"libhidcommand_jni.so",
	"libhidlallocatorutils.so",
	"libhidlbase.so",
	"libhidlcache.so",
	"libhidl-gen-hash.so",
	"libhidl-gen-utils.so",
	"libhidlmemory.so",
	"libhidltransport.so",
	"libhwbinder_noltopgo.so",
	"libhwbinder.so",
	"libhwc2on1adapter.so",
	"libhwui.so",
	"libicui18n.so",
	"libicuuc.so",
	"libimg_utils.so",
	"libincident.so",
	"libinputflinger.so",
	"libinputservice.so",
	"libinput.so",
	"libion.so",
	"libiprouteutil.so",
	"libjavacore.so",
	"libjavacrypto.so",
	"libjdwp.so",
	"libjnigraphics.so",
	"libjni_pacprocessor.so",
	"libjpeg.so",
	"libjsoncpp.so",
	"libkeymaster4support.so",
	"libkeymaster_messages.so",
	"libkeymaster_portable.so",
	"libkeystore_aidl.so",
	"libkeystore_binder.so",
	"libkeystore-engine.so",
	"libkeystore_parcelables.so",
	"libkeyutils.so",
	"liblayers_proto.so",
	"libldacBT_abr.so",
	"libldacBT_enc.so",
	"libldnhncr.so",
	"libLLVM_android.so",
	"liblog.so",
	"liblogwrap.so",
	"liblshal.so",
	"liblz4.so",
	"liblzma.so",
	"libmdnssd.so",
	"libmediadrm.so",
	"libmediaextractorservice.so",
	"libmedia_helper.so",
	"libmedia_jni.so",
	"libmedialogservice.so",
	"libmediametrics.so",
	"libmediandk.so",
	"libmedia_omx.so",
	"libmediaplayerservice.so",
	"libmedia.so",
	"libmediautils.so",
	"libmemtrack.so",
	"libmemunreachable.so",
	"libmetricslogger.so",
	"libmidiextractor.so",
	"libminijail.so",
	"libminikin.so",
	"libmkbootimg_abi_check.so",
	"libmkvextractor.so",
	"libmp3extractor.so",
	"libmp4extractor.so",
	"libmpeg2extractor.so",
	"libm.so",
	"libmtp.so",
	"libnativehelper.so",
	"libnativewindow.so",
	"libnbaio_mono.so",
	"libnbaio.so",
	"libnblog.so",
	"libnetd_client.so",
	"libnetdutils.so",
	"libnetlink.so",
	"libnetutils.so",
	"libneuralnetworks.so",
	"libnfc_nci_jni.so",
	"libnfc-nci.so",
	"libnl.so",
	"libnpt.so",
	"liboggextractor.so",
	"libopenjdkd.so",
	"libopenjdkjvmd.so",
	"libopenjdkjvm.so",
	"libopenjdkjvmtid.so",
	"libopenjdkjvmti.so",
	"libopenjdk.so",
	"libOpenMAXAL.so",
	"libOpenSLES.so",
	"libopus.so",
	"libpackagelistparser.so",
	"libpagemap.so",
	"libpcap.so",
	"libpcre2.so",
	"libpcrecpp.so",
	"libpdfium.so",
	"libpdx_default_transport.so",
	"libpiex.so",
	"libpixelflinger.so",
	"libpng.so",
	"libpowermanager.so",
	"libpower.so",
	"libprintspooler_jni.so",
	"libprocessgroup.so",
	"libprocinfo.so",
	"libprotobuf-cpp-full.so",
	"libprotobuf-cpp-lite.so",
	"libprotoutil.so",
	"libpuresoftkeymasterdevice.so",
	"libqtaguid.so",
	"libradio_metadata.so",
	"libreference-ril.so",
	"libresourcemanagerservice.so",
	"libreverbwrapper.so",
	"libril.so",
	"librilutils.so",
	"libRSCacheDir.so",
	"libRScpp.so",
	"libRSCpuRef.so",
	"libRSDriver.so",
	"libRS_internal.so",
	"librs_jni.so",
	"libRS.so",
	"librtp_jni.so",
	"libschedulerservicehidl.so",
	"libselinux.so",
	"libsensorservicehidl.so",
	"libsensorservice.so",
	"libsensor.so",
	"libsepol.so",
	"libservices.so",
	"libsigchain.so",
	"libsoftkeymasterdevice.so",
	"libsonic.so",
	"libsonivox.so",
	"libsoundpool.so",
	"libsoundtriggerservice.so",
	"libsoundtrigger.so",
	"libsparse.so",
	"libspeexresampler.so",
	"libsqlite.so",
	"libssl.so",
	"libstagefright_amrnb_common.so",
	"libstagefright_bufferpool@2.0.so",
	"libstagefright_bufferqueue_helper.so",
	"libstagefright_enc_common.so",
	"libstagefright_flacdec.so",
	"libstagefright_foundation.so",
	"libstagefright_httplive.so",
	"libstagefright_http_support.so",
	"libstagefright_omx.so",
	"libstagefright_omx_utils.so",
	"libstagefright.so",
	"libstagefright_soft_aacdec.so",
	"libstagefright_soft_aacenc.so",
	"libstagefright_soft_amrdec.so",
	"libstagefright_soft_amrnbenc.so",
	"libstagefright_soft_amrwbenc.so",
	"libstagefright_soft_avcdec.so",
	"libstagefright_soft_avcenc.so",
	"libstagefright_soft_flacdec.so",
	"libstagefright_soft_flacenc.so",
	"libstagefright_soft_g711dec.so",
	"libstagefright_soft_gsmdec.so",
	"libstagefright_soft_hevcdec.so",
	"libstagefright_soft_mp3dec.so",
	"libstagefright_soft_mpeg2dec.so",
	"libstagefright_soft_mpeg4dec.so",
	"libstagefright_soft_mpeg4enc.so",
	"libstagefright_softomx.so",
	"libstagefright_soft_opusdec.so",
	"libstagefright_soft_rawdec.so",
	"libstagefright_soft_vorbisdec.so",
	"libstagefright_soft_vpxdec.so",
	"libstagefright_soft_vpxenc.so",
	"libstagefright_xmlparser.so",
	"libstatslog.so",
	"libstdc++.so",
	"libsurfaceflinger.so",
	"libsuspend.so",
	"libsync.so",
	"libsysutils.so",
	"libtextclassifier_hash.so",
	"libtextclassifier.so",
	"libtinyalsa.so",
	"libtinycompress.so",
	"libtinyxml2.so",
	"libtombstoned_client.so",
	"libui.so",
	"libunwind.so",
	"libunwindstack.so",
	"libusbhost.so",
	"libutilscallstack.so",
	"libutils.so",
	"libvintf.so",
	"libvisualizer.so",
	"libvixl-arm64.so",
	"libvixl-arm.so",
	"libvndksupport.so",
	"libvorbisidec.so",
	"libvulkan.so",
	"libwavextractor.so",
	"libwebrtc_audio_preprocessing.so",
	"libwebviewchromium_loader.so",
	"libwebviewchromium_plat_support.so",
	"libwfds.so",
	"libwifikeystorehal.so",
	"libwifi-service.so",
	"libwifi-system-iface.so",
	"libwifi-system.so",
	"libwilhelm.so",
	"libxml2.so",
	"libyuv.so",
	"libziparchive.so",
	"libz.so",
]

IGNORE_FILENAMES = [
	# Property files
	"build.prop",
	"default.prop",

	# config.fs
	"fs_config_dirs",
	"fs_config_files",
	"group",

	# Licenses
	"NOTICE.xml.gz",
	"NOTICE_GPL.html.gz",
	"NOTICE_GPL.xml.gz",
	"passwd",

	# Recovery patch
	"recovery-from-boot.p",

	# Ueventd
	"ueventd.rc",

	# Partition symlinks
	"odm",
	"product",
	"system",
	"system_ext",
	"vendor",
]

IGNORE_EXTENSIONS = [
	# Apps's odex/vdex
	"odex",
	"vdex",
]

IGNORE_FOLDERS = [
	# Hostapd config
	"etc/hostapd",

	# Device init scripts
	"etc/init/hw",

	# Permissions
	"etc/permissions",

	# SELinux
	"etc/selinux",

	# Kernel modules
	"lib/modules",

	# ADSP tests
	"lib/rfsa/adsp/tests",

	# RRO overlays
	"overlay",

	# RFS symlinks
	"rfs",
]

IGNORE_PATHS = [
	# VINTF
	"etc/vintf/compatibility_matrix.xml",
	"etc/vintf/manifest.xml",
]

IGNORE_PATTERNS = [re.compile(pattern) for pattern in [
	# Shell scripts
	"bin/.*\.sh",

	# TODO: Find a cleaner way to exclude AOSP interfaces libs,
	# We're currently excluding all AOSP interfaces libs except impl
	"^(?!lib(64)?/(hw/)?android\..*\..*-impl.so)lib(64)?/(hw/)?android\..*\..*.so",

	# Versioned libprotobuf library
	"lib(64)?/libprotobuf-cpp-(full|lite)-.*.so",
]]

def is_blob_allowed(file: Path) -> bool:
	"""
	Check if the lib is not in the disallowed list.
	"""
	if file.name in IGNORE_BINARIES:
		return False

	if file.name in IGNORE_SHARED_LIBS:
		return False

	if file.name in IGNORE_FILENAMES:
		return False

	if removeprefix(file.suffix, '.') in IGNORE_EXTENSIONS:
		return False

	for folder in [str(folder) for folder in file.parents]:
		if folder in IGNORE_FOLDERS:
			return False

	if str(file) in IGNORE_PATHS:
		return False

	for pattern in IGNORE_PATTERNS:
		if pattern.match(str(file)):
			return False

	return True
