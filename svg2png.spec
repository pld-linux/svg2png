Summary:	svg2png - render an SVG image to a PNG image (using cairo)
Summary(pl):	svg2png - tworzenie obrazków PNG z SVG przy u¿yciu cairo
Name:		svg2png
Version:	0.1.1
Release:	1
License:	BSD-like
Group:		Applications/Graphics
Source0:	http://cairographics.org/snapshots/%{name}-%{version}.tar.gz
# Source0-md5:	620a5dc43e0c6e2d171926369cd3b73d
URL:		http://cairographics.org/
BuildRequires:	libsvg-cairo-devel >= 0.1.3
BuildRequires:	pkgconfig
Requires:	libsvg-cairo >= 0.1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility to render an SVG image to a PNG image (using cairo).

%description -l pl
Narzêdzie do tworzenia obrazków PNG z SVG przy u¿yciu cairo.

%prep
%setup -q

%build
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
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
