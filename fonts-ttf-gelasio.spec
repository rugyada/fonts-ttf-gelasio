Name:		fonts-ttf-gelasio
Version:	1.0
Release:	1
Summary:	Gelasio ttf fonts
License:	OFL-1.1 License
Group:		System/Fonts/True type
Url:		https://github.com/SorkinType/Gelasio
Source0:	%{name}-%version.tar.gz
BuildArch:	noarch

%description
Gelasio is an original typeface which is metrics compatible with Georgia.

%prep
%autosetup -p1 -c %{name}

%install
mkdir -p %{buildroot}%{_datadir}/fonts/TTF/gelasio
install -Dm 644 *.ttf  %{buildroot}%{_datadir}/fonts/TTF/gelasio/

%files
%dir %{_datadir}/fonts/TTF/gelasio
%{_datadir}/fonts/TTF/gelasio/*.ttf

