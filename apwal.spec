Summary:	Application launcher
Summary(pl):	Program do uruchamiania aplikacji
Name:		apwal
Version:	0.4.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://apwal.free.fr/download/%{name}-%{version}.tar.gz
# Source0-md5:	87327fd1665d64c58b675708de1f0067
URL:		http://apwal.free.fr/
BuildRequires:	gtk+2
BuildRequires:	libxml2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apwal is an simple and powerful application launcher. It is composed
in 2 parts: the application launcher itself and a good looking easy to
use editor.

%description -l pl
Apwal jest prostym i potê¿nym programem do uruchamiania aplikacji.
Zbudowany jest z dwóch czê¶ci: do uruchamiania aplikacji i ³atwego w
u¿yciu edytora.

%prep
%setup -q -n %{name}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_mandir}/man1}
install src/%{name} $RPM_BUILD_ROOT%{_bindir}/
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
