%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}}

Name:           vera++
Version:        1.3.0
Release:        1%{?dist}
Summary:        vera++ tool
Group:          Development/Tools
License:        Boost
URL:            https://bitbucket.org/verateam/ver://bitbucket.org/verateam/vera/wiki/Home 
# wget "https://bitbucket.org/verateam/vera/downloads/vera%2B%2B-1.3.0.tar.gz" -O "vera++-1.3.0.tar.gz"
Source0:        %{name}-%{version}.tar.gz
Patch0:         lua-cmake.patch
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  boost-static
BuildRequires:  tcl-devel


%description
Vera++ is a programmable tool for verification, analysis and transformation of C++ source code.

%clean
rm -rf %{buildroot};
make clean

%prep
%setup -q
%patch0 -p0

%build
%cmake -DVERA_USE_SYSTEM_LUA=OFF -DBoost_NO_BOOST_CMAKE=ON
make %{?_smp_mflags}

%check
ctest -V

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%dir %attr(0755,root,root) %{_exec_prefix}/lib/vera++
%dir %attr(0755,root,root) %{_prefix}/share/vera++
%doc LICENSE_1_0.txt
%doc README.txt
#%{_pkgdocdir}/*
%{_bindir}/vera++
%{_exec_prefix}/lib/vera++/*
%{_mandir}/man1/*
%{_prefix}/share/vera++/*

%changelog
* Wed Mar 25 2015 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 1.3.0-1
- First version of the packaging

