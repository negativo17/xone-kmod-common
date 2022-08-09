%global commit0 8311a25f2b4e69b7a3f8133b884cede065b253cc
%global date 20220606
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global tag %{version}

%global real_name xone

Name:           %{real_name}-kmod-common
Version:        0.3
Release:        1%{?dist}
Summary:        Linux kernel driver for Xbox One and Xbox Series X|S accessories common files
License:        GPLv2
URL:            https://github.com/medusalix/%{real_name}
BuildArch:      noarch

%if 0%{?tag:1}
Source0:        %{url}/archive/v%{version}.tar.gz#/%{real_name}-%{version}.tar.gz
%else
Source0:        %{url}/archive/%{commit0}.tar.gz#/%{real_name}-%{shortcommit0}.tar.gz
%endif
# Windows driver and firmware file:
Source1:        http://download.windowsupdate.com/c/msdownload/update/driver/drvs/2017/07/1cd6a87c-623f-4407-a52d-c31be49e925c_e19f60808bdcbfbd3c3df6be3e71ffc52e43261e.cab

BuildRequires:  cabextract
# UDev rule location (_udevrulesdir) and systemd macros:
BuildRequires:  systemd-rpm-macros

Requires:       %{real_name}-kmod = %{?epoch:%{epoch}:}%{version}
Provides:       %{real_name}-kmod-common = %{?epoch:%{epoch}:}%{version}

%description
Linux kernel driver for Xbox One and Xbox Series X|S accessories common files.
 
%prep
%if 0%{?tag:1}
%autosetup -p1 -n %{real_name}-%{version}
%else
%autosetup -p1 -n %{real_name}-%{commit0}
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
* Tue Aug 9 2022 Simone Caronni <negativo17@gmail.com> - 0.3-1
- First build.
