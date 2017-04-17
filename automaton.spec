#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : automaton
Version  : 1.9.0
Release  : 28
URL      : https://pypi.debian.net/automaton/automaton-1.9.0.tar.gz
Source0  : https://pypi.debian.net/automaton/automaton-1.9.0.tar.gz
Summary  : Friendly state machines for python.
Group    : Development/Tools
License  : Apache-2.0
Requires: automaton-python
Requires: debtcollector
Requires: pbr
Requires: six
BuildRequires : configparser
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
=========
Automaton
=========
.. image:: https://img.shields.io/pypi/v/automaton.svg
:target: https://pypi.python.org/pypi/automaton/
:alt: Latest Version

%package python
Summary: python components for the automaton package.
Group: Default

%description python
python components for the automaton package.


%prep
%setup -q -n automaton-1.9.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1492457935
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1492457935
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
