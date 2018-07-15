%global __python2 /usr/bin/python2
%global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
%global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")
%global python2_version %(%{__python2} -c "import sys; sys.stdout.write('{0.major}.{0.minor}'.format(sys.version_info))")
%global python2_version_nodots %(%{__python2} -c "import sys; sys.stdout.write('{0.major}{0.minor}'.format(sys.version_info))")

%global py2_shbang_opts -s

%global py2_build() %{expand:\
CFLAGS="%{optflags}" %{__python2} %{py_setup} %{?py_setup_args} build --executable="%{__python2} %{py2_shbang_opts}" %{?1};\
sleep 1\
}

%global py2_install() %{expand:\
CFLAGS="%{optflags}" %{__python2} %{py_setup} %{?py_setup_args} install -O1 --skip-build --root %{buildroot} %{?1}\
}

# %global __python3 /usr/bin/python3
# 
# %global python3_sitelib %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
# %global python3_sitearch %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")
# %global python3_version %(%{__python3} -c "import sys; sys.stdout.write(sys.version[:3])")
# %global python3_version_nodots %(%{__python3} -c "import sys; sys.stdout.write(sys.version[:3].replace('.',''))")
# %global py3dir %{_builddir}/python3-%{name}-%{version}-%{release}
# 
# %global py3_shbang_opts -s
# 
# %global py3_build() %{expand:\
# CFLAGS="%{optflags}" %{__python3} %{py_setup} %{?py_setup_args} build --executable="%{__python3} %{py3_shbang_opts}" %{?1};\
# sleep 1\
# }
# 
# %global py3_install() %{expand:\
# CFLAGS="%{optflags}" %{__python3} %{py_setup} %{?py_setup_args} install -O1 --skip-build --root %{buildroot} %{?1}\
# }

%global modname zamia-ai
%global altname zamiaai
%global eggname zamia_ai

%global _docdir_fmt %{name}

Name:           %{modname}
Version:        0.1.1
Release:        4%{?dist}
Summary:        Free and open source A.I. system based on Python, TensorFlow and Prolog.

License:        Apache-2
URL:            http://zamia-ai.org
Source0:        zamia-ai-%{version}.tar.gz

Requires:       python-nltools
Requires:       python-pyxsb
Requires:       python-cmdln
Requires:       pytz
Requires:       python-sqlalchemy
Requires:       python-six
Requires:       python-tzlocal
Requires:       scipy


%{?python_provide:%python_provide python-%{altname}}
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
# BuildRequires:  python3-devel
# BuildRequires:  python3-setuptools
BuildRequires:  pytest
BuildRequires:  xsb

%description
%{summary}.

%prep
%autosetup -n zamia-ai-%{version}

%build
%py2_build
# %py3_build

%install
%py2_install
# %py3_install

pwd
ls

for M in %{buildroot}%{_datadir}/zamia-ai/modules/* ; do
    pushd $M

    for i in *.pl ; do 
        bn=`basename ${i} .pl`
        xsb -e "[${bn}]." < /dev/null
    done

    popd
done

%check
# py.test-%{python2_version} -v
# py.test-%{python3_version} -v

%files -n %{modname}
# %license LICENSE
# %doc HISTORY.rst README.rst
%doc README.md
%{python2_sitelib}/%{eggname}-*.egg-info
%{python2_sitelib}/%{altname}/
%{_datadir}/zamia-ai
%{_bindir}/zaicli

# %files -n python3-%{altname}
# %doc README.md
# %{python3_sitearch}/%{eggname}-*.egg-info
# %{python3_sitearch}/%{altname}/

%changelog
* Sun Jul 15 2018 Guenter Bartsch <guenter@zamia.org> - 0.1.1-3
- Dependency fixes
* Sun Jul 15 2018 Guenter Bartsch <guenter@zamia.org> - 0.1.1-2
- Dependency fixes
* Sun Jul 15 2018 Guenter Bartsch <guenter@zamia.org> - 0.1.1-1
- Dependency fixes
* Sun Jul 15 2018 Guenter Bartsch <guenter@zamia.org> - 0.1.0-1
- Initial package
