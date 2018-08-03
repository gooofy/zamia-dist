%if 0%{?fedora}
%global with_python3 1
%else
%global with_python3 0
%endif

%{?filter_provides_in: %filter_provides_in .*/h5py/.*\.so}
%{?filter_setup}

Summary:        A Python interface to the HDF5 library
Name:           h5py
Version:        2.3.1
Release:        2%{?dist}
Group:          Applications/Engineering
License:        BSD
URL:            http://www.h5py.org/
Source0:        https://pypi.python.org/packages/source/h/h5py/h5py-%{version}.tar.gz
# patch to use a system liblzf rather than bundled liblzf
Patch0:         h5py-system-lzf.patch
BuildRequires:  liblzf-devel
BuildRequires:  hdf5-devel >= 1.8.3
BuildRequires:  python-devel >= 2.6
BuildRequires:  python-sphinx
BuildRequires:  numpy >= 1.0.3
BuildRequires:  Cython
%if 0%{?with_python3}
BuildRequires:  python-tools
BuildRequires:  python3-devel >= 3.2
BuildRequires:  python3-sphinx 
BuildRequires:  python3-numpy >= 1.0.3
BuildRequires:  python3-Cython
%endif
Requires:       hdf5 = %{_hdf5_version}
Requires:       numpy >= 1.0.3

%description
The h5py package provides both a high- and low-level interface to the
HDF5 library from Python. The low-level interface is intended to be a
complete wrapping of the HDF5 API, while the high-level component
supports access to HDF5 files, data sets and groups using established
Python and NumPy concepts.

A strong emphasis on automatic conversion between Python (Numpy)
data types and data structures and their HDF5 equivalents vastly
simplifies the process of reading and writing data from Python.

%if 0%{?with_python3}
%package -n     python3-h5py
Summary:        A Python 3 interface to the HDF5 library
Group:          Applications/Engineering
Requires:       python3-numpy >= 1.0.3

%description -n python3-h5py
The h5py package provides both a high- and low-level interface to the
HDF5 library from Python. The low-level interface is intended to be a
complete wrapping of the HDF5 API, while the high-level component
supports access to HDF5 files, data sets and groups using established
Python and NumPy concepts.

A strong emphasis on automatic conversion between Python (Numpy)
data types and data structures and their HDF5 equivalents vastly
simplifies the process of reading and writing data from Python.
This is the Python 3 version of h5py.
%endif

%prep
%setup -q
# use system libzlf and remove private copy
%patch0 -p1 -b .lzf
rm -rf lzf/lzf
%{__python} api_gen.py
%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build
export CFLAGS="%{optflags} -fopenmp"
%{__python} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd 
%endif

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
chmod 0755 %{buildroot}%{python_sitearch}/%{name}/*.so

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
chmod 0755 %{buildroot}%{python3_sitearch}/%{name}/*.so
%endif

%check
%{__python} setup.py test || :
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py test || :
popd
%endif

%files
%doc licenses/*.txt ANN.rst README.rst examples
%{python_sitearch}/%{name}/
%{python_sitearch}/%{name}-%{version}-*.egg-info

%if 0%{?with_python3}
%files -n python3-h5py
%doc licenses/*.txt ANN.rst README.rst
%{python3_sitearch}/%{name}/
%{python3_sitearch}/%{name}-%{version}-*.egg-info
%endif

%changelog
* Wed Jun 25 2014 Orion Poplawski <orion@cora.nwra.com> - 2.3.1-1
- Update to 2.3.1

* Tue Jun 10 2014 Orion Poplawski <orion@cora.nwra.com> - 2.3.0-4
- Rebuild for hdf 1.8.13

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 9 2014 Orion Poplawski <orion@cora.nwra.com> - 2.3.0-2
- Rebuild for Python 3.4

* Tue Apr 22 2014 Orion Poplawski <orion@cora.nwra.com> - 2.3.0-1
- Update to 2.3.0

* Sun Jan 5 2014 Orion Poplawski <orion@cora.nwra.com> - 2.2.1-2
- Rebuild for hdf5 1.8.12
- Add requires for hdf5 version

* Thu Dec 19 2013 Orion Poplawski <orion@cora.nwra.com> - 2.2.1-1
- 2.2.1

* Thu Sep 26 2013 Terje Rosten <terje.rosten@ntnu.no> - 2.2.0-1
- 2.2.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 10 2013 Terje Rosten <terje.rosten@ntnu.no> - 2.1.3-1
- 2.1.3
- add Python 3 import patches (#962250)

* Thu May 16 2013 Orion Poplawski <orion@cora.nwra.com> - 2.1.0-3
- rebuild for hdf5 1.8.11

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 06 2012 Terje Rosten <terje.rosten@ntnu.no> - 2.1.0-1
- 2.1.0
- add Python 3 subpackage

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 24 2012 Terje Rosten <terje.rosten@ntnu.no> - 2.0.1-1
- 2.0.1
- docs is removed
- rebase patch

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon May 23 2011 Terje Rosten <terje.rosten@ntnu.no> - 1.3.1-4
- add patch from Steve Traylen (thanks!) to use system liblzf
 
* Thu Jan 13 2011 Terje Rosten <terje.rosten@ntnu.no> - 1.3.1-3
- fix buildroot
- add filter
- don't remove egg-info files
- remove explicit hdf5 req

* Sun Jan  2 2011 Terje Rosten <terje.rosten@ntnu.no> - 1.3.1-2
- build and ship docs as html

* Mon Dec 27 2010 Terje Rosten <terje.rosten@ntnu.no> - 1.3.1-1
- 1.3.1
- license is BSD only
- run tests
- new url

* Sat Jul  4 2009 Joseph Smidt <josephsmidt@gmail.com> - 1.2.0-1
- initial RPM release
