Name:          enchant2
Version:       2.2.3
Release:       3%{?snap}%{?dist}
Summary:       An Enchanting Spell Checking Library

License:       LGPLv2+
URL:           https://github.com/AbiWord/enchant
Source0:       https://github.com/AbiWord/enchant/releases/download/v%{version}/enchant-%{version}.tar.gz

BuildRequires: glib2-devel
BuildRequires: aspell-devel
BuildRequires: hunspell-devel
BuildRequires: libvoikko-devel

Provides:      bundled(gnulib)


%description
A library that wraps other spell checking backends.


%package aspell
Summary:       Integration with aspell for libenchant
Requires:      enchant2%{?_isa} = %{version}-%{release}

%description aspell
Libraries necessary to integrate applications using libenchant with aspell.

%package voikko
Summary:       Integration with voikko for libenchant
Requires:      enchant2%{?_isa} = %{version}-%{release}

%description voikko
Libraries necessary to integrate applications using libenchant with voikko.


%package devel
Summary:       Development files for %{name}
Requires:      enchant2%{?_isa} = %{version}-%{release}
Requires:      glib2-devel

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n enchant-%{version}


%build
%configure \
    --with-aspell \
    --with-hunspell-dir=%{_datadir}/myspell \
    --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g;
        s|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build pkgdatadir=%{_datadir}/enchant-2


%install
%make_install pkgdatadir=%{_datadir}/enchant-2
find %{buildroot} -name '*.la' -delete


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS NEWS README
%license COPYING.LIB
%{_bindir}/enchant-2
%{_bindir}/enchant-lsmod-2
%{_libdir}/libenchant-2.so.*
%dir %{_libdir}/enchant-2
%{_libdir}/enchant-2/enchant_hunspell.so
%{_mandir}/man1/*
%{_datadir}/enchant-2

%files aspell
%{_libdir}/enchant-2/enchant_aspell.so*

%files voikko
%{_libdir}/enchant-2/enchant_voikko.so*

%files devel
%{_libdir}/libenchant-2.so
%{_libdir}/pkgconfig/enchant-2.pc
%{_includedir}/enchant-2


%changelog
* Tue Oct 13 2020 Tomas Popela <tpopela@redhat.com> - 2.2.3-3
- Rebuild for the annobin fixes
- Resolves: rhbz#1703990

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Sandro Mani <manisandro@gmail.com> - 2.2.3-1
- Update to 2.2.3

* Wed Jan 03 2018 Sandro Mani <manisandro@gmail.com> - 2.2.1-1
- Update to 2.2.1

* Thu Dec 14 2017 Sandro Mani <manisandro@gmail.com> - 2.2.0-2
- Add patch to fix FSF addresses
- Kill rpath

* Wed Dec 13 2017 Sandro Mani <manisandro@gmail.com> - 2.2.0-1
- Initial package
