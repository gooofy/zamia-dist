Name:           kenlm
Version:        1.0
Release:        0.3.20180721git328cc29%{?dist}
Summary:        KenLM: Faster and Smaller Language Model Queries

Group:          Applications/Text
License:        LGPLv2+
URL:            http://kheafield.com/code/kenlm/
Source0:        http://kheafield.com/code/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  eigen3-devel
BuildRequires:  boost-static
BuildRequires:  zlib-devel
BuildRequires:  bzip2-devel
BuildRequires:  xz-devel

%description
KenLM: Faster and Smaller Language Model Queries

%prep
%setup -q

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

# add kenlm_ prefix to generic binary names to avoid collisions

mv %{buildroot}%{_bindir}/probing_hash_table_benchmark  %{buildroot}%{_bindir}/kenlm_probing_hash_table_benchmark
mv %{buildroot}%{_bindir}/query                         %{buildroot}%{_bindir}/kenlm_query
mv %{buildroot}%{_bindir}/fragment                      %{buildroot}%{_bindir}/kenlm_fragment
mv %{buildroot}%{_bindir}/build_binary                  %{buildroot}%{_bindir}/kenlm_build_binary
mv %{buildroot}%{_bindir}/count_ngrams                  %{buildroot}%{_bindir}/kenlm_count_ngrams
mv %{buildroot}%{_bindir}/filter                        %{buildroot}%{_bindir}/kenlm_filter
mv %{buildroot}%{_bindir}/phrase_table_vocab            %{buildroot}%{_bindir}/kenlm_phrase_table_vocab
mv %{buildroot}%{_bindir}/interpolate                   %{buildroot}%{_bindir}/kenlm_interpolate
mv %{buildroot}%{_bindir}/streaming_example             %{buildroot}%{_bindir}/kenlm_streaming_example

# shared libraries

mkdir -p %{buildroot}%{_libdir}

%{__install} -p -m 0755 %{_target_platform}/lib/libkenlm_filter.so       %{buildroot}%{_libdir}/libkenlm_filter.so
%{__install} -p -m 0755 %{_target_platform}/lib/libkenlm_util.so         %{buildroot}%{_libdir}/libkenlm_util.so
%{__install} -p -m 0755 %{_target_platform}/lib/libkenlm.so              %{buildroot}%{_libdir}/libkenlm.so
%{__install} -p -m 0755 %{_target_platform}/lib/libkenlm_builder.so      %{buildroot}%{_libdir}/libkenlm_builder.so
%{__install} -p -m 0755 %{_target_platform}/lib/libkenlm_interpolate.so  %{buildroot}%{_libdir}/libkenlm_interpolate.so

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_bindir}/*
%{_libdir}/*

%changelog
* Sat Jul 21 2018 Guenter Bartsch <guenter@zamia.org> - 1.0-0.3.20180721
- add eigen3 dependency, build interpolate libs and binaries

* Sat Jul 21 2018 Guenter Bartsch <guenter@zamia.org> - 1.0-0.1.20180721
- add shared libs

* Sat Jul 21 2018 Guenter Bartsch <guenter@zamia.org> - 1.0-20180721
- initial build

