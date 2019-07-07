%define orig_name qca9377
%define orig_timestamp 20180927

Name: firmware-qca9377
Version: 3
Release: alt1.%{orig_timestamp}

Packager: Pavel Nakonechnyi <zorg@altlinux.org>

Summary: Microcode for qca9377
License: GPL
Group: System/Kernel and hardware

Source0: %{orig_name}-%{orig_timestamp}.tar

BuildArch: noarch

%description
The microcode data for QCA9377.

%prep
%setup -q -n %orig_name-%{orig_timestamp}

%install
mkdir -p %buildroot/lib/firmware/wlan
mv *.bin %buildroot/lib/firmware/
mv wlan/* %buildroot/lib/firmware/wlan/

%files
%dir /lib/firmware/wlan
/lib/firmware/*

%changelog
* Sun Jul 07 2019 Pavel Nakonechnyi <zorg@altlinux.org> 3-alt1.20180927
- initial build of QCA9377 firmware
