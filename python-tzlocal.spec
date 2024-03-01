%global           pypi_name tzlocal
%define debug_package %nil

Name:             python-tzlocal
Version:          5.2
Release:          1

Summary:          A Cassowary constraint solving algorithm
License:          BSD
Group:            Development/Python

URL:              https://pypi.org/project/tzlocal/
Source0:	https://files.pythonhosted.org/packages/04/d3/c19d65ae67636fe63953b20c2e4a8ced4497ea232c43ff8d01db16de8dc0/%{pypi_name}-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3egg(setuptools)
BuildRequires:	python3dist(setuptools-scm)

%description
A small C++ header library which makes it easier to write Python
extension modules.
The primary feature is a PyObject smart pointer which automatically
handles reference counting and provides convenience methods for
performing common object operations.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
#rm -rf %{pypi_name}.egg-info

%build
%py3_build


%install
%py3_install

%files -n python-tzlocal
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info


