%define orig_name qca9377

Name: firmware-qca9377
Version: 3_2.0.4
Release: alt1

Packager: Pavel Nakonechnyi <zorg@altlinux.org>

Summary: Microcode for qca9377
License: GPL
Group: System/Kernel and hardware

Source0: %{orig_name}-%version.tar

BuildArch: noarch

%description
The microcode data for QCA9377.

%prep
%setup -q -n %orig_name-%version

%install
mkdir -p %buildroot/{etc,lib}
cp -a etc/* %buildroot/etc/
cp -a lib/* %buildroot/lib/

%files
/lib/firmware/*
/etc/bluetooth/*

%changelog
* Tue Oct 27 2020 Pavel Nakonechnyi <zorg@altlinux.org> 3_2.0.4-alt1
- updated to 2.0.4 version

* Thu Dec 26 2019 Pavel Nakonechnyi <zorg@altlinux.org> 3_2.0.3-alt1
- updated to use NXP mirror

* Sun Jul 07 2019 Pavel Nakonechnyi <zorg@altlinux.org> 3-alt1.20180927
- initial build of QCA9377 firmware
