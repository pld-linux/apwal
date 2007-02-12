Summary:	Application launcher
Summary(pl.UTF-8):	Program do uruchamiania aplikacji
Name:		apwal
Version:	0.4.5
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://apwal.free.fr/download/%{name}-%{version}.tar.gz
# Source0-md5:	2f15a1a680f842d8373a1c2725b53130
URL:		http://apwal.free.fr/
Patch0:		%{name}-Makefile.patch
BuildRequires:	gtk+2-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apwal is an simple and powerful application launcher. It is composed
in 2 parts: the application launcher itself and a good looking easy to
use editor.

%description -l pl.UTF-8
Apwal jest prostym i potężnym programem do uruchamiania aplikacji.
Zbudowany jest z dwóch części: do uruchamiania aplikacji i łatwego w
użyciu edytora.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} `pkg-config --cflags gtk+-2.0 gthread-2.0`" \
	LDFLAGS="%{rpmldflags} `pkg-config --libs gtk+-2.0 gthread-2.0` `xml2-config --libs`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_mandir}/man1}

install src/%{name} $RPM_BUILD_ROOT%{_bindir}
ln -s %{_bindir}/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}-editor
cp -aR pixmaps/* $RPM_BUILD_ROOT%{_pixmapsdir}
install debian/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ABOUT Changelog FAQ README example/apwalrc.xml
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_pixmapsdir}/*
