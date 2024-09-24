%global commit0 29ec3577e52a50f876440c81267f609575c5161e
%global date 20240425
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
#global tag %{version}

%global real_name xone

Name:           %{real_name}-kmod-common
Version:        0.3%{!?tag:^%{date}git%{shortcommit0}}
Release:        6%{?dist}
Summary:        Linux kernel driver for Xbox One and Xbox Series X|S accessories common files
License:        GPLv2
URL:            https://github.com/medusalix/%{real_name}
BuildArch:      noarch

%if 0%{?tag:1}
Source0:        %{url}/archive/v%{version}.tar.gz#/xone-%{version}.tar.gz
%else
Source0:        %{url}/archive/%{commit0}.tar.gz#/xone-%{shortcommit0}.tar.gz
%endif

# Windows driver and firmware file:
Source1:        http://download.windowsupdate.com/c/msdownload/update/driver/drvs/2017/07/1cd6a87c-623f-4407-a52d-c31be49e925c_e19f60808bdcbfbd3c3df6be3e71ffc52e43261e.cab

BuildRequires:  cabextract
# UDev rule location (_udevrulesdir) and systemd macros:
BuildRequires:  systemd-rpm-macros

Requires:       wireless-regdb
Requires:       %{real_name}-kmod = %{?epoch:%{epoch}:}%{version}
Provides:       %{real_name}-kmod-common = %{?epoch:%{epoch}:}%{version}

%description
Linux kernel driver for Xbox One and Xbox Series X|S accessories common files.
 
%prep
%if 0%{?tag:1}
%autosetup -p1 -n xone-%{version}
%else
%autosetup -p1 -n xone-%{commit0}
%endif

# Firmware:
cabextract -F FW_ACC_00U.bin %{SOURCE1}

%install
mkdir -p %{buildroot}%{_udevrulesdir}
mkdir -p %{buildroot}%{_prefix}/lib/modprobe.d/

# Blacklist:
install -p -m 0644 install/modprobe.conf %{buildroot}%{_prefix}/lib/modprobe.d/xone.conf

# Firmware:
install -p -m 0644 -D FW_ACC_00U.bin %{buildroot}%{_prefix}/lib/firmware/xow_dongle.bin

%files
%license LICENSE
%doc README.md
%{_prefix}/lib/modprobe.d/%{real_name}.conf
%{_prefix}/lib/firmware/xow_dongle.bin

%changelog
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
