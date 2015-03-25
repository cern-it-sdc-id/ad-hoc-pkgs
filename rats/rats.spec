Name:           rats
Version:        2.4
Release:        1%{?dist}
Summary:        Rough Auditing Tool For Security
Group:          Development/Tools
License:        GPLv2
URL:            https://rough-auditing-tool-for-security.googlecode.com
# wget "https://rough-auditing-tool-for-security.googlecode.com/files/rats-2.4.tgz" -O "rats-2.4.tgz"
Source0:        %{name}-%{version}.tgz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  expat-devel 

%description
A tool for scanning C, C++, Perl, PHP, Python (and soon Ruby) source code
and flagging common security related programming errors

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
make clean

%prep
%setup -q

%build
%configure --prefix=/usr --datadir=%{_datadir}/rats
make %{?_smp_mflags}

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
mkdir -p %{buildroot}/{%{_datadir}/rats,%{_bindir},%{_mandir}/man1}
install -c rats %{buildroot}/%{_bindir}
install -c -m644 *.xml %{buildroot}/%{_datadir}/rats
install -c -m644 *.1 %{buildroot}/%{_mandir}/man1

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%dir %{_datadir}/rats
%doc COPYING 
%doc README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/rats/*
%{_mandir}/man1/*

%changelog
* Wed Mar 25 2015 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 2.4-1
- First version of the packaging

