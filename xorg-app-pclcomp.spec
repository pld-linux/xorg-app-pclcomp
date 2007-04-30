Summary:	pclcomp application - compress PCL graphics files
Summary(pl.UTF-8):	Aplikacja pclcomp do kompresji plików graficznych PCL
Name:		xorg-app-pclcomp
Version:	0.99.2
Release:	0.1
License:	unknown, (C) HP
Group:		X11/Applications
# last version in X11R7.0-RC3, then removed due to (unclear?) license
Source0:	pclcomp-%{version}.tar.bz2
# Source0-md5:	8b8f20662da6a85c965718c0174d2cfd
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pclcomp compresses (or decompresses) HP-PCL (Printer Control Language)
graphics data. The supported compression modes are 0 (uncompressed),
1, 2 and 3. pclcomp will read files using any of the modes 0 through
3, and will output using the modes which will give the best
compression. This compressed version of the file may be sent directly
to a PCL compatible printer, thus reducing I/O bandwidth. Pictures may
also be saved in compressed form, reducing disk usage. In addition,
PCL "imaging" files for the PaintJet XL are also supported.

%description -l pl.UTF-8
pclcomp kompresuje (lub dekompresuje) dane graficzne w języku HP-PCL
(Printer Control Language). Obsługiwane metody kompresji to 0 (brak
kompresji), 1, 2 i 3. pclcomp odczytuje pliki skompresowane metodą 0
do 3 i tworzy dane metodą dającą najlepszą kompresję. Taką
skompresowaną wersję pliku można wysłać bezpośrednio na drukarkę
zgodną z PCL ograniczając wykorzystanie I/O. Obrazy także można
zapisywać w postaci skompresowanej, zmniejszając wykorzystanie dysku.
Ponadto obsługiwane są także pliki obrazów PCL dla drukarek PaintJet
XL.

%prep
%setup -q -n pclcomp-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1x*
