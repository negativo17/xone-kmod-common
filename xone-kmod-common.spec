%global real_name xone

Name:           %{real_name}-kmod-common
Version:        0.4.5
Release:        1%{?dist}
Summary:        Linux kernel driver for Xbox One and Xbox Series X|S accessories common files
License:        GPLv2
URL:            https://github.com/dlundqvist/xone
BuildArch:      noarch

Source0:        %{url}/archive/v%{version}.tar.gz#/xone-%{version}.tar.gz

# Windows driver and firmware file (firmware/install.sh):
Source1:        http://download.windowsupdate.com/c/msdownload/update/driver/drvs/2017/07/1cd6a87c-623f-4407-a52d-c31be49e925c_e19f60808bdcbfbd3c3df6be3e71ffc52e43261e.cab
Source2:        https://catalog.s.download.windowsupdate.com/d/msdownload/update/driver/drvs/2015/12/20810869_8ce2975a7fbaa06bcfb0d8762a6275a1cf7c1dd3.cab

BuildRequires:  p7zip-plugins
# UDev rule location (_udevrulesdir) and systemd macros:
BuildRequires:  systemd-rpm-macros

Requires:       wireless-regdb
Requires:       %{real_name}-kmod = %{?epoch:%{epoch}:}%{version}
Provides:       %{real_name}-kmod-common = %{?epoch:%{epoch}:}%{version}

%description
Linux kernel driver for Xbox One and Xbox Series X|S accessories common files.
 
%prep
%autosetup -p1 -n xone-%{version}

# Firmware:
7z e %{SOURCE1} FW_ACC_00U.bin
mv FW_ACC_00U.bin xow_dongle.bin
7z e %{SOURCE2} FW_ACC_00U.bin
mv FW_ACC_00U.bin xow_dongle_045e_02e6.bin

%install
mkdir -p %{buildroot}%{_udevrulesdir}
mkdir -p %{buildroot}%{_prefix}/lib/firmware/
mkdir -p %{buildroot}%{_prefix}/lib/modprobe.d/

# Blacklist:
install -p -m 0644 install/modprobe.conf %{buildroot}%{_prefix}/lib/modprobe.d/xone.conf

# Firmware:
install -p -m 0644 xow_dongle*.bin %{buildroot}%{_prefix}/lib/firmware/

%files
%license LICENSE
%doc README.md
%{_prefix}/lib/modprobe.d/%{real_name}.conf
%{_prefix}/lib/firmware/xow_dongle.bin
%{_prefix}/lib/firmware/xow_dongle_045e_02e6.bin

%changelog
* Tue Sep 09 2025 Simone Caronni <negativo17@gmail.com> - 0.4.5-1
- Update to 0.4.5.

* Tue Sep 02 2025 Simone Caronni <negativo17@gmail.com> - 0.4.4-1
- Update to 0.4.4.

* Wed Aug 20 2025 Simone Caronni <negativo17@gmail.com> - 0.4.3-1
- Update to 0.4.3.

* Sun Aug 10 2025 Simone Caronni <negativo17@gmail.com> - 0.4.2-1
- Update to 0.4.2.

* Sun Aug 03 2025 Simone Caronni <negativo17@gmail.com> - 0.4.1-1
- Update to 0.4.1.

* Fri Aug 01 2025 Simone Caronni <negativo17@gmail.com> - 0.3.5-1
- Update to 0.3.5.

* Sat May 10 2025 Simone Caronni <negativo17@gmail.com> - 0.3^20250502git197b160-8
- Update to latest snapshot.
- Add also second firmware.

* Wed Dec 25 2024 Simone Caronni <negativo17@gmail.com> - 0.3^20241223git6b9d59a-7
- Switch to https://github.com/dlundqvist/xone fork.

* Tue Sep 24 2024 Simone Caronni <negativo17@gmail.com> - 0.3^20240425git29ec357-6
- Use new packaging guidelines for snapshots.

* Mon May 13 2024 Simone Caronni <negativo17@gmail.com> - 0.3-5.20240425git29ec357
- Update to latest snapshot.

* Tue Jan 23 2024 Simone Caronni <negativo17@gmail.com> - 0.3-4.20240118giteaa55d0
- Update to latest snapshot.

* Wed Jan 17 2024 Simone Caronni <negativo17@gmail.com> - 0.3-3
- Clean up SPEC file.

* Sat Dec 17 2022 Simone Caronni <negativo17@gmail.com> - 0.3-2
- Kernel module checks for wireless frequency regulatory compliance.

* Tue Aug 9 2022 Simone Caronni <negativo17@gmail.com> - 0.3-1
- First build.
