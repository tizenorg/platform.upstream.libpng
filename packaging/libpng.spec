Name:           libpng
Version:        1.2.46
Release:        1
License:        zlib
Summary:        A library of functions for manipulating PNG image format files
Url:            http://www.libpng.org/pub/png/
Group:          System/Libraries
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  zlib-devel
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

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
Requires:       libpng = %{version}
Requires:       zlib-devel

%description devel
The libpng-devel package contains header files and documentation necessary
for developing programs using the PNG (Portable Network Graphics) library.

%prep
%setup -q

%build

%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
rm -rf %{buildroot}/usr/share/man

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/libpng*.so.*

%files devel
%{_bindir}/*
%{_includedir}/*
%{_libdir}/libpng*.so
%{_libdir}/pkgconfig/*

