%define version   0.2.0
%define release   %mkrel 2

%define scim_version   1.4.1
%define uim_version    1.1.0

%define libname_orig lib%{name}
%define libname %mklibname %{name} 0

Name:      scim-uim
Summary:   A wrapper for uim
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPL
URL:       http://www.scim-im.org/
Source0:   %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:        %{libname} = %{version}-%{release}
Requires:        scim >= %{scim_version}
Requires:        uim >= %{uim_version}
BuildRequires:   scim-devel >= %{scim_version}
BuildRequires:   libuim-devel >= %{uim_version}
BuildRequires:   automake
BuildRequires:   m17n-lib-devel

%description
A wrapper for uim.


%package -n %{libname}
Summary:    Scim-uim library
Group:      System/Internationalization
Provides:   %{libname_orig} = %{version}-%{release}

%description -n %{libname}
Scim-uim library.


%prep
%setup -q

%build
./bootstrap
%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove unneeded files
rm -f %{buildroot}/%{_libdir}/scim-1.0/*/*/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS COPYING
%{_datadir}/scim/icons/*

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/scim-1.0/*/IMEngine/*.so
