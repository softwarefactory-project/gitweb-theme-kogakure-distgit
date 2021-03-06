%global         commit0 4305b3551551c470339c24a6567b1ac9e642ae54
%global         shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global         uname gitweb-theme
%global         checkout 20170220git%{shortcommit0}
%global         gitwebver 1.8.3.1

Name:           gitweb-theme-kogakure
Version:        %{gitwebver}
Release:        1%{checkout}%{?dist}
Summary:        Gitweb theme Kogakure

License:        MIT
URL:            http://kogakure.github.io/gitweb-theme
Source0:        https://github.com/kogakure/%{uname}/archive/%{commit0}.tar.gz#/%{uname}-%{shortcommit0}.tar.gz

BuildArch:      noarch

#BuildRequires:  python-pathlib
#BuildRequires:  python-enum34
#BuildRequires:  python-scss

Requires:       gitweb

%description
Gitweb theme kogakure

%prep
%autosetup -n %{uname}-%{commit0}

%build
# Minification does not work and returns a syntax error
#pyscss gitweb.css -o kagakure.min.css

%install
install -p -D -m 644 gitweb.css %{buildroot}/%{_var}/www/git/static/kogakure.css

%files
%{_var}/www/git/static/kogakure.css

%changelog
* Sat Mar 11 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 1.8.3.1-120170220git4305b35
- Fix release number

* Mon Feb 20 2017 Fabien Boucher <fboucher@redhat.com> - 1.8.3.1-02202017git4305b35
- Initial Packaging
