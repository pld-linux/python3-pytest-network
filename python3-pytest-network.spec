Summary:	A simple plugin to disable network on socket level
Summary(pl.UTF-8):	Prosta wtyczka wyłączająca sieć na poziomie gniazd
Name:		python3-pytest-network
Version:	0.0.1
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-network/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-network/pytest_network-%{version}.tar.gz
# Source0-md5:	ff90ac6c57611f1fa4a4d651fe074a3f
URL:		https://pypi.org/project/pytest-network/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple pytest plugin to disable network on socket level.

%description -l pl.UTF-8
Prosta wtyczka pytesta wyłączająca sieć na poziomie gniazd.

%prep
%setup -q -n pytest_network-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/pytest_network.py
%{py3_sitescriptdir}/__pycache__/pytest_network.cpython-*.py[co]
%{py3_sitescriptdir}/pytest_network-%{version}-py*.egg-info
