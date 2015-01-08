Name:           libpng
Version:        1.6.13
Release:        1
License:        Zlib
Summary:        A library of functions for manipulating PNG image format files
Url:            http://www.libpng.org/pub/png/
Group:          System/Libraries
Source:         %{name}-%{version}.tar.bz2
Source1001:     libpng.manifest
BuildRequires:  zlib-devel

%description
The libpng package contains a library of functions for creating and
manipulating PNG (Portable Network Graphics) image format files.  PNG
is a bit-mapped graphics format similar to the GIF format.  PNG was
created to replace the GIF format, since GIF uses a patented data
compression algorithm.

Libpng should be installed if you need to manipulate PNG format image
files.

%package devel
Summary:        Development tools for programs to manipulate PNG image format files
Group:          Development/Libraries
Requires:       %{name} = %{version}
Requires:       zlib-devel

%description devel
The libpng-devel package contains header files and documentation necessary
for developing programs using the PNG (Portable Network Graphics) library.

%prep
%setup -q
cp %{SOURCE1001} .

%build

%configure \
    --disable-static \
%ifarch %arm armv7l armv7el aarch64
    --enable-arm-neon=check
%endif


make %{?_smp_mflags}

%install
%make_install
rm -rf %{buildroot}/usr/share/man

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%license LICENSE
%{_libdir}/libpng*.so.*

%files devel
%manifest %{name}.manifest
%{_bindir}/*
%{_includedir}/*
%{_libdir}/libpng*.so
%{_libdir}/pkgconfig/*

