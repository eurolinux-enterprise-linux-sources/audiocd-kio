Name:    audiocd-kio 
Summary: Audiocd kio slave
Version: 4.10.5
Release: 3%{?dist}

# code GPLv2+, handbook/docs GFDL
License: GPLv2+ and GFDL
URL:     https://projects.kde.org/projects/kde/kdemultimedia/%{name}
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches

BuildRequires: cdparanoia-devel cdparanoia
BuildRequires: kdelibs4-devel >= %{version}
BuildRequires: libkcddb-devel >= %{version}
BuildRequires: libkcompactdisc-devel >= %{version}
BuildRequires: pkgconfig(flac)
BuildRequires: pkgconfig(phonon)
BuildRequires: pkgconfig(theora)
BuildRequires: pkgconfig(vorbis)

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: kde-runtime%{?_kde4_version: >= %{_kde4_version}}

# when split occurred
Obsoletes: kdemultimedia-kio_audiocd < 6:4.8.80
Provides:  kdemultimedia-kio_audiocd = 6:%{version}-%{release}
Provides:  kio_audiocd = %{version}-%{release}

%description
%{summary}.

%package libs
Summary: Runtime libraries for %{name}
Requires: %{name} = %{version}-%{release}
Requires: kdelibs4%{?_isa}%{?_kde4_version: >= %{_kde4_version}}
Requires: libkcddb%{?_isa}%{?_kde4_version: >= %{_kde4_version}}
Requires: libkcompactdisc%{?_isa}%{?_kde4_version: >= %{_kde4_version}}
# when split occurred
Conflicts: kdemultimedia-libs < 6:4.8.80
%description libs
%{summary}.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: kdelibs4-devel
# when split occured
Conflicts: kdemultimedia-devel < 6:4.8.80
%description devel
%{summary}.


%prep
%setup -q


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang %{name} --with-kde --all-name

# fix documentation multilib conflict in index.cache
bunzip2 %{buildroot}%{_kde4_docdir}/HTML/en/kioslave/audiocd/index.cache.bz2
sed -i -e 's!name="id[a-z]*[0-9]*"!!g' %{buildroot}%{_kde4_docdir}/HTML/en/kioslave/audiocd/index.cache
sed -i -e 's!#id[a-z]*[0-9]*"!!g' %{buildroot}%{_kde4_docdir}/HTML/en/kioslave/audiocd/index.cache
bzip2 -9 %{buildroot}%{_kde4_docdir}/HTML/en/kioslave/audiocd/index.cache


#check


%files -f %{name}.lang
%doc COPYING COPYING.DOC
# own these to avoid dep on kdebase
%dir %{_kde4_appsdir}/konqsidebartng/
%dir %{_kde4_appsdir}/konqsidebartng/virtual_folders/
%dir %{_kde4_appsdir}/konqsidebartng/virtual_folders/services/
%{_kde4_appsdir}/konqsidebartng/virtual_folders/services/audiocd.desktop
%{_kde4_appsdir}/solid/actions/solid_audiocd.desktop
%{_kde4_datadir}/kde4/services/audiocd.desktop
%{_kde4_datadir}/kde4/services/audiocd.protocol
%{_kde4_datadir}/config.kcfg/audiocd*.kcfg
%{_kde4_libdir}/kde4/kcm_audiocd.so
%{_kde4_libdir}/kde4/kio_audiocd.so

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files libs
%{_kde4_libdir}/libaudiocdplugins.so.4*
%{_kde4_libdir}/kde4/libaudiocd_encoder_flac.so
%{_kde4_libdir}/kde4/libaudiocd_encoder_lame.so
%{_kde4_libdir}/kde4/libaudiocd_encoder_vorbis.so
%{_kde4_libdir}/kde4/libaudiocd_encoder_wav.so

%files devel
%{_kde4_includedir}/audiocdencoder.h
%{_kde4_libdir}/libaudiocdplugins.so


%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 4.10.5-3
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 4.10.5-2
- Mass rebuild 2013-12-27

* Sun Jun 30 2013 Than Ngo <than@redhat.com> - 4.10.5-1
- 4.10.5

* Sat Jun 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.4-1
- 4.10.4

* Mon May 06 2013 Than Ngo <than@redhat.com> - 4.10.3-1
- 4.10.3

* Wed Apr 24 2013 Than Ngo <than@redhat.com> - 4.10.2-2
- fix multilib issue

* Sun Mar 31 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.2-1
- 4.10.2

* Sat Mar 02 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.1-1
- 4.10.1

* Fri Feb 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.0-1
- 4.10.0

* Sun Jan 20 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.98-1
- 4.9.98

* Fri Jan 04 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.97-1
- 4.9.97

* Thu Dec 20 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.95-1
- 4.9.95

* Mon Dec 03 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.90-1
- 4.9.90 (4.10 beta2)

* Mon Dec 03 2012 Than Ngo <than@redhat.com> - 4.9.4-1
- 4.9.4

* Sat Nov 03 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.3-1
- 4.9.3

* Sat Sep 29 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.2-1
- 4.9.2

* Mon Sep 03 2012 Than Ngo <than@redhat.com> - 4.9.1-1
- 4.9.1

* Thu Jul 26 2012 Lukas Tinkl <ltinkl@redhat.com> - 4.9.0-1
- 4.9.0

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.97-1
- 4.8.97

* Wed Jun 27 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.95-1
- 4.8.95

* Wed Jun 13 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.90-2
- License: GPLv2+ and GFDL

* Fri Jun 08 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.90-1
- audiocd-kio-4.8.90

