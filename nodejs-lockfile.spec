%define		pkg	lockfile
Summary:	A very polite lock file utility
Name:		nodejs-%{pkg}
Version:	0.3.0
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/lockfile
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	2e298908fedb5e10bfe238dab8f7dc26
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A very polite lock file utility, which endeavors to not litter, and
to wait patiently for others.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{nodejs_libdir}/%{pkg}}
cp -a package.json lockfile.js $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%{nodejs_libdir}/%{pkg}
