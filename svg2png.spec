Summary:	svg2png - render an SVG image to a PNG image (using cairo)
Summary(pl.UTF-8):	svg2png - tworzenie obrazków PNG z SVG przy użyciu cairo
Name:		svg2png
Version:	0.1.3
Release:	6
License:	BSD-like
Group:		Applications/Graphics
Source0:	http://cairographics.org/snapshots/%{name}-%{version}.tar.gz
# Source0-md5:	ba266c00486ffd93b8a46d59028aaef9
Patch0:		build.patch
URL:		http://cairographics.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libsvg-cairo-devel >= 0.1.6
BuildRequires:	pkgconfig
Requires:	libsvg-cairo >= 0.1.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility to render an SVG image to a PNG image (using cairo).

%description -l pl.UTF-8
Narzędzie do tworzenia obrazków PNG z SVG przy użyciu cairo.

%prep
%setup -q
%patch -P0 -p1

%build
%{__aclocal}
%{__autoconf}
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
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/svg2png
%{_mandir}/man1/svg2png.1*
