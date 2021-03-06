#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-identity
Version  : 1.3.1
Release  : 3
URL      : https://files.pythonhosted.org/packages/fe/f0/e43371a952774eb2c18dc64ba6cb824bcddebc496aea58514915276e9c41/azure-identity-1.3.1.zip
Source0  : https://files.pythonhosted.org/packages/fe/f0/e43371a952774eb2c18dc64ba6cb824bcddebc496aea58514915276e9c41/azure-identity-1.3.1.zip
Summary  : Microsoft Azure Identity Library for Python
Group    : Development/Tools
License  : MIT
Requires: azure-identity-python = %{version}-%{release}
Requires: azure-identity-python3 = %{version}-%{release}
Requires: azure-core
Requires: azure-nspkg
Requires: cryptography
Requires: msal
Requires: python-mock
Requires: six
BuildRequires : azure-core
BuildRequires : azure-nspkg
BuildRequires : buildreq-distutils3
BuildRequires : cryptography
BuildRequires : msal
BuildRequires : python-mock
BuildRequires : six

%description
Azure Identity authenticating with Azure Active Directory for Azure SDK
        libraries. It provides credentials Azure SDK clients can use to authenticate
        their requests.

%package python
Summary: python components for the azure-identity package.
Group: Default
Requires: azure-identity-python3 = %{version}-%{release}

%description python
python components for the azure-identity package.


%package python3
Summary: python3 components for the azure-identity package.
Group: Default
Requires: python3-core
Provides: pypi(azure_identity)
Requires: pypi(azure_core)
Requires: pypi(cryptography)
Requires: pypi(msal)
Requires: pypi(msal_extensions)
Requires: pypi(six)

%description python3
python3 components for the azure-identity package.


%prep
%setup -q -n azure-identity-1.3.1
cd %{_builddir}/azure-identity-1.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1591207142
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
