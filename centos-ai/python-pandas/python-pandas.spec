%if 0%{?fedora}
%global with_python3 1
%endif
%global pkgname pandas

Name:           python-pandas
Version:        0.17.1
Release:        2%{?dist}
Summary:        Python library providing high-performance data analysis tools

Group:          Development/Languages
License:        BSD
URL:            http://pandas.pydata.org/
Source0:        http://pypi.python.org/packages/source/p/pandas/pandas-%{version}.tar.gz

BuildRequires:  python2-devel, python-setuptools, python-matplotlib
BuildRequires:  Cython
Requires:       pytz
# pandas actually supports datautil 2
# https://github.com/pydata/pandas/issues/9305
Requires:       python-dateutil
Requires:       numpy
Requires:       scipy
Requires:       python-tables
Requires:       python-matplotlib
Requires:       python-Bottleneck
Requires:       python-numexpr
%if 0%{?fedora}
Recommends:     python-xlrd, python-xlwt
%endif
Provides:       python2-%{pkgname} = %{version}-%{release}

%global __provides_exclude_from ^(%{python2_sitearch}|%{python3_sitearch})/.*\\.so$

%description
pandas is an open source, BSD-licensed library providing 
high-performance, easy-to-use data structures and data 
analysis tools for the Python programming language.

%if 0%{?with_python3}
%package -n python3-pandas
Summary:        Python library providing high-performance data analysis tools
BuildRequires:  python3-devel, python3-setuptools, python3-matplotlib
BuildRequires:  python3-Cython
Requires:       python3-pytz
Requires:       python3-dateutil
Requires:       python3-numpy
Requires:       python3-scipy
Requires:       python3-tables
Requires:       python3-matplotlib
Requires:       python3-Bottleneck
Requires:       python3-numexpr
%if 0%{?fedora}
# python3-xlwt doesn't exist: bz #1282235
# openpyxl version is higher than 2.0
Recommends:     python3-xlrd
%endif

%description -n python3-pandas
pandas is an open source, BSD-licensed library providing 
high-performance, easy-to-use data structures and data 
analysis tools for the Python programming language.

%endif # with_python3

%prep
%setup -q -n %{pkgname}-%{version}

%build
%py2_build

%if 0%{?with_python3}
%py3_build
%endif # with_python3


%install
%if 0%{?with_python3}
%py3_install
%endif # with_python3

%py2_install

%files
%doc RELEASE.md
%license LICENSE
%{python2_sitearch}/pandas*

%if 0%{?with_python3}
%files -n python3-pandas
%doc RELEASE.md
%license LICENSE
%{python3_sitearch}/pandas*
%endif # with_python3


%changelog
* Sun Jan 03 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 0.17.1-1
- New upstream version (0.17.1)
- Add new dependecy as weak dep (fixes bz #1288919)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Oct 28 2015 Orion Poplawski <orion@cora.nwra.com> - 0.17.0-2
- Use common build directory, new python macros
- Filter provides
- Fix provides

* Mon Oct 12 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.17.0-1
- New release of pandas 0.17.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.16.2-1
- New release of pandas 0.16.2

* Mon May 18 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.16.1-1
- New release of pandas 0.16.1

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.16.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Mar 24 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.16.0-1
- New release of pandas 0.16.0
- Use license macro
- Don't use py3dir (new python guidelines)

* Tue Jan 20 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.15.2-3
- Pandas actually supports dateutil 2

* Mon Jan 19 2015 Sergio Pascual <sergiopr@fedoraproject.org> - 0.15.2-2
- Update dependency on dateutil to dateutil15 (bz #1183368)

* Wed Dec 17 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.15.2-1
- New release of pandas 0.15.2

* Thu Nov 20 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.15.1-1
- New release of pandas 0.15.1

* Mon Oct 20 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.15.0-1
- New release of pandas 0.15.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul 13 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.14.1-1
- New release of pandas 0.14.1

* Mon Jun 16 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.14.0-1
- New release of pandas 0.14.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Jan 28 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.12.0-4
- Enable python3 build
- Set CFLAGS before build

* Fri Dec 13 2013 Kushal Das <kushal@fedoraproject.org> 0.12.0-3
- Fixed dependency name

* Fri Dec 06 2013 Pierre-Yves Chibon <pingou@pingoured>fr - 0.12.0-2
- Change BR from python-setuptools-devel to python-setuptools
  See https://fedoraproject.org/wiki/Changes/Remove_Python-setuptools-devel

* Fri Sep 20 2013 Kushal Das <kushal@fedoraproject.org> 0.12.0-1
- New release of pandas 0.12.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 24 2012 Kushal Das <kushal@fedoraproject.org> 0.10.0-1
- New release of pandas 0.10.0

* Thu Nov 08 2012 Kushal Das <kushal@fedoraproject.org> 0.10.0-1
- New release of pandas 0.10.0

* Thu Nov 08 2012 Kushal Das <kushal@fedoraproject.org> 0.9-1
- New release of pandas

* Fri Aug 03 2012 Kushal Das <kushal@fedoraproject.org> 0.8.1-2
- Fixes from review request

* Tue Jul 10 2012 Kushal Das <kushal@fedoraproject.org> 0.8.1-1
- Initial release in Fedora

