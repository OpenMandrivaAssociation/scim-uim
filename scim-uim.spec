%define version   0.2.0

%define scim_version   1.4.1
%define uim_version    1.5.0

%define libname_orig lib%{name}
%define libname %mklibname %{name} 0

Name:      scim-uim
Summary:   A wrapper for uim
Version:   %{version}
Release:   %mkrel 4
Group:     System/Internationalization
License:   GPLv2+
URL:       http://www.scim-im.org/
Source0:   %{name}-%{version}.tar.gz
Patch1: scim-uim-0.2.0-uim-1.5.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:        scim >= %{scim_version}
Requires:        uim >= %{uim_version}
BuildRequires:   scim-devel >= %{scim_version}
BuildRequires:   uim-devel >= %{uim_version}
BuildRequires:   automake
BuildRequires:   m17n-lib-devel
Obsoletes:	%{libname}

%description
A wrapper for uim.

%prep
%setup -q
%patch1 -p1

%build
./bootstrap
%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove unneeded files
rm -f %{buildroot}%scim_plugins_dir/*/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING
%{_datadir}/scim/icons/*
%scim_plugins_dir/IMEngine/*.so
