#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : automaton
Version  : 1.17.0
Release  : 38
URL      : https://files.pythonhosted.org/packages/fb/9b/5efe64f88c3de1836a719c9b6fd48443f9fa71b3bbf873d1a688b74e57e7/automaton-1.17.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/fb/9b/5efe64f88c3de1836a719c9b6fd48443f9fa71b3bbf873d1a688b74e57e7/automaton-1.17.0.tar.gz
Summary  : Friendly state machines for python.
Group    : Development/Tools
License  : Apache-2.0
Requires: automaton-license = %{version}-%{release}
Requires: automaton-python = %{version}-%{release}
Requires: automaton-python3 = %{version}-%{release}
Requires: pbr
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : six

%description
Automaton
        =========

%package license
Summary: license components for the automaton package.
Group: Default

%description license
license components for the automaton package.


%package python
Summary: python components for the automaton package.
Group: Default
Requires: automaton-python3 = %{version}-%{release}

%description python
python components for the automaton package.


%package python3
Summary: python3 components for the automaton package.
Group: Default
Requires: python3-core

%description python3
python3 components for the automaton package.


%prep
%setup -q -n automaton-1.17.0
cd %{_builddir}/automaton-1.17.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573774659
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/automaton
cp %{_builddir}/automaton-1.17.0/LICENSE %{buildroot}/usr/share/package-licenses/automaton/c700a8b9312d24bdc57570f7d6a131cf63d89016
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/automaton/c700a8b9312d24bdc57570f7d6a131cf63d89016

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
