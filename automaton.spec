#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : automaton
Version  : 1.5.0
Release  : 18
URL      : https://pypi.debian.net/automaton/automaton-1.5.0.tar.gz
Source0  : https://pypi.debian.net/automaton/automaton-1.5.0.tar.gz
Summary  : Friendly state machines for python.
Group    : Development/Tools
License  : Apache-2.0
Requires: automaton-python
BuildRequires : Babel-python
BuildRequires : Jinja2
BuildRequires : Sphinx-python
BuildRequires : coverage-python
BuildRequires : debtcollector-python
BuildRequires : discover-python
BuildRequires : doc8-python
BuildRequires : docutils
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : hacking
BuildRequires : imagesize-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : prettytable
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : wrapt-python

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
Requires: debtcollector-python
Requires: prettytable
Requires: six-python

%description python
python components for the automaton package.


%prep
%setup -q -n automaton-1.5.0

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
